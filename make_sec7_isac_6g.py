# make_sec7_isac_6g.py

def get_chapter7():
    return r"""
\clearpage
%% ==========================================================================
%%  CHAPTER 7: ADVANCED 6G SYSTEM INTEGRATION: MMWAVE BEAMFORMING AND ISAC
%% ==========================================================================
\chapter{Advanced 6G System Integration: mmWave Beamforming and ISAC}

\section{Wireless Channel Modeling for RIS-Assisted mmWave Links}
\justifying
In conventional cellular networks, the wireless propagation environment between a base station (BS) and user equipment (UE) is strictly passive and unalterable, governed by multipath fading, shadow fading, and obstacle geometry. Deploying a Reconfigurable Intelligent Surface transforms the channel into an active, programmable participant.

Consider a downlink mmWave communication system comprising a base station equipped with $M_{BS}$ antennas, an RIS comprising $N = N_x \times N_y$ reconfigurable unit cells, and a mobile user equipment (UE) with a single antenna, operating at $f_0 = 29.4\text{ GHz}$. The direct line-of-sight path between BS and UE is assumed to be severely obstructed by concrete urban buildings ($>35\text{ dB}$ attenuation).

\subsection{Cascaded Channel Matrix Formulation}
The end-to-end cascaded wireless channel is modeled as:
\begin{equation}
y = \left( \mathbf{h}_{d}^H + \mathbf{h}_{r}^H \mathbf{\Phi} \mathbf{G} \right) \mathbf{w} s + n
\label{eq:channel_cascaded}
\end{equation}
where:
\begin{itemize}[itemsep=2pt]
  \item $s \in \mathbb{C}$ is the transmitted information symbol ($\mathbb{E}[|s|^2] = 1$).
  \item $\mathbf{w} \in \mathbb{C}^{M_{BS} \times 1}$ is the base station active transmit beamforming vector ($\|\mathbf{w}\|^2 \le P_t$).
  \item $\mathbf{h}_{d} \in \mathbb{C}^{M_{BS} \times 1}$ is the direct channel between BS and UE (heavily attenuated, $\mathbf{h}_{d} \approx \mathbf{0}$).
  \item $\mathbf{G} \in \mathbb{C}^{N \times M_{BS}}$ is the channel matrix between the base station and the RIS.
  \item $\mathbf{h}_{r} \in \mathbb{C}^{N \times 1}$ is the channel vector between the RIS and the UE.
  \item $n \sim \mathcal{CN}(0, \sigma_n^2)$ is additive white Gaussian noise at the receiver.
  \item $\mathbf{\Phi} = \text{diag}(\alpha_1 e^{j\phi_1}, \alpha_2 e^{j\phi_2}, \dots, \alpha_N e^{j\phi_N}) \in \mathbb{C}^{N \times N}$ is the diagonal reflection phase-shift matrix of the RIS, where $\alpha_n \in [0, 1]$ represents the reflection magnitude and $\phi_n \in [0, 2\pi)$ represents the programmable phase shift of the $n$-th unit cell.
\end{itemize}

\begin{table}[H]
\centering
\caption{Mathematical Comparison of Wireless Propagation Channel Paradigms}
\label{tab:channel_comparison}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|l|c|p{7.2cm}|}
\hline
\textbf{Channel Link Paradigm} & \textbf{Path Loss Scaling} & \textbf{Physical Propagation Mechanics} \\
\hline
Direct Free-Space LoS & $P_r \propto d^{-2}$ & Classical spherical wave expansion in unobstructed free space. \\
Blocked Urban NLoS & $P_r \propto d^{-\alpha_{NLOS}} 10^{-\chi/10}$ & Severe log-normal shadowing ($\chi \ge 35\text{ dB}$, path loss exponent $\alpha \ge 4.2$). \\
Far-Field Cascaded RIS & $P_r \propto (d_1 d_2)^{-2}$ & Product path loss: spherical expansion from BS to RIS, followed by re-radiation from RIS to UE. \\
Near-Field Aperture RIS & $P_r \propto (d_1 + d_2)^{-2}$ & Planar wavefront scattering when user operates within the Fresnel aperture zone ($d \le 2D^2/\lambda_0$). \\
\hline
\end{tabular}
\end{table}

\subsection{Path Loss Scaling: Product vs Sum Path Loss}
A widespread misconception in metasurface research is that an RIS always suffers from the severe "product path loss" law ($P_r \propto d_1^{-2} d_2^{-2}$), where $d_1$ is BS-to-RIS distance and $d_2$ is RIS-to-UE distance. While this is true for a tiny single scatterer, an electrically large RIS panel acts as an anomalous reflecting plate. When the aperture dimension $D = N_x P_x$ is large, the near-field Fresnel boundary extends to:
\begin{equation}
d_{Fresnel} = \frac{2 D^2}{\lambda_0}
\label{eq:fresnel_boundary}
\end{equation}
For a 256-element panel ($16 \times 16$ cells, $D = 80\text{ mm}$), $d_{Fresnel} \approx 1.25\text{ m}$. When operating within or near this boundary, the array acts as a coherent mirror where received power scales with the sum of distances ($P_r \propto (d_1 + d_2)^{-2}$), drastically mitigating propagation attenuation.

\section{Progressive Phase Shift Beamsteering and Codebook Optimization}
To maximize the Signal-to-Noise Ratio (SNR) at the mobile receiver, the reflection phase shifts of all $N$ unit cells must be aligned coherently:
\begin{equation}
\max_{\{\phi_n\}} \text{SNR} = \frac{P_t \left| \sum_{n=1}^N \alpha_n e^{j\phi_n} g_n h_{r,n} \right|^2}{\sigma_n^2}
\label{eq:snr_max}
\end{equation}
The optimal phase shift for the $n$-th unit cell located at physical coordinates $(x_n, y_n)$ is derived as:
\begin{equation}
\phi_n^* = -\arg(g_n) - \arg(h_{r,n}) = k_0 \left[ x_n (\sin\theta_i \cos\phi_i - \sin\theta_r \cos\phi_r) + y_n (\sin\theta_i \sin\phi_i - \sin\theta_r \sin\phi_r) \right]
\label{eq:optimal_phase_steering}
\end{equation}
where $(\theta_i, \phi_i)$ is the angle of arrival (AoA) from the base station and $(\theta_r, \phi_r)$ is the intended angle of departure (AoD) toward the mobile receiver.

\subsection{Beam Squinting Across Wide mmWave Bandwidths}
Because the progressive phase shift $\phi_n^*$ in Equation~(\ref{eq:optimal_phase_steering}) is programmed for a fixed center frequency ($f_0 = 29.4\text{ GHz}$), operating across a wide fractional bandwidth ($B = 1\text{ GHz}$) causes the reflected beam angle $\theta_r(f)$ to shift with frequency:
\begin{equation}
\sin\theta_r(f) = \frac{f_0}{f} \sin\theta_r(f_0) + \left( 1 - \frac{f_0}{f} \right) \sin\theta_i
\label{eq:beam_squint}
\end{equation}
This phenomenon, known as \textbf{beam squinting}, causes high-frequency subcarriers to deviate from the intended receiver direction. In the proposed hybrid design, the continuous graphene tuning sheets provide real-time analog phase compensation across individual frequency sub-bands, mitigating beam-squint dispersion.

\section{Integrated Sensing and Communication (ISAC) Implementation}
Sixth-generation (6G) cellular standards mandate the convergence of radar sensing and data communications onto shared hardware and spectral allocations. The hybrid PIN--Graphene SIW RIS is uniquely suited for ISAC:
\begin{itemize}[itemsep=2pt]
  \item The \textbf{top radiating metasurface} reflects communication data beams toward mobile user terminals.
  \item The \textbf{underlying SIW cavity and slotted ground sensors} simultaneously capture backscattered radar echoes, enabling high-resolution target detection, ranging, and velocity tracking.
\end{itemize}

\subsection{Dual-Functional Radar-Communication (DFRC) Waveform}
The system employs a unified Dual-Functional Radar-Communication (DFRC) waveform. A Linear Frequency Modulated (LFM) chirp is combined with orthogonal frequency division multiplexing (OFDM) communication symbols:
\begin{equation}
s_{ISAC}(t) = \sum_{k=0}^{K-1} c_k \exp\left( j 2\pi f_k t + j \pi \mu t^2 \right) \text{rect}\left( \frac{t - T_p/2}{T_p} \right)
\label{eq:dfrc_waveform}
\end{equation}
where $c_k$ is the communication QAM data symbol on the $k$-th subcarrier, $f_k = f_0 + k\Delta f$, $\mu = B / T_p$ is the chirp rate, $B = 1.0\text{ GHz}$ is the sweep bandwidth, and $T_p = 1.0\,\mu\text{s}$ is the pulse duration.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.72\textwidth]{figures/plot_isac_waveform_range_profile.png}
    \caption{6G Integrated Sensing and Communication (ISAC) System Performance: (Left) Dual-Functional Radar-Communication Linear Chirp Spectrogram ($28.9 - 29.9\text{ GHz}$); (Right) High-Resolution Radar Target Range Profile Resolving Multiple Targets at $18.5\text{ m}$ and $32.0\text{ m}$.}
    \label{fig:isac_radar_profile}
\end{figure}

As demonstrated in Figure~\ref{fig:isac_radar_profile}:
\begin{itemize}[itemsep=2pt]
  \item \textbf{Radar Range Resolution ($\Delta R$):} Governed by the chirp bandwidth $B = 1.0\text{ GHz}$:
  \begin{equation}
  \Delta R = \frac{c}{2B} = \frac{3 \times 10^8\text{ m/s}}{2 \times 1.0 \times 10^9\text{ Hz}} = 0.15\text{ m} = 15.0\text{ cm}
  \label{eq:range_resolution}
  \end{equation}
  This sub-meter resolution enables precision positioning of vehicles and pedestrians in smart city environments.
  \item \textbf{Target Range Profile:} The matched-filter range profile in Figure~\ref{fig:isac_radar_profile} cleanly resolves two distinct scattering targets positioned at $R_1 = 18.5\text{ m}$ and $R_2 = 32.0\text{ m}$ with high peak-to-sidelobe ratios ($>18\text{ dB}$).
\end{itemize}

\begin{table}[H]
\centering
\caption{ISAC Radar and Communication Operating Specifications at $29.4\text{ GHz}$}
\label{tab:isac_specs}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|l|c|l|}
\hline
\textbf{System Parameter} & \textbf{Numerical Value} & \textbf{Operational Role} \\
\hline
Carrier Center Frequency ($f_0$) & $29.40\text{ GHz}$ & Nominal Ka-band resonance center. \\
Chirp RF Bandwidth ($B$) & $1.0\text{ GHz}$ ($28.9 - 29.9\text{ GHz}$) & Governs radar range resolution ($15\text{ cm}$). \\
Pulse Duration ($T_p$) & $1.0\,\mu\text{s}$ & Radar pulse repetition interval (PRI). \\
Range Resolution ($\Delta R$) & $0.15\text{ m}$ ($15.0\text{ cm}$) & Target localization precision. \\
Maximum Unambiguous Range & $150.0\text{ m}$ & Urban street canyon coverage radius. \\
Data Modulation & $64\text{-QAM}$ OFDM & Communication throughput ($>2.5\text{ Gbps}$). \\
SIW Resonant Sensitivity & $185\text{ MHz/RIU}$ & Real-time environmental dielectric sensing. \\
\hline
\end{tabular}
\end{table}

\section{Urban mmWave Blockage Bypass and Deployment Scenarios}
The practical utility of the proposed hybrid RIS is manifested in challenging urban communication environments:
\begin{enumerate}
  \item \textbf{Urban Street Canyons and Blind Corners:} In dense metropolitan centers (e.g., smart intersections), skyscrapers create deep shadow zones. Mounting hybrid RIS panels on building facades at heights of $4-6\text{ m}$ enables non-line-of-sight anomalous reflection, delivering seamless gigabit connectivity to connected autonomous vehicles (V2X).
  \item \textbf{Outdoor-to-Indoor Penetration Enhancement:} Modern energy-efficient glass windows incorporate metallic thermal coatings that attenuate mmWave signals by $>30\text{ dB}$. Installing an RIS on exterior walls or transparent smart metasurfaces on window panes directs collimated beams through indoor corridors, eliminating indoor dead zones.
  \item \textbf{Industrial IoT and Smart Warehouses:} In automated factory environments with moving robotic arms and metal shelving units causing dynamic blockage, RIS arrays dynamically track moving automated guided vehicles (AGVs), maintaining continuous URLLC telemetry.
\end{enumerate}
"""
