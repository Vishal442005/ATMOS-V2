# make_sec9_appendices_refs.py

def get_appendices_and_refs():
    return r"""
\clearpage
%% ==========================================================================
%%  APPENDICES
%% ==========================================================================
\appendix

\chapter{Python PyAEDT \& Ansys HFSS Automated Modeling Scripts}
\justifying
To ensure repeatability and facilitate rapid parametric optimization, an automated Python script was developed utilizing the \textbf{PyAEDT} (Ansys Electronics Desktop Python API) library. The script automates the complete 3D geometric construction, material assignments, Boolean anti-pad clearances, Floquet port excitations, and adaptive meshing setups directly within Ansys HFSS.

\begin{lstlisting}[caption={Python PyAEDT Script for Automated 3D Unit-Cell Modeling in Ansys HFSS}, label={lst:pyaedt_script}]
# pyaedt_hfss_ris_generator.py
# Automated Parametric Modeling of Hybrid PIN-Graphene RIS in Ansys HFSS

import os
from pyaedt import Hfss

# 1. Initialize HFSS Session
hfss = Hfss(specified_version="2026.1", designname="PIN_Graphene_RIS_29GHz", 
            solution_type="Modal", new_desktop_session=False)
hfss.modeler.model_units = "mm"

# 2. Define Parametric Variables
params = {
    "P_cell": "5.0mm",       # Unit cell period (0.49 lambda)
    "W_patch": "4.6mm",      # Radiating patch width
    "H_patch": "0.035mm",    # Copper foil thickness (1 oz)
    "H_diel": "0.175mm",     # Individual Isola layer thickness
    "H_sub": "0.700mm",      # Total 4-layer substrate height
    "W_gap": "0.500mm",      # Radiating gap width
    "R_via": "0.150mm",      # Central signal via radius
    "R_antipad": "0.350mm",  # Ground plane anti-pad clearance radius
    "R_siw": "0.300mm",      # Peripheral SIW shielding via radius
    "P_siw": "1.000mm",      # SIW via longitudinal pitch
    "Z_gnd": "2.3399mm",     # Ground plane Z-coordinate
    "Air_H": "2.550mm"       # Radiation air box height (lambda / 4)
}

for k, v in params.items():
    hfss[k] = v

# 3. Create 4-Layer Isola Substrate Dielectric
for i in range(1, 5):
    z_start = f"Z_gnd + {(i-1)} * H_diel"
    diel_name = f"Layer{i}_Dielectric"
    hfss.modeler.create_box(
        origin=["0mm", "0mm", z_start],
        sizes=["P_cell", "P_cell", "H_diel"],
        name=diel_name,
        material="isola_terragreen"
    )

# 4. Create Continuous mmWave Ground Plane with Annular Anti-Pad
gnd = hfss.modeler.create_rectangle(
    origin=["0mm", "0mm", "Z_gnd"],
    sizes=["P_cell", "P_cell"],
    plane="XY",
    name="mmWave_Ground",
    is_covered=True
)

antipad_tool = hfss.modeler.create_circle(
    origin=["P_cell/2", "P_cell/2", "Z_gnd"],
    radius="R_antipad",
    plane="XY",
    name="Antipad_Tool",
    is_covered=True
)

# Subtract anti-pad to isolate central via from ground
hfss.modeler.subtract(blank_list=[gnd.name], tool_list=[antipad_tool.name], keep_tools=False)
hfss.assign_perfecte_to_sheets(sheet_list=[gnd.name], sourcename="PEC_Ground")

# 5. Create Central Signal Bias Via
central_via = hfss.modeler.create_cylinder(
    origin=["P_cell/2", "P_cell/2", "Z_gnd - 0.00005mm"],
    radius="R_via",
    height="H_sub + H_patch",
    axis="Z",
    name="Central_Signal_Via",
    material="copper"
)

# 6. Create Top Copper Radiating Patch with Boolean "Cookie-Cutter" Gap
patch_z = "Z_gnd + H_sub"
patch = hfss.modeler.create_box(
    origin=["(P_cell - W_patch)/2", "(P_cell - W_patch)/2", patch_z],
    sizes=["W_patch", "W_patch", "H_patch"],
    name="Top_Radiating_Patch",
    material="copper"
)

# Slicing gap via Boolean subtraction
gap_cutter = hfss.modeler.create_box(
    origin=["(P_cell - W_gap)/2", "(P_cell - W_patch)/2 - 0.1mm", patch_z],
    sizes=["W_gap", "W_patch + 0.2mm", "H_patch"],
    name="Gap_Cutter",
    material="vacuum"
)
hfss.modeler.subtract(blank_list=[patch.name], tool_list=[gap_cutter.name], keep_tools=False)

# 7. Create Master Radiation Air Box and Floquet Port
air_z_min = "Z_gnd - Air_H"
air_h_tot = "H_sub + H_patch + 2 * Air_H"
airbox = hfss.modeler.create_box(
    origin=["0mm", "0mm", air_z_min],
    sizes=["P_cell", "P_cell", air_h_tot],
    name="Radiation_AirBox",
    material="vacuum"
)

# Assign Master / Slave Periodic Boundaries
hfss.assign_master_slave(
    master_face_id=hfss.modeler[airbox.name].faces[0].id,
    slave_face_id=hfss.modeler[airbox.name].faces[1].id,
    u_vector=["P_cell", "0mm", "0mm"],
    name="MasterSlave_X"
)

# 8. Assign De-embedded Floquet Port on Top Air Face
top_air_face = hfss.modeler[airbox.name].top_face_z
hfss.create_floquet_port(
    face_id=top_air_face.id,
    deembed_distance="Air_H",
    port_name="Floquet_Port_1"
)

# 9. Setup Adaptive Analysis Setup \& Frequency Sweep
setup = hfss.create_setup(name="KaBand_Setup", Frequency="29.4GHz", MaximumPasses=20, MaxDeltaS=0.02)
sweep = setup.create_frequency_sweep(
    name="Sweep_24_to_36GHz",
    start_frequency="24.0GHz",
    stop_frequency="36.0GHz",
    num_of_points=401,
    sweep_type="Interpolating"
)

print("HFSS Model Construction and Setup Completed Successfully!")
\end{lstlisting}

\clearpage
\chapter{Geometric Parameter Master Reference Table}
\justifying
Table~\ref{tab:master_parameter_reference} compiles all dimensional variables, spatial tolerances, material attributions, and functional mechanisms incorporated into the final Ansys HFSS simulation model.

\begin{table}[H]
\centering
\caption{Complete Geometric Parameter Master Look-Up Table}
\label{tab:master_parameter_reference}
\small
\renewcommand{\arraystretch}{1.10}
\begin{tabular}{|l|c|c|l|}
\hline
\textbf{Parameter Description} & \textbf{Symbol} & \textbf{Assigned Value} & \textbf{Electromagnetic \& Physical Function} \\
\hline
Unit Cell Spatial Period & $P_x, P_y$ & $5.000\text{ mm}$ & $0.490 \lambda_0$; enforces spatial Nyquist grating-lobe suppression. \\
Radiating Copper Patch Width & $W_p$ & $4.600\text{ mm}$ & Dictates fundamental LC patch resonance near $29.4\text{ GHz}$. \\
Radiating Gap Width (Nominal) & $g_{nom}$ & $0.500\text{ mm}$ & Houses active PIN diodes and continuous graphene sheets. \\
Radiating Gap Width (Enlarged) & $g_{wide}$ & $0.800\text{ mm}$ & Swept in parametric study; shifts resonance to $30.55\text{ GHz}$. \\
Copper Foil Thickness & $H_{cu}$ & $0.035\text{ mm}$ ($35\,\mu\text{m}$) & Standard $1\text{ oz/ft}^2$ electrodeposited annealed copper. \\
Total Substrate Dielectric Height & $H_{sub}$ & $0.700\text{ mm}$ & 4-layer Isola core/prepreg stack ($4 \times 0.175\text{ mm}$). \\
Substrate Dielectric Constant & $\epsilon_r$ & $3.00 \pm 0.04$ & High-frequency low-loss Isola TerraGreen laminate. \\
Dielectric Loss Tangent & $\tan\delta$ & $0.0035$ & Low-dissipation tangent at mmWave Ka-band. \\
Central Signal Bias Via Radius & $r_v$ & $0.150\text{ mm}$ & Extruded metallic cylinder for DC bias routing. \\
Ground Clearance Anti-Pad Radius & $r_{ap}$ & $0.350\text{ mm}$ & Subtracted 2D circle; prevents DC ground short circuit. \\
Annular Anti-Pad Clearance Gap & $\Delta r$ & $0.200\text{ mm}$ & Coaxial clearance annulus ($r_{ap} - r_v$). \\
Peripheral SIW Via Diameter & $d_{siw}$ & $0.600\text{ mm}$ & Substrate Integrated Waveguide perimeter shielding. \\
Peripheral SIW Via Pitch & $p_{siw}$ & $1.000\text{ mm}$ & Via-to-via center spacing satisfying $d/p = 0.6 \ge 0.5$. \\
Equivalent SIW Waveguide Width & $a_{eq}$ & $4.200\text{ mm}$ & Fundamental $\text{TE}_{10}$ mode cutoff $f_{c,10} = 20.61\text{ GHz}$. \\
PIN Diode Forward Resistance & $R_s$ & $1.50\,\Omega$ & Forward-bias ON-state carrier injection resistance. \\
PIN Diode Forward Inductance & $L_s$ & $0.05\text{ nH}$ & Beam-lead bonding ribbon parasitic series inductance. \\
PIN Diode Reverse Capacitance & $C_j$ & $0.028\text{ pF}$ & Reverse-bias OFF-state intrinsic depletion capacitance. \\
PIN Diode Reverse Resistance & $R_p$ & $10.0\text{ k}\Omega$ & Bulk reverse semiconductor shunt leakage resistance. \\
Graphene Chemical Potential & $\mu_c$ & $0.1 - 1.0\text{ eV}$ & Electrostatic Fermi level tuning via DC gate voltage. \\
Graphene Carrier Relaxation Time & $\tau$ & $0.50\text{ ps}$ & Momentum scattering lifetime in Kubo formalism. \\
Radiation Air Box Height & $H_{air}$ & $2.550\text{ mm}$ & $\lambda_0 / 4$ reactive near-field buffer above patch and ground. \\
Floquet De-Embedding Distance & $d_{deembed}$ & $2.550\text{ mm}$ & Translates phase reference to copper patch face. \\
\hline
\end{tabular}
\end{table}

\clearpage
\chapter{Material Properties and Dielectric Database}
\justifying
Table~\ref{tab:material_database} details the constitutive electromagnetic, thermal, and mechanical parameters assigned to all materials within the Ansys HFSS simulation database.

\begin{table}[H]
\centering
\caption{Constitutive Material Properties Database in Ansys HFSS}
\label{tab:material_database}
\small
\renewcommand{\arraystretch}{1.10}
\begin{tabular}{|l|c|c|c|l|}
\hline
\textbf{Material Name} & \textbf{Rel. Permittivity ($\epsilon_r$)} & \textbf{Loss Tan ($\tan\delta$)} & \textbf{Conductivity ($\sigma$)} & \textbf{Physical Assignment in RIS} \\
\hline
Annealed Copper & $1.00$ & $0.0000$ & $5.80 \times 10^7\text{ S/m}$ & Radiating patch, ground sheet, and vias. \\
Isola TerraGreen & $3.00$ & $0.0035$ & $0.00\text{ S/m}$ & 4-layer low-loss dielectric substrate core. \\
Isola Astra MT77 Prepreg & $3.00$ & $0.0017$ & $0.00\text{ S/m}$ & Multi-layer bonding prepreg laminates. \\
Vacuum / Air & $1.00006$ & $0.0000$ & $0.00\text{ S/m}$ & Radiation air box and annular anti-pad. \\
Monolayer Graphene & Complex Kubo & $\text{Im}\{\sigma_g\}$ & Equation~(\ref{eq:sigma_g_real_imag}) & Active 2D impedance boundary sheets. \\
GaAs Semiconductor Die & $12.90$ & $0.0006$ & $10^{-6}\text{ S/m}$ & PIN diode intrinsic semiconductor body. \\
Gold (ENIG Finish) & $1.00$ & $0.0000$ & $4.10 \times 10^7\text{ S/m}$ & Anti-oxidation pad surface metallization. \\
Nickel (Barrier Layer) & $1.00$ & $0.0000$ & $1.43 \times 10^7\text{ S/m}$ & Under-gold electroplated diffusion barrier. \\
EPO-TEK H20E Epoxy & $3.80$ & $0.0200$ & $1.00 \times 10^6\text{ S/m}$ & Conductive silver component bonding paste. \\
\hline
\end{tabular}
\end{table}

\clearpage
%% ==========================================================================
%%  BIBLIOGRAPHY & REFERENCES
%% ==========================================================================
\begin{thebibliography}{99}
\addcontentsline{toc}{chapter}{REFERENCES}
\small
\setlength{\itemsep}{2pt plus 0.5pt minus 0.5pt}
\setlength{\parskip}{0pt}

\bibitem{yu2011light}
N.~Yu, P.~Genevet, M.~A.~Kats, F.~Aieta, J.-P.~Tetienne, F.~Capasso, and Z.~Gaburow, 
``Light propagation with phase discontinuities: generalized laws of reflection and refraction,'' 
\textit{Science}, vol.~334, no.~6054, pp.~333--337, 2011.

\bibitem{cui2014coding}
T.~J.~Cui, M.~Q.~Qi, X.~Wan, J.~Zhao, and Q.~Cheng, 
``Coding metamaterials, digital metamaterials and programmable metamaterials,'' 
\textit{Light: Science \& Applications}, vol.~3, no.~10, p.~e218, 2014.

\bibitem{huang2020holographic}
C.~Huang, S.~Hu, G.~C.~Alexandropoulos, A.~Zappone, C.~Yuen, R.~Zhang, M.~Di~Renzo, and M.~Debbah, 
``Holographic MIMO surfaces for 6G wireless networks: Opportunities, challenges, and trends,'' 
\textit{IEEE Wireless Communications}, vol.~27, no.~5, pp.~118--125, 2020.

\bibitem{wu2019towards}
Q.~Wu and R.~Zhang, 
``Towards smart and reconfigurable environment: Intelligent reflecting surface aided wireless network,'' 
\textit{IEEE Communications Magazine}, vol.~58, no.~1, pp.~106--112, 2019.

\bibitem{wu2021intelligent}
Q.~Wu, S.~Zhang, B.~Zheng, C.~You, and R.~Zhang, 
``Intelligent reflecting surface-aided wireless communications: A tutorial,'' 
\textit{IEEE Transactions on Communications}, vol.~69, no.~5, pp.~3313--3351, 2021.

\bibitem{direnzo2020smart}
M.~Di~Renzo, A.~Zappone, M.~Debbah, M.-S.~Alouini, C.~Yuen, J.~de~Rosny, and S.~Tretyakov, 
``Smart radio environments empowered by reconfigurable intelligent surfaces: How it works, state of research, and the road ahead,'' 
\textit{IEEE Journal on Selected Areas in Communications}, vol.~38, no.~11, pp.~2450--2525, 2020.

\bibitem{basar2019wireless}
E.~Basar, M.~Di~Renzo, J.~De~Rosny, M.~Debbah, M.-S.~Alouini, and R.~Zhang, 
``Wireless communications through reconfigurable intelligent surfaces,'' 
\textit{IEEE Access}, vol.~7, pp.~116753--116773, 2019.

\bibitem{tang2021wireless}
W.~Tang, M.~Z.~Chen, X.~Chen, J.~Y.~Dai, Y.~Han, M.~Di~Renzo, Y.~Zeng, S.~Jin, Q.~Cheng, and T.~J.~Cui, 
``Wireless communications with reconfigurable intelligent surface: Path loss modeling and experimental measurement,'' 
\textit{IEEE Transactions on Wireless Communications}, vol.~20, no.~1, pp.~421--439, 2021.

\bibitem{hanson2008dyadic}
G.~W.~Hanson, 
``Dyadic Green's functions and guided surface waves for a surface conductivity model of graphene,'' 
\textit{Journal of Applied Physics}, vol.~103, no.~6, p.~064302, 2008.

\bibitem{gusynin2006transport}
V.~P.~Gusynin, S.~G.~Sharapov, and J.~P.~Carbotte, 
``Magneto-optical conductivity in graphene,'' 
\textit{Journal of Physics: Condensed Matter}, vol.~19, no.~2, p.~026222, 2006.

\bibitem{novoselov2004electric}
K.~S.~Novoselov, A.~K.~Geim, S.~V.~Morozov, D.~Jiang, Y.~Zhang, S.~V.~Dubonos, I.~V.~Grigorieva, and A.~A.~Firsov, 
``Electric field effect in atomically thin carbon films,'' 
\textit{Science}, vol.~306, no.~5696, pp.~666--669, 2004.

\bibitem{castroneto2009electronic}
A.~H.~Castro~Neto, F.~Guinea, N.~M.~R.~Peres, K.~S.~Novoselov, and A.~K.~Geim, 
``The electronic properties of graphene,'' 
\textit{Reviews of Modern Physics}, vol.~81, no.~1, pp.~109--162, 2009.

\bibitem{deslandes2006accurate}
D.~Deslandes and K.~Wu, 
``Accurate modeling, wave mechanisms, and design considerations of a substrate integrated waveguide,'' 
\textit{IEEE Transactions on Microwave Theory and Techniques}, vol.~54, no.~6, pp.~2516--2524, 2006.

\bibitem{cassivi2002dispersion}
Y.~Cassivi, L.~Perregrini, P.~Arcioni, M.~Bressan, K.~Wu, and R.~G.~Bosisio, 
``Dispersion characteristics of substrate integrated rectangular waveguide,'' 
\textit{IEEE Microwave and Wireless Components Letters}, vol.~12, no.~9, pp.~333--335, 2002.

\bibitem{wu2003guided}
K.~Wu, D.~Deslandes, and Y.~Cassivi, 
``The substrate integrated circuits (SICs) concept---a new planar technological platform for microwave and millimeter-wave applications,'' 
in \textit{6th International Conference on Telecommunications in Modern Satellite, Cable and Broadcasting Service}, 2003, pp.~P--III.

\bibitem{bozzi2011substrate}
M.~Bozzi, A.~Georgiadis, and K.~Wu, 
``Review of substrate-integrated waveguide circuits and antennas,'' 
\textit{IET Microwaves, Antennas \& Propagation}, vol.~5, no.~8, pp.~909--920, 2011.

\bibitem{balanis2016antenna}
C.~A.~Balanis, 
\textit{Antenna Theory: Analysis and Design}, 4th~ed. Hoboken, NJ: John Wiley \& Sons, 2016.

\bibitem{pozar2011microwave}
D.~M.~Pozar, 
\textit{Microwave Engineering}, 4th~ed. Hoboken, NJ: John Wiley \& Sons, 2011.

\bibitem{rappiport2013millimeter}
T.~S.~Rappaport, S.~Sun, R.~Mayzus, H.~Zhao, Y.~Azar, K.~Wang, G.~N.~Wong, J.~K.~Schulz, M.~Samimi, and F.~Gutierrez, 
``Millimeter wave mobile communications for 5G cellular: It will work!'' 
\textit{IEEE Access}, vol.~1, pp.~335--349, 2013.

\bibitem{boccardi2014five}
F.~Boccardi, R.~W.~Heath, A.~Lozano, T.~L.~Marzetta, and P.~Popovski, 
``Five disruptive technology directions for 5G,'' 
\textit{IEEE Communications Magazine}, vol.~52, no.~2, pp.~74--80, 2014.

\bibitem{liu2021reconfigurable}
Y.~Liu, X.~Liu, X.~Mu, T.~Hou, J.~Xu, M.~Di~Renzo, and N.~Al-Dhahir, 
``Reconfigurable intelligent surfaces: Principles and opportunities,'' 
\textit{IEEE Communications Surveys \& Tutorials}, vol.~23, no.~3, pp.~1546--1577, 2021.

\bibitem{pan2021reconfigurable}
C.~Pan, H.~Ren, K.~Wang, J.~F.~Kolb, M.~Elkashlan, and M.~Di~Renzo, 
``Reconfigurable intelligent surfaces for 6G: Emerging applications, challenges, and opportunities,'' 
\textit{IEEE Wireless Communications}, vol.~28, no.~6, pp.~70--77, 2021.

\bibitem{bjornson2020intelligent}
E.~Björnson, Ö.~Özdogan, and E.~G.~Larsson, 
``Intelligent reflecting surface versus decode-and-forward relaying: Does the IRS beat the relay?'' 
\textit{IEEE Wireless Communications Letters}, vol.~9, no.~5, pp.~586--589, 2020.

\bibitem{ozdogan2020using}
Ö.~Özdogan, E.~Björnson, and E.~G.~Larsson, 
``Using intelligent reflecting surfaces for rank improvement in MIMO channels,'' 
\textit{IEEE Transactions on Wireless Communications}, vol.~19, no.~6, pp.~3936--3947, 2020.

\bibitem{zheng2019intelligent}
B.~Zheng and R.~Zhang, 
``Intelligent reflecting surface-enhanced OFDM: Channel estimation and reflection optimization,'' 
\textit{IEEE Wireless Communications Letters}, vol.~9, no.~4, pp.~518--522, 2019.

\bibitem{you2020channel}
C.~You, B.~Zheng, and R.~Zhang, 
``Channel estimation and passive beamforming for intelligent reflecting surface: Discrete phase shift and progressive refinement,'' 
\textit{IEEE Journal on Selected Areas in Communications}, vol.~38, no.~11, pp.~2604--2620, 2020.

\bibitem{liu2022integrated}
F.~Liu, C.~Masouros, A.~P.~Petropulu, H.~Griffiths, and L.~Hanzo, 
``Joint radar and communication design: Applications, state-of-the-art, and the road ahead,'' 
\textit{IEEE Transactions on Communications}, vol.~68, no.~6, pp.~3834--3862, 2020.

\bibitem{cui2021integrating}
Y.~Cui, F.~Liu, X.~Jing, and J.~Mu, 
``Integrating sensing and communications for ubiquitous IoT: Applications, trends, and challenges,'' 
\textit{IEEE Network}, vol.~35, no.~5, pp.~158--167, 2021.

\bibitem{zhang2021overview}
J.~A.~Zhang, F.~Liu, C.~Masouros, R.~W.~Heath, P.~Zheng, A.~Petropulu, and K.~Wu, 
``An overview of signal processing techniques for joint communication and radar sensing,'' 
\textit{IEEE Journal of Selected Topics in Signal Processing}, vol.~15, no.~6, pp.~1295--1315, 2021.

\bibitem{chen2021reconfigurable}
Z.~Chen, X.~Ma, B.~Zhang, Y.~Zhang, Z.~Niu, N.~Kuipers, and R.~He, 
``A survey on terahertz communications: Applications, challenges, and key technologies,'' 
\textit{IEEE Communications Surveys \& Tutorials}, vol.~23, no.~2, pp.~863--919, 2021.

\bibitem{saad2019vision}
W.~Saad, M.~Bennis, and M.~Chen, 
``A vision of 6G wireless systems: Applications, trends, technologies, and open research problems,'' 
\textit{IEEE Network}, vol.~34, no.~3, pp.~134--142, 2019.

\bibitem{yang20206g}
P.~Yang, Y.~Xiao, M.~Xiao, and S.~Li, 
``6G wireless communications: Vision and potential key technologies,'' 
\textit{IEEE Network}, vol.~33, no.~4, pp.~70--75, 2019.

\bibitem{perruisseau2018graphene}
J.~Perruisseau-Carrier, 
``Graphene for reconfigurable terahertz and microwave applications,'' 
in \textit{European Microwave Conference (EuMC)}, 2012, pp.~381--384.

\bibitem{tamagnone2012reconfigurable}
M.~Tamagnone, J.~S.~Gómez-Díaz, J.~R.~Mosig, and J.~Perruisseau-Carrier, 
``Reconfigurable terahertz plasmonic devices based on graphene,'' 
\textit{Applied Physics Letters}, vol.~101, no.~24, p.~244102, 2012.

\bibitem{carrasco2013reflectarray}
E.~Carrasco, M.~Tamagnone, and J.~Perruisseau-Carrier, 
``Tunable graphene reflectarray at terahertz frequencies,'' 
\textit{IEEE Transactions on Antennas and Propagation}, vol.~61, no.~7, pp.~3590--3596, 2013.

\bibitem{fallahi2012design}
A.~Fallahi and J.~Perruisseau-Carrier, 
``Design of tunable biperiodic graphene metasurfaces,'' 
\textit{Physical Review B}, vol.~86, no.~19, p.~195411, 2012.

\bibitem{liang2021anomalous}
J.~Liang, L.~Zhang, and T.~J.~Cui, 
``Anomalous reflection and refraction based on coding metasurfaces,'' 
\textit{Advanced Optical Materials}, vol.~9, no.~14, p.~2100201, 2021.

\bibitem{wan2016broadband}
X.~Wan, M.~Q.~Qi, T.~Y.~Chen, and T.~J.~Cui, 
``Field-programmable beam reconfiguring based on digitally controllable metasurface,'' 
\textit{Scientific Reports}, vol.~6, no.~1, p.~20663, 2016.

\bibitem{chen2020reconfigurable}
M.~Chen, W.~Tang, J.~Dai, X.~Chen, S.~Jin, Q.~Cheng, and T.~Cui, 
``Accurate and fast synthesis of spatial beam patterns for reconfigurable intelligent surfaces,'' 
\textit{IEEE Communications Letters}, vol.~24, no.~12, pp.~2864--2867, 2020.

\bibitem{vasisht2021in}
D.~Vasisht, G.~Zou, and F.~Adib, 
``In-body backscatter communication and localization,'' 
in \textit{ACM SIGCOMM}, 2018, pp.~132--146.

\end{thebibliography}

\end{document}
"""
