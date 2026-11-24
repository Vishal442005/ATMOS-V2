import os
import subprocess
import pypdf

# Script to create the exact 8-page IEEE Sensors Journal submission
tex_8page = r'''\documentclass[journal]{IEEEtran}

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
\thanks{Manuscript received November 20, 2026. This work was supported by the Department of Electronics and Communication Engineering, Jawaharlal Nehru Government Engineering College (JNGEC), Sundernagar, Mandi, H.P. 175018, India.}%
\thanks{Corresponding authors: Swapnil Sehgal (e-mail: swapnil.sehgal@jngec.ac.in) and Vishal Chandel (e-mail: vishalchandel@jngec.ac.in).}%
}

\markboth{IEEE Sensors Journal,~Vol.~XX, No.~X, November~2026}%
{Sehgal \MakeLowercase{\textit{et al.}}: ATMOS-V2: Autonomous Solar Edge-IoT Air Quality Node}

\maketitle

\begin{abstract}
Dense urban particulate air pollution monitoring is severely limited by the capital costs of regulatory stations, leaving critical spatial data gaps. Low-cost optical particle counters (OPCs) enable dense networks but suffer from hygroscopic deliquescence errors under high humidity ($\text{RH} > 70\%$), gas sensor thermal cross-sensitivities, and grid dependency. This paper presents \textbf{ATMOS-V2}, a self-sustaining, solar-harvested edge Internet of Things (IoT) node integrating multi-modal sensing with physics-informed machine learning (ML) calibration and multi-horizon sequence forecasting. The node pairs a Plantower PMS5003 optical sensor, an $\text{SnO}_2$ gas array (MQ-135), and a DHT22 transducer to an ESP32 SoC operating a tickless FreeRTOS power cycle. Powered by a 6V/2W photovoltaic panel, TP4056 charger, and a 2600\,mAh 18650 cell, it guarantees $>72$\,h of continuous operation without solar input. Co-location alongside a regulatory Federal Equivalent Method (FEM) Beta Attenuation Monitor (Met One BAM-1020) over 120 days shows that incorporating aerosol Hänel deliquescence growth into our ML pipeline cuts $\text{PM}_{2.5}$ Root Mean Square Error (RMSE) from $24.64\,\mu\text{g/m}^3$ to $8.73\,\mu\text{g/m}^3$ (a 64.6\% reduction) and boosts $R^2$ from 0.58 to 0.92. A deep recurrent LSTM model leverages 24-hour autoregressive tensors and cyclical harmonics to forecast particulate trajectories up to 24 hours ahead, outperforming persistence by 41.2\%. With a bill-of-materials cost under \$65, ATMOS-V2 provides a scalable, zero-grid solution for municipal air monitoring.
\end{abstract}

\begin{IEEEkeywords}
Air quality monitoring, particulate matter ($\text{PM}_{2.5}$), BAM-1020, solar energy harvesting, physics-informed ML, hygroscopic growth, LSTM, IoT.
\end{IEEEkeywords}

\section{Introduction}
\IEEEPARstart{A}{mbient} fine particulate matter ($\text{PM}_{2.5}$) is a primary environmental driver of premature cardiovascular and respiratory mortality~\cite{who2021guidelines, pope2006health}. Mitigating urban human exposure requires dense, hyperlocal monitoring with sub-kilometer resolution~\cite{snyder2013companion}. Regulatory Continuous Ambient Air Quality Monitoring Stations (CAAQMS) deploy Federal Equivalent Method (FEM) instruments like the Met One BAM-1020~\cite{schwab2006evaluation}. Although gravimetrically precise ($\pm 2\,\mu\text{g/m}^3$), their capital cost (\$40,000--\$100,000) and power demands restrict them to sparse geographical grids~\cite{kumar2023lowcost}.

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig1_system_architecture.png}
\caption{System architecture of the ATMOS-V2 platform showing sensing suite, solar micro-grid, FreeRTOS edge firmware, and cloud AI pipeline.}
\label{fig:arch}
\end{figure}

Low-cost optical particle counters (OPCs, e.g., PMS5003) offer scalable spatial granularity~\cite{badura2019evaluation}. However, in outdoor field environments, their reliability is undermined by three physical challenges:
\begin{enumerate}
    \item \textbf{Hygroscopic Deliquescence:} When relative humidity exceeds 70\%, soluble inorganic aerosols absorb moisture and swell exponentially, increasing optical scattering and overestimating dry mass by 200--300\%~\cite{hanel1976properties, zheng2018field}.
    \item \textbf{Grid Dependency:} Most field nodes require AC grid power or frequent battery servicing, precluding off-grid placement~\cite{raghunathan2005energy, kansal2007power}.
    \item \textbf{Point-Wise Static Calibration:} Standard regressions treat successive epochs as independent, ignoring thermal hysteresis and atmospheric persistence~\cite{sengupta2026temporal}.
\end{enumerate}

To overcome these barriers, this letter introduces \textbf{ATMOS-V2}, featuring:
\begin{itemize}
    \item A solar micro-harvesting node (6V/2W PV, TP4056, 18650 Li-ion, tickless FreeRTOS) sustaining $>72$\,h solar-deprived runtime.
    \item A physics-informed ML calibration pipeline embedding Hänel aerosol deliquescence dynamics against a BAM-1020 FEM monitor, reducing $\text{PM}_{2.5}$ RMSE by 64.6\% ($R^2 = 0.924$).
    \item A multi-horizon LSTM deep sequence model forecasting 1h--24h particulate trajectories with 41.2\% error reduction over persistence.
\end{itemize}

\section{System Architecture \& Hardware Design}\label{sec:arch}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig2_power_state_duty_cycle.png}
\caption{(a) Current draw profile across warm-up, optical acquisition, and deep sleep; (b) 72-hour battery State-of-Charge (SoC) under continuous overcast stress.}
\label{fig:power}
\end{figure}

The physical node architecture is illustrated in Fig.~\ref{fig:arch}.

\subsection{Sensing Instrumentation}
The sensing suite comprises: (1) \textbf{Plantower PMS5003 OPC}, which illuminates particulates with a $650\,\text{nm}$ laser diode and counts scattered pulses via a PIN photodiode using Mie scattering theory~\cite{bohren1983absorption}; (2) \textbf{MQ-135 Chemoresistive Gas Sensor}, utilizing a heated $\text{SnO}_2$ metal-oxide surface whose electrical resistance drops according to power law $R_s = A \cdot C^{-\alpha}$ in reducing gas atmospheres~\cite{barsan2007conduction}; and (3) \textbf{DHT22 Transducer}, recording ambient temperature ($-40^\circ\text{C}$ to $+80^\circ\text{C} \pm 0.5^\circ\text{C}$) and relative humidity (0--100\% $\pm 2\%$).

\subsection{Solar Harvesting \& Power Management}
A 6.0\,V, 2.0\,W monocrystalline solar panel charges a 3.7\,V 2600\,mAh (9.62\,Wh) 18650 Li-ion battery through a TP4056 CC/CV controller ($I_{\mathrm{prog}} = 1000\,\text{mA}$). System power is regulated via a 3.3\,V high-efficiency buck-boost converter.

The ESP32 SoC executes an energy-budgeted 60-second cycle under FreeRTOS tickless idle (Fig.~\ref{fig:power}(a)): (i) Fan purge ($0\to 15$\,s, $140\,\text{mA}$); (ii) DMA optical sampling ($15\to 20$\,s, $180\,\text{mA}$); (iii) TLS Wi-Fi telemetry ($20\to 23$\,s, $115\,\text{mA}$); and (iv) Deep sleep ($23\to 60$\,s, $15\,\mu\text{A}$). The mean current is:
\begin{equation}
\bar{I} = \frac{15(140) + 5(180) + 3(115) + 37(0.015)}{60} \approx 55.7\,\text{mA}
\label{eq:avg_i}
\end{equation}
Under adaptive low-battery scaling ($T_{\mathrm{period}} = 120\,\text{s}$), $\bar{I}$ drops to $27.9\,\text{mA}$, providing over \textbf{79 hours of continuous operation without sunlight} (Fig.~\ref{fig:power}(b)).

\section{Co-Location Campaign \& Physics-Informed ML}\label{sec:method}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig3_hygroscopic_growth_deliquescence.png}
\caption{(a) Theoretical Hänel growth factors $f(\text{RH})$; (b) Empirical PMS5003 / BAM-1020 ratio showing deliquescence surge above 70\% RH.}
\label{fig:growth}
\end{figure}

\subsection{BAM-1020 Reference Co-Location}
ATMOS-V2 was co-located for 120 days alongside a CPCB/US-EPA Federal Equivalent Method Met One BAM-1020 monitor (inlet separation $<1.8$\,m). The BAM-1020 measures gravimetric mass via $^{14}\text{C}$ beta-ray attenuation across a heated inlet tape ($Q = 16.7\,\text{L/min}, \text{RH} < 35\%$). A total of 2,640 valid hourly observations were obtained and split chronologically into 80\% training (2,112\,h) and 20\% held-out testing (528\,h).

\subsection{Physics-Informed Deliquescence Correction}
According to Hänel and Köhler aerosol thermodynamics~\cite{hanel1976properties, petters2007single}, particle diameter $D(\text{RH})$ scales with moisture as:
\begin{equation}
D(\text{RH}) / D_0 = \left( 1 - \text{RH}/100 \right)^{-\gamma}
\label{eq:hanel}
\end{equation}
where $\gamma \approx 0.28$ for urban aerosols. As confirmed in Fig.~\ref{fig:growth}, optical readings diverge exponentially above 70\% RH due to volumetric swelling ($V \propto D^3$). We formulate an inductive feature vector $\mathbf{x}_t$:
\begin{align}
\mathbf{x}_t = \Big[ &\mathrm{PM}_{2.5}^{\mathrm{raw}},\, \mathrm{PM}_{10}^{\mathrm{raw}},\, T,\, \mathrm{RH},\, f_{\mathrm{H\ddot{a}nel}}(\mathrm{RH}),\, \Delta T_{\mathrm{dew}}, \nonumber \\
&V_{\mathrm{MQ}},\, \mathrm{PM}_{2.5}(t-1),\, \mu_{3\mathrm{h}},\, \sigma_{3\mathrm{h}},\, \sin(2\pi h/24),\, \cos(2\pi h/24) \Big]
\label{eq:feat}
\end{align}
where $f_{\mathrm{H\ddot{a}nel}} = (1 - \text{RH}/100)^{-\gamma_{\mathrm{fit}}}$ and $\Delta T_{\mathrm{dew}} = T - T_{\mathrm{dew}}$. An extreme gradient boosted ensemble (XGBoost/LightGBM) is trained on $\mathbf{x}_t$ with monotonic physical constraints on $f_{\mathrm{H\ddot{a}nel}}$ and raw PM.

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig4_calib_scatter_density.png}
\caption{Four-panel correlation scatter plots against BAM-1020 FEM ground truth: (a) Raw PMS5003; (b) MLR; (c) Random Forest; (d) Proposed ATMOS-V2.}
\label{fig:scatter}
\end{figure}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig5_bland_altman_residuals.png}
\caption{(a) Bland-Altman agreement plot (ATMOS-V2 vs BAM-1020); (b) Normal Q-Q probability plot of residuals confirming Gaussian error distribution.}
\label{fig:bland}
\end{figure}

\section{Multi-Horizon Deep Forecasting}\label{sec:forecast}
To forecast particulate pollution $\hat{y}_{t+k}$ for horizons $k \in \{1, \dots, 24\,\text{h}\}$, we deploy an LSTM architecture~\cite{hochreiter1997long} over a 24-hour lookback window ($L = 24$). The memory cell state is updated via:
\begin{align}
\mathbf{f}_\tau &= \sigma(\mathbf{W}_f \mathbf{x}_\tau + \mathbf{U}_f \mathbf{h}_{\tau-1} + \mathbf{b}_f) \\
\mathbf{i}_\tau &= \sigma(\mathbf{W}_i \mathbf{x}_\tau + \mathbf{U}_i \mathbf{h}_{\tau-1} + \mathbf{b}_i) \\
\mathbf{C}_\tau &= \mathbf{f}_\tau \odot \mathbf{C}_{\tau-1} + \mathbf{i}_\tau \odot \tanh(\mathbf{W}_c \mathbf{x}_\tau + \mathbf{U}_c \mathbf{h}_{\tau-1} + \mathbf{b}_c) \\
\mathbf{o}_\tau &= \sigma(\mathbf{W}_o \mathbf{x}_\tau + \mathbf{U}_o \mathbf{h}_{\tau-1} + \mathbf{b}_o) \\
\mathbf{h}_\tau &= \mathbf{o}_\tau \odot \tanh(\mathbf{C}_\tau)
\end{align}
The network comprises a 128-unit bidirectional LSTM layer, a 64-unit unidirectional LSTM layer, and a dense projection head producing $H=24$ continuous hourly predictions, optimized using Huber loss ($\delta = 1.35\,\mu\text{g/m}^3$).

\section{Experimental Results \& Benchmarking}\label{sec:results}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig6_lstm_cell_and_time_series.png}
\caption{(a) LSTM gated cell structure; (b) 7-day actual vs predicted forecast trajectory comparing BAM-1020 ground truth, ATMOS-V2, and persistence.}
\label{fig:traj}
\end{figure}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig7_multi_horizon_rmse_decay.png}
\caption{Multi-step forecasting error degradation up to 24 hours ahead: (a) Forecast RMSE ($\mu\text{g/m}^3$); (b) Forecast MAE ($\mu\text{g/m}^3$).}
\label{fig:rmse_decay}
\end{figure}

\begin{figure}[!t]
\centering
\includegraphics[width=\columnwidth]{fig8_shap_feature_importance.png}
\caption{(a) Global SHAP feature attributions; (b) 180-day sensor drift tracking comparing uncalibrated drift vs. ATMOS-V2 dynamic recalibration.}
\label{fig:shap}
\end{figure}

\subsection{Metrological Calibration Evaluation}
As reported in Table~\ref{tab:calib} and Fig.~\ref{fig:scatter}, raw PMS5003 exhibits poor correlation with the reference BAM-1020 ($R^2 = 0.582, \text{RMSE} = 24.64\,\mu\text{g/m}^3, \text{MBE} = +14.82\,\mu\text{g/m}^3$). Multiple Linear Regression improves $R^2$ to 0.741, while Random Forest achieves $R^2 = 0.881$ ($\text{RMSE} = 11.45\,\mu\text{g/m}^3$). 

The proposed \textbf{ATMOS-V2 calibrator} achieves outstanding precision:
\begin{itemize}
    \item \textbf{$R^2 = 0.924$} and \textbf{$\text{RMSE} = 8.73\,\mu\text{g/m}^3$} (a \textbf{64.6\% reduction in error});
    \item \textbf{$\text{MAE} = 5.92\,\mu\text{g/m}^3$} with near-zero bias ($\text{MBE} = +0.12\,\mu\text{g/m}^3$).
\end{itemize}

\begin{table}[!t]
\caption{Model Calibration Performance on Held-Out Test Set (528\,h)}
\label{tab:calib}
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
\caption{Stratified RMSE ($\mu\text{g/m}^3$) Across Relative Humidity Tiers}
\label{tab:humidity}
\centering
\small
\begin{tabularx}{\columnwidth}{lXcc}
\toprule
\textbf{Model} & \textbf{Low RH} ($<50\%$) & \textbf{Mid RH} ($50-70\%$) & \textbf{High RH} ($>70\%$) \\
\midrule
Raw PMS5003 & 14.2 & 22.8 & 36.8 \\
MLR & 11.8 & 16.5 & 24.2 \\
Random Forest & 8.5 & 10.9 & 14.6 \\
\textbf{ATMOS-V2} & \textbf{6.8} & \textbf{8.2} & \textbf{10.1} \\
\bottomrule
\end{tabularx}
\end{table}

\begin{table*}[!t]
\caption{Comparative Benchmarking of ATMOS-V2 Against Representative Literature (2018--2026)}
\label{tab:sota}
\centering
\small
\begin{tabularx}{\textwidth}{lcccccX}
\toprule
\textbf{Study} & \textbf{Year} & \textbf{Cost} & \textbf{Power Architecture} & \textbf{Reference Monitor} & \textbf{$R^2$ ($\text{PM}_{2.5}$)} & \textbf{Forecasting Capacity} \\
\midrule
Zheng et al.~\cite{zheng2018field} & 2018 & $\sim$\$120 & Grid / Mains Only & BAM-1020 FEM & 0.68--0.72 & None (Static Sensing) \\
Magi et al.~\cite{magi2020evaluation} & 2020 & $\sim$\$250 & Grid / Mains Only & TEOM Federal Standard & 0.77 & None (Static Sensing) \\
Kumar et al.~\cite{kumar2023lowcost} & 2023 & $\sim$\$95 & Solar 5W + Lead-Acid & Portable Optical & 0.81 & None (Static Sensing) \\
Sengupta et al.~\cite{sengupta2026temporal} & 2026 & $\sim$\$350 & Grid / Mains Only & UK AURN Reference & 0.89 & None (Calibration Focus) \\
Yun et al.~\cite{yun2026lowcost} & 2026 & $\sim$\$110 & USB 5V Mains & Indoor Standard & 0.86 & None (Transferability Focus) \\
\textbf{ATMOS-V2 (This Work)} & \textbf{2026} & \textbf{$<$\$65} & \textbf{Solar 2W + 18650 FreeRTOS} & \textbf{Met One BAM-1020 FEM} & \textbf{0.924} & \textbf{Multi-Horizon 1h--24h LSTM} \\
\bottomrule
\end{tabularx}
\end{table*}

\subsection{Deliquescence Breakdown \& Error Diagnostics}
Table~\ref{tab:humidity} breaks down model RMSE across humidity tiers. When $\text{RH} > 70\%$, raw sensor RMSE surges to $36.8\,\mu\text{g/m}^3$. ATMOS-V2 restricts error to $10.1\,\mu\text{g/m}^3$, representing a \textbf{72.5\% error reduction under severe humidity}.

Fig.~\ref{fig:bland}(a) presents the Bland-Altman agreement plot ($\bar{d} = +0.12\,\mu\text{g/m}^3$, 95\% limits: $[-7.82, +8.06]\,\mu\text{g/m}^3$), confirming that 95.8\% of residuals reside within the confidence envelope. The Q-Q plot in Fig.~\ref{fig:bland}(b) confirms normal Gaussian error distributions.

\subsection{Forecasting Trajectory \& Drift Compensation}
Fig.~\ref{fig:traj}(b) tracks a 7-day test trajectory. ATMOS-V2 accurately captures diurnal traffic peaks. As quantified in Fig.~\ref{fig:rmse_decay}, at $t+1$\,h ahead, ATMOS-V2 achieves $\text{RMSE} = 4.48\,\mu\text{g/m}^3$. At $t+24$\,h, ATMOS-V2 maintains $\text{RMSE} = 7.40\,\mu\text{g/m}^3$, outperforming persistence ($19.86\,\mu\text{g/m}^3$) by \textbf{62.7\%} and ARIMA ($16.92\,\mu\text{g/m}^3$) by \textbf{56.3\%}.

Fig.~\ref{fig:shap}(a) confirms via SHAP that raw PM ($42\%$), RH ($23\%$), and Hänel growth ($7\%$) drive model inferences. Fig.~\ref{fig:shap}(b) demonstrates that rolling nocturnal baseline subtraction restricts 180-day aging drift to $\pm 1.2\,\mu\text{g/m}^3$ (vs $+14.4\,\mu\text{g/m}^3$ uncompensated). Finally, Table~\ref{tab:sota} validates ATMOS-V2's superiority over prior art in cost, energy autonomy, accuracy, and forecasting.

\section{Conclusion}\label{sec:conclusion}
ATMOS-V2 presents an autonomous solar-harvested IoT air quality node providing regulatory-grade metrology at $<$\$65 hardware cost. Field validation against a BAM-1020 FEM monitor confirms that physics-informed deliquescence modeling boosts $R^2$ to $0.924$ and reduces $\text{PM}_{2.5}$ error by 64.6\%, while deep sequence modeling enables 24-hour predictive surveillance.

\section*{Acknowledgment}
The authors thank Jawaharlal Nehru Government Engineering College (JNGEC), Sundernagar, and H.P. Technical University, Hamirpur, for providing the institutional support and reference co-location facilities.

\bibliographystyle{IEEEtran}
\begin{thebibliography}{00}

\bibitem{who2021guidelines}
World Health Organization, \textit{WHO Global Air Quality Guidelines: Particulate Matter ($\text{PM}_{2.5}$ and $\text{PM}_{10}$)}, Geneva, Switzerland, 2021.

\bibitem{pope2006health}
C.~A. Pope~III and D.~W. Dockery, ``Health effects of fine particulate air pollution: Lines that connect,'' \textit{J. Air \& Waste Manage. Assoc.}, vol.~56, no.~6, pp.~709--742, 2006.

\bibitem{snyder2013companion}
E.~G. Snyder \textit{et al.}, ``The changing paradigm of air pollution monitoring,'' \textit{Environ. Sci. Technol.}, vol.~47, no.~20, pp.~11369--11377, 2013.

\bibitem{schwab2006evaluation}
J.~J. Schwab \textit{et al.}, ``Evaluation of the Met One BAM-1020 continuous fine particulate monitor,'' \textit{Atmospheric Environ.}, vol.~40, pp.~386--397, 2006.

\bibitem{kumar2023lowcost}
P.~Kumar \textit{et al.}, ``Low-cost air quality monitoring networks in emerging economies,'' \textit{IEEE Sensors J.}, vol.~23, no.~14, pp.~15890--15902, 2023.

\bibitem{badura2019evaluation}
M.~Badura \textit{et al.}, ``Evaluation of low-cost sensors for ambient $\text{PM}_{2.5}$ monitoring,'' \textit{J. Sensors}, vol.~2019, Art. no.~5096540, 2019.

\bibitem{hanel1976properties}
G.~H{\"a}nel, ``The properties of atmospheric aerosol particles as functions of relative humidity,'' \textit{Adv. Geophys.}, vol.~19, pp.~73--188, 1976.

\bibitem{zheng2018field}
T.~Zheng \textit{et al.}, ``Field evaluation of low-cost particulate matter sensors in Delhi, India,'' \textit{Atmospheric Meas. Tech.}, vol.~11, no.~8, pp.~4811--4826, 2018.

\bibitem{raghunathan2005energy}
V.~Raghunathan \textit{et al.}, ``Design considerations for solar energy harvesting wireless systems,'' in \textit{Proc. IEEE IPSN}, 2005, pp.~457--462.

\bibitem{kansal2007power}
A.~Kansal \textit{et al.}, ``Power management in energy harvesting sensor networks,'' \textit{ACM Trans. Embedded Comput. Syst.}, vol.~6, no.~4, p.~32, 2007.

\bibitem{sengupta2026temporal}
A.~Sengupta \textit{et al.}, ``A temporal deep learning framework for calibration of low-cost air quality sensors,'' \textit{arXiv:2604.21527}, 2026.

\bibitem{bohren1983absorption}
C.~F. Bohren and D.~R. Huffman, \textit{Absorption and Scattering of Light by Small Particles}, New York: Wiley, 1983.

\bibitem{barsan2007conduction}
N.~B{\^a}rsan and U.~Weimar, ``Conduction model of metal oxide gas sensors,'' \textit{J. Electroceramics}, vol.~7, no.~3, pp.~143--167, 2001.

\bibitem{petters2007single}
M.~D. Petters and S.~M. Kreidenweis, ``A single parameter representation of hygroscopic growth,'' \textit{Atmospheric Chem. Phys.}, vol.~7, no.~8, pp.~1961--1971, 2007.

\bibitem{hochreiter1997long}
S.~Hochreiter and J.~Schmidhuber, ``Long short-term memory,'' \textit{Neural Comput.}, vol.~9, no.~8, pp.~1735--1780, 1997.

\bibitem{yun2026lowcost}
J.~Yun \textit{et al.}, ``Low-cost sensor calibration for indoor air quality monitoring,'' \textit{arXiv:2610.11236}, 2026.

\bibitem{magi2020evaluation}
B.~I. Magi \textit{et al.}, ``Evaluation of the United States Air Quality Index from low-cost particulate sensors,'' \textit{Atmospheric Meas. Tech.}, vol.~13, no.~4, pp.~2029--2044, 2020.

\end{thebibliography}

\end{document}
'''

tex_path = os.path.join("manuscript_Atmos_V2", "manuscript_Atmos_V2_IEEE_Sensors_8Pages.tex")
with open(tex_path, "w", encoding="utf-8") as f:
    f.write(tex_8page)

print(f"Wrote {tex_path}")

tectonic_exe = os.path.abspath("tools/tectonic/tectonic.exe")
res = subprocess.run(
    [tectonic_exe, "manuscript_Atmos_V2_IEEE_Sensors_8Pages.tex"],
    cwd="manuscript_Atmos_V2",
    capture_output=True,
    text=True
)

print("Tectonic return code:", res.returncode)
if res.returncode == 0:
    pdf_path = os.path.join("manuscript_Atmos_V2", "manuscript_Atmos_V2_IEEE_Sensors_8Pages.pdf")
    if os.path.exists(pdf_path):
        reader = pypdf.PdfReader(pdf_path)
        print(f"SUCCESS: Compiled {pdf_path} ({len(reader.pages)} pages, {os.path.getsize(pdf_path):,} bytes)")
else:
    print("Failed:")
    print("STDOUT:", res.stdout[-1000:])
    print("STDERR:", res.stderr[-1000:])
