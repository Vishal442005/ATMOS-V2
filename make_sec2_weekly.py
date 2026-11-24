# make_sec2_weekly.py

def get_chapter2():
    return r"""
\clearpage
%% ==========================================================================
%%  CHAPTER 2: WEEKLY PROGRESS REPORT
%% ==========================================================================
\chapter{Weekly Progress Report}

\section{Chronological Internship Progression Overview}
\justifying
The six-week research internship at the Department of Electronics and Communication Engineering, National Institute of Technology (NIT) Jalandhar, spanned from \textbf{17 June 2026 to 27 July 2026}. The training was structured systematically into six distinct, progressive phases, transitioning from foundational literature exploration and mathematical modeling to advanced 3D numerical electromagnetic simulations, parametric optimization, and final academic thesis compilation.

\begin{table}[H]
\centering
\caption{Comprehensive Six-Week Research Progression and Milestone Master Table}
\label{tab:six_week_progression}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|c|p{2.2cm}|p{5.5cm}|p{3.8cm}|}
\hline
\textbf{Week} & \textbf{Date Range} & \textbf{Key Technical Activities \& Tasks Conducted} & \textbf{Deliverables \& Milestones} \\
\hline
\textbf{1} & 17 June -- 23 June 2026 & Extensive literature survey on mmWave 5G/6G RIS, Snell's generalized laws, and Ansys HFSS environment setup. & Comprehensive literature matrix, software workstation validation. \\
\textbf{2} & 24 June -- 30 June 2026 & Mathematical formulation of graphene conductivity (Kubo formula) and equivalent circuit modeling of PIN diodes. & Python numerical Kubo script, dielectric stack-up blueprint. \\
\textbf{3} & 01 July -- 07 July 2026 & 3D geometric CAD construction in Ansys HFSS; resolving non-manifold 3D intersection errors using Boolean cuts. & Clean, error-free 3D unit-cell model; annular anti-pad ground cut. \\
\textbf{4} & 08 July -- 14 July 2026 & Setup of Master/Slave periodic boundaries, Floquet port excitations, and reference plane de-embedding. & Validated Floquet port setup, convergence threshold $\Delta S \le 0.02$. \\
\textbf{5} & 15 July -- 21 July 2026 & Execution of Ka-band interpolating frequency sweeps ($24 - 36\text{ GHz}$); extraction of $S_{11}$, VSWR, and phase. & Dual-resonance confirmation ($29.40\text{ GHz} / 30.55\text{ GHz}$), VSWR tables. \\
\textbf{6} & 22 July -- 27 July 2026 & Far-field radiation directivity, 3D axial ratio extraction, gap-width parametric study, and final report drafting. & 3D gain patterns, comparative literature synthesis, thesis draft. \\
\hline
\end{tabular}
\end{table}

The following sections provide an exhaustive, chronological account of the technical investigations, engineering methodologies, mathematical formulations, debugging breakthroughs, and research insights accomplished during each week of the internship.

\section{Week 1: Literature Review, Theoretical Formulation, and Ansys HFSS Environment Configuration}
\subsection{Objectives and Research Context}
The inaugural week focused on establishing a solid theoretical foundation in reconfigurable intelligent surfaces, metasurface physics, and millimeter-wave computational electromagnetics. Under the academic guidance of \textbf{Dr. Kundan Kumar}, primary emphasis was placed on analyzing peer-reviewed scientific publications from IEEE Transactions on Antennas and Propagation (IEEE TAP), IEEE Transactions on Wireless Communications (IEEE TWC), and Nature Electronics.

\subsection{Key Technical Tasks Accomplished}
\begin{itemize}[itemsep=2pt]
  \item \textbf{Survey of Millimeter-Wave Propagation Bottlenecks:} Investigated Friis free-space path loss scaling, atmospheric attenuation characteristics across Ka-band ($26.5-40\text{ GHz}$), and physical blockage modeling in urban 5G/6G deployments.
  \item \textbf{Exploration of Metasurface Phase Gradient Concepts:} Studied Generalized Snell's Laws of Reflection and Refraction as pioneered by Yu et al. (2011), evaluating how phase discontinuities $\Phi(x,y)$ impart anomalous transverse wavevectors to reflected wavefronts.
  \item \textbf{Comparative Assessment of RIS Tuning Mechanisms:} Evaluated trade-offs between semiconductor PIN diodes, varactor diodes, micro-electro-mechanical systems (MEMS), liquid crystals, and 2D nanomaterials (graphene). Identified the hybrid PIN--graphene architecture as an unexplored frontier capable of combining discrete digital switching with analog continuous impedance agility.
  \item \textbf{Workstation Configuration and Licensing:} Configured the high-performance computational workstation in the Microwave \& Antenna Laboratory at NIT Jalandhar, verifying the Ansys Electronics Desktop (AEDT / HFSS 2026) licensing, CUDA GPU acceleration drivers, and Python 3.11 scientific environments.
\end{itemize}

\subsection{Weekly Milestone Achieved}
Compilation of an annotated bibliography comprising 35 seminal papers on RIS architectures, establishing the precise research niche for a dual-resonance PIN--Graphene metasurface operating at $29.4\text{ GHz}$.

\section{Week 2: Electromagnetic Derivations, Kubo Formula Modeling, and Unit-Cell Stack-Up Definition}
\subsection{Objectives and Analytical Formulations}
Week 2 was dedicated to the mathematical and physical formulation of the active materials and the multi-layer printed circuit board dielectric stack-up.

\subsection{Key Technical Tasks Accomplished}
\begin{itemize}[itemsep=2pt]
  \item \textbf{Graphene Surface Conductivity Derivation (Kubo Formula):} Formulated the quantum mechanical Kubo equation, decomposing surface conductivity into intra-band ($\sigma_{intra}$) and inter-band ($\sigma_{inter}$) terms. Proved mathematically that at $29.4\text{ GHz}$ ($\hbar\omega \approx 0.12\text{ meV} \ll \mu_c$), inter-band transitions are strongly suppressed by Pauli blocking, allowing the intra-band term to dominate completely.
  \item \textbf{Python Numerical Kubo Implementation:} Developed a standalone Python script to evaluate $\sigma_{intra}(\omega, \mu_c, \Gamma, T)$ as a function of chemical potential $\mu_c$ ($0.0\text{ to }1.0\text{ eV}$) and relaxation time $\tau$ ($0.1\text{ to }1.0\text{ ps}$). Extracted the corresponding complex surface impedance $Z_s = R_s + j X_s$.
  \item \textbf{PIN Diode Equivalent Circuit Parameterization:} Modeled discrete high-frequency PIN diodes using equivalent lumped RLC networks for both forward-bias ($R_s = 1.5\,\Omega, L_s = 0.05\text{ nH}$) and reverse-bias ($R_p = 10\text{ k}\Omega, C_j = 0.028\text{ pF}$) states.
  \item \textbf{Dielectric Substrate Trade-Off Analysis:} Conducted a comparative trade-off study between high-frequency microwave laminates (Rogers RT/duroid 5880, Taconic TLY-5, and Isola TerraGreen/Astra MT77). Selected a 4-layer Isola substrate ($\epsilon_r = 3.0, \tan\delta = 0.0035$, total dielectric height $h = 0.700\text{ mm}$) due to its excellent dimensional stability and multi-layer manufacturing compatibility.
  \item \textbf{Z-Axis Stack-Up Definition:} Formulated the exact vertical coordinate map from ground sheet ($Z = 2.3399\text{ mm}$) to top copper patch ($Z = 3.03985\text{ to }3.07485\text{ mm}$), establishing the baseline geometric blueprint.
\end{itemize}

\subsection{Weekly Milestone Achieved}
Completed analytical mathematical framework for the hybrid unit cell, verified via Python scripts, and established the dimensional stack-up table.

\section{Week 3: High-Frequency Structure Simulator (HFSS) 3D Geometry Modeling and Boolean Subtraction Operations}
\subsection{Objectives and 3D CAD Modeling Challenges}
The third week marked the transition from mathematical formulations to exact 3D solid geometry construction within the Ansys HFSS computer-aided design (CAD) modeler.

\subsection{Key Technical Tasks Accomplished}
\begin{itemize}[itemsep=2pt]
  \item \textbf{Parametric 3D Solid Construction:} Modeled the $5\text{ mm} \times 5\text{ mm}$ unit-cell geometry, extruding four individual dielectric layers (Layer 1 to Layer 4, each $0.175\text{ mm}$ thick) and defining the top copper radiating patch ($35\,\mu\text{m}$ thick, $Z = 3.03985\text{ to }3.07485\text{ mm}$).
  \item \textbf{Resolution of 3D Intersection and Non-Manifold Errors:} Encountered severe meshing errors when standard drawing tools created microscopic overlapping slivers along the radiating patch gap. Developed a "cookie-cutter" Boolean subtraction methodology using a temporary vacuum box of exact thickness ($0.035\text{ mm}$) to cleanly slice out a flawless $0.5\text{ mm}$ gap without piercing the underlying dielectric.
  \item \textbf{Central Signal Via and Ground Plane Anti-Pad Isolation:} Modeled the central metallic bias via ($r = 0.15\text{ mm}$) extruding from $Z = 2.33985\text{ mm}$ to $Z = 3.07485\text{ mm}$. Solved a critical short-circuit challenge: early iterations subtracted a 3D cylinder through the substrate, creating an undesirable dielectric cavity. Deducing that the via only needed electrical clearance from the ground plane, a 2D circular anti-pad of radius $r = 0.35\text{ mm}$ was subtracted directly from the 2D copper ground sheet at $Z = 2.3399\text{ mm}$, creating a perfect $0.20\text{ mm}$ annular isolation gap.
  \item \textbf{Peripheral SIW Shielding Via Array:} Modeled a row of peripheral metallized vias ($d = 0.6\text{ mm}, p = 1.0\text{ mm}$) along the unit-cell perimeter to synthesize the Substrate Integrated Waveguide lateral boundary.
  \item \textbf{Active Boundary Integration:} Assigned 2D lumped RLC boundary sheets for the PIN diode pair and continuous impedance boundary sheets for the graphene strips across the $0.5\text{ mm}$ copper gap.
\end{itemize}

\subsection{Weekly Milestone Achieved}
A fully parameterized, error-free 3D unit-cell CAD model in Ansys HFSS that passed all geometric validation checks without topological intersection conflicts.

\section{Week 4: Boundary Conditions, Master-Slave Periodic Boundaries, and Floquet Port De-embedding}
\subsection{Objectives and Computational Boundary Assignment}
Week 4 concentrated on establishing the rigorous electromagnetic boundary conditions necessary to simulate an infinite periodic metasurface array using a single unit cell.

\subsection{Key Technical Tasks Accomplished}
\begin{itemize}[itemsep=2pt]
  \item \textbf{Master/Slave Periodic Boundary Formulation:} Applied Master and Slave boundary conditions to the orthogonal lateral faces of the air box. Master~1 and Slave~1 were assigned to the X-Z planes (enforcing periodicity along Y), while Master~2 and Slave~2 were assigned to the Y-Z planes (enforcing periodicity along X). Coordinate axes (u, v vectors) were precisely aligned to guarantee proper phase synchronization.
  \item \textbf{Radiation Air Box Dimensioning:} Dimensioned the master vacuum air box to extend exactly $\lambda_0/4 \approx 2.55\text{ mm}$ above the top copper patch ($+Z$) and $\lambda_0/4$ below the bottom ground sheet ($-Z$), ensuring that reactive near-fields decay before impinging on the absorbing boundaries.
  \item \textbf{Floquet Port Excitation Setup:} Positioned a Floquet port on the top $+Z$ surface of the air box. Configured the port to solve for both orthogonal fundamental polarizations: Transverse Electric ($\text{TE}_{00}$) and Transverse Magnetic ($\text{TM}_{00}$) plane waves.
  \item \textbf{Floquet Reference Plane De-embedding:} Activated phase de-embedding within the Floquet port settings, shifting the phase reference plane exactly $2.55\text{ mm}$ downward to the physical surface of the copper patch ($Z = 3.07485\text{ mm}$). This eliminated phase shifts accumulated during transit through the air box volume.
  \item \textbf{Adaptive Finite Element Mesh Configuration:} Defined adaptive meshing parameters: solution frequency $f_0 = 29.4\text{ GHz}$, maximum number of passes = 20, convergence criterion $\Delta S \le 0.02$, with mixed-order polynomial basis functions.
\end{itemize}

\subsection{Weekly Milestone Achieved}
Full-wave electromagnetic simulation setup fully validated and converging within 8 adaptive passes at $29.4\text{ GHz}$ with $\Delta S = 0.0084 \ll 0.02$.

\section{Week 5: Parameter Sweeps, S-Parameter Extraction, VSWR Analysis, and Phase Response Characterization}
\subsection{Objectives and Numerical Simulation Execution}
With the computational setup verified, Week 5 focused on running extensive interpolating frequency sweeps ($24.0\text{ to }36.0\text{ GHz}$) across all diode switching states and analyzing the resulting S-parameters.

\subsection{Key Technical Tasks Accomplished}
\begin{itemize}[itemsep=2pt]
  \item \textbf{Multi-State Switching Simulation:} Swept the binary states of the diode pair ($D_1 \in \{0,1\}, D_2 \in \{0,1\}$), simulating four distinct operational states: State 00 (both OFF), State 01 ($D_1$ OFF, $D_2$ ON), State 10 ($D_1$ ON, $D_2$ OFF), and State 11 (both ON).
  \item \textbf{Reflection Coefficient ($S_{11}$) Analysis:} Extracted $|S_{11}|$ magnitude in dB across the $24-36\text{ GHz}$ band. Discovered a dual-resonance characteristic with a primary reflection dip of $-21.59\text{ dB}$ at $29.40\text{ GHz}$ (Marker m1) and a secondary dip of $-15.35\text{ dB}$ at $30.55\text{ GHz}$ (Marker m2). Observed that all four diode states closely overlapped, revealing that the resonance magnitude is dominated by the passive SIW patch geometry.
  \item \textbf{VSWR Extraction and Marker Processing:} Plotted Voltage Standing Wave Ratio traces. Extracted Marker Set A and Marker Set B, identifying a wide impedance matching bandwidth ($\text{VSWR} \le 2.0$) from $29.30\text{ GHz}$ to $29.93\text{ GHz}$ centered at $29.80\text{ GHz}$ ($\text{VSWR} = 1.23$).
  \item \textbf{Reflection Phase ($\angle S_{11}$) Extraction:} Extracted de-embedded reflection phase curves, recording a steep phase transition spanning $-140^\circ$ to $-30^\circ$ across the $28.5-30.0\text{ GHz}$ resonance band.
  \item \textbf{Vector Surface Current Density ($\mathbf{J}_{surf}$) Visualization:} Generated 3D vector surface current density overlays on the copper patch at $29.4\text{ GHz}$, observing peak current densities of $275.8\text{ A/m}$ concentrated along the inner edges of the radiating gap.
\end{itemize}

\subsection{Weekly Milestone Achieved}
Complete quantification of reflection magnitude, VSWR matching bandwidth, phase profile, and surface current distributions across the entire Ka-band spectrum.

\section{Week 6: Far-Field Radiation Analysis, Axial Ratio Evaluation, Literature Benchmarking, and Thesis Documentation}
\subsection{Objectives, Synthesis, and Final Thesis Formulation}
The culminating week was dedicated to far-field radiation characterization, parametric sensitivity exploration, comparative literature benchmarking, and drafting the comprehensive technical thesis.

\subsection{Key Technical Tasks Accomplished}
\begin{itemize}[itemsep=2pt]
  \item \textbf{3D Far-Field Directivity and Gain Pattern Analysis:} Extracted 3D far-field radiation patterns at $29.4\text{ GHz}$ from multiple viewing angles. Verified a maximum realized gain of $+1.46\text{ dBi}$ along boresight ($\theta = 0^\circ, \phi = 0^\circ$), confirming directed planar reflection.
  \item \textbf{Axial Ratio (AR) Polarization Purity Evaluation:} Evaluated the axial ratio across the radiation sphere, recording a peak value of $59.88\text{ dB}$ along boresight, proving that the reflected wave maintains strict linear polarization without depolarization distortion.
  \item \textbf{Parametric Sensitivity Study of Radiating Gap Width:} Executed comparative simulations with gap width increased from $g = 0.5\text{ mm}$ to $g = 0.8\text{ mm}$. Demonstrated that increasing gap width decreases gap capacitance, shifting the resonant frequency upward from $29.40\text{ GHz}$ to $30.55\text{ GHz}$ and narrowing the phase transition bandwidth.
  \item \textbf{SIW Cavity Resonant Permittivity Sensing Evaluation:} Evaluated the SIW sensing channel by applying variable dielectric perturbation ($\epsilon_r = 1.0\text{ to }5.0$) on the sensing slot, proving a linear sensitivity slope of $S = 185\text{ MHz/RIU}$.
  \item \textbf{Comparative Literature Benchmarking:} Formulated an extensive comparative matrix benchmarking the proposed hybrid design against 10 published mmWave metasurface designs in IEEE literature.
  \item \textbf{Comprehensive Thesis Compilation:} Authored, formatted, and debugged the complete 80+ page technical internship report in LaTeX in strict adherence to HPTU Hamirpur and JNGEC Sundernagar academic guidelines.
\end{itemize}

\subsection{Weekly Milestone Achieved}
Successful defense preparation, complete generation of 34 publication-grade figures, and submission of the finalized comprehensive internship research report.

\begin{table}[H]
\centering
\caption{Summary of Technical Challenges Encountered and Engineering Solutions Implemented}
\label{tab:challenges_solutions}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|p{4.2cm}|p{4.8cm}|p{4.8cm}|}
\hline
\textbf{Technical Challenge} & \textbf{Root Physical / Computational Cause} & \textbf{Engineering Solution Implemented} \\
\hline
Non-manifold 3D geometry meshing errors in Ansys HFSS. & Overlapping polygon edges and microscopic copper slivers formed during manual gap slicing. & Designed a temporary $0.035\text{ mm}$ vacuum box and used exact Boolean Subtraction ("cookie-cutter" method). \\
\hline
Central signal bias via short-circuiting to mmWave ground plane. & Via penetrated continuous 2D ground sheet at $Z = 2.3399\text{ mm}$ without electrical isolation. & Subtracted a 2D circular clearance anti-pad ($r = 0.35\text{ mm}$) directly from the ground sheet, creating a $0.20\text{ mm}$ annular air gap. \\
\hline
Erroneous reflection phase shifts at Floquet port. & Floquet port reference plane placed at air box boundary, adding air transit phase delays. & Activated Floquet port phase de-embedding, translating the reference plane $2.55\text{ mm}$ directly to copper patch. \\
\hline
Small observed differential phase shift between diode bias states. & Strong geometric LC resonance of patch/gap dominated over the small perturbation of diode states. & Identified radiating gap width ($g$) as the primary tuning lever and recommended optimized diode placement. \\
\hline
\end{tabular}
\end{table}
"""
