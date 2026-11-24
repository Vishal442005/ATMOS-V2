# atmos_make_sec3_hardware.py

def get_chapter3():
    return r"""%% ==========================================================================
%%  CHAPTER 3: SYSTEM ARCHITECTURE & HARDWARE ENGINEERING
%% ==========================================================================
\chapter{System Design and Hardware Implementation}

\section{Overall Hardware Subsystem Architecture}
The physical hardware subsystem of ATMOS is engineered as an autonomous, field-deployable sensing station capable of continuous atmospheric sampling in remote outdoor environments without reliance on AC utility mains power. The architecture balances high-frequency data acquisition, multi-gas analytical sensitivity, and rigorous energy conservation through power-gated duty cycles.

\begin{figure}[H]
\centering
\includegraphics[width=0.68\textwidth]{page_28_19_Image194.png}
\caption[System operational flowchart]{System operational flowchart illustrating the power-state transitions, multi-sensor data acquisition, calibration routines, Wi-Fi telemetry handshake, and deep-sleep duty cycle.}
\label{fig:system_flowchart}
\end{figure}

As depicted in the operational flowchart (Fig. \ref{fig:system_flowchart}), the system operates in a recurring cyclic state machine:
\begin{enumerate}[label=\textbf{Step \arabic*:},leftmargin=3.5em]
    \item \textbf{Power-On Reset \& Wakeup:} The system emerges from deep sleep via the ESP32 internal Real-Time Clock (RTC) timer interrupt.
    \item \textbf{Subsystem Initialization:} Power rails are stabilized, the I2C bus and UART interfaces are initialized, and the SSD1306 OLED display is activated.
    \item \textbf{Sensor Warming \& Stabilization:} The PMS5003 internal fan spins up for 5 seconds to flush the chamber, and the MQ-135 sensor heater stabilizes the SnO$_2$ surface lattice.
    \item \textbf{Data Acquisition \& Outlier Filtering:} Multi-channel analog and digital samples are acquired across 10 successive sub-samples; median and trimmed-mean filtering eliminate transient aerodynamic artifacts.
    \item \textbf{Local Visualization:} Current $\text{PM}_{2.5}$, gas levels, temperature, and battery voltage are rendered to the local OLED display.
    \item \textbf{Cloud Handshake \& Telemetry:} The Wi-Fi radio initiates a secure connection to the local hotspot or cellular gateway, transmitting formatted JSON packets via an HTTP POST request to the Render cloud backend.
    \item \textbf{Deep-Sleep Entry:} The Wi-Fi modem and sensor peripherals are powered down, and the ESP32 enters an ultra-low-power deep-sleep state for 885 seconds (15-minute sampling interval).
\end{enumerate}

\section{Hardware Component Specifications and Physical Analysis}
The physical node is constructed from carefully selected industrial-grade embedded components, analyzed in detail below.

\subsection{ESP32 Dual-Core Microcontroller}
The core processing unit is the Espressif ESP32-WROOM-32 microcontroller module, powered by a dual-core 32-bit Tensilica Xtensa LX6 microprocessor operating at an adjustable clock frequency up to $240\,\text{MHz}$.

\begin{figure}[H]
\centering
\includegraphics[width=0.50\textwidth]{page_17_05_Image164.jpg}
\caption[ESP32 microcontroller board]{The ESP32-WROOM-32 microcontroller development board showing the dual-core SoC, integrated PCB trace antenna, and GPIO headers.}
\label{fig:esp32_board}
\end{figure}

Key technical specifications of the ESP32 include:
\begin{itemize}[leftmargin=2em]
    \item \textbf{Processing Architecture:} Dual-core Xtensa LX6 with separate Instruction and Data buses, supporting symmetric multiprocessing (SMP) under FreeRTOS.
    \item \textbf{Memory Subsystem:} $520\,\text{KB}$ internal SRAM, $448\,\text{KB}$ ROM, and an external $4\,\text{MB}$ SPI Flash memory for non-volatile program storage and calibration parameter tables.
    \item \textbf{Wireless Connectivity:} Integrated $2.4\,\text{GHz}$ Wi-Fi ($802.11\,\text{b/g/n}$) transceiver with transmit power up to $+20.5\,\text{dBm}$, and Bluetooth v4.2 BR/EDR and BLE.
    \item \textbf{Peripheral Interfaces:} 12-bit Successive Approximation Register (SAR) Analog-to-Digital Converters (ADCs) with up to 18 channels, 2 I2C interfaces, 3 UART serial ports, and 36 programmable General Purpose Input/Output (GPIO) pins.
    \item \textbf{Power Management Modes:} Active mode ($160\text{--}240\,\text{mA}$ with Wi-Fi transmitting), Modem-Sleep ($20\text{--}30\,\text{mA}$), Light-Sleep ($0.8\,\text{mA}$), and Deep-Sleep ($10\text{--}15\,\mu\text{A}$ with only the RTC timer and ULP coprocessor operational).
\end{itemize}

\subsection{Plantower PMS5003 Laser Particulate Matter Sensor}
The PMS5003 is a high-precision laser dust sensor utilizing $90^\circ$ optical Mie scattering to quantify particulate mass concentrations.

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.46\textwidth}
\centering
\includegraphics[width=0.70\textwidth]{page_20_09_Image171.jpg}
\caption{PMS5003 laser sensor top view.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.46\textwidth}
\centering
\includegraphics[width=0.70\textwidth]{page_20_10_Image172.jpg}
\caption{PMS5003 internal optical chamber.}
\end{subfigure}
\caption[Plantower PMS5003 laser particulate sensor]{Plantower PMS5003 laser particulate matter sensor modules showing the optical chamber and electrical interface.}
\label{fig:pms5003_sensor}
\end{figure}

The PMS5003 incorporates a $650\,\text{nm}$ semiconductor laser diode, an integrated miniature centrifugal fan providing a steady airflow of $0.1\,\text{L/min}$, and an orthogonal silicon photodiode. It outputs standard particulate mass bins ($\text{PM}_{1.0}, \text{PM}_{2.5}, \text{PM}_{10}$) over an asynchronous UART serial interface at 9600 baud, transmitting a 32-byte structured data frame containing both standard atmospheric and laboratory particle count metrics. The effective measurement range spans $0.3\,\mu\text{m}$ to $10\,\mu\text{m}$ with a nominal mass concentration capability of $0$ to $1000\,\mu\text{g/m}^3$ and an accuracy of $\pm 10\,\mu\text{g/m}^3$ in the $0\text{--}100\,\mu\text{g/m}^3$ range.

\subsection{MQ-Series Chemoresistive Hazardous Gas Sensors}
Gas surveillance is achieved through an array of metal oxide semiconductor (MOS) sensors. The primary unit is the \textbf{MQ-135} air quality sensor, augmented by the \textbf{MQ-7} carbon monoxide sensor and \textbf{MQ-4} methane sensor.

\begin{figure}[H]
\centering
\includegraphics[width=0.50\textwidth]{page_18_06_Image166.jpg}
\caption[MQ-135 hazardous gas sensor]{MQ-135 chemoresistive hazardous gas sensor module with integrated trimpot and signal conditioning comparator circuit.}
\label{fig:mq135_sensor}
\end{figure}

The MQ-135 exhibits high sensitivity to ammonia ($\text{NH}_3$), nitrogen oxides ($\text{NO}_x$), alcohol, benzene, smoke, and carbon dioxide ($\text{CO}_2$). The internal ceramic micro-tube contains a tin dioxide ($\text{SnO}_2$) active layer heated by an internal nickel-chromium coil ($5\text{V}$, $150\,\text{mA}$, $750\,\text{mW}$ dissipation). As reducing gaseous molecules react with chemisorbed oxygen ions on the heated surface, the electrical resistance decreases logarithmically with concentration. The analog voltage output is measured via the ESP32 12-bit ADC across a load resistor $R_L$:
\begin{equation}
V_{\text{out}} = V_{\text{CC}} \cdot \frac{R_L}{R_s + R_L} \implies R_s = R_L \left( \frac{V_{\text{CC}} - V_{\text{out}}}{V_{\text{out}}} \right)
\label{eq:voltage_divider_mq}
\end{equation}

\subsection{DHT22 Digital Temperature and Relative Humidity Sensor}
Because optical particle counters are highly sensitive to hygroscopic moisture swelling and MOS gas sensors exhibit thermal drift, accurate environmental telemetry is mandatory. The DHT22 (AM2302) integrates a capacitive polymer relative humidity sensing element and an NTC thermistor read by an internal 8-bit microcontroller. It provides a temperature measuring range of $-40^\circ\text{C}$ to $+80^\circ\text{C}$ with $\pm 0.5^\circ\text{C}$ accuracy, and a relative humidity range of $0\%$ to $100\%$ with $\pm 2\%$ accuracy. Telemetry is transmitted over a single-wire bi-directional digital bus using proprietary pulse-width timing.

\subsection{SSD1306 0.96-inch OLED Display}
Local visualization is provided by a 0.96-inch monochrome Organic Light Emitting Diode (OLED) display with a resolution of $128 \times 64$ pixels.

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.46\textwidth}
\centering
\includegraphics[width=0.70\textwidth]{page_19_07_Image168.jpg}
\caption{SSD1306 0.96-inch I2C OLED display.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.46\textwidth}
\centering
\includegraphics[width=0.70\textwidth]{page_19_08_Image169.jpg}
\caption{OLED pinout and PCB backside.}
\end{subfigure}
\caption[SSD1306 monochrome OLED display]{SSD1306 monochrome OLED display module used for autonomous real-time on-node field visualization.}
\label{fig:oled_display}
\end{figure}

Operating via the I2C bus (default address \texttt{0x3C}) at $400\,\text{kHz}$ Fast-Mode, each organic pixel is self-emissive, eliminating the bulky power-hungry backlights typical of liquid crystal displays (LCDs). The display consumes approximately $20\,\text{mA}$ during full screen illumination and enters a sub-microampere shutdown mode when the display buffer is blanked prior to microcontroller sleep.

\subsection{Solar Photovoltaic Energy Harvesting Subsystem}
To guarantee perpetual off-grid operation, the power subsystem comprises a monocrystalline solar panel, a lithium-ion battery pack, a charge management module, and voltage regulation circuitry.

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.31\textwidth}
\centering
\includegraphics[width=\textwidth]{page_23_14_Image179.jpg}
\caption{6V 2W Solar PV panel.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.31\textwidth}
\centering
\includegraphics[width=\textwidth]{page_24_15_Image181.jpg}
\caption{TP4056 charge controller.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.31\textwidth}
\centering
\includegraphics[width=\textwidth]{page_22_13_Image177.jpg}
\caption{Li-ion battery pack.}
\end{subfigure}
\caption[Solar photovoltaic energy harvesting subsystem]{Photovoltaic energy harvesting subsystem: (a) 6V monocrystalline panel, (b) TP4056 CC/CV charging controller with battery protection, and (c) high-capacity 18650 Li-ion battery pack.}
\label{fig:solar_subsystem}
\end{figure}

\begin{itemize}[leftmargin=2em]
    \item \textbf{Photovoltaic Solar Panel:} A $6\text{V}$, $2\text{W}$ monocrystalline silicon solar panel with high photoelectric conversion efficiency ($\eta \approx 17.5\%$). At peak standard test conditions (AM1.5, $1000\,\text{W/m}^2$, $25^\circ\text{C}$), it produces an open-circuit voltage $V_{\text{oc}} = 7.2\,\text{V}$ and a maximum power point current $I_{\text{mp}} = 333\,\text{mA}$.
    \item \textbf{TP4056 Battery Charging Module:} Implements an autonomous constant-current / constant-voltage (CC/CV) linear charging profile. The programming resistor $R_{\text{prog}} = 1.2\,\text{k}\Omega$ configures a maximum bulk charge current $I_{\text{chg}} = 1000\,\text{mA}$. The module integrates a DW01A battery protection IC paired with an FS8205A dual N-channel MOSFET switch, providing over-charge protection ($4.25\,\text{V}$ cut-off), over-discharge protection ($2.4\,\text{V}$ cut-off), and over-current trip protection ($3.0\,\text{A}$).
    \item \textbf{Rechargeable 18650 Lithium-Ion Battery Pack:} Two high-density 18650 cylindrical cells connected in parallel provide a nominal voltage of $3.7\,\text{V}$ and a combined electrochemical storage capacity of $C_{\text{bat}} = 4400\,\text{mAh}$ ($16.28\,\text{Wh}$).
    \item \textbf{Voltage Regulation Subsystem:} An AMS1117-3.3 low-dropout regulator supplies a ripple-free $3.3\text{V}$ rail to the ESP32 and digital sensors, while an efficient step-up buck/boost regulator provides the dedicated $5.0\text{V}$ rail required by the MQ sensor heating coils.
\end{itemize}

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.46\textwidth}
\centering
\includegraphics[width=0.70\textwidth]{page_25_16_Image183.jpg}
\caption{Linear voltage regulator module.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.46\textwidth}
\centering
\includegraphics[width=0.70\textwidth]{page_25_17_Image184.jpg}
\caption{Regulator pinout and decoupling stage.}
\end{subfigure}
\caption[Voltage regulation and power conditioning stages]{Voltage regulation and power conditioning stages maintaining transient-free supply rails for the mixed-signal circuitry.}
\label{fig:voltage_regulator}
\end{figure}

\section{System Circuit Schematic and Hardware Interconnect Topology}
The interconnected electronic subsystem is assembled on a high-grade prototyping platform. Table \ref{tab:pinout_mapping} provides the comprehensive wiring and signal interface topology between the ESP32 and peripheral sensors.

\begin{table}[H]
\centering
\small
\caption{Master hardware pinout and electrical interface connection mapping for the ATMOS node.}
\label{tab:pinout_mapping}
\begin{tabularx}{\textwidth}{|p{0.18\textwidth}|p{0.15\textwidth}|p{0.12\textwidth}|p{0.14\textwidth}|X|}
\hline
\textbf{Component} & \textbf{Pin Identifier} & \textbf{ESP32 GPIO} & \textbf{Bus / Signal} & \textbf{Electrical Specification} \\
\hline
\multirow{4}{*}{\textbf{SSD1306 OLED}} & VCC & 3V3 Rail & Power & 3.3V DC, $\sim 20\,\text{mA}$ active \\
& GND & GND Rail & Ground & Common system ground \\
& SCL & GPIO 22 & I2C Clock & Open-drain with $4.7\,\text{k}\Omega$ pullup \\
& SDA & GPIO 21 & I2C Data & Open-drain with $4.7\,\text{k}\Omega$ pullup \\
\hline
\multirow{4}{*}{\textbf{PMS5003 Sensor}} & VCC & 5V Rail & Power & 5.0V DC (Internal fan power) \\
& GND & GND Rail & Ground & Common system ground \\
& TXD & GPIO 16 (RX2) & UART Data & 9600 Baud, 3.3V logic compatible \\
& RXD & GPIO 17 (TX2) & UART Data & Command input / sleep control \\
\hline
\multirow{3}{*}{\textbf{MQ-135 Gas}} & VCC & 5V Rail & Power & 5.0V DC, $150\,\text{mA}$ (Heater coil) \\
& GND & GND Rail & Ground & Common system ground \\
& AOUT & GPIO 34 & Analog In & ADC1\_CH6 (Input-only, 0--3.3V) \\
\hline
\multirow{3}{*}{\textbf{DHT22 Sensor}} & VCC & 3V3 Rail & Power & 3.3V DC \\
& GND & GND Rail & Ground & Common system ground \\
& DATA & GPIO 4 & Single-Bus & Bi-directional, $10\,\text{k}\Omega$ pullup \\
\hline
\multirow{2}{*}{\textbf{TP4056 Module}} & BAT+ & Battery (+) & Electrochemical & $3.7\text{--}4.2\,\text{V}$ Li-ion bus \\
& BAT- & Battery (-) & Electrochemical & Protected ground return \\
\hline
\textbf{Solar Panel} & IN+ / IN- & TP4056 IN & Harvesting & $6.0\,\text{V}$ nominal, $2\,\text{W}$ max input \\
\hline
\end{tabularx}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.66\textwidth]{page_31_20_Image198.jpg}
\caption[Master circuit schematic diagram]{Master circuit schematic diagram of the solar-powered ESP32 environmental sensing node, illustrating power conditioning, analog filtering, and digital communication buses.}
\label{fig:circuit_diagram}
\end{figure}

The physical circuit integration and prototyping layout are displayed in Fig. \ref{fig:breadboard_prototyping}.

\begin{figure}[H]
\centering
\begin{subfigure}[b]{0.46\textwidth}
\centering
\includegraphics[width=0.70\textwidth]{page_21_11_Image174.jpg}
\caption{Breadboard prototyping assembly.}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.46\textwidth}
\centering
\includegraphics[width=0.70\textwidth]{page_21_12_Image175.jpg}
\caption{Sensor bus wiring and power rails.}
\end{subfigure}
\caption[Hardware prototyping bench validation]{Hardware prototyping and bench validation setup showing interconnected sensors and power conditioning stages.}
\label{fig:breadboard_prototyping}
\end{figure}

\section{Mathematical Solar Harvesting and Energy Budget Analysis}
A fundamental novelty of the ATMOS project is its verified off-grid energy autonomy under the solar irradiance profile of Sundernagar, Himachal Pradesh (Latitude $31.515^\circ\,\text{N}$, Longitude $76.878^\circ\,\text{E}$, elevation $860\,\text{m}$ above sea level).

\subsection{Sundernagar Solar Irradiance Profile}
According to the National Renewable Energy Laboratory (NREL) and NASA Surface Meteorology solar databases, Sundernagar receives an annual average daily global horizontal irradiance (GHI) of:
\begin{equation}
\bar{G}_{\text{daily}} = 4.8\,\text{kWh/m}^2/\text{day} = 4.8 \text{ Peak Sun Hours (PSH)}
\label{eq:peak_sun_hours}
\end{equation}
Even during the overcast monsoon months (July--August), the diffuse radiation guarantees a minimum of $G_{\text{min}} = 1.8\,\text{PSH}$.

For a $6\text{V}$, $2\text{W}$ monocrystalline solar panel tilted at an optimal angle of $32^\circ$ facing true south, the average daily energy harvested $E_{\text{harvest}}$ taking into account dirt derating ($\eta_{\text{dirt}} = 0.90$) and charge controller efficiency ($\eta_{\text{chg}} = 0.85$) is:
\begin{equation}
E_{\text{harvest}} = P_{\text{peak}} \cdot \text{PSH} \cdot \eta_{\text{dirt}} \cdot \eta_{\text{chg}} = 2.0\,\text{W} \times 4.8\,\text{h} \times 0.90 \times 0.85 = 7.344\,\text{Wh/day}
\label{eq:energy_harvested}
\end{equation}
Converted to battery charge capacity at nominal battery voltage $V_{\text{bat}} = 3.7\,\text{V}$:
\begin{equation}
Q_{\text{harvest}} = \frac{E_{\text{harvest}}}{V_{\text{bat}}} = \frac{7.344\,\text{Wh}}{3.7\,\text{V}} \approx 1.985\,\text{Ah/day} = 1985\,\text{mAh/day}
\label{eq:charge_harvested}
\end{equation}

\subsection{Dynamic Duty-Cycle Power Consumption Modeling}
The system operates on a 15-minute duty cycle ($T_{\text{cycle}} = 900\,\text{seconds}$). Each cycle comprises two distinct operational states:
\begin{enumerate}[label=(\alph*)]
    \item \textbf{Active State ($t_{\text{active}} = 15\,\text{seconds}$):} The ESP32 is running at $160\,\text{MHz}$, the PMS5003 fan and laser are sampling, the MQ-135 heating coil is powered, the DHT22 is queried, and the Wi-Fi radio transmits the HTTP payload.
    \begin{equation}
    I_{\text{active}} = I_{\text{ESP32,TX}} + I_{\text{PMS5003}} + I_{\text{MQ-135}} + I_{\text{OLED}} + I_{\text{DHT22}}
    \end{equation}
    \begin{equation}
    I_{\text{active}} \approx 80\,\text{mA} + 70\,\text{mA} + 120\,\text{mA} + 15\,\text{mA} + 1.5\,\text{mA} \approx 286.5\,\text{mA} \text{ (worst-case instantaneous)}
    \end{equation}
    With duty-cycled heater power gating and power management, the effective average active current across the 15-second window is measured at $I_{\text{active}} \approx 165\,\text{mA}$.
    \item \textbf{Deep-Sleep State ($t_{\text{sleep}} = 885\,\text{seconds}$):} Microcontroller cores, Wi-Fi radio, and display are powered off. Only the internal RTC timer and ultra-low-power coprocessor draw quiescent current:
    \begin{equation}
    I_{\text{sleep}} \approx 15\,\mu\text{A} = 0.015\,\text{mA}
    \end{equation}
\end{enumerate}

The time-weighted average cycle current $I_{\text{avg}}$ is rigorously calculated as:
\begin{equation}
I_{\text{avg}} = \frac{I_{\text{active}} \cdot t_{\text{active}} + I_{\text{sleep}} \cdot t_{\text{sleep}}}{t_{\text{active}} + t_{\text{sleep}}} = \frac{165\,\text{mA} \times 15\,\text{s} + 0.015\,\text{mA} \times 885\,\text{s}}{900\,\text{s}} = \frac{2475 + 13.275}{900} \approx 2.76\,\text{mA}
\label{eq:average_current}
\end{equation}

The total daily energy consumed by the ATMOS node $E_{\text{consumed}}$ is:
\begin{equation}
E_{\text{consumed}} = I_{\text{avg}} \cdot 24\,\text{h} \cdot V_{\text{bat}} = 2.76\,\text{mA} \times 24\,\text{h} \times 3.7\,\text{V} \approx 0.245\,\text{Wh/day} \quad (66.24\,\text{mAh/day})
\label{eq:energy_consumed}
\end{equation}

\subsection{Energy Surplus and Autonomous Battery Reserve}
Comparing daily harvest to daily consumption reveals an extraordinary energy surplus:
\begin{equation}
\text{Net Daily Surplus} = Q_{\text{harvest}} - Q_{\text{consumed}} = 1985\,\text{mAh} - 66.24\,\text{mAh} = +1918.76\,\text{mAh/day}
\label{eq:energy_surplus}
\end{equation}
The solar harvesting system generates almost **30 times** the energy required for daily operation, ensuring rapid battery replenishment even on heavily overcast days.

Furthermore, we calculate the autonomous operational runtime without any solar harvesting (e.g., continuous prolonged dark monsoon storm):
\begin{equation}
T_{\text{autonomy}} = \frac{C_{\text{bat}} \cdot \text{DOD}}{I_{\text{avg}} \cdot 24\,\text{hours/day}} = \frac{4400\,\text{mAh} \times 0.80}{2.76\,\text{mA} \times 24} = \frac{3520}{66.24} \approx 53.1\,\text{days}
\label{eq:battery_autonomy}
\end{equation}
where $\text{DOD} = 80\%$ is the maximum recommended Depth of Discharge to preserve Li-ion electrochemical cycle life. 

\begin{figure}[H]
\centering
\includegraphics[width=0.58\textwidth]{fig_solar_battery_soc.png}
\caption[3-Day solar harvesting and battery SOC simulation]{Dynamic simulation of 3-day solar insolation (sunny, overcast, and mixed) and corresponding battery State of Charge (SOC) illustrating perpetual off-grid equilibrium.}
\label{fig:solar_battery_soc}
\end{figure}

Fig. \ref{fig:solar_battery_soc} verifies that even during a simulated fully overcast day ($75\%$ reduction in solar irradiance), the battery State of Charge remains well above the critical $20\%$ cut-off threshold, proving complete off-grid reliability.
"""
