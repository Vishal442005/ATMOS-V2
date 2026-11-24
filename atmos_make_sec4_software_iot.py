# atmos_make_sec4_software_iot.py

def get_chapter4():
    return r"""%% ==========================================================================
%%  CHAPTER 4: EMBEDDED FIRMWARE, CLOUD IOT BACKEND & WEB DASHBOARD
%% ==========================================================================
\chapter{Embedded Firmware, Cloud Backend and Web Interface}

\section{Embedded Firmware Architecture and FreeRTOS Task Scheduling}
The embedded software running on the ESP32 is engineered in modern C++ utilizing the Espressif IoT Development Framework (ESP-IDF) and Arduino core under the FreeRTOS real-time operating system. Rather than relying on a traditional blocking sequential \texttt{loop()}, the firmware exploits the ESP32 dual-core Xtensa architecture by partitioning operations into independent, prioritized FreeRTOS tasks pinned to dedicated processor cores.

\begin{figure}[H]
\centering
\includegraphics[width=0.52\textwidth]{page_26_18_Image186.jpg}
\caption[Arduino IDE development environment]{Arduino IDE embedded compilation, library configuration, and serial monitor debugging environment for the ESP32 microcontroller.}
\label{fig:arduino_ide}
\end{figure}

The task architecture comprises two primary asynchronous processes synchronized via FreeRTOS queue handles:
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Sensor Acquisition Task (Core 0, Priority 2):} Responsible for acquiring telemetry from mixed-signal peripherals. It initiates the PMS5003 UART reception buffer, verifies the 32-byte frame start delimiters (\texttt{0x42 0x4D}), computes the 16-bit additive checksum, and extracts integer $\text{PM}_{1.0}, \text{PM}_{2.5}, \text{PM}_{10}$ mass metrics. Simultaneously, it triggers the DHT22 single-bus acquisition and samples the MQ-135 analog voltage via ADC1 Channel 6. To suppress transient turbulence and electrical switching noise, the task performs a 10-point running median filter before packing the telemetry into a global data structure.
    \item \textbf{Network Telemetry \& Sleep Manager Task (Core 1, Priority 1):} Manages the Wi-Fi protocol stack. It executes an exponential-backoff connection state machine. Once connected to the local wireless gateway, it serializes the acquired telemetry into a structured JSON string, dispatches an HTTPS POST request with a timeout threshold of $5000\,\text{ms}$, verifies the HTTP 200/201 response status code, and subsequently invokes \texttt{esp\_deep\_sleep\_start()} to place the SoC into sub-microampere dormancy.
\end{enumerate}

\subsection{UART Particulate Frame Checksum Validation}
The Plantower PMS5003 serial communication protocol transmits 32 bytes per frame. To eliminate corrupted packets caused by EMI or timing jitter, the firmware implements strict cyclic checksum validation:
\begin{equation}
\text{Checksum}_{\text{calc}} = \sum_{k=0}^{29} \text{Byte}[k] \quad (\text{mod } 65536)
\label{eq:uart_checksum}
\end{equation}
\begin{equation}
\text{Valid Frame} \iff \text{Checksum}_{\text{calc}} == \left( \text{Byte}[30] \ll 8 \right) + \text{Byte}[31]
\label{eq:uart_validity}
\end{equation}
Packets failing Eq. \eqref{eq:uart_validity} are discarded, preventing corrupted data from contaminating the cloud feature store.

\subsection{FreeRTOS Firmware Implementation Snippet}
Listing \ref{lst:esp32_firmware} illustrates the core FreeRTOS task creation, sensor polling, and JSON telemetry construction implemented in the firmware.

\begin{lstlisting}[language=C++,caption={Core FreeRTOS dual-task scheduling and HTTP telemetry transmission in ESP32 firmware.},label={lst:esp32_firmware}]
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <DHT.h>
#include <Adafruit_SSD1306.h>

#define DHTPIN 4
#define DHTTYPE DHT22
#define MQ135_PIN 34
#define TIME_TO_SLEEP 900 // 15 minutes sleep

DHT dht(DHTPIN, DHTTYPE);
Adafruit_SSD1306 display(128, 64, &Wire, -1);

struct SensorTelemetry {
  float pm25;
  float pm10;
  float temp;
  float humidity;
  int mq135_raw;
  float battery_volts;
} currentData;

void sensorTask(void *pvParameters) {
  for(;;) {
    currentData.temp = dht.readTemperature();
    currentData.humidity = dht.readHumidity();
    currentData.mq135_raw = analogRead(MQ135_PIN);
    currentData.battery_volts = analogRead(35) * (3.3 / 4095.0) * 2.0;
    
    // Read PMS5003 via HardwareSerial Serial2
    if (Serial2.available() >= 32) {
      uint8_t buffer[32];
      Serial2.readBytes(buffer, 32);
      if (buffer[0] == 0x42 && buffer[1] == 0x4D) {
        currentData.pm25 = (buffer[12] << 8) | buffer[13];
        currentData.pm10 = (buffer[14] << 8) | buffer[15];
      }
    }
    vTaskDelay(pdMS_TO_TICKS(2000));
  }
}
\end{lstlisting}

\section{Cloud Backend Microservices Architecture on Render}
To process, store, and serve the streaming environmental telemetry, a cloud-hosted microservice backend was deployed on the \textbf{Render} cloud platform. Render provides scalable containerized application hosting with continuous automated Git deployment, automated SSL/TLS encryption, and 99.9\% service availability.

\begin{figure}[H]
\centering
\includegraphics[width=0.70\textwidth]{page_35_21_Image203.png}
\caption[Render cloud platform backend]{Render cloud microservices platform hosting the Python Flask REST API server and persistent time-series database.}
\label{fig:render_dashboard_overview}
\end{figure}

The backend service is developed in Python using the \textbf{Flask} web framework, selected for its micro-footprint, high asynchronous throughput, and seamless integration with scientific Python libraries (NumPy, Scikit-Learn, Pandas).

\subsection{RESTful API Endpoint Architecture}
The Flask application exposes five core RESTful API endpoints:
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \texttt{POST /api/telemetry:} Ingests streaming JSON payloads dispatched by the ESP32 node. The endpoint validates payload integrity, computes the real-time CPCB sub-index using Eq. \eqref{eq:cpcb_subindex}, triggers the Stage 1 calibration algorithm, and persists the timestamped observation into the relational database.
    \item \texttt{GET /api/current:} Returns the most recent environmental snapshot, including calibrated $\text{PM}_{2.5}$, composite AQI, ambient weather, battery State of Charge, and network health indicators.
    \item \texttt{GET /api/history?window=24h:} Retrieves historical time-series vectors formatted for Chart.js client-side rendering over user-selected intervals (24 hours, 7 days, 30 days).
    \item \texttt{GET /api/forecast:} Executes the Stage 2 machine learning predictive model using the latest 24 hourly lag observations stored in the database. Returns predicted $\text{PM}_{2.5}$ concentrations and risk tiers for 1-hour, 6-hour, 12-hour, and 24-hour future horizons.
    \item \texttt{GET /api/weather:} Fetches localized meteorological context (wind speed, wind direction, barometric pressure) via real-time integration with the OpenWeatherMap API for Sundernagar, H.P.
\end{enumerate}

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.48\textwidth}
\centering
\includegraphics[width=0.82\textwidth]{page_38_25_Image210.png}
\caption{Flask server execution terminal and log streams.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.48\textwidth}
\centering
\includegraphics[width=0.82\textwidth]{page_38_26_Image211.png}
\caption{REST API endpoint response inspection.}
\end{subfigure}
\caption[Flask backend execution and request logs]{Cloud backend server execution environment on Render showing active request logging and JSON serialization pipelines.}
\label{fig:flask_backend_logs}
\end{figure}

\section{Interactive Web Dashboard and Hyperlocal GIS Interface}
The front-end user interface is designed as an interactive, single-page progressive web application (PWA) constructed using HTML5, modern CSS3 styling, and modular asynchronous JavaScript (ES6+).

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.48\textwidth}
\centering
\includegraphics[width=0.82\textwidth]{page_36_22_Image205.png}
\caption{Real-time AQI and temperature cards.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.48\textwidth}
\centering
\includegraphics[width=0.82\textwidth]{page_36_23_Image206.png}
\caption{Humidity and particulate matter cards.}
\end{subfigure}
\caption[Real-time environmental status cards]{Responsive real-time environmental metric cards displaying live telemetry and health status categories.}
\label{fig:dashboard_metric_cards}
\end{figure}

\subsection{Key UI Modules and Visual Components}
\begin{itemize}[leftmargin=2em]
    \item \textbf{Dynamic Environmental Status Cards:} Real-time metric cards (Fig. \ref{fig:dashboard_metric_cards}) display instantaneous readings for $\text{PM}_{2.5}$, $\text{PM}_{10}$, MQ-135 air quality, temperature, and relative humidity. Each card features dynamic background color transitions based on CPCB health category thresholds.
    \item \textbf{Interactive Telemetry Visualizations:} Powered by Chart.js, the historical telemetry module (Fig. \ref{fig:chartjs_graph}) renders multi-axis time-series curves enabling users to toggle individual sensor traces, inspect localized diurnal peaks, and zoom into specific temporal events.
    \item \textbf{Hyperlocal GIS Mapping Integration:} Utilizing Leaflet.js with OpenStreetMap cartography, the dashboard pinpoints the exact geographic deployment locus of the ATMOS node in Sundernagar (Latitude $31.515355^\circ\,\text{N}$, Longitude $76.878331^\circ\,\text{E}$). A color-coded pulsing marker visualizes the immediate micro-zone air quality category.
    \item \textbf{AI Trend Forecasting Widget:} Visualizes the forward-looking predictions generated by the machine learning engine (Fig. \ref{fig:forecast_cards}), providing actionable early warnings regarding impending pollution spikes.
    \item \textbf{Meteorological Contextualization:} Real-time weather cards (Fig. \ref{fig:weather_cards}) stream atmospheric pressure, cloud cover, and wind vectors, enabling correlation of wind dispersion with particulate clearance.
\end{itemize}

\begin{figure}[H]
\centering
\includegraphics[width=0.70\textwidth]{page_37_24_Image208.png}
\caption[Interactive Chart.js telemetry visualization]{Interactive Chart.js telemetry visualization showing real-time multi-sensor historical trends and diurnal variations.}
\label{fig:chartjs_graph}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.48\textwidth}
\centering
\includegraphics[width=0.82\textwidth]{page_40_29_Image216.png}
\caption{AI trend forecasting cards.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.48\textwidth}
\centering
\includegraphics[width=0.82\textwidth]{page_41_30_Image218.png}
\caption{OpenWeatherMap meteorological integration.}
\end{subfigure}
\caption[Predictive trend cards and meteorological integration]{Dashboard analytical modules: (a) machine learning predictive trend cards, and (b) regional meteorological context integration.}
\label{fig:forecast_and_weather}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[width=0.70\textwidth]{page_43_33_Image223.png}
\caption[Leaflet GIS geographical mapping interface]{Leaflet OpenStreetMap GIS interface showing the geographic deployment coordinate of the ATMOS node in Sundernagar, H.P.}
\label{fig:leaflet_map}
\end{figure}

\section{Automated Early Warning and Alert Engine}
To provide actionable public health protection, the backend incorporates an automated alert dispatch service utilizing the Simple Mail Transfer Protocol (SMTP). 

When incoming telemetry triggers any of the following critical conditions:
\begin{enumerate}[label=(\roman*)]
    \item $\text{Composite AQI} > 200$ (Entering ``Poor'' or ``Very Poor'' CPCB category),
    \item $\text{PM}_{2.5} > 120\,\mu\text{g/m}^3$ sustained over three consecutive measurement cycles,
    \item Predicted 1-hour ahead $\text{PM}_{2.5} > 150\,\mu\text{g/m}^3$ (Imminent toxic smog episode),
\end{enumerate}
the alert engine automatically formats and dispatches high-priority email notifications to registered municipal officials, school administrators, and vulnerable citizen subscribers. The alert payload specifies the active pollutant, clinical health risks, and recommended mitigation actions (such as closing classroom ventilation dampers or issuing outdoor activity advisories).
"""
