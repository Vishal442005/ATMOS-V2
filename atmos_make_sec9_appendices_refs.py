# atmos_make_sec9_appendices_refs.py

def get_appendices_and_refs():
    return r"""%% ==========================================================================
%%  REFERENCES & APPENDICES
%% ==========================================================================

\cleardoublepage
\phantomsection
\addcontentsline{toc}{chapter}{References}

\begin{thebibliography}{99}
\small
\setlength{\itemsep}{2pt}

\bibitem{who2021}
World Health Organization, \emph{WHO Global Air Quality Guidelines: Particulate Matter ($\text{PM}_{2.5}$ and $\text{PM}_{10}$), Ozone, Nitrogen Dioxide, Sulfur Dioxide and Carbon Monoxide}, World Health Organization, Geneva, Switzerland, 2021.

\bibitem{cpcb2014}
Central Pollution Control Board (CPCB), \emph{National Air Quality Index: Report of the Technical Study Group}, Ministry of Environment, Forest and Climate Change, Government of India, New Delhi, Oct. 2014.

\bibitem{bohren1983}
C.~F.~Bohren and D.~R.~Huffman, \emph{Absorption and Scattering of Light by Small Particles}, John Wiley \& Sons, New York, NY, USA, 1983.

\bibitem{vandeHulst1981}
H.~C.~van de Hulst, \emph{Light Scattering by Small Particles}, Dover Publications, Mineola, NY, USA, 1981.

\bibitem{hanel1976}
G.~H\"anel, ``The properties of atmospheric aerosol particles as functions of the relative humidity at thermodynamic equilibrium with the surrounding moist air,'' \emph{Advances in Geophysics}, vol. 19, pp. 73--188, 1976.

\bibitem{petters2007}
M.~D.~Petters and S.~M.~Kreidenweis, ``A single parameter representation of hygroscopic growth and cloud condensation nucleus activity,'' \emph{Atmospheric Chemistry and Physics}, vol. 7, no. 8, pp. 1961--1971, 2007.

\bibitem{schwab2006}
J.~J.~Schwab, O.~V.~Rattigan, H.~D.~Felton, and K.~L.~Demerjian, ``Continuous ambient air quality monitoring: Beta attenuation monitor field evaluations and sampling artifacts,'' \emph{Atmospheric Environment}, vol. 40, pp. 433--444, 2006.

\bibitem{patashnick1991}
H.~Patashnick and E.~G.~Rupprecht, ``Continuous PM-10 measurements using the tapered element oscillating microbalance,'' \emph{Journal of the Air \& Waste Management Association}, vol. 41, no. 8, pp. 1079--1083, 1991.

\bibitem{zheng2018}
T.~Zheng, M.~H.~Bergin, K.~K.~Johnson, S.~N.~Tripathi, S.~Shirodkar, P.~S.~Landis, R.~Sutaria, and D.~E.~Carlson, ``Field evaluation of low-cost particulate matter sensors in Delhi, India,'' \emph{Atmospheric Measurement Techniques}, vol. 11, no. 8, pp. 4811--4826, 2018.

\bibitem{badura2019}
M.~Badura, P.~Batog, A.~Drzeniecka-Osiadacz, and P.~Modzel, ``Evaluation of low-cost sensors for ambient $\text{PM}_{2.5}$ monitoring in an urban environment,'' \emph{Building and Environment}, vol. 161, art. no. 106249, 2019.

\bibitem{magi2020}
B.~I.~Magi, C.~Cuprewich, P.~Heinzelman, and M.~Eppes, ``Evaluation of low-cost optical particulate matter sensors for indoor and outdoor air quality monitoring,'' \emph{Aerosol Science and Technology}, vol. 54, no. 2, pp. 147--159, 2020.

\bibitem{sayahi2019}
T.~Sayahi, A.~Butterfield, and K.~E.~Kelly, ``Long-term field evaluation of the Plantower PMS low-cost particulate matter sensor in Salt Lake City, Utah,'' \emph{Aerosol Science and Technology}, vol. 53, no. 9, pp. 1022--1037, 2019.

\bibitem{zimmerman2018}
N.~Zimmerman, A.~A.~Presto, S.~P.~S.~Kumar, J.~Gu, G.~J.~Hauryliuk, E.~S.~Robinson, and R.~Subramanian, ``A machine learning calibration model using random forests to improve sensor-based air quality measurements,'' \emph{Atmospheric Measurement Techniques}, vol. 11, no. 1, pp. 291--313, 2018.

\bibitem{malings2019}
C.~Malings, R.~Tanzer, A.~Hauryliuk, S.~P.~S.~Kumar, and R.~Subramanian, ``Development of a general calibration model and sensor evaluation for low-cost particulate matter sensors,'' \emph{Atmospheric Measurement Techniques}, vol. 13, pp. 2489--2507, 2020.

\bibitem{devito2008}
S.~De Vito, E.~Massera, M.~Piga, L.~Martinotto, and G.~Di Francia, ``On-field calibration of an electronic nose for benzene estimation in an urban monitoring scenario,'' \emph{Sensors and Actuators B: Chemical}, vol. 129, no. 2, pp. 750--757, 2008.

\bibitem{ali2024}
M.~Ali, A.~Sharif, and K.~Mehmood, ``Harnessing temporal dynamics for enhanced machine learning calibration of low-cost environmental sensors,'' \emph{IEEE Sensors Journal}, vol. 24, no. 6, pp. 8412--8423, 2024.

\bibitem{breiman2001}
L.~Breiman, ``Random Forests,'' \emph{Machine Learning}, vol. 45, no. 1, pp. 5--32, 2001.

\bibitem{chen2016}
T.~Chen and C.~Guestrin, ``XGBoost: A scalable tree boosting system,'' in \emph{Proc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery and Data Mining}, San Francisco, CA, USA, 2016, pp. 785--794.

\bibitem{ke2017}
G.~Ke, Q.~Meng, T.~Finley, T.~Wang, W.~Chen, W.~Ma, Q.~Ye, and T.-Y.~Liu, ``LightGBM: A highly efficient gradient boosting decision tree,'' \emph{Advances in Neural Information Processing Systems (NeurIPS)}, vol. 30, pp. 3146--3154, 2017.

\bibitem{hochreiter1997}
S.~Hochreiter and J.~Schmidhuber, ``Long short-term memory,'' \emph{Neural Computation}, vol. 9, no. 8, pp. 1735--1780, 1997.

\bibitem{boxjenkins2015}
G.~E.~P.~Box, G.~M.~Jenkins, G.~C.~Reinsel, and G.~M.~Ljung, \emph{Time Series Analysis: Forecasting and Control}, 5th ed., John Wiley \& Sons, Hoboken, NJ, USA, 2015.

\bibitem{hyndman2018}
R.~J.~Hyndman and G.~Athanasopoulos, \emph{Forecasting: Principles and Practice}, 2nd ed., OTexts, Melbourne, Australia, 2018.

\bibitem{raghunathan2005}
V.~Raghunathan, A.~Kansal, J.~Hsu, J.~Friedman, and M.~Srivastava, ``Design considerations for solar energy harvesting wireless embedded systems,'' in \emph{Proc. 4th Int. Symp. Information Processing in Sensor Networks (IPSN)}, Los Angeles, CA, USA, 2005, pp. 457--462.

\bibitem{kansal2007}
A.~Kansal, J.~Hsu, S.~Zahedi, and M.~B.~Srivastava, ``Power management in energy harvesting sensor networks,'' \emph{ACM Transactions on Embedded Computing Systems}, vol. 6, no. 4, art. no. 32, 2007.

\bibitem{espressif2023}
Espressif Systems, \emph{ESP32 Technical Reference Manual (Version 5.0)}, Espressif Systems Co., Ltd., Shanghai, China, 2023.

\bibitem{plantower2016}
Plantower Technology, \emph{PMS5003 Digital Universal Particle Concentration Sensor Data Sheet}, Beijing Plantower Co., Ltd., Beijing, China, 2016.

\bibitem{hanwei2015}
Zhengzhou Winsen Electronics Technology, \emph{MQ-135 Semiconductor Sensor for Air Quality Manual}, Zhengzhou, Henan, China, 2015.

\bibitem{kumar2023}
A.~Kumar, S.~Singh, and R.~K.~Sharma, ``Autonomous solar-powered air pollution monitoring node using IoT and chemoresistive sensors in sub-Himalayan valleys,'' \emph{Environmental Monitoring and Assessment}, vol. 195, art. no. 412, 2023.

\bibitem{tiwary2018}
A.~Tiwary, I.~D.~Williams, and V.~Colls, \emph{Air Pollution: Measurement, Modelling and Mitigation}, 4th ed., CRC Press, Boca Raton, FL, USA, 2018.

\bibitem{seinfeld2016}
J.~H.~Seinfeld and S.~N.~Pandis, \emph{Atmospheric Chemistry and Physics: From Air Pollution to Climate Change}, 3rd ed., John Wiley \& Sons, Hoboken, NJ, USA, 2016.

\end{thebibliography}

\newpage

%% ==========================================================================
%%  APPENDIX A: EMBEDDED FIRMWARE SOURCE CODE (STRICTLY 1 PAGE)
%% ==========================================================================
\chapter*{Appendix A: Master Embedded Firmware}
\addcontentsline{toc}{chapter}{Appendix A: Master Embedded Firmware}

The following firmware implementation is written in C++ for the Espressif ESP32 dual-core microcontroller under FreeRTOS, demonstrating hardware initialization, multi-channel sensor acquisition, JSON serialization, and power-managed deep-sleep scheduling.

\begin{lstlisting}[language=C++,basicstyle=\ttfamily\tiny,lineskip=-0.8pt,caption={Core ESP32 Arduino/FreeRTOS embedded firmware for the ATMOS node.},label={lst:full_firmware}]
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <DHT.h>
#include <Wire.h>
#include <Adafruit_SSD1306.h>

#define DHTPIN 4
#define DHTTYPE DHT22
#define MQ135_PIN 34
#define BATTERY_PIN 35
#define uS_TO_S_FACTOR 1000000ULL
#define TIME_TO_SLEEP 900 // 15 minutes sleep interval

const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";
const char* serverEndpoint = "https://atmos-aqi-api.onrender.com/api/telemetry";

DHT dht(DHTPIN, DHTTYPE);
Adafruit_SSD1306 display(128, 64, &Wire, -1);

struct SensorReading {
  float pm25, pm10, temp, rh, vbat;
  int mq135_raw;
} data;

void setup() {
  Serial.begin(115200);
  Serial2.begin(9600, SERIAL_8N1, 16, 17); // PMS5003 UART
  dht.begin();
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextColor(WHITE);
  display.println("ATMOS Sensing...");
  display.display();
  delay(5000); // Sensor stabilization
  
  data.temp = dht.readTemperature();
  data.rh = dht.readHumidity();
  data.mq135_raw = analogRead(MQ135_PIN);
  data.vbat = analogRead(BATTERY_PIN) * (3.3 / 4095.0) * 2.0;
  
  if (Serial2.available() >= 32) {
    uint8_t buf[32];
    Serial2.readBytes(buf, 32);
    if (buf[0] == 0x42 && buf[1] == 0x4D) {
      data.pm25 = (buf[12] << 8) | buf[13];
      data.pm10 = (buf[14] << 8) | buf[15];
    }
  }
  
  WiFi.begin(ssid, password);
  int tries = 0;
  while (WiFi.status() != WL_CONNECTED && tries++ < 15) delay(500);
  
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverEndpoint);
    http.addHeader("Content-Type", "application/json");
    StaticJsonDocument<256> doc;
    doc["node_id"] = "ATMOS_JNGEC_01";
    doc["raw_pm25"] = data.pm25;
    doc["temp"] = data.temp;
    doc["rh"] = data.rh;
    doc["mq135"] = data.mq135_raw;
    doc["vbat"] = data.vbat;
    String json;
    serializeJson(doc, json);
    http.POST(json);
    http.end();
  }
  
  WiFi.disconnect(true);
  display.ssd1306_command(SSD1306_DISPLAYOFF);
  esp_sleep_enable_timer_wakeup(TIME_TO_SLEEP * uS_TO_S_FACTOR);
  esp_deep_sleep_start();
}
void loop() {}
\end{lstlisting}

\newpage

%% ==========================================================================
%%  APPENDIX B: BILL OF MATERIALS & ECONOMIC FEASIBILITY (STRICTLY 1 PAGE)
%% ==========================================================================
\chapter*{Appendix B: Bill of Materials and Economic Feasibility}
\addcontentsline{toc}{chapter}{Appendix B: Bill of Materials and Economic Feasibility}

\vspace{-0.2cm}
\begin{table}[H]
\centering
\scriptsize
\caption{Comprehensive Bill of Materials (BOM) and manufacturing cost analysis for the ATMOS node.}
\label{tab:bom_detailed}
\begin{tabularx}{\textwidth}{|p{0.18\textwidth}|p{0.24\textwidth}|c|p{0.18\textwidth}|r|r|}
\hline
\textbf{Subsystem} & \textbf{Component Description} & \textbf{Qty} & \textbf{Part / Vendor} & \textbf{Cost (INR)} & \textbf{Cost (USD)} \\
\hline
\textbf{Core Processor} & ESP32-WROOM-32 Dev Board & 1 & Espressif Systems & 380 & \$4.58 \\
\hline
\textbf{Particulate Sensor} & PMS5003 Laser Particle Counter & 1 & Plantower Technology & 2,200 & \$26.50 \\
\hline
\textbf{Gas Sensor Array} & MQ-135 Multi-Gas / Air Quality & 1 & Zhengzhou Winsen & 150 & \$1.81 \\
\hline
\textbf{Climate Telemetry} & DHT22 (AM2302) Temp \& Humidity & 1 & Aosong Electronics & 280 & \$3.37 \\
\hline
\textbf{Local Display} & SSD1306 0.96-inch OLED (I2C) & 1 & Solomon Systech & 180 & \$2.17 \\
\hline
\textbf{Energy Harvesting} & 6V 2W Monocrystalline PV Panel & 1 & Generic High-Eff & 450 & \$5.42 \\
\hline
\textbf{Battery Storage} & 18650 Li-ion Cells (2200mAh $\times$ 2) & 2 & Panasonic / LG & 440 & \$5.30 \\
\hline
\textbf{Charge Controller} & TP4056 CC/CV Protection Module & 1 & NanJing Top Power & 45 & \$0.54 \\
\hline
\textbf{Power Conditioning} & AMS1117-3.3 + Step-Up Regulator & 2 & Advanced Monolithic & 75 & \$0.90 \\
\hline
\textbf{Mechanical Housing} & Weatherproof Stevenson Box & 1 & Custom 3D Printed & 650 & \$7.83 \\
\hline
\textbf{Passive Hardware} & Resistors, Capacitors, Wiring, PCB & 1 & Multicomp Pro & 250 & \$3.01 \\
\hline
\multicolumn{4}{|r|}{\textbf{Total Hardware Component Cost}} & \textbf{INR 5,100} & \textbf{\$61.44} \\
\hline
\multicolumn{4}{|r|}{\textbf{Assembly, Testing \& Margin (25\%)}} & \textbf{INR 1,275} & \textbf{\$15.36} \\
\hline
\multicolumn{4}{|r|}{\textbf{Complete Unit Manufacturing Cost}} & \textbf{INR 6,375} & \textbf{\$76.80} \\
\hline
\end{tabularx}
\end{table}

\vspace{-0.3cm}
\subsubsection*{Comparative Economic Assessment against Regulatory CAAQMS}
As demonstrated in Table \ref{tab:bom_detailed}, the complete unit manufacturing cost of an autonomous ATMOS node is approximately \textbf{INR 6,375 (\$76.80 USD)}. Compared to a single continuous ambient regulatory station (CAAQMS) utilizing a Met One BAM-1020, which demands a minimum capital expenditure of \textbf{INR 35,00,000 (\$42,000 USD)}:
\begin{equation}
\text{Cost Ratio} = \frac{\text{Cost}_{\text{CAAQMS}}}{\text{Cost}_{\text{ATMOS}}} = \frac{\text{INR } 35,00,000}{\text{INR } 6,375} \approx 549\times
\label{eq:cost_ratio}
\end{equation}
For the financial investment required to install and maintain just \textbf{one} central CAAQMS station, a municipal government or smart city development authority can manufacture, configure, and deploy over \textbf{500 distributed ATMOS nodes}. This provides unprecedented spatial granularity, transforming air pollution management from coarse regional estimates into fine-scale, street-by-street actionable intelligence.

\end{document}
"""
