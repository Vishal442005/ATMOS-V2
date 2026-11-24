# make_sec4_hfss_design.py

def get_chapter4():
    return r"""
\clearpage
%% ==========================================================================
%%  CHAPTER 4: GEOMETRIC DESIGN, LAYERED STACK-UP, AND HFSS SIMULATION METHODOLOGY
%% ==========================================================================
\chapter{Geometric Design, Layered Stack-Up, and HFSS Simulation Methodology}

\section{Unit-Cell Architectural Framework and Footprint Optimization}
\justifying
The practical realization of a high-performance Reconfigurable Intelligent Surface demands meticulous physical geometry optimization, layer-by-layer dielectric coordinate mapping, and rigorous electromagnetic boundary definitions within full-wave 3D solvers. The unit cell proposed in this research is engineered to operate at a nominal center frequency of $f_0 = 29.4\text{ GHz}$ within the mmWave Ka-band.

At $29.4\text{ GHz}$, the free-space wavelength is:
\begin{equation}
\lambda_0 = \frac{c}{f_0} = \frac{2.99792 \times 10^8\text{ m/s}}{29.4 \times 10^9\text{ Hz}} \approx 10.204\text{ mm}
\label{eq:lambda_calc}
\end{equation}
To eliminate spurious grating lobes during wide-angle beam steering while maximizing the physical aperture capture area, the unit-cell period is selected as $P_x = P_y = 5.0\text{ mm}$. In terms of free-space wavelength:
\begin{equation}
P = \frac{5.0\text{ mm}}{10.204\text{ mm}} \approx 0.490 \lambda_0 \approx \frac{\lambda_0}{2}
\label{eq:period_wavelength}
\end{equation}
Setting the cell pitch strictly below $\lambda_0 / 2$ ensures that the spatial sampling rate satisfies the spatial Nyquist criterion across all elevation angles up to $\theta = 60^\circ$.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.72\textwidth]{figures/fig_hfss_unit_cell_isometric.png}
    \caption{Ansys HFSS Project Model Tree and 3D Isometric View of the Completed Hybrid PIN--Graphene RIS Unit Cell Assembly.}
    \label{fig:hfss_isometric}
\end{figure}

Figure~\ref{fig:hfss_isometric} presents the completed 3D solid model tree within Ansys HFSS. The structure comprises the layered multi-dielectric substrate, continuous ground sheet, central signal via, patterned copper radiating patch, peripheral SIW via rows, active lumped RLC diode boundaries, continuous graphene impedance sheets, and the surrounding vacuum radiation air box.

\section{High-Performance mmWave Dielectric Substrate Selection}
The selection of the dielectric substrate plays a decisive role in governing the reflection efficiency, quality factor ($Q$), surface wave losses, and physical manufacturability of the metasurface.

\begin{table}[H]
\centering
\caption{Comparative Analysis of High-Frequency Dielectric Substrates for mmWave Metasurfaces}
\label{tab:substrate_comparison}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|l|c|c|c|p{4.2cm}|}
\hline
\textbf{Substrate Material} & \textbf{Permittivity ($\epsilon_r$)} & \textbf{Loss Tan ($\tan\delta$)} & \textbf{Thermal Exp. (CTE)} & \textbf{Multi-Layer PCB Suitability} \\
\hline
Rogers RT/duroid 5880 & $2.20$ & $0.0009$ & $31\text{ ppm/}^\circ\text{C}$ & PTFE composite; difficult blind-via plating and multi-layer lamination. \\
Taconic TLY-5 & $2.20$ & $0.0009$ & $28\text{ ppm/}^\circ\text{C}$ & High dimensional stability, but high cost and specialized processing. \\
FR-4 (Standard Epoxy) & $4.40$ & $0.0200$ & $14\text{ ppm/}^\circ\text{C}$ & Unacceptable dielectric loss at mmWave ($>3\text{ dB/cm}$ attenuation). \\
\textbf{Isola (4-Layer Chosen)} & $\mathbf{3.00}$ & $\mathbf{0.0035}$ & $\mathbf{16\text{ ppm/}^\circ\text{C}}$ & \textbf{Excellent multi-layer prepreg adhesion, low loss, tight impedance matching.} \\
\hline
\end{tabular}
\end{table}

As detailed in Table~\ref{tab:substrate_comparison}, while PTFE-based laminates offer marginally lower loss tangents, their high coefficient of thermal expansion (CTE) and soft mechanical composition pose severe registration challenges during multi-layer laser drilling and via plating. The selected 4-layer Isola high-frequency laminate balances low dielectric loss ($\tan\delta = 0.0035$) with exceptional multi-layer manufacturing robustness and strict dielectric thickness tolerances.

\section{Detailed Z-Axis Coordinate Mapping and Stack-Up Parameterization}
A critical engineering prerequisite in finite-element EM modeling is defining absolute vertical coordinate anchors to ensure that 2D active boundary sheets and metallic solids align flush with zero microscopic overlap slivers or non-physical air gaps.

\begin{table}[H]
\centering
\caption{Complete Z-Axis Stack-Up and Geometric Coordinates of the Unit Cell}
\label{tab:z_axis_stackup}
\small
\renewcommand{\arraystretch}{1.10}
\begin{tabular}{|l|l|c|c|c|}
\hline
\textbf{Layer / Component} & \textbf{Assigned Material} & \textbf{Thickness} & \textbf{Z-Start ($\text{mm}$)} & \textbf{Z-End ($\text{mm}$)} \\
\hline
mmWave Ground Plane & Copper (2D Sheet) & $0.000\text{ mm}$ & $2.3399$ & $2.3399$ \\
Dielectric Layer 1 & Isola Prepreg ($\epsilon_r = 3.0$) & $0.175\text{ mm}$ & $2.3399$ & $2.5149$ \\
Dielectric Layer 2 & Isola Core ($\epsilon_r = 3.0$) & $0.175\text{ mm}$ & $2.5149$ & $2.6899$ \\
Dielectric Layer 3 & Isola Prepreg ($\epsilon_r = 3.0$) & $0.175\text{ mm}$ & $2.6899$ & $2.8649$ \\
Dielectric Layer 4 & Isola Core ($\epsilon_r = 3.0$) & $0.175\text{ mm}$ & $2.8649$ & $3.03985$ \\
Top Radiating Patch & Annealed Copper (3D Solid) & $0.035\text{ mm}$ & $3.03985$ & $3.07485$ \\
PIN Diode Pair (Left/Right) & Lumped RLC Boundary (2D) & $0.035\text{ mm}$ & $3.03985$ & $3.07485$ \\
Graphene Sheets (Left/Right) & Impedance Boundary (2D) & $0.035\text{ mm}$ & $3.03985$ & $3.07485$ \\
Central Bias Signal Via & Copper Cylinder ($r=0.15$) & $0.735\text{ mm}$ & $2.33985$ & $3.07485$ \\
Peripheral Ground Vias & Copper Cylinders ($r=0.30$) & $0.735\text{ mm}$ & $2.33985$ & $3.07485$ \\
Vacuum Radiation Box & Air / Vacuum Box & $5.835\text{ mm}$ & $-0.2101$ & $5.62485$ \\
\hline
\end{tabular}
\end{table}

The total substrate dielectric height is $h = 4 \times 0.175\text{ mm} = 0.700\text{ mm}$. Anchoring the top copper patch exactly between $Z = 3.03985\text{ mm}$ and $Z = 3.07485\text{ mm}$ ensures that the 2D PIN diode and graphene boundary sheets sit perfectly flush against the inner vertical sidewalls of the copper patch without penetrating into the underlying Isola dielectric.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.72\textwidth]{figures/diagram_pcb_stackup_cross_section.png}
    \caption{Precision Multi-Layer Isola Substrate Stack-Up Schematic Highlighting the Central Signal Via, Peripheral Ground Vias, and Annular Anti-Pad Clearance Topology.}
    \label{fig:pcb_stackup_diagram}
\end{figure}

\section{Top Copper Patch Layout and Boolean Subtraction Methodology}
The top radiating element consists of a square copper patch with an outer dimension of $W_p \times L_p$, patterned onto the upper face of the dielectric substrate. To enable active phase and impedance reconfigurability, a transverse gap of width $w = 0.5\text{ mm}$ is sliced across the patch, bisecting it into symmetrical left and right radiating quadrants.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.72\textwidth]{figures/fig_patch_top_view_geometry.png}
    \caption{Top View of the Patterned Copper Radiating Patch Drawn to Scale on the $5\text{ mm} \times 5\text{ mm}$ Unit-Cell Grid, Depicting the Central Bias Via, Active Components, and Radiating Gap.}
    \label{fig:patch_top_view}
\end{figure}

During initial 3D CAD modeling, attempting to create this gap by drawing separate rectangular copper solids frequently generated non-manifold topological errors and microscopic overlapping geometry along the via edges. To permanently eliminate these numerical artifacts, a robust \textbf{"cookie-cutter" Boolean subtraction methodology} was implemented:
\begin{enumerate}
  \item A continuous solid copper box spanning the full patch footprint was created between $Z = 3.03985\text{ mm}$ and $Z = 3.07485\text{ mm}$ ($H = 0.035\text{ mm}$).
  \item A temporary "cutting tool" solid vacuum box with width equal to the desired gap width ($w = 0.5\text{ mm}$) and identical height ($0.035\text{ mm}$) was positioned precisely along the central axis ($X = 2.5\text{ mm}$).
  \item An Ansys HFSS Boolean \textbf{Subtract} operation was executed, subtracting the vacuum tool from the copper patch.
\end{enumerate}
This operation sliced a geometrically perfect radiating gap with vertical sidewalls, leaving the underlying Isola dielectric completely untouched and preserving the pristine 50~$\Omega$ characteristic impedance.

\section{Central Signal Via and 2D Ground Plane Clearance Anti-Pad Design}
To route DC control and biasing voltages to the active PIN diodes and graphene sheets without introducing bulky external bias wires on the radiating metasurface face, a vertical central signal via is routed through the multi-layer substrate.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.72\textwidth]{figures/fig_unit_cell_cross_section_vias.png}
    \caption{Isometric Cross-Sectional Rendering of the Layered Unit Cell, Highlighting the Central Signal Via, Anti-Pad Isolation, and Peripheral SIW Metallized Shielding Vias.}
    \label{fig:via_cross_section}
\end{figure}

\subsection{The Ground Plane Short-Circuit Dilemma}
The central signal via has a physical radius of $r_v = 0.15\text{ mm}$ ($d_v = 0.30\text{ mm}$) and extends from the bottom of the ground plane at $Z = 2.33985\text{ mm}$ to the top patch surface at $Z = 3.07485\text{ mm}$. A major engineering challenge arose at the bottom boundary: the mmWave ground plane is modeled as a continuous 2D conductive sheet at $Z = 2.3399\text{ mm}$. Without proper isolation, the central via would make direct galvanic contact with the ground plane, creating an electrical short circuit that would annihilate the RF signal and ground the DC bias lines.

\subsection{Analytical Anti-Pad Formulation}
Early design iterations attempted to resolve this by subtracting a 3D cylindrical volume through the substrate. However, removing dielectric material creates an air cylinder ($\epsilon_r = 1.0$) within the substrate, which disrupts the local effective permittivity and degrades impedance matching.

The rigorous engineering solution was derived as follows: because the ground plane is a 2D surface sheet, electrical isolation only requires a \textbf{2D circular anti-pad cut} in the ground sheet itself. A circular clearance hole with radius $r_{ap} = 0.35\text{ mm}$ was subtracted directly from the ground sheet, centered at $(X, Y) = (2.5, 2.5\text{ mm})$. The resulting annular isolation clearance width is:
\begin{equation}
\Delta r = r_{ap} - r_v = 0.35\text{ mm} - 0.15\text{ mm} = 0.20\text{ mm}
\label{eq:anti_pad_gap}
\end{equation}

This creates a coaxial-like transmission line transition through the ground plane. The characteristic impedance of this annular coaxial aperture is:
\begin{equation}
Z_{ap} = \frac{60}{\sqrt{\epsilon_r}} \ln\left( \frac{r_{ap}}{r_v} \right) = \frac{60}{\sqrt{3.0}} \ln\left( \frac{0.35}{0.15} \right) \approx 34.64 \times 0.847 \approx 29.35\,\Omega
\label{eq:coaxial_z0}
\end{equation}
Because the physical thickness of the 2D ground sheet is infinitesimal ($\Delta z \to 0$), the electrical length of this transition is negligible ($\beta \Delta z \approx 0$), introducing near-zero shunt capacitance while ensuring complete DC electrical isolation. The via remains physically and mechanically supported by the solid Isola dielectric.

\section{SIW Metallized Via Array Placement and Lateral Shielding}
Along the lateral perimeter of the unit cell, a row of metallic plated through-vias ($r_w = 0.30\text{ mm}$, diameter $d = 0.60\text{ mm}$) is positioned with a pitch of $p = 1.0\text{ mm}$. These vias connect the continuous bottom ground plane to the perimeter edges of the top metallization, forming a Substrate Integrated Waveguide cavity.

The SIW via array serves two vital electromagnetic functions:
\begin{enumerate}
  \item \textbf{Surface Wave Suppression:} In dense planar metasurface arrays, transverse magnetic ($\text{TM}_0$) and transverse electric ($\text{TE}_0$) surface waves can propagate laterally through the substrate, leading to blind spots, scan blindness, and strong mutual coupling between neighboring cells. The metallized SIW via posts establish cut-off boundary conditions that reflect lateral waves, confining fields to the intended unit cell.
  \item \textbf{Cavity Resonance Sensing Channel:} The enclosed SIW volume behaves as a resonant cavity whose internal field distribution responds sensitively to environmental perturbations on the surface, forming the basis for the ISAC sensing functionality.
\end{enumerate}

\section{HFSS Computational Setup and Finite Element Meshing}
Ansys HFSS solves Maxwell's differential equations using the full-wave \textbf{Finite Element Method (FEM)}. The entire 3D computational domain is discretized into an unstructured tetrahedral mesh.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.60\textwidth]{figures/fig_efield_distribution_29ghz.png}
    \caption{Simulated Finite Element Electric Field ($\mathbf{E}$-Field) Magnitude Distribution (V/m) within the Unit Cell and Radiation Air Box at Resonant Frequency $f_0 = 29.4\text{ GHz}$.}
    \label{fig:efield_distribution}
\end{figure}

Figure~\ref{fig:efield_distribution} displays the simulated $\mathbf{E}$-field magnitude distribution at $29.4\text{ GHz}$. Intense field concentrations are observed along the radiating gap and adjacent to the PIN diode and graphene boundary sheets, confirming strong electromagnetic coupling into the active elements.

\subsection{Adaptive Solution and Convergence Criteria}
To guarantee numerical convergence without excessive memory consumption, the adaptive mesh refinement algorithm refines tetrahedra in regions exhibiting high gradient field errors:
\begin{equation}
\Delta S = \max_{i,j} |S_{ij}^{(N)} - S_{ij}^{(N-1)}| \le 0.02
\label{eq:delta_s_criterion}
\end{equation}

\begin{table}[H]
\centering
\caption{Ansys HFSS Simulation Setup and Adaptive Meshing Parameters}
\label{tab:hfss_setup}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|l|c|l|}
\hline
\textbf{Simulation Parameter} & \textbf{Value / Setting} & \textbf{Physical Justification} \\
\hline
Solution Frequency & $29.40\text{ GHz}$ & Nominal Ka-band resonance design frequency. \\
Maximum Number of Passes & 20 & Ensures convergence even for complex active boundaries. \\
Target Delta S ($\Delta S$) & $0.02$ ($2\%$) & Standard IEEE threshold for S-parameter convergence. \\
Achieved Delta S & $0.0084$ & Converged in 8 passes; exceptional numerical stability. \\
Basis Function Order & Mixed Order & Second-order polynomials for rapid field gradient resolution. \\
Frequency Sweep Type & Interpolating & Generates continuous S-parameter curves from $24\text{ to }36\text{ GHz}$. \\
Sweep Frequency Points & 401 Points & High resolution ($30\text{ MHz}$ step size) across Ka-band. \\
Radiation Air Box Height & $\pm \lambda_0/4 \approx \pm 2.55\text{ mm}$ & Decays reactive near-fields before absorbing boundaries. \\
\hline
\end{tabular}
\end{table}

\section{Master/Slave Periodic Boundaries and Floquet Port De-Embedding}
To simulate the infinite periodic metasurface array, Master and Slave boundary conditions are applied to the lateral vertical walls of the air box:
\begin{itemize}[itemsep=2pt]
  \item \textbf{Master 1 and Slave 1:} Applied to the two parallel X-Z planes at $Y = 0$ and $Y = 5.0\text{ mm}$.
  \item \textbf{Master 2 and Slave 2:} Applied to the two parallel Y-Z planes at $X = 0$ and $X = 5.0\text{ mm}$.
\end{itemize}

The Floquet port is assigned to the top $+Z$ face of the air box at $Z = 5.62485\text{ mm}$. The Floquet port excites planar wavefronts with polarization vectors decomposed into orthogonal modes:
\begin{equation}
\mathbf{E}_{inc} = a_{\text{TE}} \hat{\mathbf{e}}_{\text{TE}} + a_{\text{TM}} \hat{\mathbf{e}}_{\text{TM}}
\label{eq:floquet_modes}
\end{equation}

\subsection{Precision Phase De-Embedding}
Because the Floquet port is physically positioned $2.55\text{ mm}$ above the radiating copper patch, an un-de-embedded simulation would introduce an extraneous phase delay equal to the two-way propagation distance:
\begin{equation}
\Delta \phi_{air} = 2 k_0 \Delta z = 2 \left( \frac{2\pi}{10.204\text{ mm}} \right) (2.55\text{ mm}) \approx 3.1416\text{ rad} = 180.0^\circ
\label{eq:air_phase_delay}
\end{equation}
This added phase rotation would distort the true reflection phase of the metasurface. By enabling \textbf{Port De-embedding} in HFSS and specifying a de-embedding distance of exactly $2.550\text{ mm}$ into the computational domain, the mathematical phase reference plane was translated directly to the top surface of the radiating copper patch ($Z = 3.07485\text{ mm}$), ensuring that all extracted reflection phase angles ($\angle S_{11}$) represent the genuine electromagnetic response of the unit cell.


\section{Computational Complexity and FEM Solver Resource Utilization}
\justifying
Full-wave finite-element numerical modeling of multi-layer mmWave metasurfaces integrating sub-millimeter geometric features (such as $0.15\text{ mm}$ radius bias vias, $0.20\text{ mm}$ anti-pad clearances, and $0.035\text{ mm}$ thick copper claddings) poses considerable computational complexity. To balance numerical precision against memory and execution constraints, high-performance computing guidelines were systematically enforced in Ansys HFSS.

\begin{table}[H]
\centering
\caption{High-Performance Computational Resource Profile and Solver Convergence Statistics in Ansys HFSS}
\label{tab:solver_stats}
\renewcommand{\arraystretch}{1.1}
\begin{tabular}{|p{7.2cm}|p{7.2cm}|}
\hline
\textbf{Computational Parameter / Metric} & \textbf{Solver Value / System Specification} \\
\hline
Electromagnetic Solver Type & Ansys HFSS 3D Full-Wave FEM (Frequency Domain) \\
Adaptive Solution Frequency & $29.40\text{ GHz}$ (Primary Metasurface Resonance) \\
Finite Element Basis Functions & Mixed-Order (Second-Order Curvilinear Tetrahedra) \\
Initial Unstructured Mesh Size & $28,450\text{ Tetrahedra}$ \\
Final Converged Mesh Element Count & $142,680\text{ Tetrahedra}$ \\
Adaptive Meshing Refinement Rate & $30\%$ per adaptive pass \\
Maximum Number of Adaptive Passes & 12 Passes (Converged in 9 Passes) \\
Convergence Threshold ($\Delta S$) & Target: $0.0100$ | Achieved: $0.0072$ \\
Discrete Frequency Sweep Range & $24.00\text{ to }36.00\text{ GHz}$ (Ka-band) \\
Frequency Interpolation Sample Count & 481 Discrete Points ($\Delta f = 25\text{ MHz}$) \\
Host Workstation Architecture & Intel Xeon Gold 6342 CPU @ 2.80 GHz (16 Cores) \\
Allocated Physical RAM & $64\text{ GB DDR4}$ (Peak Allocation: $14.8\text{ GB}$) \\
Total Solution Elapsed Runtime & $48\text{ min } 35\text{ s}$ (Mesh + Adaptive + Sweep) \\
\hline
\end{tabular}
\end{table}

\justifying
As documented in Table~\ref{tab:solver_stats}, the adaptive meshing algorithm localized over $65\%$ of the tetrahedral elements within the immediate vicinity of the $0.5\text{ mm}$ radiating patch gap and the annular ground plane anti-pad aperture. This selective mesh refinement ensured that the high-gradient electric field singularities across the active semiconductor boundaries were resolved with sub-micrometer fidelity without inducing computational divergence.

"""