# make_sec1_intro.py

def get_chapter1():
    return r"""
\clearpage
\pagenumbering{arabic}
\setcounter{page}{1}

%% ==========================================================================
%%  CHAPTER 1: INTRODUCTION TO THE INTERNSHIP & RESEARCH PROJECT
%% ==========================================================================
\chapter{Introduction to the Internship and Research Project}

\section{Project Overview and Executive Summary}
\justifying
The inexorable surge in global mobile data traffic, driven by ultra-high-definition video streaming, autonomous vehicular telematics, immersive extended reality (XR), and industrial Internet of Things (IoT) ecosystems, has pushed fourth-generation (4G) and early fifth-generation (5G) sub-6 GHz cellular bands to their theoretical Shannon capacity limits. Consequently, modern telecommunication infrastructure is aggressively expanding into the millimeter-wave (mmWave) spectrum ($24\text{ to }100\text{ GHz}$) and pioneering architectural blueprints for emerging sixth-generation (6G) networks. The mmWave band offers unprecedented contiguous bandwidths spanning gigahertz, enabling multi-gigabit-per-second (Gbps) data rates and sub-millisecond air-interface latencies.

However, mmWave electromagnetic signals suffer from severe free-space path loss (governed by Friis transmission law where path attenuation scales inversely with the square of the operational wavelength, $\lambda^2$), intense atmospheric resonance absorption (such as the oxygen molecule absorption peak near $60\text{ GHz}$ and water vapor attenuation at $22\text{ GHz}$), and extreme susceptibility to shadowing and physical blockage by buildings, terrain, foliage, and human bodies. In dense urban topographies, mmWave propagation is predominantly line-of-sight (LoS). When the direct LoS trajectory between an active base station (gNodeB) and user equipment (UE) is obstructed, received signal power plummets by $25\text{ to }40\text{ dB}$, inducing severe connection dropouts and creating pervasive communication "dead zones".

\begin{figure}[H]
    \centering
    \includegraphics[width=0.74\textwidth]{figures/diagram_6g_ris_smart_environment.png}
    \caption{6G Smart Radio Environment: Blockage Bypass and Non-Line-of-Sight Coverage Restoration via Hybrid PIN--Graphene Reconfigurable Intelligent Surface.}
    \label{fig:ch1_smart_env}
\end{figure}

To surmount these physical propagation bottlenecks without deploying cost-prohibitive and power-hungry active base stations or traditional relays, \textbf{Reconfigurable Intelligent Surfaces (RIS)}---also referred to as software-controlled metasurfaces or intelligent reflecting surfaces (IRS)---have emerged as a revolutionary paradigm. An RIS is a planar two-dimensional array composed of a vast number of sub-wavelength metallic or dielectric meta-atoms (unit cells). By dynamically controlling the electromagnetic boundary conditions of each unit cell via integrated switching or tuning elements, an RIS can customize the phase, amplitude, frequency, and polarization of impinging electromagnetic waves in real time. This capability transforms the traditionally stochastic and hostile wireless propagation channel into a deterministic, software-reconfigurable "smart radio environment."

This internship research project, conducted at the \textbf{Department of Electronics and Communication Engineering, National Institute of Technology (NIT) Jalandhar}, investigates the design, electromagnetic modeling, and full-wave 3D numerical simulation of a novel \textbf{hybrid PIN--Graphene Reconfigurable Intelligent Surface unit cell with Substrate Integrated Waveguide (SIW) sensing integration} optimized for $29.4\text{ GHz}$ mmWave operation. By pairing discrete semiconductor PIN diodes with continuous, chemically tunable monolayer graphene impedance sheets on a multi-layer Isola dielectric substrate, this architecture synthesizes both coarse binary phase switching and continuous analog impedance trimming, while the underlying SIW cavity enables simultaneous environmental sensing.

\section{Motivation and Millimeter-Wave Propagation Challenges}
\subsection{The mmWave Propagation Dilemma}
The transition from sub-6 GHz microwave bands to the mmWave spectrum represents a fundamental paradigm shift in electromagnetic wave propagation. While Friis free-space transmission formula dictates that received power is:
\begin{equation}
P_r = P_t G_t G_r \left( \frac{\lambda_0}{4\pi d} \right)^2 = P_t G_t G_r \left( \frac{c}{4\pi f d} \right)^2
\label{eq:friis_path_loss}
\end{equation}
where $P_t$ is transmitted power, $G_t$ and $G_r$ are transmitter and receiver antenna gains, $\lambda_0$ is free-space wavelength, $c$ is the speed of light, $f$ is operating frequency, and $d$ is separation distance. At $f = 29.4\text{ GHz}$, $\lambda_0 \approx 10.2\text{ mm}$, resulting in an intrinsic free-space path loss that is approximately $20\text{ dB}$ higher than at $3\text{ GHz}$ for identical isotropic antennas over the same distance $d$.

\begin{table}[H]
\centering
\caption{Millimeter-Wave Frequency Bands and Channel Propagation Characteristics}
\label{tab:mmwave_bands}
\small
\renewcommand{\arraystretch}{1.05}
\begin{tabular}{|l|c|c|p{6.5cm}|}
\hline
\textbf{Band Designation} & \textbf{Frequency ($f$)} & \textbf{Wavelength ($\lambda_0$)} & \textbf{Dominant Atmospheric \& Channel Phenomena} \\
\hline
Ka-Band (Design Focus) & $26.5 - 40.0\text{ GHz}$ & $11.3 - 7.5\text{ mm}$ & Moderate rain fade, low molecular absorption, primary 5G NR n257/n258/n261 deployment bands. \\
V-Band & $50.0 - 75.0\text{ GHz}$ & $6.0 - 4.0\text{ mm}$ & Intense $O_2$ molecular resonance attenuation ($\sim 15\text{ dB/km}$ at $60\text{ GHz}$); short-range security links. \\
E-Band & $71.0 - 86.0\text{ GHz}$ & $4.2 - 3.5\text{ mm}$ & Low atmospheric absorption window; point-to-point ultra-high-capacity mobile backhaul. \\
W-Band & $75.0 - 110.0\text{ GHz}$ & $4.0 - 2.7\text{ mm}$ & Sub-THz transition; extreme diffraction loss, severe shadow fading, automotive imaging radar. \\
\hline
\end{tabular}
\end{table}

Beyond free-space spreading, mmWave wavelengths are comparable to the surface roughness of common building materials, transitioning electromagnetic scattering from specular reflection to diffuse, incoherent scattering. Penetration through solid structures is virtually non-existent; standard tinted building glass introduces $20\text{ to }40\text{ dB}$ of attenuation, while reinforced concrete blocks signals by over $50\text{ to }80\text{ dB}$. Consequently, outdoor-to-indoor signal penetration fails completely, isolating indoor user equipment unless dedicated relaying infrastructure is installed.

\subsection{Limitations of Traditional Relay Networks and Active MIMO}
To mitigate severe shadow fading and blockage, conventional wireless network engineering relies on two established strategies:
\begin{enumerate}[itemsep=3pt]
  \item \textbf{Dense Small-Cell Densification:} Deploying high densities of active base stations (micro- and pico-cells) across urban street canyons.
  \item \textbf{Active Amplify-and-Forward (AF) / Decode-and-Forward (DF) Relays:} Installing dedicated transceiver repeaters to capture, amplify, and retransmit signals around physical obstacles.
\end{enumerate}

While effective in expanding coverage, these active approaches exhibit severe fundamental drawbacks that render them unsustainable for massive 6G scaling:
\begin{itemize}[itemsep=2pt]
  \item \textbf{Prohibitive Power Consumption:} Active relays require complete radio frequency (RF) front-ends, including high-linearity Power Amplifiers (PAs), Low Noise Amplifiers (LNAs), mixers, phase-locked loops (PLLs), and power-hungry Digital Signal Processors (DSPs). A typical 5G active relay consumes hundreds of watts, escalating operational expenditure (OPEX) and carbon footprints.
  \item \textbf{Full-Duplex Self-Interference:} In-band active relays suffer from severe self-interference caused by strong transmit signals leaking into sensitive receive antenna ports, necessitating complex, lossy analog and digital cancellation circuitry.
  \item \textbf{Noise Amplification and Latency:} Amplify-and-forward repeaters indiscriminately amplify channel noise and out-of-band interference, degrading end-to-end Signal-to-Noise Ratio (SNR). Decode-and-forward systems introduce significant baseband processing latency ($5\text{ to }20\text{ ms}$), violating ultra-reliable low-latency communication (URLLC) mandates.
  \item \textbf{High Capital Hardware Expenditure (CAPEX):} Installing active micro-cells requires expensive site acquisition, dedicated fiber-optic backhaul links, and complex thermal dissipation infrastructure.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.72\textwidth]{figures/plot_ris_link_budget_comparison.png}
    \caption{Comparative Received Signal Power ($P_r$) vs Propagation Distance at $29.4\text{ GHz}$ for Direct LoS, Blocked NLoS ($35\text{ dB}$ Shadowing), Active Relay, and Hybrid PIN--Graphene RIS ($256$ Elements).}
    \label{fig:ch1_link_budget}
\end{figure}

\section{The Paradigm of Reconfigurable Intelligent Surfaces}
Reconfigurable Intelligent Surfaces circumvent the fundamental trade-offs of active relays by introducing an entirely passive, software-defined wavefront engineering layer into the wireless channel. An RIS does not generate new RF signals or amplify incoming waveforms; instead, it acts as an anomalous electromagnetic mirror whose spatial phase response can be programmed digitally.

When an electromagnetic wave impinges upon a conventional metallic surface, it obeys classic Snell's Law: the angle of reflection equals the angle of incidence ($\theta_r = \theta_i$). In stark contrast, an RIS establishes an artificial, spatially varying phase gradient along its aperture:
\begin{equation}
\frac{d\Phi(x)}{dx} = \xi
\label{eq:phase_grad_simple}
\end{equation}
According to the Generalized Snell's Law of Reflection, the tangential phase discontinuity imparts momentum to the reflected wavefront, steering it into arbitrary, non-specular directions:
\begin{equation}
\sin(\theta_r) - \sin(\theta_i) = \frac{\lambda_0}{2\pi} \frac{d\Phi(x)}{dx}
\label{eq:gen_snell_intro}
\end{equation}

By dynamically synthesizing linear or two-dimensional phase gradients across thousands of unit cells, an RIS can anomalous-reflect a base station's pencil beam around a concrete building corner, focusing electromagnetic energy directly onto an otherwise blocked mobile receiver. Because each unit cell operates passively without power amplifiers or analog-to-digital converters (ADCs), the entire metasurface consumes minimal DC power---typically only milliwatts to bias the tuning elements.

\begin{table}[H]
\centering
\caption{Comparative Architectural Matrix: Traditional Relays vs Phased Arrays vs Hybrid RIS}
\label{tab:relay_vs_ris}
\small
\renewcommand{\arraystretch}{1.05}
\begin{tabular}{|p{3.5cm}|p{2.6cm}|p{2.6cm}|p{2.6cm}|p{2.8cm}|}
\hline
\textbf{Metric / Attribute} & \textbf{Active Small Cell} & \textbf{Active AF Relay} & \textbf{Phased Array} & \textbf{Hybrid RIS (Proposed)} \\
\hline
Operational Mode & Full Active (Tx/Rx) & Active Amplification & Active Transmit & Passive Anomalous Reflection \\
RF Front-End Hardware & Full RF chains, PA, LNA, Mixers, ADC & Full RF front-end, high-gain PAs & Active Phase Shifters, Power Splitters & Passive Unit Cells with PIN/Graphene \\
DC Power Dissipation & Hundreds of Watts & Tens to Hundreds of Watts & $10 - 50\text{ Watts}$ & Milliwatts ($\le 2.5\text{ W}$ for $16\times16$ array) \\
Self-Interference & None (Dedicated Tx) & Severe In-Band Leakage & N/A & Zero (Passive Metasurface) \\
Noise Amplification & None (Regenerated) & High (Amplifies Noise) & Low & Zero Noise Figure ($NF = 0\text{ dB}$) \\
Backhaul Requirement & High-Speed Fiber/E-Band & Wireless Backhaul & Dedicated Baseband & Zero Backhaul (Low-speed control link) \\
Hardware Cost & Very High & High & Moderate to High & Ultra-Low \\
\hline
\end{tabular}
\end{table}

\section{Hybrid PIN--Graphene Integration Strategy}
A decisive factor dictating the practical efficacy of an RIS is the tuning mechanism embedded within its unit cells. Contemporary metasurfaces predominantly employ one of two active technologies:
\begin{enumerate}
  \item \textbf{Discrete Semiconductor Devices (PIN Diodes or Varactors):}
  PIN diodes operate as high-speed digital switches, toggling between low-impedance forward-bias (ON) and high-impedance reverse-bias (OFF) states. While highly reliable and mature, they provide only coarse, discrete phase quantization ($1$-bit or $2$-bit resolution), which introduces phase quantization loss ($0.5\text{ to }3.0\text{ dB}$) into the reflected beam. Varactor diodes allow continuous capacitive tuning, but suffer from high series resistance, elevated insertion loss, and severe nonlinear intermodulation distortion at mmWave frequencies.
  \item \textbf{2D Nanomaterials (Graphene Sheets):}
  Graphene, a single two-dimensional layer of $sp^2$-hybridized carbon atoms, exhibits extraordinary electromagnetic properties. Its surface conductivity $\sigma_g$ can be tuned continuously across a wide dynamic range by modulating its chemical potential (Fermi energy, $\mu_c$) through an electrostatic gate voltage. However, pure graphene metasurfaces often exhibit shallow modulation depths and require high gate voltages to achieve full $360^\circ$ phase agile cycles.
\end{enumerate}

To synthesize the complementary strengths of both approaches while overcoming their individual limitations, this project pioneers a \textbf{hybrid PIN--Graphene integration architecture}. Discrete PIN diodes provide rigid, high-contrast digital baseline switching states, while continuous monolayer graphene strips, integrated across the radiating patch gap, deliver fine, analog continuous phase trimming. This hybrid synergy enables high phase resolution, reduces quantization side-lobes, and optimizes reflection magnitude matching.

\section{Substrate Integrated Waveguide (SIW) Integration for Sensing}
Future 6G wireless communication networks are envisioned to merge communication and radar capabilities into a unified physical framework known as \textbf{Integrated Sensing and Communication (ISAC)}. Beyond passively redirecting communication beams, an intelligent surface deployed on building facades should actively perceive its surrounding electromagnetic and dielectric environment.

To realize this sensing dimension without compromising the radiating metasurface aperture, this design embeds a \textbf{Substrate Integrated Waveguide (SIW)} structure within the multi-layer dielectric substrate. SIW technology synthesizes artificial, non-planar rectangular waveguides within standard printed circuit boards using periodic rows of metallic plated through-vias connecting top and bottom ground planes. The SIW cavity provides:
\begin{itemize}[itemsep=2pt]
  \item \textbf{Complete Lateral Electromagnetic Shielding:} Suppressing substrate surface waves and mutual coupling between adjacent unit cells.
  \item \textbf{Integrated Resonant Sensing Channel:} Serving as an electromagnetic cavity sensor whose resonant frequency shifts predictably when perturbed by ambient dielectric changes (humidity, chemical vapors, or proximity of scattering targets).
  \item \textbf{Isolated DC Biasing Infrastructure:} Facilitating the routing of control traces through central vias without distorting the radiating RF aperture.
\end{itemize}

\section{Identified Research Gap and Specific Project Objectives}
\subsection{Identified Research Gap}
A thorough survey of current mmWave metasurface literature reveals several critical research gaps:
\begin{enumerate}[itemsep=2pt]
  \item \textbf{Binary vs. Continuous Tuning Dichotomy:} Most published RIS designs strictly utilize pure PIN diodes (suffering from severe phase quantization error) or pure varactors (suffering from unacceptable insertion losses at $28-30\text{ GHz}$). Hybridization of PIN diodes with 2D graphene sheets remains largely unexplored at Ka-band frequencies.
  \item \textbf{Lack of Integrated Sensing in Planar Metasurfaces:} Prior RIS research focuses almost exclusively on anomalous reflection beamforming, treating the surface as an unmonitored reflector. The integration of SIW-based cavity sensing within the same unit-cell volume is virtually unaddressed.
  \item \textbf{3D CAD Modeling and Boolean Meshing Artifacts:} Numerical simulation of multi-layer hybrid unit cells in finite-element EM solvers (Ansys HFSS) frequently suffers from non-manifold 3D intersection errors and overlapping geometric slivers, leading to false meshing failures or inaccurate Floquet port de-embedding.
\end{enumerate}

\subsection{Specific Objectives of the Research}
To address these research challenges, the specific objectives of this six-week internship project were formulated as follows:
\begin{enumerate}[itemsep=3pt]
  \item \textbf{Theoretical \& Mathematical Modeling:} Formulate the full electromagnetic governing equations for the hybrid RIS unit cell, including Generalized Snell's Law, the quantum mechanical Kubo formula for graphene conductivity, PIN diode high-frequency lumped RLC circuit models, and SIW cavity dispersion equations.
  \item \textbf{Precision 3D Geometric Parameterization:} Design and implement a robust 4-layer Isola dielectric stack-up in Ansys HFSS ($5\text{ mm} \times 5\text{ mm}$ footprint, $0.49 \lambda_0$ at $29.4\text{ GHz}$), resolving all 3D intersection conflicts using exact boolean subtraction operations.
  \item \textbf{Central Via \& Annular Anti-Pad Ground Clearance Isolation:} Implement an isolated central bias via routed through the 2D mmWave ground plane using a mathematically optimized concentric annular clearance hole ($r = 0.35\text{ mm}$) to prevent RF grounding shorts while preserving the 50~$\Omega$ characteristic impedance.
  \item \textbf{Finite Element HFSS Simulation \& Floquet De-embedding:} Establish Master/Slave periodic boundary conditions and Floquet port excitation with precise phase-reference de-embedding to the top copper patch surface, simulating all four discrete diode switching states ($D_1 \in \{0,1\}$, $D_2 \in \{0,1\}$) across $24\text{ to }36\text{ GHz}$.
  \item \textbf{Extraction \& Quantitative Analysis of Electromagnetic Metrics:} Extract and evaluate reflection coefficient magnitude ($|S_{11}|$), Voltage Standing Wave Ratio (VSWR), reflection phase ($\angle S_{11}$), vector surface current density ($\mathbf{J}_{surf}$), 3D far-field realized gain, and axial ratio (AR).
  \item \textbf{Parametric Sensitivity and Sensing Evaluation:} Execute parametric sweeps of radiating gap dimensions ($g = 0.5\text{ mm}$ vs $g = 0.8\text{ mm}$) and evaluate SIW cavity resonant frequency shifts under variable dielectric loading.
  \item \textbf{Comprehensive Comparative Benchmarking:} Benchmark the proposed hybrid unit-cell performance against state-of-the-art literature and establish practical guidelines for PCB fabrication and experimental VNA validation.
\end{enumerate}

\section{Tools, Technologies, and Computational Environment}
The modeling, numerical simulation, and mathematical post-processing carried out during this research relied on industry-grade engineering software suites:

\begin{table}[H]
\centering
\caption{Software Tools and Computational Environment Utilized in the Internship}
\label{tab:tools_used}
\small
\renewcommand{\arraystretch}{1.05}
\begin{tabular}{|p{4.0cm}|p{3.2cm}|p{6.5cm}|}
\hline
\textbf{Software / Technology} & \textbf{Developer / Provider} & \textbf{Primary Technical Role in Research} \\
\hline
Ansys HFSS (High-Frequency Structure Simulator) & Ansys Inc. & 3D full-wave Finite Element Method (FEM) electromagnetic simulation, adaptive meshing, Floquet port de-embedding, Master/Slave periodic boundaries, and far-field radiation extraction. \\
Python Scientific Stack (NumPy, SciPy, Matplotlib) & Open-Source Community & Analytical modeling of Kubo graphene conductivity, numerical integration, VSWR marker processing, beamsteering array factor synthesis, and publication-quality data visualization. \\
PyAEDT (Ansys Electronics Desktop Python API) & Ansys Inc. & Scripted parametric geometry generation, automated coordinate parameterization, and simulation workflow automation. \\
Keysight ADS (Advanced Design System) & Keysight Technologies & Equivalent lumped-element circuit schematic verification and S-parameter network modeling. \\
LaTeX & TeX Users Group / Tectonic & Typesetting of equations, mathematical matrices, algorithmic pseudocode, and high-precision technical thesis documentation. \\
\hline
\end{tabular}
\end{table}

\section{Organization of the Report}
The remainder of this internship report is organized into the following chapters:
\begin{itemize}[itemsep=2pt]
  \item \textbf{Chapter 2 (Weekly Progress Report):} Details the chronological week-by-week technical progression across the six-week internship tenure at NIT Jalandhar, summarizing weekly milestones, debugging breakthroughs, and research deliverables.
  \item \textbf{Chapter 3 (Electromagnetic Foundations and Mathematical Formulation):} Establishes the rigorous mathematical derivations governing Generalized Snell's Law, the quantum mechanical Kubo formalism for graphene, equivalent RLC semiconductor circuits, SIW guided-wave physics, and planar array theory.
  \item \textbf{Chapter 4 (Geometric Design, Layered Stack-Up, and HFSS Simulation Methodology):} Presents the complete 3D topological architecture, material stack-up coordinates, Boolean subtraction techniques, central via anti-pad isolation, finite-element meshing, and Floquet port configuration.
  \item \textbf{Chapter 5 (Findings, Numerical Simulation Results, and Parametric Analysis):} Comprehensively analyzes simulation results, including $S_{11}$ reflection dips, VSWR matching bands, reflection phase profiles, surface current density maps, 3D far-field directivity, axial ratio polarization purity, gap-width sensitivity, and comparative literature synthesis.
  \item \textbf{Chapter 6 (Practical Implementation, DC Biasing Network Design, and Fabrication Constraints):} Explores multi-layer PCB photolithography tolerances, chemical vapor deposition (CVD) graphene wet transfer procedures, RF choke isolation networks, surface-mount diode assembly, and anechoic chamber measurement methodologies.
  \item \textbf{Chapter 7 (Advanced 6G System Integration: mmWave Beamforming and ISAC):} Investigates cascading wireless channel link budgets, progressive phase beamsteering synthesis, dual-functional radar-communication (DFRC) waveforms, and urban smart radio deployment scenarios.
  \item \textbf{Chapter 8 (Conclusion, Research Learnings, and Future Trajectories):} Concludes the report with a synthesis of technical contributions, acknowledgment of study limitations, personal and professional research competencies acquired, and a strategic roadmap for future multi-cell array fabrication.
  \item \textbf{Appendices \& References:} Provides automated PyAEDT Python modeling scripts, geometric parameter master look-up tables, material property databases, and a comprehensive bibliography of peer-reviewed scientific literature.
\end{itemize}
"""
