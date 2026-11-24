# atmos_make_sec2_litreview.py

def get_chapter2():
    return r"""%% ==========================================================================
%%  CHAPTER 2: COMPREHENSIVE LITERATURE REVIEW
%% ==========================================================================
\chapter{Literature Review}

\section{Introduction and Historical Overview}
Over the past three decades, atmospheric science and environmental engineering have transitioned from intermittent gravimetric filter sampling toward automated, real-time telemetry and predictive modeling. The historical progression of air quality monitoring can be demarcated into three distinct technological paradigms:
\begin{enumerate}[label=\textbf{\arabic*.}]
    \item \textbf{First-Generation Manual Gravimetric Networks (1970s--1990s):} Utilized high-volume air samplers drawing ambient air through pre-weighed quartz or Teflon membrane filters over 24-hour periods. While providing indisputable gravimetric mass accuracy, these systems required labor-intensive laboratory conditioning, desiccator weighing, and post-exposure chemical extraction, introducing data reporting latencies of days to weeks.
    \item \textbf{Second-Generation Continuous Automated Stations (2000s--2010s):} Introduced automated reference instruments capable of continuous hourly reporting, notably the Beta Attenuation Monitor (BAM) and Tapered Element Oscillating Microbalance (TEOM). Although revolutionizing regulatory compliance tracking, their immense capital expenditure restricted deployments to sparse municipal centers.
    \item \textbf{Third-Generation Distributed IoT and Edge-AI Networks (2015--Present):} Enabled by micro-electro-mechanical systems (MEMS), compact laser optical particle counters (OPCs), low-power wireless microcontrollers (e.g., ESP32, STM32), and cloud-hosted machine learning. This paradigm democratizes environmental data, providing hyperlocal spatial granularity at a fraction of conventional costs.
\end{enumerate}

This chapter conducts a thorough, critical review of the physical principles, sensor operational mechanisms, hygroscopic deliquescence physics, machine learning calibration paradigms, and time-series forecasting frameworks that establish the scientific foundation of the ATMOS project.

\section{Regulatory Continuous Air Quality Instrumentation}
To evaluate the performance of low-cost sensors, it is imperative to understand the analytical physics governing regulatory gold-standard instruments against which sensors are calibrated.

\subsection{Beta Attenuation Monitoring (BAM)}
The Beta Attenuation Monitor (most notably the Met One BAM-1020) serves as the primary Federal Equivalent Method (FEM) benchmark adopted by the US EPA and India's Central Pollution Control Board. The instrument operates on the physical principle of beta radiation absorption by particulate mass deposited on a continuous continuous-roll glass fiber filter tape.

The fundamental governing relation is derived from the Beer-Lambert radiometric attenuation law:
\begin{equation}
I = I_0 \cdot \exp(-\mu \cdot x) = I_0 \cdot \exp\left(-\mu_m \cdot \frac{m}{A}\right)
\label{eq:beer_lambert}
\end{equation}
where $I_0$ is the incident beta ray intensity emitted from a low-level radioactive carbon-14 ($^{14}\text{C}$) or krypton-85 ($^{85}\text{Kr}$) source, $I$ is the transmitted intensity detected by a scintillation counter or semiconductor detector, $\mu$ is the linear attenuation coefficient, $\mu_m = \mu / \rho$ is the mass attenuation coefficient (which remains remarkably invariant across diverse chemical species of aerosol), $m$ is the particulate mass collected, and $A$ is the exposed filter deposit area.

By taking the natural logarithm of the intensity ratio before and after sample collection over an accurately metered volumetric air sample $V = Q \cdot \Delta t$ (where $Q$ is the volumetric flow rate regulated by a mass flow controller, typically $16.67\,\text{L/min}$ to yield $1.0\,\text{m}^3/\text{hour}$), the ambient particulate mass concentration $C_{\text{BAM}}$ is computed directly:
\begin{equation}
C_{\text{BAM}} = \frac{1}{\mu_m \cdot Q \cdot \Delta t} \ln\left(\frac{I_{\text{blank}}}{I_{\text{sample}}}\right)
\label{eq:bam_concentration}
\end{equation}
Because beta particle absorption depends almost exclusively on the electron density of the absorbed matter rather than optical color, refractive index, or morphology, BAM-1020 measurements provide an authoritative ground truth with an analytical measurement resolution of $\pm 0.1\,\mu\text{g/m}^3$ and an hourly precision of $\pm 2.0\,\mu\text{g/m}^3$.

\subsection{Tapered Element Oscillating Microbalance (TEOM)}
The TEOM (Thermo Fisher Scientific) operates on an inertial microbalance principle. Ambient air is drawn through a hollow tapered quartz element carrying a replaceable filter cartridge at its tip. The element is maintained in continuous oscillation at its natural resonant frequency $\omega_n$ by an electronic feedback circuit. As particulate matter accumulates on the filter, the total mass increases, causing an inverse shift in resonant frequency:
\begin{equation}
\Delta m = K_0 \cdot \left(\frac{1}{f_1^2} - \frac{1}{f_0^2}\right)
\label{eq:teom_freq}
\end{equation}
where $K_0$ is a factory-calibrated spring constant and $f_0, f_1$ denote the resonant oscillation frequencies before and after sampling. While providing sub-hourly mass tracking, TEOM systems require heated sample inlets ($50^\circ\text{C}$) to eliminate relative humidity interference, which volatilizes semi-volatile organic compounds and ammonium nitrate, leading to systematic mass underestimation during cold winter conditions.

\section{Low-Cost Optical Particulate Matter Sensors and Mie Theory}
Compact low-cost particulate matter sensors, such as the Plantower PMS5003, Sensirion SPS30, and Nova Fitness SDS011, estimate mass concentration using optical light scattering.

\subsection{Electrodynamic Mie Scattering Physics}
When a collimated laser beam of wavelength $\lambda$ (typically $650\,\text{nm}$ red semiconductor diode laser) illuminates an aerosol particle suspended within the sensing chamber, light is scattered across all spatial angles. Because atmospheric $\text{PM}_{2.5}$ particles possess aerodynamic diameters ($0.1\,\mu\text{m} \le d_p \le 2.5\,\mu\text{m}$) comparable to the incident optical wavelength, the scattering behavior lies strictly within the electrodynamic \textbf{Mie scattering regime}, where the dimensionless size parameter $x$ is defined as:
\begin{equation}
x = \frac{\pi \cdot d_p}{\lambda} \approx 0.5 \text{ to } 12.0
\label{eq:size_parameter}
\end{equation}

Under Mie theory, the scattered light intensity $I_s(\theta, \phi)$ observed at scattering angle $\theta$ relative to the incident forward beam at distance $r$ is expressed in terms of the dimensionless scattering amplitude functions $S_1(\theta)$ and $S_2(\theta)$:
\begin{equation}
I_s(\theta) = \frac{\lambda^2}{8\pi^2 r^2} \left( |S_1(\theta)|^2 + |S_2(\theta)|^2 \right) I_0
\label{eq:mie_intensity}
\end{equation}
where $S_1(\theta)$ and $S_2(\theta)$ are infinite series expansions of spherical Bessel functions and Legendre polynomials parameterized by the complex refractive index of the aerosol $m = n - i\kappa$:
\begin{equation}
S_1(\theta) = \sum_{n=1}^{\infty} \frac{2n+1}{n(n+1)} \left[ a_n \pi_n(\cos\theta) + b_n \tau_n(\cos\theta) \right]
\label{eq:mie_s1}
\end{equation}
\begin{equation}
S_2(\theta) = \sum_{n=1}^{\infty} \frac{2n+1}{n(n+1)} \left[ a_n \tau_n(\cos\theta) + b_n \pi_n(\cos\theta) \right]
\label{eq:mie_s2}
\end{equation}

The photodiode detector in the PMS5003 is positioned at an orthogonal angle ($\theta = 90^\circ$) to collect scattered flux over a defined solid angle $\Omega$. The integrated photoelectric current is converted to voltage pulses via a transimpedance amplifier, counted, and binned into size distributions. Total mass concentration $C_{\text{PM}}$ is subsequently estimated assuming spherical particle volume and an empirical density constant $\rho_{\text{eff}} \approx 1.65\,\text{g/cm}^3$:
\begin{equation}
C_{\text{PM2.5}} = \frac{\pi}{6} \rho_{\text{eff}} \sum_{i \in \text{bins}} N_i \cdot \bar{d}_{p,i}^3
\label{eq:optical_mass}
\end{equation}

\subsection{Hygroscopic Growth and Deliquescence Physics}
The primary physical limitation of optical particle counters stems from atmospheric moisture. Atmospheric aerosols contain hydrophilic inorganic salts (e.g., ammonium sulfate $(\text{NH}_4)_2\text{SO}_4$, ammonium nitrate $\text{NH}_4\text{NO}_3$, and sodium chloride $\text{NaCl}$). As ambient relative humidity ($\text{RH}$) increases toward the deliquescence relative humidity point ($\text{DRH} \approx 70\%\text{--}75\%$), these salt particles spontaneously undergo a phase transition from solid crystals into liquid aqueous droplets.

According to classical Köhler theory, droplet equilibrium water activity is governed by the curvature (Kelvin) effect and solute Raoult term:
\begin{equation}
\ln\left(\frac{\text{RH}}{100}\right) = \frac{4\sigma_{w} M_w}{R T \rho_w d_p} - \frac{6 n_s M_w}{\pi \rho_w (d_p^3 - d_0^3)}
\label{eq:koehler}
\end{equation}
where $\sigma_w$ is the surface tension of water, $M_w$ is the molecular weight of water, and $n_s$ is moles of solute.

To correct for this optical enhancement in field sensors without knowing exact chemical species, atmospheric physicists utilize Hänel's empirical hygroscopic growth factor $f(\text{RH})$:
\begin{equation}
f(\text{RH}) = \frac{C_{\text{measured}}}{C_{\text{dry}}} = 1 + a \cdot \left( \frac{\text{RH}}{100 - \text{RH}} \right)^b
\label{eq:hanel_theory}
\end{equation}
where $a$ represents the particle hygroscopicity parameter and $b$ characterizes the deliquescence curvature rate. When $\text{RH} < 60\%$, $f(\text{RH}) \approx 1.0$. However, as $\text{RH}$ exceeds $80\%$, $f(\text{RH})$ can exceed $2.5$ to $4.0$, causing uncalibrated optical sensors to over-report $\text{PM}_{2.5}$ by up to $300\%$. Incorporating Hänel's formula into machine learning calibration architectures is thus a vital novel enhancement.

\section{Chemoresistive Metal Oxide Gas Sensing Physics}
Atmospheric hazardous gases ($\text{CO}, \text{NH}_3, \text{CH}_4, \text{NO}_2$) are monitored in ATMOS using SnO$_2$ metal oxide semiconductor (MOS) sensors (MQ-135, MQ-7, MQ-4). The sensing mechanism is governed by oxygen chemisorption on the surface of n-type semiconductor grains heated to $300^\circ\text{C}$ to $400^\circ\text{C}$.

In clean ambient air, atmospheric oxygen molecules adsorb onto the SnO$_2$ crystalline grain boundaries, extracting conduction-band electrons to form ionized oxygen species ($\text{O}_2^-, \text{O}^-, \text{O}^{2-}$):
\begin{equation}
\text{O}_{2\text{,(gas)}} + 2e^- \rightleftharpoons 2\text{O}^-_{\text{(ads)}}
\label{eq:chemisorption}
\end{equation}
This electron extraction creates an electron-depletion layer (space-charge region) across the grain boundaries, elevating the electrical potential barrier $qV_s$ and yielding a high baseline sensor resistance $R_0$:
\begin{equation}
R_0 \propto \exp\left( \frac{q V_s}{k_B T} \right)
\label{eq:depletion_resistance}
\end{equation}

When a reducing gas such as carbon monoxide ($\text{CO}$) or ammonia ($\text{NH}_3$) enters the chamber, it undergoes a surface oxidation-reduction reaction with the adsorbed oxygen ions:
\begin{equation}
\text{CO} + \text{O}^-_{\text{(ads)}} \longrightarrow \text{CO}_{2\text{,(gas)}} + e^-
\label{eq:co_redox}
\end{equation}
\begin{equation}
2\text{NH}_3 + 3\text{O}^-_{\text{(ads)}} \longrightarrow \text{N}_{2\text{,(gas)}} + 3\text{H}_2\text{O}_{\text{,(gas)}} + 3e^-
\label{eq:nh3_redox}
\end{equation}
The liberated electrons are reinjected into the SnO$_2$ conduction band, thinning the space-charge depletion barrier and drastically lowering the electrical resistance $R_s$. The gas concentration $C$ in parts per million (ppm) follows the power-law empirical relation:
\begin{equation}
R_s = A \cdot C^{-\alpha} \implies \log(R_s / R_0) = -\alpha \log(C) + \beta
\label{eq:mos_powerlaw}
\end{equation}

\section{Machine Learning Paradigms for Sensor Calibration}
Calibrating low-cost sensors against reference monitors has evolved from simple univariate laboratory gains to multi-variate machine learning models deployed on co-located field data.

\subsection{Multivariate Linear Regression (MLR / OLS)}
Multivariate linear regression models express the reference concentration $y_i$ as an affine combination of the raw optical particulate measurement and environmental covariates:
\begin{equation}
\hat{y}_i = \beta_0 + \beta_1 x_{i,\text{raw}} + \beta_2 x_{i,\text{temp}} + \beta_3 x_{i,\text{rh}} + \epsilon_i
\label{eq:mlr_form}
\end{equation}
The parameter vector $\boldsymbol{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ is solved analytically via Ordinary Least Squares. While structurally simple, linear regression is highly regularized by construction. It avoids generating extreme anomalous predictions when encountering unobserved covariate combinations, providing robust out-of-sample generalization in non-stationary outdoor environments.

\subsection{Random Forest Regressor (RF)}
Random Forest is an ensemble learning method based on bootstrap aggregation (bagging) of $B$ decorrelated decision trees $\{T_1, \dots, T_B\}$. For an input vector $\mathbf{x}$, the ensemble prediction is the arithmetic mean:
\begin{equation}
\hat{y}_{\text{RF}}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^{B} T_b(\mathbf{x})
\label{eq:rf_ensemble}
\end{equation}
Each tree is grown using a randomized subset of $m \le p$ features at each node split, optimizing variance reduction according to the Mean Squared Error impurity criterion:
\begin{equation}
Q(R) = \frac{1}{|R|} \sum_{i \in R} (y_i - \bar{y}_R)^2
\label{eq:mse_impurity}
\end{equation}
While Random Forest can capture subtle non-linear interactions (such as the exponential rise in sensor response at high RH), it cannot extrapolate beyond the minimum and maximum target bounds present in the training set. If noisy sensor spikes occur during training, unpruned decision trees risk memorizing the noise, leading to degraded test set performance.

\section{Time-Series Forecasting Models and the Persistence Baseline}
Predicting future air quality requires modeling dynamic temporal sequences $\mathbf{y}_{1:t} \to \hat{y}_{t+h}$.

\subsection{The Persistence Baseline Model}
In atmospheric science, the persistence (naive random-walk) benchmark assumes that the physical atmosphere is inertial over short intervals:
\begin{equation}
\hat{y}_{t+h}^{\text{pers}} = y_t
\label{eq:persistence_model}
\end{equation}
For a 1-hour prediction horizon ($h=1$), persistence is an exceptionally strong benchmark because particulate dispersion, wind velocity changes, and boundary layer mixing occur gradually. In published literature, many purported machine learning models fail to outperform the persistence benchmark when rigorously tested. Any valid novel forecasting model must explicitly benchmark its performance against persistence to demonstrate true predictive value.

\subsection{Autoregressive and Multi-Lag Architectures}
Advanced statistical forecasting constructs a multi-lag feature matrix incorporating the preceding $p$ hourly observations:
\begin{equation}
\hat{y}_{t+1} = f\left( y_t, y_{t-1}, y_{t-2}, \dots, y_{t-p+1}, \mathbf{z}_t \right)
\label{eq:autoregressive_general}
\end{equation}
where $\mathbf{z}_t$ includes deterministic cyclical diurnal features:
\begin{equation}
\mathbf{z}_t = \left[ \sin\left(\frac{2\pi \cdot \text{hour}_t}{24}\right),\, \cos\left(\frac{2\pi \cdot \text{hour}_t}{24}\right) \right]
\label{eq:diurnal_harmonic}
\end{equation}
Embedding cyclical harmonics accounts for rush-hour traffic peaks (08:00 and 18:00) and nocturnal boundary layer compression without requiring separate categorical indicator variables.

\section{Comprehensive Comparative Literature Synthesis}
To delineate the precise academic contribution of ATMOS, Tables \ref{tab:lit_comparison} and \ref{tab:technique_comparison} present a systematic comparative evaluation against prominent published research works.

\begin{table}[H]
\renewcommand{\arraystretch}{0.88}
\centering
\scriptsize
\caption{Systematic comparison of published air quality research against the proposed ATMOS project.}
\label{tab:lit_comparison}
\begin{tabularx}{\textwidth}{|p{0.14\textwidth}|p{0.08\textwidth}|p{0.15\textwidth}|p{0.12\textwidth}|p{0.16\textwidth}|X|}
\hline
\textbf{Author \& Year} & \textbf{Power} & \textbf{Sensor Array} & \textbf{Algorithm} & \textbf{Validation Data} & \textbf{Primary Limitations vs. ATMOS} \\
\hline
Zheng et al. (2018) & Grid AC & Plantower PMS3003 & Linear \& Quadratic MLR & 3 months co-location (US Embassy) & Mains dependent; no gas sensing; no predictive forecasting pipeline. \\
\hline
Badura et al. (2019) & Grid AC & PMS7003, SDS011, OPC-N2 & OLS, Ridge, SVR & 6 months field data (Wroclaw, Poland) & Benchmarks sensors but lacks autonomous energy harvesting and IoT dashboard. \\
\hline
Magi et al. (2020) & Grid AC & PurpleAir PA-II (Dual PMS5003) & Univariate RH correction & Multi-year EPA network & Static correction factors; lacks multi-gas sensing and temporal AI forecasting. \\
\hline
Ali et al. (2024) & Grid AC & Optical PM2.5 + Temp/RH & LSTM \& Temporal CNN & 12 months urban co-location & Complex deep learning with high computational overhead; no solar autonomy. \\
\hline
Kumar et al. (2023) & Solar (5W) & MQ-135, MQ-7, DHT11 & Threshold Alert Logic & Laboratory test chamber only & No regulatory BAM co-location; no ML calibration; no time-series forecasting. \\
\hline
\textbf{ATMOS (Proposed Work)} & \textbf{Solar (2W) + Li-ion} & \textbf{PMS5003 + MQ-135 + MQ-7 + MQ-4 + DHT22} & \textbf{Hänel + MLR/RF + 24-Lag Forecasting} & \textbf{15,755 hourly BAM co-location records} & \textbf{Completely autonomous off-grid node with end-to-end cloud GIS, two-stage ML, and persistence benchmarking.} \\
\hline
\end{tabularx}
\end{table}

\begin{table}[H]
\renewcommand{\arraystretch}{0.88}
\centering
\small
\caption{Technique-based literature comparison across monitoring, calibration, and forecasting methodologies.}
\label{tab:technique_comparison}
\begin{tabularx}{\textwidth}{|p{0.20\textwidth}|p{0.22\textwidth}|X|p{0.24\textwidth}|}
\hline
\textbf{Methodology Area} & \textbf{Conventional Approach} & \textbf{Key Advantages \& Inherent Drawbacks} & \textbf{ATMOS Project Advancement} \\
\hline
\textbf{Particulate Monitoring} & Centralized BAM-1020 / TEOM stations & Gold-standard gravimetric accuracy, but prohibitive cost (\$40,000+) and extreme spatial sparsity. & Low-cost optical PMS5003 calibrated via machine learning against reference BAM. \\
\hline
\textbf{Power Supply Architecture} & Continuous 230V AC mains connection & Reliable continuous power, but limits deployment to electrified municipal structures. & 6V/2W solar harvesting with TP4056 and dual Li-ion cells yielding 53-day autonomy. \\
\hline
\textbf{Environmental Calibration} & Laboratory chamber gas-span calibration & High precision under controlled conditions, but fails completely in complex dynamic field environments. & 15,755-hour field co-location modeling with Hänel hygroscopic deliquescence compensation. \\
\hline
\textbf{Predictive Analytics} & Single-step statistical extrapolation & Reports purely historical readings; predictive claims rarely benchmarked against persistence. & 24-hour lag feature store rigorously benchmarked against persistence baseline ($R^2 = 0.902$). \\
\hline
\textbf{Spatial Presentation} & Tabular data dumps or static CSVs & Inconvenient for municipal administrators and general public health awareness. & Interactive Leaflet GIS mapping with live GPS and dynamic CPCB sub-index computation. \\
\hline
\end{tabularx}
\end{table}

\section{Identified Research Gaps and Project Motivation}
A synthesis of the existing literature reveals four critical research gaps:
\begin{enumerate}[label=(\roman*)]
    \item \textbf{Disconnection between Hardware and Advanced Analytics:} Most studies either focus exclusively on embedded IoT hardware assembly (reporting raw, uncalibrated sensor values) or focus on computer science datasets without designing physical off-grid hardware.
    \item \textbf{Neglect of Hygroscopic Aerosol Physics in ML:} Standard machine learning papers treat relative humidity purely as an arbitrary regression feature without embedding the non-linear deliquescence behavior characterized by Hänel's equation.
    \item \textbf{Failure to Benchmark Against Persistence in Air Quality Forecasting:} Numerous works claim high forecasting accuracy using complex neural networks but fail to compare their models against the naive persistence baseline, masking the fact that persistence often outperforms machine learning over short horizons.
    \item \textbf{Absence of Off-Grid Himalayan Valley Case Studies:} Valley topographies in the Western Himalayas (such as Sundernagar) experience unique winter thermal inversions that demand solar-powered, localized monitoring.
\end{enumerate}

ATMOS is expressly designed to bridge these gaps by uniting rigorous hardware micro-grid engineering with a scientifically verified, two-stage machine learning predictive analytics pipeline.
"""
