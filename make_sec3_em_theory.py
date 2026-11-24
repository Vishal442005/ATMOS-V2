# make_sec3_em_theory.py

def get_chapter3():
    return r"""
\clearpage
%% ==========================================================================
%%  CHAPTER 3: ELECTROMAGNETIC FOUNDATIONS AND MATHEMATICAL FORMULATION
%% ==========================================================================
\chapter{Electromagnetic Foundations and Mathematical Formulation}

\section{Generalized Snell's Law and Anomalous Wavefront Manipulation}
\justifying
Classical electromagnetic wave reflection and refraction at a planar interface separating two semi-infinite, homogeneous media are governed by Fermat's principle of stationary phase. Under conventional conditions, the boundary introduces no tangential phase discontinuity across the interface, enforcing the conservation of tangential wavevectors. Consequently, the angle of reflection strictly equals the angle of incidence ($\theta_r = \theta_i$), and refraction obeys standard Snell's Law ($n_t \sin\theta_t = n_i \sin\theta_i$).

In metasurfaces, however, sub-wavelength resonators introduce an abrupt, spatially dependent phase shift $\Phi(\mathbf{r})$ along the boundary. Consider two parallel light trajectories originating from a planar wavefront impinging at an angle $\theta_i$ on an interface endowed with a continuous, one-dimensional tangential phase gradient $d\Phi/dx$, as depicted in Figure~\ref{fig:snell_anomalous}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.68\textwidth]{figures/plot_generalized_snells_law.png}
    \caption{Generalized Snell's Law: Anomalous Reflection Angle $\theta_r$ as a Function of Tangential Phase Gradient $d\Phi/dx$ for Varying Incidence Angles ($\theta_i = 0^\circ, 15^\circ, 30^\circ, 45^\circ$) at $29.4\text{ GHz}$.}
    \label{fig:snell_anomalous}
\end{figure}

The total phase difference accumulated between two rays traversing paths separated by an infinitesimal transverse distance $dx$ along the surface is expressed as:
\begin{equation}
d\phi_{total} = \left[ k_0 \sin(\theta_i) dx \right] + d\Phi(x) - \left[ k_0 \sin(\theta_r) dx \right]
\label{eq:fermat_diff}
\end{equation}
where $k_0 = 2\pi / \lambda_0 = \omega / c$ is the free-space wavenumber. According to Fermat's generalized principle, the actual physical path traversed by the reflected wave must render the total phase stationary with respect to variations along the coordinate $x$, requiring:
\begin{equation}
\frac{d\phi_{total}}{dx} = 0 \implies k_0 \sin(\theta_i) + \frac{d\Phi(x)}{dx} - k_0 \sin(\theta_r) = 0
\label{eq:fermat_stationary}
\end{equation}
Rearranging terms yields the fundamental \textbf{Generalized Snell's Law of Reflection}:
\begin{equation}
\sin(\theta_r) - \sin(\theta_i) = \frac{1}{k_0} \frac{d\Phi(x)}{dx} = \frac{\lambda_0}{2\pi} \frac{d\Phi(x)}{dx}
\label{eq:gen_snells_law_full}
\end{equation}

Similarly, for electromagnetic transmission (refraction) into a second medium with refractive index $n_t$, Generalized Snell's Law is formulated as:
\begin{equation}
n_t \sin(\theta_t) - n_i \sin(\theta_i) = \frac{\lambda_0}{2\pi} \frac{d\Phi(x)}{dx}
\label{eq:gen_snells_refract}
\end{equation}

\subsection{Critical Angle and Surface Wave Conversion}
Equation~(\ref{eq:gen_snells_law_full}) reveals that by engineering the spatial phase gradient $d\Phi/dx$, the reflection angle $\theta_r$ can be steered into arbitrary directions, including negative angles of reflection ($\theta_r < 0$). However, because the sine function is bounded within $[-1, 1]$, an anomalous reflected propagating wave can only exist when:
\begin{equation}
\left| \sin(\theta_i) + \frac{\lambda_0}{2\pi} \frac{d\Phi(x)}{dx} \right| \le 1
\label{eq:propagation_condition}
\end{equation}

When the phase gradient exceeds this threshold, namely:
\begin{equation}
\left| \frac{d\Phi(x)}{dx} \right| > k_0 (1 - \sin\theta_i)
\label{eq:critical_gradient}
\end{equation}
the reflected wavevector along the interface exceeds the free-space wavenumber ($k_x > k_0$). Consequently, the normal wavevector component becomes purely imaginary:
\begin{equation}
k_z = \sqrt{k_0^2 - k_x^2} = -j \sqrt{k_x^2 - k_0^2} = -j \alpha_z
\label{eq:evanescent_wave}
\end{equation}
In this regime, the reflected electromagnetic wave cannot propagate into the far-field; instead, it is bound to the metasurface as an evanescent surface wave (Spoof Surface Plasmon Polariton, SSPP). For the design operating at $f_0 = 29.4\text{ GHz}$, $\lambda_0 = 10.204\text{ mm}$, yielding $k_0 \approx 615.75\text{ rad/m}$. To prevent surface wave trapping and maintain efficient far-field reflection, the spatial phase gradient must satisfy $|d\Phi/dx| \le 615.75\text{ rad/m} \approx 35.28^\circ/\text{mm}$.

\section{Graphene Electronic Physics and Quantum Mechanics}
\subsection{Crystal Honeycomb Lattice and Band Structure}
Graphene is a two-dimensional allotrope of carbon consisting of a single atomic layer arranged in a hexagonal honeycomb crystal lattice. Carbon atoms possess an atomic number of 6 with an electronic ground-state configuration of $1s^2 2s^2 2p^2$. In graphene, the $2s$, $2p_x$, and $2p_y$ atomic orbitals undergo planar $sp^2$ hybridization, forming three strong in-plane covalent $\sigma$-bonds with neighboring carbon atoms separated by an interatomic distance $a_0 = 1.42\text{ \AA} = 0.142\text{ nm}$. These robust $\sigma$-bonds impart exceptional mechanical tensile strength ($130\text{ GPa}$) and high thermal conductivity ($5000\text{ W/m}\cdot\text{K}$).

\begin{figure}[H]
    \centering
    \includegraphics[width=0.68\textwidth]{figures/diagram_graphene_lattice_dirac_cone.png}
    \caption{Graphene Quantum Electronic Architecture: (Left) Real-Space Honeycomb Crystal Lattice with $sp^2$ Hybridization ($a_0 = 1.42\text{ \AA}$); (Right) 3D Conical Energy Dispersion $E(\mathbf{k}) = \pm\hbar v_F |\mathbf{k}|$ Demonstrating Zero-Bandgap Degeneracy at the Dirac Points ($K$ and $K'$).}
    \label{fig:graphene_dirac_cones}
\end{figure}

The remaining unhybridized $2p_z$ orbital oriented perpendicular to the lattice plane overlaps with adjacent $2p_z$ orbitals, forming a delocalized out-of-plane $\pi$-electron network. The honeycomb lattice is composed of two interpenetrating triangular Bravais sub-lattices, denoted $A$ and $B$. The real-space primitive basis vectors are given by:
\begin{equation}
\mathbf{a}_1 = \frac{a}{2} \left( 3\hat{\mathbf{x}} + \sqrt{3}\hat{\mathbf{y}} \right), \quad \mathbf{a}_2 = \frac{a}{2} \left( 3\hat{\mathbf{x}} - \sqrt{3}\hat{\mathbf{y}} \right)
\label{eq:basis_vectors}
\end{equation}
where $a = \sqrt{3} a_0 \approx 2.46\text{ \AA}$ is the lattice constant.

The reciprocal lattice is likewise hexagonal, defined by primitive vectors:
\begin{equation}
\mathbf{b}_1 = \frac{2\pi}{3a} \left( \hat{\mathbf{x}} + \sqrt{3}\hat{\mathbf{y}} \right), \quad \mathbf{b}_2 = \frac{2\pi}{3a} \left( \hat{\mathbf{x}} - \sqrt{3}\hat{\mathbf{y}} \right)
\label{eq:reciprocal_vectors}
\end{equation}
Of paramount physical importance are the six corners of the first Brillouin zone, which group into two inequivalent sets of high-symmetry points, termed the \textbf{Dirac points} ($K$ and $K'$):
\begin{equation}
\mathbf{K} = \left( \frac{2\pi}{3a}, \frac{2\pi}{3\sqrt{3}a} \right), \quad \mathbf{K}' = \left( \frac{2\pi}{3a}, -\frac{2\pi}{3\sqrt{3}a} \right)
\label{eq:dirac_points}
\end{equation}

Applying the tight-binding Hamiltonian considering nearest-neighbor hopping energy $\gamma_0 \approx 2.8\text{ eV}$, the electronic energy dispersion relation is derived as:
\begin{equation}
E(\mathbf{k}) = \pm \gamma_0 \sqrt{1 + 4\cos\left( \frac{3 k_x a_0}{2} \right)\cos\left( \frac{\sqrt{3} k_y a_0}{2} \right) + 4\cos^2\left( \frac{\sqrt{3} k_y a_0}{2} \right)}
\label{eq:tight_binding_dispersion}
\end{equation}
Expanding Equation~(\ref{eq:tight_binding_dispersion}) via Taylor series in the vicinity of the Dirac points ($\mathbf{q} = \mathbf{k} - \mathbf{K}$ with $|\mathbf{q}| a_0 \ll 1$), the energy dispersion becomes strictly linear:
\begin{equation}
E(\mathbf{q}) = \pm \hbar v_F |\mathbf{q}| = \pm \hbar v_F \sqrt{q_x^2 + q_y^2}
\label{eq:linear_dirac_dispersion}
\end{equation}
where $\hbar = h / (2\pi) \approx 1.05457 \times 10^{-34}\text{ J}\cdot\text{s}$ is the reduced Planck constant, and $v_F$ is the electronic Fermi velocity:
\begin{equation}
v_F = \frac{3 \gamma_0 a_0}{2 \hbar} \approx 1.0 \times 10^6\text{ m/s} \approx \frac{c}{300}
\label{eq:fermi_velocity}
\end{equation}

Because the energy dispersion is strictly linear rather than quadratic ($E \propto q$ instead of $E \propto q^2/2m^*$), charge carriers in graphene behave as massless relativistic Dirac fermions governed by the 2D Dirac-Weyl equation rather than the non-relativistic Schrödinger equation. At thermal equilibrium without external bias, the Fermi energy level $E_F$ intersects exactly at the conical Dirac apex (the charge neutrality point), where the conduction and valence bands touch with zero bandgap.

\begin{table}[H]
\centering
\caption{Fundamental Physical and Quantum Constants for Graphene Modeling}
\label{tab:graphene_constants}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|l|c|c|l|}
\hline
\textbf{Physical Constant} & \textbf{Symbol} & \textbf{Numerical Value} & \textbf{SI Units} \\
\hline
Elementary Electronic Charge & $e$ & $1.602176634 \times 10^{-19}$ & $\text{Coulombs (C)}$ \\
Reduced Planck's Constant & $\hbar$ & $1.054571817 \times 10^{-34}$ & $\text{Joule-seconds (J}\cdot\text{s)}$ \\
Boltzmann Constant & $k_B$ & $1.380649 \times 10^{-23}$ & $\text{Joules/Kelvin (J/K)}$ \\
Speed of Light in Vacuum & $c$ & $2.99792458 \times 10^8$ & $\text{Meters/second (m/s)}$ \\
Graphene Fermi Velocity & $v_F$ & $1.0 \times 10^6$ & $\text{Meters/second (m/s)}$ \\
Carbon-Carbon Interatomic Spacing & $a_0$ & $1.42 \times 10^{-10}$ & $\text{Meters (m)}$ \\
Graphene Sheet Thickness (Mono) & $\Delta z$ & $0.34 \times 10^{-9}$ & $\text{Meters (m)}$ \\
\hline
\end{tabular}
\end{table}

\section{Tunable Surface Conductivity via the Kubo Formalism}
The macroscopic interaction of graphene with high-frequency electromagnetic radiation is fully characterized by its complex surface conductivity, $\sigma_g(\omega, \mu_c, \Gamma, T)$. Using the quantum mechanical Kubo formalism derived from linear response theory, $\sigma_g$ is decomposed into two distinct physical contributions:
\begin{equation}
\sigma_g = \sigma_{intra}(\omega, \mu_c, \Gamma, T) + \sigma_{inter}(\omega, \mu_c, \Gamma, T)
\label{eq:kubo_decomp}
\end{equation}
where $\omega = 2\pi f$ is the angular operating frequency, $\mu_c$ is the chemical potential (Fermi level $E_F$), $\Gamma = 1 / (2\tau)$ is the phenomenological scattering rate ($\tau$ being carrier momentum relaxation time), and $T$ is absolute ambient temperature ($300\text{ K}$).

\subsection{Intra-Band Surface Conductivity ($\sigma_{intra}$)}
The intra-band contribution arises from intraband electron-hole scattering within the same electronic band (Drude-like intraband free-carrier motion). Applying the random-phase approximation (RPA) at finite temperatures, $\sigma_{intra}$ is analytically expressed as:
\begin{equation}
\sigma_{intra}(\omega, \mu_c, \Gamma, T) = -j \frac{e^2 k_B T}{\pi \hbar^2 (\omega - j 2\Gamma)} \left[ \frac{\mu_c}{k_B T} + 2 \ln\left( \exp\left(-\frac{\mu_c}{k_B T}\right) + 1 \right) \right]
\label{eq:sigma_intra_full}
\end{equation}
When the chemical potential is substantially higher than the thermal energy ($\mu_c \gg k_B T$, where $k_B T \approx 25.86\text{ meV}$ at $T = 300\text{ K}$), the logarithmic thermal term converges to $\mu_c / k_B T$, simplifying Equation~(\ref{eq:sigma_intra_full}) to the classic Drude dispersion form:
\begin{equation}
\sigma_{intra}(\omega, \mu_c, \Gamma) \approx \frac{e^2 \mu_c}{\pi \hbar^2} \frac{-j}{\omega - j 2\Gamma} = \frac{e^2 \mu_c}{\pi \hbar^2} \frac{\tau}{1 + j \omega \tau}
\label{eq:drude_simplified}
\end{equation}

\subsection{Inter-Band Surface Conductivity ($\sigma_{inter}$)}
The inter-band contribution accounts for quantum mechanical transitions of electrons absorbing an incident photon of energy $\hbar\omega$ and jumping across the Dirac point from the occupied valence band to the unoccupied conduction band:
\begin{equation}
\sigma_{inter}(\omega, \mu_c, \Gamma, T) = \frac{e^2}{4\hbar} \left[ \frac{1}{2} + \frac{1}{\pi} \arctan\left( \frac{\hbar\omega - 2\mu_c}{2 k_B T} \right) - \frac{j}{2\pi} \ln\left( \frac{(\hbar\omega + 2\mu_c)^2}{(\hbar\omega - 2\mu_c)^2 + (2 k_B T)^2} \right) \right]
\label{eq:sigma_inter_full}
\end{equation}

\subsection{Pauli Blocking and mmWave Simplification}
At the targeted mmWave operating frequency of $f = 29.4\text{ GHz}$, the photon energy is calculated as:
\begin{equation}
\hbar\omega = (1.05457 \times 10^{-34}\text{ J}\cdot\text{s})(2\pi \times 29.4 \times 10^9\text{ rad/s}) \approx 1.948 \times 10^{-23}\text{ J} \approx 0.1216\text{ meV}
\label{eq:photon_energy}
\end{equation}
Under typical electrostatic gating conditions, the chemical potential $\mu_c$ ranges between $0.1\text{ eV}$ and $1.0\text{ eV}$ ($100\text{ to }1000\text{ meV}$). Comparing photon energy with chemical potential:
\begin{equation}
\hbar\omega \approx 0.1216\text{ meV} \ll 2\mu_c \ge 200\text{ meV}
\label{eq:pauli_blocking_condition}
\end{equation}

Because photon energy is several orders of magnitude smaller than $2\mu_c$, optical absorption transitions are completely forbidden by \textbf{Pauli blocking} (the available conduction band states at energy $E = \hbar\omega$ are already fully occupied by degenerate Dirac electrons). Consequently, the inter-band conductivity term $\sigma_{inter} \approx 0$, and the surface conductivity at $29.4\text{ GHz}$ is governed entirely by the intra-band Drude conductivity $\sigma_{intra}$:
\begin{equation}
\sigma_g \approx \sigma_{intra} = \frac{e^2 \mu_c \tau}{\pi \hbar^2 (1 + \omega^2 \tau^2)} - j \frac{e^2 \mu_c \omega \tau^2}{\pi \hbar^2 (1 + \omega^2 \tau^2)}
\label{eq:sigma_g_real_imag}
\end{equation}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.68\textwidth]{figures/plot_graphene_kubo_conductivity.png}
    \caption{Graphene Complex Surface Conductivity ($\text{Re}\{\sigma_g\}$ and $\text{Im}\{\sigma_g\}$ in milli-Siemens) as a Function of Chemical Potential $\mu_c$ at $29.4\text{ GHz}$ for Variable Relaxation Times ($\tau = 0.1, 0.5, 1.0\text{ ps}$).}
    \label{fig:kubo_conductivity}
\end{figure}

Figure~\ref{fig:kubo_conductivity} plots the resulting surface conductivity as a function of $\mu_c$. Crucially, both the real and imaginary parts of $\sigma_g$ increase monotonically and linearly with $\mu_c$. By modulating an external DC bias voltage $V_g$, the carrier concentration $n_s$ is tuned via electrostatic field effect:
\begin{equation}
\mu_c = \hbar v_F \sqrt{\pi n_s} = \hbar v_F \sqrt{\frac{\pi \epsilon_0 \epsilon_{sub} V_g}{e d_{gate}}}
\label{eq:chemical_potential_voltage}
\end{equation}
where $\epsilon_{sub}$ and $d_{gate}$ are the relative permittivity and thickness of the gate dielectric. Thus, varying $V_g$ dynamically modulates the sheet impedance bridging the radiating patch gap.

\section{Surface Impedance Boundary Formulation}
In computational electromagnetic solvers such as Ansys HFSS, representing a 2D atomically thin graphene monolayer ($\Delta z = 0.34\text{ nm}$) as a 3D volumetric solid is computationally intractable because finite element meshing would require sub-nanometer tetrahedral aspect ratios, inducing severe matrix ill-conditioning. Instead, graphene is modeled as an infinitesimal 2D complex \textbf{surface impedance boundary condition}:
\begin{equation}
Z_s = \frac{1}{\sigma_g} = R_s + j X_s
\label{eq:surface_impedance}
\end{equation}

Substituting Equation~(\ref{eq:sigma_g_real_imag}) into Equation~(\ref{eq:surface_impedance}), the surface resistance $R_s$ and surface reactance $X_s$ are derived as:
\begin{equation}
R_s = \text{Re}\{Z_s\} = \frac{\pi \hbar^2}{e^2 \mu_c \tau}, \quad X_s = \text{Im}\{Z_s\} = \frac{\pi \hbar^2 \omega}{e^2 \mu_c}
\label{eq:rs_xs_explicit}
\end{equation}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.68\textwidth]{figures/plot_graphene_impedance_vs_freq.png}
    \caption{Graphene Surface Resistance $R_s$ ($\Omega/\text{sq}$) and Inductive Surface Reactance $X_s$ ($\Omega/\text{sq}$) Across the mmWave Spectrum ($15 - 45\text{ GHz}$) for Chemical Potentials $\mu_c = 0.1, 0.5, 0.9\text{ eV}$.}
    \label{fig:graphene_impedance_freq}
\end{figure}

As demonstrated in Figure~\ref{fig:graphene_impedance_freq}, $R_s$ is frequency-independent across the mmWave spectrum, dictated solely by $\mu_c$ and $\tau$, while $X_s$ is strictly positive and linear with $\omega$. This proves that in the mmWave regime, graphene behaves as an \textbf{inductively reactive sheet} whose inductive impedance can be modulated dynamically by gating voltage, providing an ideal mechanism for continuous phase trimming.

\section{High-Frequency Semiconductor Modeling of the PIN Diode}
While graphene provides analog tuning, discrete high-frequency semiconductor PIN diodes are integrated to establish distinct, orthogonal digital switching states. A PIN diode consists of a heavily doped P-type ($p^+$) semiconductor region and an N-type ($n^+$) region separated by a wide, high-resistivity intrinsic ($i$) semiconductor layer.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.68\textwidth]{figures/plot_pin_diode_impedance.png}
    \caption{High-Frequency PIN Diode Equivalent Circuit Model: Forward Bias (ON) and Reverse Bias (OFF) Impedance Magnitude $|Z_d|$ Across the Ka-Band ($20 - 40\text{ GHz}$).}
    \label{fig:pin_impedance}
\end{figure}

\subsection{Forward-Bias (ON) State Mechanics}
When a positive forward DC bias ($V_F \approx 0.8\text{ to }1.2\text{ V}$) is applied across the PIN junction, electron and hole carriers are injected from the $p^+$ and $n^+$ contacts into the intrinsic region. The intrinsic region becomes saturated with a dense plasma of charge carriers with an effective carrier lifetime $\tau_c \approx 10\text{ to }50\text{ ns}$. Because the RF period at $29.4\text{ GHz}$ ($T_{RF} \approx 34\text{ ps}$) is much shorter than $\tau_c$, the intrinsic layer cannot un-charge within a single RF half-cycle. Consequently, the diode behaves as a linear, ultra-low resistance $R_s$ in series with parasitic lead inductance $L_s$:
\begin{equation}
Z_{ON}(\omega) = R_s + j \omega L_s
\label{eq:pin_on_impedance}
\end{equation}
For commercial mmWave PIN diodes (such as the MACOM MA4AGBL912 AlGaAs beam-lead diode), typical forward parameters are $R_s = 1.5\,\Omega$ and $L_s = 0.05\text{ nH}$.

\subsection{Reverse-Bias (OFF) State Mechanics}
Under reverse bias ($V_R \le 0\text{ V}$), the intrinsic region is fully depleted of free carriers. The wide, low-dielectric intrinsic layer acts as an extremely small parallel-plate junction capacitance $C_j$ in parallel with a large reverse leakage resistance $R_p \approx 10\text{ k}\Omega$. Accounting for packaging parasitics ($L_p = 0.08\text{ nH}, C_p = 0.015\text{ pF}$), the total equivalent input impedance in the OFF state is:
\begin{equation}
Z_{OFF}(\omega) = j\omega L_p + \left[ \frac{1}{R_p} + j\omega (C_j + C_p) \right]^{-1}
\label{eq:pin_off_impedance}
\end{equation}
At $29.4\text{ GHz}$, the total effective capacitance $C_{tot} = C_j + C_p \approx 0.043\text{ pF}$, producing a high reactive impedance $|Z_{OFF}| \approx 125.8\,\Omega$, creating an open-circuit boundary condition that interrupts RF surface currents across the radiating gap.

\begin{table}[H]
\centering
\caption{High-Frequency PIN Diode Equivalent Circuit Parameters in Ansys HFSS}
\label{tab:pin_parameters}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|l|c|c|l|}
\hline
\textbf{Equivalent Circuit Element} & \textbf{Symbol} & \textbf{Assigned Value} & \textbf{Physical Mechanism} \\
\hline
Forward Series Resistance & $R_s$ & $1.5\,\Omega$ & Intrinsic layer conductivity modulation under carrier injection. \\
Forward Series Inductance & $L_s$ & $0.05\text{ nH}$ & Bond-wire / metallized contact ribbon parasitic inductance. \\
Reverse Junction Capacitance & $C_j$ & $0.028\text{ pF}$ & Depletion layer dielectric capacitance of intrinsic zone. \\
Reverse Leakage Resistance & $R_p$ & $10.0\text{ k}\Omega$ & Finite bulk semiconductor shunt resistivity. \\
Package Inductance & $L_p$ & $0.08\text{ nH}$ & Outer beam-lead / surface-mount packaging parasitic. \\
Package Capacitance & $C_p$ & $0.015\text{ pF}$ & Ceramic / substrate fringe pad capacitance. \\
\hline
\end{tabular}
\end{table}

\section{Substrate Integrated Waveguide (SIW) Physics and Guided Waves}
Substrate Integrated Waveguide (SIW) technology synthesizes artificial, low-profile metallic waveguides directly inside multi-layer planar substrates by replacing the continuous metallic sidewalls of conventional rectangular waveguides with linear arrays of plated through-vias connecting top and bottom ground planes.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.68\textwidth]{figures/diagram_siw_geometry_parameters.png}
    \caption{Substrate Integrated Waveguide (SIW) Structural Geometry: Via Diameter $d$, Longitudinal Pitch $p$, Physical Width $w$, and Metallized Shielding Ground Planes.}
    \label{fig:siw_geometry}
\end{figure}

\subsection{Equivalent Waveguide Width Formulation}
Due to the periodic gaps between adjacent metallic vias, electromagnetic fringing fields penetrate slightly beyond the via centerlines. Consequently, an SIW with physical via center-to-center width $w$, via diameter $d$, and via pitch $p$ is electromagnetically equivalent to a conventional dielectric-filled rectangular waveguide with effective width $a_{eq}$. Using Cassivi's empirical formulation:
\begin{equation}
a_{eq} = w - 1.08 \frac{d^2}{p} + 0.1 \frac{d^3}{p^2}
\label{eq:siw_aeq}
\end{equation}

For the fundamental Transverse Electric mode ($\text{TE}_{10}$), the cutoff frequency is:
\begin{equation}
f_{c,10} = \frac{c}{2 a_{eq} \sqrt{\epsilon_r}}
\label{eq:siw_cutoff_10}
\end{equation}
and for higher-order modes ($\text{TE}_{20}$):
\begin{equation}
f_{c,20} = \frac{c}{a_{eq} \sqrt{\epsilon_r}} = 2 f_{c,10}
\label{eq:siw_cutoff_20}
\end{equation}

\subsection{Via Array Design Rules and Leakage Radiation Suppression}
To prevent electromagnetic energy from leaking between adjacent vias into the substrate, the via geometry must satisfy strict dimensional criteria established by Deslandes and Wu:
\begin{enumerate}
  \item \textbf{Pitch-to-Diameter Ratio:} To suppress radiation leakage through via spacings:
  \begin{equation}
  \frac{d}{p} \ge 0.5 \quad \text{or} \quad p \le 2d
  \label{eq:siw_rule1}
  \end{equation}
  \item \textbf{Diameter-to-Wavelength Ratio:} To prevent localized Bragg reflections and internal scattering:
  \begin{equation}
  \frac{d}{\lambda_g} \le 0.1 \quad \text{where} \quad \lambda_g = \frac{\lambda_0}{\sqrt{\epsilon_r - (f_{c,10}/f)^2}}
  \label{eq:siw_rule2}
  \end{equation}
\end{enumerate}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.68\textwidth]{figures/plot_siw_dispersion_curve.png}
    \caption{Substrate Integrated Waveguide (SIW) Dispersion Characteristic ($\beta$ vs Frequency) on Isola Substrate ($\epsilon_r = 3.0$), Confirming Single-Mode $\text{TE}_{10}$ Propagation Across the $24 - 36\text{ GHz}$ Band.}
    \label{fig:siw_dispersion}
\end{figure}

In this design, $d = 0.6\text{ mm}$ and $p = 1.0\text{ mm}$, yielding $d/p = 0.6 \ge 0.5$. With $\epsilon_r = 3.0$ and $a_{eq} = 4.2\text{ mm}$, the cutoff frequency is $f_{c,10} = 20.61\text{ GHz}$. As demonstrated in Figure~\ref{fig:siw_dispersion}, the operating frequency $f_0 = 29.4\text{ GHz}$ falls squarely within the single-mode $\text{TE}_{10}$ passband well below $f_{c,20} = 41.22\text{ GHz}$.

\section{Planar Array Theory and Floquet Periodic Boundaries}
When unit cells are arranged in an infinite 2D periodic planar array along the $x$- and $y$-axes with periods $P_x$ and $P_y$, the scattered electromagnetic fields can be expanded into an infinite series of discrete spatial Floquet modes. According to the \textbf{Floquet-Bloch Theorem}, the electric field satisfies:
\begin{equation}
\mathbf{E}(x + P_x, y + P_y, z) = \mathbf{E}(x, y, z) \exp(-j k_{x0} P_x) \exp(-j k_{y0} P_y)
\label{eq:floquet_bloch}
\end{equation}
where $k_{x0} = k_0 \sin\theta \cos\phi$ and $k_{y0} = k_0 \sin\theta \sin\phi$ represent the transverse phase shifts imposed by an incident plane wave arriving from direction $(\theta, \phi)$.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.68\textwidth]{figures/plot_floquet_grating_lobe_diagram.png}
    \caption{Floquet Periodic Grating Lobe Diagram in the Normalized $k_x$-$k_y$ Plane ($P_x = P_y = 5.0\text{ mm} \approx 0.49 \lambda_0$), Demonstrating That All Higher-Order Floquet Modes $(m,n) \neq (0,0)$ Fall Outside the Visible Radiation Circle.}
    \label{fig:floquet_grating}
\end{figure}

The transverse wavenumbers of the higher-order Floquet spatial harmonics $(m, n)$ are:
\begin{equation}
k_{xm} = k_{x0} + \frac{2\pi m}{P_x}, \quad k_{yn} = k_{y0} + \frac{2\pi n}{P_y}
\label{eq:floquet_harmonics}
\end{equation}
with longitudinal propagation constants:
\begin{equation}
k_{z,mn} = \sqrt{k_0^2 - k_{xm}^2 - k_{yn}^2}
\label{eq:floquet_kz}
\end{equation}

To guarantee that no energy is lost into spurious diffracted grating lobes across all scan angles ($\theta \in [0, 90^\circ]$), all modes with $(m, n) \neq (0, 0)$ must possess imaginary longitudinal wavenumbers ($k_{z,mn} = -j\alpha_{z,mn}$), enforcing:
\begin{equation}
P_x < \frac{\lambda_0}{1 + \sin\theta_{max}}, \quad P_y < \frac{\lambda_0}{1 + \sin\theta_{max}}
\label{eq:grating_lobe_suppression}
\end{equation}

For broadside reflection ($\theta = 0^\circ$), the grating lobe condition requires $P \le \lambda_0 \approx 10.2\text{ mm}$. For wide-angle beam steering up to $\theta_{max} = 60^\circ$, $P < \lambda_0 / (1 + \sin 60^\circ) = 10.2 / 1.866 \approx 5.46\text{ mm}$. The selected unit-cell period of $P_x = P_y = 5.0\text{ mm} \approx 0.49 \lambda_0$ rigorously fulfills this requirement, ensuring complete grating lobe suppression as depicted in Figure~\ref{fig:floquet_grating}.

\subsection{Phase Discretization and Quantization Loss}
When synthesizing a progressive phase distribution across a large array of $M \times N$ unit cells, continuous phase tuning is often approximated by $B$-bit discrete phase quantization:
\begin{equation}
\Delta \Phi = \frac{360^\circ}{2^B}
\label{eq:quant_step}
\end{equation}
Assuming uniformly distributed phase quantization errors over $[-\Delta\Phi/2, \Delta\Phi/2]$, the resulting directivity loss (quantization efficiency $\eta_q$) is expressed analytically as:
\begin{equation}
\eta_q = \left[ \frac{\sin(\pi / 2^B)}{\pi / 2^B} \right]^2 = \text{sinc}^2\left( \frac{\pi}{2^B} \right)
\label{eq:quant_efficiency}
\end{equation}

\begin{table}[H]
\centering
\caption{Phase Quantization Resolution vs Directivity Quantization Loss}
\label{tab:quantization_loss}
\small
\renewcommand{\arraystretch}{1.08}
\begin{tabular}{|c|c|c|c|l|}
\hline
\textbf{Resolution ($B$)} & \textbf{Discrete States ($2^B$)} & \textbf{Phase Step ($\Delta\Phi$)} & \textbf{Quantization Loss ($\text{dB}$)} & \textbf{Typical Implementation} \\
\hline
1-bit & 2 & $180^\circ$ & $-3.92\text{ dB}$ & Single PIN diode per unit cell. \\
2-bit & 4 & $90^\circ$ & $-0.91\text{ dB}$ & Dual PIN diode configuration. \\
3-bit & 8 & $45^\circ$ & $-0.22\text{ dB}$ & Multi-diode / varactor network. \\
Continuous & $\infty$ & $0^\circ$ & $0.00\text{ dB}$ & Voltage-gated Graphene / Hybrid. \\
\hline
\end{tabular}
\end{table}

As quantified in Table~\ref{tab:quantization_loss}, a 1-bit RIS suffers a severe $3.92\text{ dB}$ gain penalty. The proposed hybrid PIN--Graphene architecture uses the dual PIN diodes to bridge the $90^\circ / 180^\circ$ macro-states, while the voltage-tunable graphene impedance provides continuous micro-phase trimming, virtually eliminating quantization loss and suppressing side-lobe levels.
"""
