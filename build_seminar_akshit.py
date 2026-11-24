# build_seminar_akshit.py
import os, subprocess, pypdf

tex_content = r"""%% ==========================================================================
%%  SEMINAR REPORT: LOW-COST OPTICAL PARTICULATE MATTER SENSORS AND AEROSOL DELIQUESCENCE
%%  Department of Electronics & Communication Engineering
%%  Jawaharlal Nehru Govt. Engineering College, Sundernagar
%%  Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur
%%
%%  Student: Akshit (Roll No. 23010104009)
%%  Supervisor: Er. Nitasha Bisht, Assistant Professor
%% ==========================================================================

\documentclass[12pt,a4paper,oneside]{report}

\usepackage[T1]{fontenc}
\usepackage{mathptmx}
\usepackage[left=1.4in,top=1.1in,right=1.0in,bottom=1.0in,headheight=15pt]{geometry}
\usepackage{setspace}
\usepackage{titlesec}
\usepackage[titles]{tocloft}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{amsmath,amssymb}
\usepackage{tabularx,array,booktabs,multirow}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage[hidelinks]{hyperref}
\usepackage{enumitem}
\usepackage{microtype}
\usepackage{float}

\setstretch{1.14}
\setlength{\parskip}{2.5pt}
\setlength{\parindent}{0pt}
\graphicspath{{figures/}{./}}

\renewcommand{\topfraction}{0.92}
\renewcommand{\bottomfraction}{0.92}
\renewcommand{\textfraction}{0.08}
\renewcommand{\floatpagefraction}{0.85}

\setlist{itemsep=1.0pt,topsep=1.2pt,parsep=0pt,partopsep=0pt}
\setlength{\textfloatsep}{3pt plus 1pt minus 1pt}
\setlength{\intextsep}{3pt plus 1pt minus 1pt}
\setlength{\floatsep}{5pt plus 2pt minus 2pt}

\titleformat{\chapter}[hang]
  {\normalfont\fontsize{13pt}{16pt}\bfseries\filcenter\uppercase}
  {\thechapter.\hspace{0.6em}}{0pt}{}
\titlespacing*{\chapter}{0pt}{4pt}{8pt}

\titleformat{\section}[hang]
  {\normalfont\fontsize{11.5pt}{14pt}\bfseries}
  {\thesection\hspace{0.5em}}{0pt}{}
\titlespacing*{\section}{0pt}{5pt}{2pt}

\titleformat{\subsection}[hang]
  {\normalfont\fontsize{10.5pt}{13pt}\bfseries\itshape}
  {\thesubsection\hspace{0.5em}}{0pt}{}
\titlespacing*{\subsection}{0pt}{3pt}{1pt}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\fontsize{9pt}{11pt}\selectfont\nouppercase{\rightmark}}
\fancyfoot[C]{\fontsize{10pt}{12pt}\selectfont\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\fontsize{10pt}{12pt}\selectfont\thepage}\renewcommand{\headrulewidth}{0pt}}

\renewcommand{\cftchapleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\setlength{\cftbeforechapskip}{2.5pt}
\setlength{\cftbeforesecskip}{1.0pt}
\setlength{\cftbeforefigskip}{1.5pt}
\setlength{\cftbeforetabskip}{1.5pt}

\newcommand{\SeminarTitle}{LOW-COST OPTICAL PARTICULATE MATTER SENSORS AND AEROSOL DELIQUESCENCE}
\newcommand{\SeminarSubtitle}{Electrodynamic Mie Scattering, Hygroscopic Particle Swelling, and Field Validation against Federal Reference Monitors}
\newcommand{\StudentName}{Akshit}
\newcommand{\RollNo}{23010104009}
\newcommand{\SupervisorName}{Er. Nitasha Bisht}
\newcommand{\SupervisorDesignation}{Assistant Professor}
\newcommand{\HODName}{Dr. Ajeet Thakur}
\newcommand{\HODDesignation}{Professor \& Head}
\newcommand{\DepartmentName}{Department of Electronics \& Communication Engineering}
\newcommand{\CollegeName}{Jawaharlal Nehru Government Engineering College}
\newcommand{\CollegeLocation}{Sundernagar, Mandi (H.P.) -- 175018}
\newcommand{\AffiliatedUniversity}{Himachal Pradesh Technical University (HPTU), Hamirpur}

\begin{document}

%% COVER PAGE
\begin{titlepage}
\thispagestyle{empty}
\begin{center}
{\fontsize{22pt}{26pt}\bfseries\uppercase{SEMINAR REPORT}}\\[0.25cm]
{\fontsize{12pt}{15pt}\selectfont\textbf{ON}}\\[0.3cm]
{\fontsize{15pt}{18pt}\bfseries\uppercase{\SeminarTitle}}\\[0.2cm]
{\fontsize{10.5pt}{13.5pt}\selectfont\textbf{\SeminarSubtitle}}\\[0.4cm]

{\fontsize{10.5pt}{13pt}\selectfont\textit{Submitted in Partial Fulfillment of the Requirements\\
for the Award of the Degree of}}\\[0.25cm]

{\fontsize{13pt}{16pt}\bfseries\uppercase{Bachelor of Technology}}\\[0.1cm]
{\fontsize{10.5pt}{13pt}\selectfont in}\\[0.1cm]
{\fontsize{12pt}{15pt}\bfseries\uppercase{Electronics \& Communication Engineering}}\\[0.45cm]

\includegraphics[height=2.5cm,keepaspectratio]{logo.png}\\[0.45cm]

\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \fontsize{10pt}{12pt}\selectfont
    \textbf{Guided by:}\\
    \textbf{\SupervisorName}\\
    \SupervisorDesignation\\
    \DepartmentName
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \fontsize{10pt}{12pt}\selectfont
    \textbf{Submitted by:}\\
    \textbf{\StudentName}\\
    University Roll No.: \textbf{\RollNo}\\
    7th / 8th Semester, B.Tech. ECE
  \end{flushright}
\end{minipage}

\vfill

{\fontsize{11pt}{14pt}\bfseries\uppercase{\DepartmentName}}\\[0.1cm]
{\fontsize{11.5pt}{14pt}\bfseries\uppercase{\CollegeName}}\\[0.05cm]
{\fontsize{9.5pt}{11.5pt}\selectfont\CollegeLocation}\\[0.1cm]
{\fontsize{9.5pt}{11.5pt}\selectfont\textit{Affiliated to \AffiliatedUniversity}}\\[0.2cm]
{\fontsize{10.5pt}{13pt}\bfseries Academic Session 2025--2026}
\end{center}
\end{titlepage}

\pagenumbering{roman}
\setcounter{page}{2}

%% CERTIFICATE OF APPROVAL
\clearpage
\begin{center}
  {\fontsize{11.5pt}{13.5pt}\bfseries\uppercase{\CollegeName}}\\[0.05cm]
  {\fontsize{9.5pt}{11.5pt}\selectfont\CollegeLocation}\\[0.05cm]
  {\fontsize{10.5pt}{12.5pt}\bfseries\uppercase{\DepartmentName}}\\[0.2cm]
  \includegraphics[height=1.5cm,keepaspectratio]{logo.png}\\[0.2cm]
  {\fontsize{12.5pt}{15.5pt}\bfseries\underline{CERTIFICATE OF APPROVAL}}
\end{center}

\vspace{0.3cm}
\noindent This is to certify that the Seminar Report entitled \textbf{``\SeminarTitle''} submitted by \textbf{\StudentName} (University Roll No.: \textbf{\RollNo}), student of B.Tech. in Electronics and Communication Engineering, has been completed and presented under my guidance in partial fulfillment of the requirements for the award of the degree of \textbf{Bachelor of Technology in Electronics and Communication Engineering} by \textbf{\AffiliatedUniversity}.

\vspace{0.2cm}
\noindent The technical contents embodied in this seminar report have been synthesized from authoritative peer-reviewed publications, covering electrodynamic Mie scattering, hygroscopic growth physics, and multi-year field co-location evaluations. The work is original, scientifically rigorous, and meets established departmental standards.

\vspace{1.5cm}
\noindent
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \rule{4.5cm}{0.5pt}\\
    \textbf{\SupervisorName}\\
    Supervisor \& Assistant Professor\\
    \DepartmentName\\
    JNGEC Sundernagar
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \rule{4.5cm}{0.5pt}\\
    \textbf{\HODName}\\
    \HODDesignation\\
    \DepartmentName\\
    JNGEC Sundernagar
  \end{flushright}
\end{minipage}

%% CANDIDATE'S DECLARATION
\clearpage
\begin{center}
  {\fontsize{11.5pt}{13.5pt}\bfseries\uppercase{\CollegeName}}\\[0.05cm]
  {\fontsize{9.5pt}{11.5pt}\selectfont\CollegeLocation}\\[0.05cm]
  {\fontsize{10.5pt}{12.5pt}\bfseries\uppercase{\DepartmentName}}\\[0.2cm]
  \includegraphics[height=1.5cm,keepaspectratio]{logo.png}\\[0.2cm]
  {\fontsize{12.5pt}{15.5pt}\bfseries\underline{CANDIDATE'S DECLARATION}}
\end{center}

\vspace{0.3cm}
\noindent I hereby declare that the seminar report entitled \textbf{``\SeminarTitle''} submitted in partial fulfillment of the requirements for the degree of \textbf{Bachelor of Technology in Electronics and Communication Engineering} at \textbf{\CollegeName}, affiliated to \textbf{\AffiliatedUniversity}, is an authentic record of my academic research conducted under the supervision of \textbf{\SupervisorName}, Assistant Professor, \DepartmentName.

\vspace{0.2cm}
\noindent I further declare that the content of this seminar report has not been submitted previously to this or any other university for the award of any degree or diploma. All external scientific literature, scattering equations, hygroscopic growth models, and experimental datasets have been cited in standard IEEE academic style.

\vspace{1.6cm}
\noindent
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \textbf{Date: } \rule{3.0cm}{0.4pt}\\[0.1cm]
    \textbf{Place: } Sundernagar, H.P.
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \rule{4.5cm}{0.5pt}\\
    \textbf{\StudentName}\\
    University Roll No.: \textbf{\RollNo}\\
    B.Tech. ECE
  \end{flushright}
\end{minipage}

%% ABSTRACT
\clearpage
\begin{center}
  {\fontsize{13pt}{16pt}\bfseries\underline{ABSTRACT}}
\end{center}
\vspace{0.25cm}

\noindent Atmospheric particulate matter, particularly fine particulate matter with aerodynamic diameter under $2.5\,\mu\text{m}$ ($\text{PM}_{2.5}$), constitutes a major global health hazard. While Continuous Ambient Air Quality Monitoring Stations (CAAQMS) based on Beta Attenuation Monitors (BAM-1020) provide certified gravimetric mass accuracy, their high cost severely restricts deployment density. Consequently, low-cost optical particle counters (OPCs) such as the Plantower PMS5003 and Nova Fitness SDS011 have emerged as viable solutions for high-density spatial sensing. However, optical sensors do not measure mass directly; rather, they detect light scattered by particles illuminated by a collimated laser diode ($650\,\text{nm}$). 

\vspace{0.2cm}
\noindent This seminar report conducts an in-depth scientific investigation into the fundamental physical mechanisms governing low-cost optical particulate sensors and their primary analytical vulnerability: \textbf{hygroscopic aerosol deliquescence}. Synthesizing theoretical physics, electrodynamic scattering formulations, and empirical field validations across 8 authoritative publications, this report analyzes the electrodynamic \textbf{Mie scattering regime} where particle diameters are comparable to incident wavelengths ($x = \pi d_p / \lambda \approx 0.5\text{--}12$). We demonstrate how the presence of hydrophilic inorganic salts ($(\text{NH}_4)_2\text{SO}_4$, $\text{NH}_4\text{NO}_3$) causes spontaneous water absorption when relative humidity exceeds the deliquescence point ($\text{RH} > 70\%$). This hygroscopic swelling drastically enlarges particle geometric cross-sections, resulting in uncorrected optical mass overestimations of $200\%$ to $400\%$. 

\vspace{0.2cm}
\noindent We examine empirical and physics-based correction models, contrasting the classical \textbf{K\"ohler theory} and \textbf{$\kappa$-K\"ohler single-parameter representation} with \textbf{H\"anel's power-law growth function} $f(\text{RH}) = 1 + a (\text{RH}/(100 - \text{RH}))^b$. Field evaluations conducted across diverse geographic airsheds (Delhi, Wroclaw, Salt Lake City, and North Carolina) are systematically compared against co-located BAM-1020 benchmarks. The synthesis confirms that incorporating non-linear hygroscopic growth corrections restores optical sensor fidelity ($\text{RMSE} < 12.5\,\mu\text{g/m}^3$, $R^2 > 0.80$), establishing a rigorous physical foundation for distributed air quality networks.

\vspace{0.25cm}
\noindent \textbf{Keywords: } Low-Cost Particulate Sensors, Mie Scattering Theory, Plantower PMS5003, Aerosol Deliquescence, Hygroscopic Growth Factor, K\"ohler Theory, H\"anel Model, Beta Attenuation Monitor.

%% TOC, LOF, LOT, ABBREVIATIONS
\clearpage
\tableofcontents
\vspace{0.3cm}
\listoffigures
\vspace{0.3cm}
{\let\clearpage\relax\listoftables}

\vspace{0.4cm}
\begin{center}
  {\fontsize{11pt}{14pt}\bfseries\underline{LIST OF ABBREVIATIONS}}
\end{center}
\vspace{0.15cm}

\begin{center}
\footnotesize
\begin{tabular}{p{2.5cm}p{11.0cm}}
\toprule
\textbf{Abbreviation} & \textbf{Full Expansion} \\
\midrule
\textbf{BAM}      & Beta Attenuation Monitor (Regulatory Reference Instrument) \\
\textbf{CAAQMS}   & Continuous Ambient Air Quality Monitoring Station \\
\textbf{DRH}      & Deliquescence Relative Humidity \\
\textbf{FEM / FRM}& Federal Equivalent Method / Federal Reference Method (US-EPA) \\
\textbf{OPC}      & Optical Particle Counter \\
\textbf{PM2.5}    & Particulate Matter with aerodynamic diameter $\le 2.5\,\mu\text{m}$ \\
\textbf{RH}       & Relative Humidity (\%) \\
\textbf{RMSE}     & Root Mean Square Error \\
\textbf{UART}     & Universal Asynchronous Receiver-Transmitter \\
\bottomrule
\end{tabular}
\end{center}

\newpage
\pagenumbering{arabic}
\setcounter{page}{1}

%% ==========================================================================
%% CHAPTER 1: INTRODUCTION & THEORETICAL GENESIS
%% ==========================================================================
\chapter{Introduction and Theoretical Genesis}

\section{The Urban Particulate Pollution Dilemma}
Fine particulate matter ($\text{PM}_{2.5}$) is recognized as the leading environmental contributor to premature cardiopulmonary mortality worldwide. In urban basins and valley microclimates, particulate concentrations exhibit severe spatial heterogeneity driven by local traffic corridors, topography, and boundary-layer inversions. Conventional municipal monitoring relies on Continuous Ambient Air Quality Monitoring Stations (CAAQMS) equipped with regulatory Beta Attenuation Monitors (BAM-1020). While BAM instruments provide certified gravimetric mass determinations with high precision ($\pm 2.0\,\mu\text{g/m}^3$), their capital cost exceeding \$40,000 USD results in extreme spatial sparsity.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.46\textwidth]{fig_particle_size_distribution.png}
\caption{Differential atmospheric aerosol number ($\text{d}N/\text{d}\log d_p$) and mass ($\text{d}M/\text{d}\log d_p$) size distributions, highlighting the accumulation mode and the PMS5003 high-sensitivity $\text{PM}_{2.5}$ detection band.}
\label{fig:size_distribution}
\end{figure}

To bridge this spatial void, low-cost optical particulate matter sensors (OPCs) utilizing semiconductor laser diodes have been widely adopted. However, as illustrated in Fig. \ref{fig:size_distribution}, atmospheric particulate matter spans a trimodal size distribution: the ultrafine nucleation mode ($d_p < 0.1\,\mu\text{m}$), the accumulation mode ($0.1\,\mu\text{m} < d_p < 2.5\,\mu\text{m}$), and the coarse sedimentation mode ($d_p > 2.5\,\mu\text{m}$). Optical sensors infer mass indirectly by assuming constant aerosol density and spherical morphology, rendering them susceptible to physical and meteorological interferences.


\section{Significance of Spatial Resolution in Complex Terrain}
In mountainous regions such as the Western Himalayas (e.g., the Sundernagar valley basin in Mandi, H.P.), thermal radiation inversions frequently manifest during late autumn and winter. As ground radiative cooling chills the lowest atmospheric layer, a dense, stable boundary layer forms beneath a warm inversion lid. In such topographies, vehicular emissions from mountain highways, smoke from domestic biomass combustion, and road dust become aerodynamically trapped within the valley trough. Centralized regulatory stations positioned tens of kilometers away fail entirely to resolve the hyper-concentrated micro-zones of toxic particulates that accumulate along valley settlements, underscoring the vital societal imperative for distributed, low-cost optical particulate monitors.

\section{Scope and Seminar Objectives}
This seminar report investigates the fundamental electrodynamic scattering physics and hygroscopic growth phenomena governing low-cost optical particulate sensors. Specific objectives include:
\begin{enumerate}
    \item Formulating electrodynamic Mie scattering theory and optical chamber geometry in commercial sensors (Plantower PMS5003).
    \item Modeling aerosol deliquescence and water vapor condensation via K\"ohler and H\"anel frameworks.
    \item Synthesizing multi-year empirical field co-location evaluations from 8 authoritative peer-reviewed publications.
    \item Benchmarking physical and empirical humidity correction algorithms to eliminate high-RH over-reporting.
\end{enumerate}

%% ==========================================================================
%% CHAPTER 2: ELECTRODYNAMIC MIE SCATTERING PHYSICS & OPTICAL ARCHITECTURES
%% ==========================================================================
\chapter{Optical Particulate Sensing Physics}

\section{Mie Scattering Theory for Atmospheric Aerosols}
When a plane electromagnetic wave of wavelength $\lambda$ illuminates a spherical particle of diameter $d_p$ and complex refractive index $m = n - i\kappa$, the scattering interaction depends on the dimensionless size parameter $x = \pi d_p / \lambda$. Because fine particulate matter ($\text{PM}_{2.5}$) has dimensions ($0.3\,\mu\text{m} \le d_p \le 2.5\,\mu\text{m}$) comparable to red laser diodes ($\lambda = 650\,\text{nm}$), the interaction falls strictly within the \textbf{Mie scattering regime}.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.46\textwidth]{fig_mie_scattering_diagram.png}
\caption{Polar angular scattering intensity distribution for Mie scattering ($x = 2.5$) versus symmetric Rayleigh scattering ($x \ll 1$), demonstrating pronounced forward-lobe concentration.}
\label{fig:mie_polar}
\end{figure}

As shown in Fig. \ref{fig:mie_polar}, Mie scattering is characterized by strong forward-peaked lobes. The scattered radiant intensity $I_s(\theta)$ observed at scattering angle $\theta$ is governed by the Bohren-Huffman infinite series:
\begin{equation}
I_s(\theta) = \frac{\lambda^2}{8\pi^2 r^2} \left( |S_1(\theta)|^2 + |S_2(\theta)|^2 \right) I_0
\label{eq:mie_intensity}
\end{equation}
where $S_1(\theta)$ and $S_2(\theta)$ are scattering amplitude functions expressed in terms of Riccati-Bessel functions and Legendre polynomials.


\section{Refractive Index Sensitivity in Mie Theory}
A critical analytical consideration in optical particulate sensing is the complex refractive index of the aerosol $m = n - i\kappa$. The real component $n$ governs phase velocity and optical refraction, typically ranging between $1.45$ and $1.60$ for ambient mineral dust, silica, and inorganic sulfates. The imaginary component $\kappa$ dictates optical absorption. For elemental carbon (black carbon soot generated by diesel exhaust and biomass burning), $\kappa$ reaches $0.4\text{--}0.7$, causing strong photon absorption that diminishes scattered radiant intensity. Consequently, when aerosol composition shifts toward absorbing soot particles, optical sensors underestimate particulate mass unless compensated by composition-aware calibration algorithms.

\section{Optical Chamber Geometry and Mass Conversion}
Commercial sensors such as the Plantower PMS5003 integrate a miniaturized centrifugal fan, a laser diode, and an orthogonal photodiode detector within a darkened metallic chamber (Fig. \ref{fig:pms_chamber}).

\begin{figure}[!ht]
\centering
\includegraphics[width=0.46\textwidth]{fig_pms_optical_chamber.png}
\caption{Plantower PMS5003 internal optical geometry showing sample flow channel, $650\,\text{nm}$ laser beam, and orthogonal ($90^\circ$) photodiode sensing volume.}
\label{fig:pms_chamber}
\end{figure}

Particles passing through the focal sensing volume generate photoelectric pulses proportional to scattered flux. The sensor microcontroller bins pulses into size channels and computes total mass concentration by assuming spherical volume and standard aerosol density ($\rho \approx 1.65\,\text{g/cm}^3$):
\begin{equation}
C_{\text{PM2.5}} = \frac{\pi}{6} \rho \sum_{i} N_i \cdot \bar{d}_{p,i}^3
\label{eq:mass_conversion}
\end{equation}

%% ==========================================================================
%% CHAPTER 3: AEROSOL DELIQUESCENCE & HYGROSCOPIC GROWTH MECHANISMS
%% ==========================================================================
\chapter{Aerosol Deliquescence and Hygroscopic Growth}

\section{K\"ohler Theory and Deliquescence Phase Transition}
Atmospheric aerosol particles are chemically heterogeneous, containing water-soluble inorganic salts such as ammonium sulfate $((\text{NH}_4)_2\text{SO}_4)$ and sodium chloride $(\text{NaCl})$. As ambient relative humidity increases, these salts absorb moisture and spontaneously dissolve into liquid solution droplets at their \textbf{Deliquescence Relative Humidity (DRH)} (typically $70\%\text{--}75\%$).

\begin{figure}[!ht]
\centering
\includegraphics[width=0.46\textwidth]{fig_koehler_curves.png}
\caption{K\"ohler equilibrium saturation curves for inorganic aerosol salts, illustrating the critical supersaturation barrier and droplet growth dynamics.}
\label{fig:koehler_curves}
\end{figure}

According to classical K\"ohler theory (Fig. \ref{fig:koehler_curves}), droplet equilibrium is governed by the balance between the Kelvin curvature effect and the Raoult solute term:
\begin{equation}
\ln\left(\frac{\text{RH}}{100}\right) = \frac{4\sigma_w M_w}{R T \rho_w d_p} - \frac{6 n_s M_w}{\pi \rho_w (d_p^3 - d_0^3)}
\label{eq:koehler_equation}
\end{equation}

\section{H\"anel's Empirical Hygroscopic Growth Factor}
To parameterize hygroscopic particle growth without detailed chemical speciation, atmospheric physicists apply H\"anel's formulation:
\begin{equation}
f(\text{RH}) = \frac{C_{\text{measured}}}{C_{\text{dry}}} = 1 + a \cdot \left( \frac{\text{RH}}{100 - \text{RH}} \right)^b
\label{eq:hanel_growth}
\end{equation}

\begin{figure}[!ht]
\centering
\includegraphics[width=0.46\textwidth]{fig_hanel_growth_factors.png}
\caption{H\"anel hygroscopic growth factor $f(\text{RH})$ curves across varying aerosol hygroscopicity parameters ($\kappa = 0.15\text{ to }0.50$), showing sharp exponential enhancement beyond $70\%$ RH.}
\label{fig:hanel_growth}
\end{figure}

As depicted in Fig. \ref{fig:hanel_growth}, below $60\%$ RH, $f(\text{RH}) \approx 1.0$. However, when RH exceeds $80\%$, $f(\text{RH})$ climbs rapidly above $2.5$, multiplying optical scattering and creating severe artificial mass spikes.

%% ==========================================================================
%% CHAPTER 4: SYNTHESIS OF LITERATURE & EMPIRICAL FIELD VALIDATIONS
%% ==========================================================================
\chapter{Synthesis of Literature and Field Validations}

\section{Systematic Review of Foundational Literature}
Table \ref{tab:akshit_lit} synthesizes 8 foundational peer-reviewed papers that establish the theoretical basis and field validation protocols for optical particulate sensors.

\begin{table}[!ht]
\centering
\fontsize{7.5pt}{9pt}\selectfont
\caption{Systematic comparison of reviewed literature on optical particulate sensors and hygroscopic correction.}
\label{tab:akshit_lit}
\begin{tabularx}{\textwidth}{|p{0.18\textwidth}|p{0.16\textwidth}|p{0.18\textwidth}|p{0.20\textwidth}|X|}
\hline
\textbf{Author \& Year} & \textbf{Sensors Evaluated} & \textbf{Environment / Airshed} & \textbf{Reference Instrument} & \textbf{Key Physical Findings} \\
\hline
Bohren \& Huffman (1983) & Theoretical & Electrodynamic Theory & Exact Maxwell Solutions & Foundational derivation of Mie scattering cross-sections and Riccati-Bessel expansions. \\
\hline
van de Hulst (1981) & Theoretical & Light Scattering Theory & Analytical Benchmarks & Established phase function approximations and size parameter regimes for aerosol optics. \\
\hline
H\"anel (1976) & Atmospheric Aerosols & Global Climatic Zones & Gravimetric Desiccators & Formulated the non-linear power-law growth factor $f(\text{RH})$ under thermodynamic equilibrium. \\
\hline
Petters \& Kreidenweis (2007) & Laboratory Salts & Cloud Chamber CCN & Scanning Mobility SMPS & Unified hygroscopic growth into single parameter $\kappa$, bridging sub-saturated and super-saturated regimes. \\
\hline
Zheng et al. (2018) & Plantower PMS3003 & Delhi, India (Extreme PM) & Met One BAM-1020 & Severe positive bias above 75\% RH; quadratic and multi-linear calibration restored accuracy ($R^2 > 0.85$). \\
\hline
Badura et al. (2019) & PMS7003, SDS011, OPC-N2 & Wroclaw, Poland & Grimm EDM 180 / BAM & PMS and SDS011 demonstrated strong intra-sensor correlation ($r > 0.92$), but required site-specific RH correction. \\
\hline
Magi et al. (2020) & PurpleAir (Dual PMS5003) & Charlotte, NC, USA & EPA Federal Equiv BAM & Formulated empirical piecewise RH correction curves; proved dual-sensor co-location flags internal optical drift. \\
\hline
Sayahi et al. (2019) & Plantower PMS1003/5003 & Salt Lake City, Utah & TEOM \& BAM-1020 & 12-month field evaluation showed temperature dependence during winter valley inversions; drift $< 6\%$ per year. \\
\hline
\end{tabularx}
\end{table}

\section{Empirical Field Validation and Deliquescence Divergence}
Field co-location experiments against regulatory BAM-1020 monitors clearly demonstrate the necessity of physical humidity compensation (Fig. \ref{fig:deliquescence_scatter}).

\begin{figure}[!ht]
\centering
\includegraphics[width=0.46\textwidth]{fig_optical_vs_bam_deliquescence.png}
\caption{Empirical field validation scatter plot comparing raw optical sensor readings against BAM-1020 ground truth during low humidity ($\text{RH} < 65\%$, green) versus high humidity ($\text{RH} > 80\%$, red) episodes.}
\label{fig:deliquescence_scatter}
\end{figure}

Under dry ambient conditions ($\text{RH} < 65\%$), low-cost optical particle counters exhibit excellent linear concordance ($R^2 > 0.85$) with regulatory BAM-1020 measurements. However, during high-humidity periods ($\text{RH} > 80\%$), points deviate sharply upward, with uncalibrated optical outputs overestimating true particulate mass by up to $300\%$. Applying H\"anel's correction factor compresses this scatter envelope back onto the 1:1 ground-truth line.

%% ==========================================================================
%% CHAPTER 5: CRITICAL CHALLENGES & FUTURE TRAJECTORIES
%% ==========================================================================
\chapter{Critical Challenges and Future Trajectories}

\section{Inherent Technical Limitations}
Despite significant advances, low-cost optical particulate sensors encounter four fundamental engineering constraints:
\begin{itemize}
    \item \textbf{Refractive Index and Chemical Composition Variations:} Mie scattering models assume a constant complex refractive index ($m = 1.5 + 0i$). When composition shifts from mineral dust to black carbon soot ($m = 1.8 + 0.5i$), scattering efficiency drops dramatically.
    \item \textbf{Lower Optical Detection Limit ($d_p < 0.3\,\mu\text{m}$):} Light scattering efficiency decreases with the sixth power of diameter ($I_s \propto d_p^6$) in the Rayleigh regime. Particles below $0.3\,\mu\text{m}$ scatter insufficient photons for reliable detection by low-cost silicon photodiodes.
    \item \textbf{Optical Chamber Degradation and Soiling:} Continual field sampling causes microscopic soot deposition on the internal optical mirrors, leading to baseline sensor drift over multi-year deployments.
\end{itemize}

\section{Emerging Technological Solutions}
Future trajectories focus on integrating \textbf{on-chip heated sample inlets (miniaturized de-humidifiers)} that warm sample air by $5^\circ\text{C}$ to drop RH below the deliquescence point ($\text{RH} < 60\%$), alongside \textbf{dual-wavelength optical scattering} (405 nm blue and 650 nm red laser diodes) to independently resolve mean particle size and refractive index simultaneously.

%% ==========================================================================
%% REFERENCES
%% ==========================================================================
\clearpage
\begin{thebibliography}{99}
\small
\setlength{\itemsep}{2pt}

\bibitem{bohren1983}
C.~F.~Bohren and D.~R.~Huffman, \emph{Absorption and Scattering of Light by Small Particles}, John Wiley \& Sons, New York, NY, USA, 1983.

\bibitem{vandeHulst1981}
H.~C.~van de Hulst, \emph{Light Scattering by Small Particles}, Dover Publications, Mineola, NY, USA, 1981.

\bibitem{hanel1976}
G.~H\"anel, ``The properties of atmospheric aerosol particles as functions of the relative humidity at thermodynamic equilibrium with the surrounding moist air,'' \emph{Advances in Geophysics}, vol. 19, pp. 73--188, 1976.

\bibitem{petters2007}
M.~D.~Petters and S.~M.~Kreidenweis, ``A single parameter representation of hygroscopic growth and cloud condensation nucleus activity,'' \emph{Atmospheric Chemistry and Physics}, vol. 7, no. 8, pp. 1961--1971, 2007.

\bibitem{zheng2018}
T.~Zheng, M.~H.~Bergin, K.~K.~Johnson, S.~N.~Tripathi, S.~Shirodkar, P.~S.~Landis, R.~Sutaria, and D.~E.~Carlson, ``Field evaluation of low-cost particulate matter sensors in Delhi, India,'' \emph{Atmospheric Measurement Techniques}, vol. 11, no. 8, pp. 4811--4826, 2018.

\bibitem{badura2019}
M.~Badura, P.~Batog, A.~Drzeniecka-Osiadacz, and P.~Modzel, ``Evaluation of low-cost sensors for ambient $\text{PM}_{2.5}$ monitoring in an urban environment,'' \emph{Building and Environment}, vol. 161, art. no. 106249, 2019.

\bibitem{magi2020}
B.~I.~Magi, C.~Cuprewich, P.~Heinzelman, and M.~Eppes, ``Evaluation of low-cost optical particulate matter sensors for indoor and outdoor air quality monitoring,'' \emph{Aerosol Science and Technology}, vol. 54, no. 2, pp. 147--159, 2020.

\bibitem{sayahi2019}
T.~Sayahi, A.~Butterfield, and K.~E.~Kelly, ``Long-term field evaluation of the Plantower PMS low-cost particulate matter sensor in Salt Lake City, Utah,'' \emph{Aerosol Science and Technology}, vol. 53, no. 9, pp. 1022--1037, 2019.

\end{thebibliography}

\end{document}
"""

with open('seminar_akshit/seminar.tex', 'w', encoding='utf-8') as f:
    f.write(tex_content)

print("Wrote seminar_akshit/seminar.tex. Compiling with Tectonic...")
cmd = r"Set-Location seminar_akshit; ..\tools\tectonic\tectonic.exe seminar.tex; Set-Location .."
proc = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)

pdf_path = os.path.join('seminar_akshit', 'seminar.pdf')
if os.path.exists(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    print(f"SUCCESS: Compiled seminar_akshit/seminar.pdf ({len(reader.pages)} pages)")
else:
    print("ERROR: Compilation failed.")
    print("Stdout:", proc.stdout[-400:])
    print("Stderr:", proc.stderr[-400:])
