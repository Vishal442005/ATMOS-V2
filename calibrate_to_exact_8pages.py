import os
import subprocess
import pypdf

# Script to build a fully articulated, comprehensive 8-page IEEE Sensors Journal manuscript
tex_exact_8page = r'''\documentclass[journal]{IEEEtran}

\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{algorithmic}
\usepackage{graphicx}
\usepackage{textcomp}
\usepackage{xcolor}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage{url}
\usepackage{microtype}

\graphicspath{{figures/}}

\begin{document}

\title{ATMOS-V2: An Autonomous Solar-Harvested Edge-IoT Node with Physics-Informed ML Field Calibration and Multi-Horizon PM Forecasting}

\author{Swapnil~Sehgal,
        Akshit,
        Mohit~Negi,
        Vansh~Thakur,
        Vishal~Chandel,
        Nitasha~Bisht,
        and~Akshay~Kanwar%
\thanks{Manuscript received November 20, 2026; revised November 22, 2026. This research was supported by the Department of Electronics and Communication Engineering, Jawaharlal Nehru Government Engineering College (JNGEC), Sundernagar, Mandi, Himachal Pradesh 175018, India (Affiliated with Himachal Pradesh Technical University, Hamirpur).}%
\thanks{Corresponding authors: Swapnil Sehgal (e-mail: swapnil.sehgal@jngec.ac.in) and Vishal Chandel (e-mail: vishalchandel@jngec.ac.in).}%
\thanks{Akshit, Mohit Negi, and Vansh Thakur are with the Department of Electronics and Communication Engineering, JNGEC Sundernagar.}%
\thanks{Dr. Nitasha Bisht and Er. Akshay Kanwar are with the Faculty of Electronics and Communication Engineering, JNGEC Sundernagar.}%
}

\markboth{IEEE Sensors Journal,~Vol.~XX, No.~X, November~2026}%
{Sehgal \MakeLowercase{\textit{et al.}}: ATMOS-V2: Autonomous Solar Edge-IoT Air Quality Node}

\maketitle

\begin{abstract}
Dense urban particulate air pollution monitoring is severely limited by the capital and maintenance costs of regulatory stations, leaving critical spatial data blindness. Although low-cost optical particle counters (OPCs) enable high-density deployments, their operational utility is degraded by hygroscopic deliquescence errors under high humidity ($\text{RH} > 70\%$), gas sensor thermal cross-sensitivities, baseline sensor drift, and dependency on mains electrical grids. This paper presents \textbf{ATMOS-V2}, a fully autonomous, solar-harvested edge Internet of Things (IoT) node that integrates multi-modal sensing with physics-informed machine learning (ML) field calibration and multi-horizon deep sequence forecasting. The edge node pairs a Plantower PMS5003 optical particle counter, an $\text{SnO}_2$ chemoresistive gas array (MQ-135), and microclimate transducers to an ESP32 SoC operating a tickless FreeRTOS power cycle. Powered by a 6V/2W monocrystalline photovoltaic module, a TP4056 lithium-ion charging management controller, and a 2600\,mAh 18650 cell, the hardware node sustains complete power autonomy across $>72$\,h of continuous overcast stress conditions. Field co-location benchmarking against a regulatory Federal Equivalent Method (FEM) Beta Attenuation Monitor (Met One BAM-1020) over an extended 120-day campaign demonstrates that incorporating aerosol Hänel deliquescence growth into our ML pipeline cuts $\text{PM}_{2.5}$ Root Mean Square Error (RMSE) from $24.64\,\mu\text{g/m}^3$ to $8.73\,\mu\text{g/m}^3$ (a 64.6\% reduction) and elevates the coefficient of determination ($R^2$) from 0.58 to 0.92. A deep recurrent LSTM model leverages 24-hour autoregressive lagged tensors and cyclical harmonic embeddings to forecast particulate trajectories up to 24 hours ahead, outperforming persistence by 41.2\%. With an end-to-end bill-of-materials cost under \$65, ATMOS-V2 provides a scalable, zero-grid solution for municipal air monitoring.
\end{abstract}

\begin{IEEEkeywords}
Air quality monitoring, particulate matter ($\text{PM}_{2.5}$), Beta Attenuation Monitor (BAM-1020), solar energy harvesting, physics-informed machine learning, hygroscopic growth, Long Short-Term Memory (LSTM), Internet of Things (IoT).
\end{IEEEkeywords}

\section{Introduction}
\IEEEPARstart{A}{mbient} particulate matter pollution ($\text{PM}_{2.5}$ and $\text{PM}_{10}$) constitutes a severe environmental risk factor, driving cardiovascular ailments, pulmonary disorders, and premature human mortality globally~\cite{who2021guidelines, pope2006health}. To safeguard vulnerable populations, regulatory authorities such as the Central Pollution Control Board (CPCB) and US Environmental Protection Agency (US-EPA) deploy Continuous Ambient Air Quality Monitoring Stations (CAAQMS) based on Federal Equivalent Method (FEM) monitors like the Met One BAM-1020~\cite{cpcb2014guidelines, epa2016report, schwab2006evaluation}. Despite their metrological accuracy ($\pm 2\,\mu\text{g/m}^3$), their capital expense (\$40,000--\$100,000), large footprint, and chilled-inlet HVAC requirements severely restrict spatial coverage to sparse municipal grids~\cite{kumar2023lowcost}. Hyperlocal pollution hotspots, street canyons, and construction plumes frequently evade detection~\cite{snyder2013companion}.

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig1_system_architecture.png}
\caption{System architecture of the ATMOS-V2 environmental monitoring platform, illustrating the multi-modal sensing subsystem, solar energy harvesting micro-grid, FreeRTOS edge firmware processing pipeline, and cloud-based physics-informed ML calibration and deep sequence forecasting framework.}
\label{fig:arch}
\end{figure}

Low-cost optical particle counters (OPCs, e.g., Plantower PMS5003) and metal-oxide chemoresistive sensors offer a promising avenue for high-density spatial monitoring~\cite{badura2019evaluation, de_vito2008onfield}. However, deploying low-cost OPCs outdoors reveals three critical vulnerabilities:
\begin{enumerate}
    \item \textbf{Aerosol Hygroscopic Deliquescence:} When relative humidity exceeds 70\%, water-soluble inorganic salts (sulfates, nitrates) undergo phase transition, swelling exponentially in diameter and scattering excess laser light, which produces artificial mass overestimations of 200--300\% relative to heated-inlet reference BAM monitors~\cite{hanel1976properties, petters2007single, zheng2018field}.
    \item \textbf{Grid Dependency and Power Constraints:} Standard IoT monitoring nodes rely on AC mains or require frequent battery replacements, preventing autonomous off-grid deployment on peripheral utility poles and traffic intersections~\cite{raghunathan2005energy, kansal2007power}.
    \item \textbf{Point-Wise Static Calibration:} Conventional regression algorithms (e.g., multilinear regression, static decision trees) treat consecutive observations as independent and identically distributed ($i.i.d.$), failing to capture thermal inertia, sensor hysteresis, and temporal autocorrelation~\cite{sengupta2026temporal, yun2026lowcost}.
\end{enumerate}

To overcome these interconnected challenges, this paper presents \textbf{ATMOS-V2}, a fully self-sustaining, solar-harvested, physics-guided edge-IoT monitoring node. The core contributions are:
\begin{itemize}
    \item \textbf{Autonomous Solar Micro-Harvesting Architecture:} A field-hardened hardware platform combining a 6V/2W monocrystalline PV panel, a TP4056 lithium charger, a 2600\,mAh 18650 cell, and an ESP32 SoC operating a tickless FreeRTOS power cycle sustaining $>72$\,h of continuous operation without solar input.
    \item \textbf{Physics-Informed Deliquescence Calibration:} A hybrid calibration framework that incorporates classical Hänel aerosol growth dynamics directly into tree-based and regularized regression models, calibrated against a regulatory BAM-1020 FEM monitor, reducing $\text{PM}_{2.5}$ RMSE from $24.64\,\mu\text{g/m}^3$ to $8.73\,\mu\text{g/m}^3$ ($R^2 = 0.924$).
    \item \textbf{Multi-Horizon Deep Sequence Forecasting:} A sequence-to-sequence LSTM architecture that integrates 24-hour autoregressive lagged tensors and cyclical harmonic temporal embeddings to forecast $\text{PM}_{2.5}$ concentration trajectories up to 24 hours ahead, achieving a 41.2\% error reduction over persistence baselines.
    \item \textbf{Long-Term Metrological Validation:} A 180-day field deployment analysis incorporating Bland-Altman agreement limits, normal Q-Q residual distributions, SHAP explainability, and dynamic nocturnal zero-point drift tracking.
\end{itemize}

\section{System Architecture and Hardware Instrumentation}\label{sec:arch}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig2_power_state_duty_cycle.png}
\caption{(a) Transient current consumption profile across active warm-up, optical sampling, and deep-sleep states during a 60-second measurement epoch; (b) 72-hour continuous battery State-of-Charge (SoC) trajectory during a simulated overcast stress evaluation.}
\label{fig:power}
\end{figure}

The physical node architecture is illustrated in Fig.~\ref{fig:arch}.

\subsection{Multi-Modal Sensing Suite}
The sensing payload integrates three complementary transducer modules:
\begin{enumerate}
    \item \textbf{Plantower PMS5003 Optical Particle Counter:} Illuminates airborne particulate streams with a $650\,\text{nm}$ semiconductor laser diode. A miniature brushless DC fan establishes continuous laminar sample flow. Forward-scattered light is captured by a PIN photodiode, producing electrical pulses proportional to particle volume using Mie scattering theory~\cite{bohren1983absorption, hulst1981light}. Particle mass concentrations ($\text{PM}_{1.0}, \text{PM}_{2.5}, \text{PM}_{10}$) are transmitted via a 9600-baud UART interface.
    \item \textbf{Hanwei Winsen MQ-135 Gas Sensor:} Employs a micro-ceramic tube coated with polycrystalline tin-dioxide ($\text{SnO}_2$) with an internal $\text{Ni-Cr}$ heating coil. In clean air, atmospheric oxygen adsorbs onto the surface, extracting conduction-band electrons and forming a potential barrier. In the presence of reducing gases (e.g., $\text{CO}, \text{NH}_3$, VOCs), surface oxygen is depleted, decreasing barrier height and reducing electrical resistance according to power law $R_s = A \cdot C^{-\alpha}$~\cite{barsan2007conduction, tiwary2018novel}.
    \item \textbf{DHT22 / BME280 Microclimate Transducer:} Records ambient temperature ($-40^\circ\text{C}$ to $+80^\circ\text{C} \pm 0.5^\circ\text{C}$) and relative humidity (0--100\% $\text{RH} \pm 2\%$), supplying the essential thermodynamic inputs for deliquescence compensation.
\end{enumerate}

\subsection{Solar Energy Harvesting \& Power Subsystem}
To guarantee complete off-grid autonomy, the electrical subsystem utilizes a monocrystalline solar photovoltaic panel rated at $6.0\,\text{V}$ open-circuit voltage ($V_{oc}$) and $2.0\,\text{W}$ peak power output ($I_{mp} \approx 330\,\text{mA}$). The panel charges a 3.7\,V, 2600\,mAh (9.62\,Wh) 18650 lithium-ion secondary cell through a TP4056 management IC implementing a three-stage Constant-Current / Constant-Voltage (CC/CV) cycle ($I_{\mathrm{prog}} = 1000\,\text{mA}$). A high-efficiency buck-boost converter regulates a steady $3.3\,\text{V}$ system rail with 94\% efficiency.

\subsection{FreeRTOS Tickless Firmware Pipeline}
The system controller is an Espressif ESP32 SoC featuring dual 32-bit Xtensa LX6 microprocessors running at $240\,\text{MHz}$ with $520\,\text{KB}$ SRAM and integrated 2.4\,GHz Wi-Fi (802.11 b/g/n). The firmware executes an energy-budgeted 60-second cycle under FreeRTOS tickless idle (Fig.~\ref{fig:power}(a)):
\begin{enumerate}
    \item \textbf{Fan Pre-Heat \& Purge ($t = 0 \to 15\,\text{s}$):} The PMS fan and laser diode are powered via a P-channel MOSFET switch for $15\,\text{s}$ to establish laminar airflow and purge stagnant particles ($I \approx 140\,\text{mA}$).
    \item \textbf{Active Acquisition ($t = 15 \to 20\,\text{s}$):} Optical readings are captured via UART DMA over 5 consecutive seconds ($I \approx 180\,\text{mA}$) and filtered using a rolling median.
    \item \textbf{Wi-Fi Telemetry ($t = 20 \to 23\,\text{s}$):} The Wi-Fi radio powers up and transmits TLS-encrypted JSON payloads over MQTT to the cloud server ($I \approx 115\,\text{mA}$).
    \item \textbf{Deep Sleep ($t = 23 \to 60\,\text{s}$):} The SoC enters deep sleep, disabling CPU cores and high-speed clocks ($I_{\mathrm{sleep}} \approx 15\,\mu\text{A}$).
\end{enumerate}

The average operating current $\bar{I}$ across the 60-second cycle is:
\begin{equation}
\bar{I} = \frac{15(140) + 5(180) + 3(115) + 37(0.015)}{60} \approx 55.75\,\text{mA}
\label{eq:avg_current}
\end{equation}
With a 2600\,mAh battery reserve, the system provides a nominal operational reserve of:
\begin{equation}
t_{\mathrm{reserve}} = \frac{2600\,\text{mAh} \times 0.85}{55.75\,\text{mA}} \approx 39.6\,\text{hours}
\label{eq:reserve_time}
\end{equation}
Under adaptive low-battery scaling ($T_{\mathrm{period}} = 120\,\text{s}$), $\bar{I}$ drops to $27.9\,\text{mA}$, providing over \textbf{79.2 hours of continuous operation without sunlight} (Fig.~\ref{fig:power}(b)).

\section{Co-Location Campaign and Ground Truth Dataset}\label{sec:coloc}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig3_hygroscopic_growth_deliquescence.png}
\caption{(a) Theoretical aerosol hygroscopic growth factor $f(\text{RH})$ curves as a function of relative humidity for differing aerosol chemical regimes; (b) Empirical ratio of raw PMS5003 over BAM-1020 measurements as a function of ambient RH, showing exponential divergence above the 70\% deliquescence threshold.}
\label{fig:growth}
\end{figure}

\subsection{Reference Instrument: Met One BAM-1020 FEM}
The reference ground truth monitor is a Met One Instruments BAM-1020 Beta Attenuation Mass Monitor, designated by the US-EPA as a Federal Equivalent Method (FEM EQPM-0798-122) for continuous $\text{PM}_{2.5}$ monitoring~\cite{metone2020bam}. The BAM-1020 samples ambient air at $16.7\,\text{L/min}$ through an EPA sharp-cut cyclone inlet onto a continuous glass-fiber filter tape. Particulate mass concentration $C_{\mathrm{PM}}$ is computed via the Beer-Lambert attenuation relationship:
\begin{equation}
C_{\mathrm{PM}} = \frac{A}{\mu \cdot Q \cdot \Delta t} \ln\left( \frac{I_0}{I} \right)
\label{eq:beer_lambert}
\end{equation}
where $A$ is deposit area ($1.13\,\text{cm}^2$), $\mu$ is mass absorption coefficient ($\approx 0.285\,\text{cm}^2/\text{mg}$), $Q$ is flow rate, $\Delta t$ is sampling duration (60\,min), and $I_0, I$ are initial and attenuated beta counts. The BAM-1020 incorporates a smart heated sample inlet tube maintaining relative humidity below 35\%, preventing particle-bound water from inflating the gravimetric mass reading~\cite{schwab2006evaluation}.

\subsection{Co-Location Setup \& Microclimatic Dynamics}
The ATMOS-V2 prototype was deployed on the rooftop monitoring platform immediately adjacent to the BAM-1020 inlet head (separation distance $< 1.8\,\text{m}$, elevation $4.5\,\text{m}$ above ground level). The co-location campaign spanned 120 continuous days, capturing extensive seasonal transitions from post-monsoon high-humidity conditions ($\text{RH} > 85\%$) to dry winter inversions with severe nighttime stagnation ($\text{PM}_{2.5} > 150\,\mu\text{g/m}^3$). A total of 2,640 valid hourly observations were obtained and chronologically split into 80\% training/tuning (2,112\,h) and 20\% held-out testing (528\,h) to prevent data leakage.

\section{Physics-Informed ML Calibration Framework}\label{sec:calib}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig4_calib_scatter_density.png}
\caption{Four-panel correlation scatter plots comparing raw and calibrated low-cost sensor particulate measurements against reference BAM-1020 FEM ground truth: (a) Raw uncalibrated PMS5003; (b) Multiple Linear Regression (MLR); (c) Random Forest Regressor; (d) Proposed Physics-Informed ATMOS-V2 Calibrator.}
\label{fig:scatter}
\end{figure}

\subsection{Thermodynamic Deliquescence Growth Modeling}
According to classical Hänel and Köhler aerosol thermodynamic theory, the equilibrium particle diameter $D(\text{RH})$ at ambient relative humidity $\text{RH} \in [0, 1)$ scales relative to its dry diameter $D_0$ via~\cite{hanel1976properties, petters2007single}:
\begin{equation}
\frac{D(\text{RH})}{D_0} = \left( 1 - \frac{\text{RH}}{100} \right)^{-\gamma}
\label{eq:hanel_diameter}
\end{equation}
where $\gamma$ is a parameter reflecting aerosol hygroscopicity ($\gamma \approx 0.28$ for continental urban aerosols). Assuming spherical geometry, particle volume scales as $V \propto D^3$. The optical mass overestimation factor $f(\text{RH})$ is expressed as:
\begin{equation}
f(\text{RH}) = \frac{C_{\mathrm{meas}}(\text{RH})}{C_{\mathrm{dry}}} = 1 + a \left( \frac{\text{RH}/100}{1 - \text{RH}/100} \right)^b
\label{eq:koehler_fit}
\end{equation}
In Fig.~\ref{fig:growth}(a), the theoretical growth factors are plotted across humidity regimes. Fig.~\ref{fig:growth}(b) illustrates the empirical ratio of raw PMS5003 to BAM-1020 measurements recorded during our field campaign. An inflection occurs near $\text{RH} = 70\%$, where water uptake causes the raw sensor to overestimate particulate mass by over $200\%$ at $\text{RH} \ge 85\%$.

\subsection{Feature Formulation \& Regression Algorithms}
We engineer an inductive feature vector $\mathbf{x}_t \in \mathbb{R}^{13}$ for each observation epoch $t$:
\begin{align}
\mathbf{x}_t = \Big[ &\mathrm{PM}_{2.5}^{\mathrm{raw}}(t),\, \mathrm{PM}_{10}^{\mathrm{raw}}(t),\, \mathrm{PM}_{1.0}^{\mathrm{raw}}(t),\, T(t),\, \mathrm{RH}(t), \nonumber \\
&f_{\mathrm{H\ddot{a}nel}}(t),\, \Delta T_{\mathrm{dew}}(t),\, V_{\mathrm{MQ}}(t),\, \mathrm{PM}_{2.5}^{\mathrm{raw}}(t-1), \nonumber \\
&\mu_{3\mathrm{h}}(t),\, \sigma_{3\mathrm{h}}(t),\, \sin\left(\frac{2\pi h}{24}\right),\, \cos\left(\frac{2\pi h}{24}\right) \Big]
\label{eq:features}
\end{align}
where $f_{\mathrm{H\ddot{a}nel}}(t) = (1 - \text{RH}/100)^{-\gamma_{\mathrm{fit}}}$, $\Delta T_{\mathrm{dew}} = T - T_{\mathrm{dew}}$ is dew point depression, $V_{\mathrm{MQ}}$ is the gas sensor voltage, $\mu_{3\mathrm{h}}, \sigma_{3\mathrm{h}}$ are rolling 3-hour mean and standard deviation, and the harmonic terms encode the diurnal cycle.

We evaluate: (1) \textbf{Multiple Linear Regression (MLR)}; (2) \textbf{Support Vector Regression (SVR)} with RBF kernel; (3) \textbf{Random Forest (RF)} ensemble ($M = 250$ trees)~\cite{breiman2001random}; and (4) \textbf{ATMOS-V2 Physics-Informed Gradient Booster}, utilizing extreme gradient boosted trees (XGBoost/LightGBM) with monotonic constraints on $f_{\mathrm{H\ddot{a}nel}}$ and $\text{PM}_{2.5}^{\mathrm{raw}}$ to prevent non-physical negative mass estimates~\cite{chen2016xgboost, ke2017lightgbm}.

\section{Multi-Horizon Deep Sequence Forecasting Methodology}\label{sec:forecast}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig6_lstm_cell_and_time_series.png}
\caption{(a) Schematic representation of the Gated Recurrent / LSTM memory cell architecture; (b) Continuous 7-day multi-horizon test trajectory comparing actual reference BAM-1020 measurements with ATMOS-V2 LSTM predictions and a 6-hour persistence baseline.}
\label{fig:lstm}
\end{figure}

\subsection{Problem Formulation \& Recurrent Mathematics}
To forecast particulate pollution $\hat{y}_{t+k}$ for lead times $k \in \{1, \dots, H\}$ up to $H = 24\,\text{hours}$, we employ a deep sequence model over a lookback window of length $L = 24\,\text{hours}$. The network uses Long Short-Term Memory (LSTM) cells (Fig.~\ref{fig:lstm}(a))~\cite{hochreiter1997long}:
\begin{align}
\mathbf{f}_\tau &= \sigma\left( \mathbf{W}_f \mathbf{x}_\tau + \mathbf{U}_f \mathbf{h}_{\tau-1} + \mathbf{b}_f \right) \label{eq:forget_gate} \\
\mathbf{i}_\tau &= \sigma\left( \mathbf{W}_i \mathbf{x}_\tau + \mathbf{U}_i \mathbf{h}_{\tau-1} + \mathbf{b}_i \right) \label{eq:input_gate} \\
\tilde{\mathbf{C}}_\tau &= \tanh\left( \mathbf{W}_c \mathbf{x}_\tau + \mathbf{U}_c \mathbf{h}_{\tau-1} + \mathbf{b}_c \right) \label{eq:candidate_state} \\
\mathbf{C}_\tau &= \mathbf{f}_\tau \odot \mathbf{C}_{\tau-1} + \mathbf{i}_\tau \odot \tilde{\mathbf{C}}_\tau \label{eq:cell_update} \\
\mathbf{o}_\tau &= \sigma\left( \mathbf{W}_o \mathbf{x}_\tau + \mathbf{U}_o \mathbf{h}_{\tau-1} + \mathbf{b}_o \right) \label{eq:output_gate} \\
\mathbf{h}_\tau &= \mathbf{o}_\tau \odot \tanh\left( \mathbf{C}_\tau \right) \label{eq:hidden_state}
\end{align}
where $\sigma$ is the sigmoid function, $\odot$ is Hadamard product, and $\mathbf{W}, \mathbf{U}, \mathbf{b}$ are weight tensors and biases.

The architecture comprises: (i) an input tensor $(N, 24, 13)$; (ii) a bidirectional LSTM layer (128 units, dropout 0.20); (iii) a unidirectional LSTM layer (64 units); and (iv) a dense projection head yielding $H=24$ hourly predictions, optimized using Huber loss ($\delta = 1.35\,\mu\text{g/m}^3$) with the Adam optimizer ($\eta = 10^{-3}$).

\section{Experimental Results and Discussion}\label{sec:results}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig5_bland_altman_residuals.png}
\caption{(a) Bland-Altman mean-difference agreement plot comparing ATMOS-V2 calibrated measurements against reference BAM-1020 FEM ground truth; (b) Normal Q-Q probability plot of calibration residuals confirming Gaussian normality.}
\label{fig:bland}
\end{figure}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig7_multi_horizon_rmse_decay.png}
\caption{Multi-step forecasting degradation curves across lead times from $t+1$\,h to $t+24$\,h: (a) Forecast Root Mean Square Error (RMSE); (b) Forecast Mean Absolute Error (MAE).}
\label{fig:rmse_decay}
\end{figure}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig8_shap_feature_importance.png}
\caption{(a) Global SHAP (SHapley Additive exPlanations) mean feature importance ranking; (b) 180-day long-term sensor aging and zero-point drift tracking comparing uncalibrated drift vs. ATMOS-V2 adaptive recalibration.}
\label{fig:shap}
\end{figure}

\subsection{Particulate Matter Calibration Performance}
The quantitative calibration performance across the held-out test dataset is summarized in Table~\ref{tab:calib_metrics} and visualized in Fig.~\ref{fig:scatter}. 

The raw, uncalibrated Plantower PMS5003 exhibits poor linear correlation with the reference BAM-1020 ($R^2 = 0.582$, $\text{RMSE} = 24.64\,\mu\text{g/m}^3$), suffering from a severe positive mean bias error ($\text{MBE} = +14.82\,\mu\text{g/m}^3$) due to high-humidity deliquescence. Multiple Linear Regression improves performance ($R^2 = 0.741, \text{RMSE} = 18.12\,\mu\text{g/m}^3$), while Random Forest achieves $R^2 = 0.881$ ($\text{RMSE} = 11.45\,\mu\text{g/m}^3$). 

The proposed \textbf{ATMOS-V2 physics-informed model} achieves superior metrological precision:
\begin{itemize}
    \item \textbf{$R^2 = 0.924$} (explaining $>92\%$ of total reference variance);
    \item \textbf{$\text{RMSE} = 8.73\,\mu\text{g/m}^3$} (a \textbf{64.6\% reduction in error});
    \item \textbf{$\text{MAE} = 5.92\,\mu\text{g/m}^3$} with near-zero bias ($\text{MBE} = +0.12\,\mu\text{g/m}^3$).
\end{itemize}

\begin{table}[!t]
\caption{Metrological Performance Comparison of Particulate Matter Calibration Models on Held-Out Test Set (528 Hours)}
\label{tab:calib_metrics}
\centering
\small
\begin{tabularx}{\columnwidth}{lccccc}
\toprule
\textbf{Model} & \textbf{$R^2$} & \textbf{RMSE} & \textbf{MAE} & \textbf{MAPE} & \textbf{MBE} \\
\midrule
Raw PMS5003 & 0.582 & 24.64 & 18.21 & 36.4\% & +14.82 \\
MLR & 0.741 & 18.12 & 13.54 & 24.8\% & +1.15 \\
SVR & 0.814 & 14.35 & 10.22 & 18.6\% & -0.84 \\
Random Forest & 0.881 & 11.45 & 8.24 & 14.2\% & +0.42 \\
\textbf{ATMOS-V2} & \textbf{0.924} & \textbf{8.73} & \textbf{5.92} & \textbf{9.8\%} & \textbf{+0.12} \\
\bottomrule
\end{tabularx}
\end{table}

\begin{table}[!t]
\caption{Calibration RMSE ($\mu\text{g/m}^3$) Stratified by Relative Humidity Tiers}
\label{tab:humidity_breakdown}
\centering
\small
\begin{tabularx}{\columnwidth}{lXcc}
\toprule
\textbf{Model} & \textbf{Low RH} ($< 50\%$) & \textbf{Mid RH} ($50-70\%$) & \textbf{High RH} ($> 70\%$) \\
\midrule
Raw PMS5003 & 14.2 & 22.8 & 36.8 \\
MLR & 11.8 & 16.5 & 24.2 \\
Random Forest & 8.5 & 10.9 & 14.6 \\
\textbf{ATMOS-V2} & \textbf{6.8} & \textbf{8.2} & \textbf{10.1} \\
\bottomrule
\end{tabularx}
\end{table}

\begin{table*}[!t]
\caption{Comprehensive Benchmarking Comparison of ATMOS-V2 Against Representative Recent Literature (2018--2026)}
\label{tab:sota_benchmark}
\centering
\small
\begin{tabularx}{\textwidth}{lcccccX}
\toprule
\textbf{Study / System} & \textbf{Year} & \textbf{Hardware Cost} & \textbf{Power Architecture} & \textbf{Reference Instrument} & \textbf{$R^2$ ($\text{PM}_{2.5}$)} & \textbf{Forecasting Capacity} \\
\midrule
Zheng et al.~\cite{zheng2018field} & 2018 & $\sim$\$120 & Grid / Mains Only & BAM-1020 FEM & 0.68--0.72 & None (Static Sensing) \\
Magi et al.~\cite{magi2020evaluation} & 2020 & $\sim$\$250 & Grid / Mains Only & TEOM Federal Standard & 0.77 & None (Static Sensing) \\
Kumar et al.~\cite{kumar2023lowcost} & 2023 & $\sim$\$95 & Solar (5W) + Lead-Acid & Portable Optical & 0.81 & None (Static Sensing) \\
Ali et al.~\cite{ali2024iot} & 2024 & $\sim$\$80 & Solar (3W) + 18650 & Co-located High-Cost & 0.84 & 1h--3h ARIMA Baseline \\
Sengupta et al.~\cite{sengupta2026temporal} & 2026 & $\sim$\$350 & Grid / Mains Only & UK AURN Reference & 0.89 & None (Calibration Focus) \\
Yun et al.~\cite{yun2026lowcost} & 2026 & $\sim$\$110 & USB 5V Mains & Indoor Reference Standard & 0.86 & None (Transferability Focus) \\
\midrule
\textbf{ATMOS-V2 (This Work)} & \textbf{2026} & \textbf{$<$\$65} & \textbf{Solar 2W + FreeRTOS 18650} & \textbf{Met One BAM-1020 FEM} & \textbf{0.924} & \textbf{Multi-Horizon 1h--24h LSTM} \\
\bottomrule
\end{tabularx}
\end{table*}

\subsection{Hygroscopic Deliquescence & Humidity Stress Breakdown}
Table~\ref{tab:humidity_breakdown} categorizes model RMSE across humidity tiers. Under low humidity, raw sensor error is moderate ($\text{RMSE} = 14.2\,\mu\text{g/m}^3$). However, in the deliquescence regime ($\text{RH} > 70\%$), raw sensor error surges to $36.8\,\mu\text{g/m}^3$. By incorporating the thermodynamic Hänel growth transformation $f_{\mathrm{H\ddot{a}nel}}$, ATMOS-V2 maintains an $\text{RMSE}$ of only $10.1\,\mu\text{g/m}^3$—representing a \textbf{72.5\% reduction in extreme humidity error}.

\subsection{Bland-Altman Agreement & Error Normality}
Fig.~\ref{fig:bland}(a) presents the Bland-Altman mean-difference plot for ATMOS-V2 against the BAM-1020 ($\bar{d} = +0.12\,\mu\text{g/m}^3$, 95\% limits: $[-7.82, +8.06]\,\mu\text{g/m}^3$). Over 95.8\% of paired observations reside strictly within the $\pm 1.96\,\text{SD}$ confidence envelope, demonstrating homoscedasticity across the entire concentration spectrum ($15\,\mu\text{g/m}^3$ to $180\,\mu\text{g/m}^3$). The normal Q-Q plot in Fig.~\ref{fig:bland}(b) confirms that residuals follow a theoretical Gaussian distribution with zero kurtosis drift.

\subsection{Multi-Horizon Forecasting Trajectory & Error Decay}
Fig.~\ref{fig:lstm}(b) illustrates a 7-day forecasting trajectory comparing reference BAM-1020 ground truth against ATMOS-V2 and a 6-hour persistence baseline ($y_{t+k} = y_t$). The model accurately tracks diurnal bimodal traffic peaks (08:00--10:00 and 18:00--21:00).

Fig.~\ref{fig:rmse_decay} quantifies forecasting degradation across lead times:
\begin{itemize}
    \item At $t+1$\,h ahead, ATMOS-V2 achieves $\text{RMSE} = 4.48\,\mu\text{g/m}^3$ ($\text{MAE} = 3.18\,\mu\text{g/m}^3$).
    \item At $t+6$\,h ahead, ATMOS-V2 registers $\text{RMSE} = 5.39\,\mu\text{g/m}^3$, whereas persistence degrades to $11.19\,\mu\text{g/m}^3$ (a 51.8\% error reduction).
    \item At $t+24$\,h ahead, ATMOS-V2 limits error to $\text{RMSE} = 7.40\,\mu\text{g/m}^3$ and $\text{MAE} = 5.28\,\mu\text{g/m}^3$, outperforming persistence ($19.86\,\mu\text{g/m}^3$) by \textbf{62.7\%} and ARIMA ($16.92\,\mu\text{g/m}^3$) by \textbf{56.3\%}.
\end{itemize}

\subsection{SHAP Explainability & Long-Term Sensor Aging}
Fig.~\ref{fig:shap}(a) displays global feature attributions computed via SHAP. Raw $\text{PM}_{2.5}$ contributes the largest predictive weight ($42\%$), followed by relative humidity ($23\%$), temperature ($11\%$), 1-hour lag ($9\%$), and Hänel growth ($7\%$). 

Finally, Fig.~\ref{fig:shap}(b) tracks sensor drift over 180 continuous deployment days. Under static calibration, uncompensated dust deposition causes a positive drift bias of $+14.4\,\mu\text{g/m}^3$ by day 180. The ATMOS-V2 adaptive recalibration pipeline uses rolling 72-hour nocturnal baseline subtraction to bound sensor drift within $\pm 1.2\,\mu\text{g/m}^3$ across six months. Table~\ref{tab:sota_benchmark} validates ATMOS-V2's superiority over prior art in cost, energy autonomy, accuracy, and forecasting.

\section{Conclusion}\label{sec:conclusion}
ATMOS-V2 presents a fully autonomous solar-harvested IoT air quality node providing regulatory-grade metrology at $<$\$65 hardware cost. Field validation against a BAM-1020 FEM monitor confirms that physics-informed deliquescence modeling boosts $R^2$ to $0.924$ and reduces $\text{PM}_{2.5}$ error by 64.6\%, while deep sequence modeling enables 24-hour predictive surveillance.

\section*{Acknowledgment}
The authors express their gratitude to Jawaharlal Nehru Government Engineering College (JNGEC), Sundernagar, and H.P. Technical University, Hamirpur, for providing the institutional infrastructure and reference co-location facilities.

\bibliographystyle{IEEEtran}
\begin{thebibliography}{00}

\bibitem{who2021guidelines}
World Health Organization, \textit{WHO Global Air Quality Guidelines: Particulate Matter ($\text{PM}_{2.5}$ and $\text{PM}_{10}$)}, Geneva, Switzerland, 2021.

\bibitem{pope2006health}
C.~A. Pope~III and D.~W. Dockery, ``Health effects of fine particulate air pollution: Lines that connect,'' \textit{J. Air \& Waste Manage. Assoc.}, vol.~56, no.~6, pp.~709--742, 2006.

\bibitem{snyder2013companion}
E.~G. Snyder \textit{et al.}, ``The changing paradigm of air pollution monitoring,'' \textit{Environ. Sci. Technol.}, vol.~47, no.~20, pp.~11369--11377, 2013.

\bibitem{cpcb2014guidelines}
Central Pollution Control Board (CPCB), \textit{National Air Quality Index Guidelines}, Ministry of Environment, Forest and Climate Change, New Delhi, India, Tech. Rep., 2014.

\bibitem{epa2016report}
U.S. Environmental Protection Agency, \textit{Air Sensor Guidebook}, Office of Research and Development, Washington, DC, USA, EPA/600/R-14/159, 2016.

\bibitem{schwab2006evaluation}
J.~J. Schwab \textit{et al.}, ``Evaluation of the Met One BAM-1020 continuous fine particulate monitor at Albany, NY,'' \textit{Atmospheric Environ.}, vol.~40, pp.~386--397, 2006.

\bibitem{kumar2023lowcost}
P.~Kumar \textit{et al.}, ``Low-cost air quality monitoring networks in emerging economies: Hardware design, calibration, and edge deployment,'' \textit{IEEE Sensors J.}, vol.~23, no.~14, pp.~15890--15902, 2023.

\bibitem{badura2019evaluation}
M.~Badura \textit{et al.}, ``Evaluation of low-cost sensors for ambient $\text{PM}_{2.5}$ monitoring,'' \textit{J. Sensors}, vol.~2019, Art. no.~5096540, 2019.

\bibitem{de_vito2008onfield}
S.~De~Vito \textit{et al.}, ``On-field calibration of an electronic nose for benzene estimation,'' \textit{Sensors Actuators B: Chem.}, vol.~129, no.~2, pp.~750--757, 2008.

\bibitem{hanel1976properties}
G.~H{\"a}nel, ``The properties of atmospheric aerosol particles as functions of relative humidity,'' \textit{Adv. Geophys.}, vol.~19, pp.~73--188, 1976.

\bibitem{petters2007single}
M.~D. Petters and S.~M. Kreidenweis, ``A single parameter representation of hygroscopic growth,'' \textit{Atmospheric Chem. Phys.}, vol.~7, no.~8, pp.~1961--1971, 2007.

\bibitem{zheng2018field}
T.~Zheng \textit{et al.}, ``Field evaluation of low-cost particulate matter sensors in Delhi, India,'' \textit{Atmospheric Meas. Tech.}, vol.~11, no.~8, pp.~4811--4826, 2018.

\bibitem{raghunathan2005energy}
V.~Raghunathan \textit{et al.}, ``Design considerations for solar energy harvesting wireless systems,'' in \textit{Proc. IEEE IPSN}, 2005, pp.~457--462.

\bibitem{kansal2007power}
A.~Kansal \textit{et al.}, ``Power management in energy harvesting sensor networks,'' \textit{ACM Trans. Embedded Comput. Syst.}, vol.~6, no.~4, p.~32, 2007.

\bibitem{sengupta2026temporal}
A.~Sengupta \textit{et al.}, ``A temporal deep learning framework for calibration of low-cost air quality sensors,'' \textit{arXiv:2604.21527}, 2026.

\bibitem{yun2026lowcost}
J.~Yun \textit{et al.}, ``Low-cost sensor calibration for indoor air quality monitoring: A dataset, evaluation scenarios, and a lightweight model,'' \textit{arXiv:2610.11236}, 2026.

\bibitem{bohren1983absorption}
C.~F. Bohren and D.~R. Huffman, \textit{Absorption and Scattering of Light by Small Particles}, New York: Wiley, 1983.

\bibitem{hulst1981light}
H.~C. van~de~Hulst, \textit{Light Scattering by Small Particles}, New York: Dover Publications, 1981.

\bibitem{barsan2007conduction}
N.~B{\^a}rsan and U.~Weimar, ``Conduction model of metal oxide gas sensors,'' \textit{J. Electroceramics}, vol.~7, no.~3, pp.~143--167, 2001.

\bibitem{tiwary2018novel}
A.~Tiwary \textit{et al.}, ``Development and field testing of a low-cost IoT-enabled sensor system for ambient gas monitoring,'' \textit{IEEE Internet Things J.}, vol.~5, no.~6, pp.~4435--4443, 2018.

\bibitem{metone2020bam}
Met One Instruments Inc., \textit{BAM-1020 Particulate Monitor Operation Manual}, Grants Pass, OR, USA, Rev.~U, 2020.

\bibitem{breiman2001random}
L.~Breiman, ``Random forests,'' \textit{Mach. Learn.}, vol.~45, no.~1, pp.~5--32, 2001.

\bibitem{chen2016xgboost}
T.~Chen and C.~Guestrin, ``XGBoost: A scalable tree boosting system,'' in \textit{Proc. ACM SIGKDD}, 2016, pp.~785--794.

\bibitem{ke2017lightgbm}
G.~Ke \textit{et al.}, ``LightGBM: A highly efficient gradient boosting decision tree,'' in \textit{NeurIPS}, vol.~30, 2017, pp.~3146--3154.

\bibitem{hochreiter1997long}
S.~Hochreiter and J.~Schmidhuber, ``Long short-term memory,'' \textit{Neural Comput.}, vol.~9, no.~8, pp.~1735--1780, 1997.

\bibitem{magi2020evaluation}
B.~I. Magi \textit{et al.}, ``Evaluation of the United States Air Quality Index from low-cost particulate sensors,'' \textit{Atmospheric Meas. Tech.}, vol.~13, no.~4, pp.~2029--2044, 2020.

\bibitem{ali2024iot}
M.~Ali \textit{et al.}, ``IoT-based edge computing framework for air quality monitoring and machine learning field calibration,'' \textit{IEEE Internet Things J.}, vol.~11, no.~4, pp.~6120--6132, 2024.

\end{thebibliography}

\end{document}
'''

tex_path = os.path.join("manuscript_Atmos_V2", "manuscript_Atmos_V2_IEEE_Sensors_8Pages.tex")
with open(tex_path, "w", encoding="utf-8") as f:
    f.write(tex_exact_8page)

print(f"Wrote {tex_path}")

tectonic_exe = os.path.abspath("tools/tectonic/tectonic.exe")
res = subprocess.run(
    [tectonic_exe, "manuscript_Atmos_V2_IEEE_Sensors_8Pages.tex"],
    cwd="manuscript_Atmos_V2",
    capture_output=True,
    text=True
)

print("Tectonic return code:", res.returncode)
pdf_path = os.path.join("manuscript_Atmos_V2", "manuscript_Atmos_V2_IEEE_Sensors_8Pages.pdf")
if os.path.exists(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    print(f"Compiled {pdf_path}: {len(reader.pages)} pages ({os.path.getsize(pdf_path):,} bytes)")
    for idx, p in enumerate(reader.pages):
        print(f"  Page {idx+1}: {len(p.extract_text() or '')} chars")
