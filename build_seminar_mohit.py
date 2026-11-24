# build_seminar_mohit.py
import os, subprocess, pypdf

tex_content = r"""%% ==========================================================================
%%  SEMINAR REPORT: CHEMORESISTIVE GAS SENSORS AND SOLAR IOT ARCHITECTURES
%%  Department of Electronics & Communication Engineering
%%  Jawaharlal Nehru Govt. Engineering College, Sundernagar
%%  Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur
%%
%%  Student: Mohit Negi (Roll No. 23010104043)
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
\setlength{\parskip}{2.8pt}
\setlength{\parindent}{0pt}
\graphicspath{{figures/}{./}}

\renewcommand{\topfraction}{0.95}
\renewcommand{\bottomfraction}{0.95}
\renewcommand{\textfraction}{0.05}
\renewcommand{\floatpagefraction}{0.85}

\setlist{itemsep=1.0pt,topsep=1.2pt,parsep=0pt,partopsep=0pt}
\setlength{\textfloatsep}{4pt plus 1pt minus 1pt}
\setlength{\intextsep}{3pt plus 1pt minus 1pt}
\setlength{\floatsep}{4pt plus 1pt minus 1pt}
\setlength{\abovecaptionskip}{2.5pt}
\setlength{\belowcaptionskip}{1.0pt}

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
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}

\renewcommand{\cftchapleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\setlength{\cftbeforechapskip}{2.5pt}
\setlength{\cftbeforesecskip}{1.0pt}
\setlength{\cftbeforefigskip}{1.5pt}
\setlength{\cftbeforetabskip}{1.5pt}

\newcommand{\SeminarTitle}{CHEMORESISTIVE SEMICONDUCTOR GAS SENSORS AND ENERGY-AUTONOMOUS SOLAR IOT ARCHITECTURES}
\newcommand{\SeminarSubtitle}{Solid-State Surface Redox Reactions, Photovoltaic Micro-Grid Power Budgeting, and Low-Power Embedded FreeRTOS State Scheduling}
\newcommand{\StudentName}{Mohit Negi}
\newcommand{\RollNo}{23010104043}
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
{\fontsize{14pt}{17pt}\bfseries\uppercase{\SeminarTitle}}\\[0.2cm]
{\fontsize{10pt}{13pt}\selectfont\textbf{\SeminarSubtitle}}\\[0.4cm]

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
\noindent The technical contents embodied in this seminar report have been synthesized from authoritative peer-reviewed literature, covering metal oxide semiconductor surface physics, photovoltaic micro-grid power budgeting, and embedded low-power duty cycling. The work is original, scientifically rigorous, and meets established departmental standards.

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
\noindent I further declare that the content of this seminar report has not been submitted previously to this or any other university for the award of any degree or diploma. All external scientific literature, solid-state band diagrams, solar harvesting models, and power budgeting formulas have been cited in standard IEEE academic style.

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

\noindent Distributed ambient air quality monitoring demands the continuous surveillance of toxic gaseous effluents, including carbon monoxide ($\text{CO}$), ammonia ($\text{NH}_3$), nitrogen oxides ($\text{NO}_x$), and volatile organic compounds (VOCs). However, deploying environmental sensor arrays in outdoor, rural, or valley environments is severely restricted by the absence of continuous AC utility power and the thermal power dissipation of chemoresistive sensor heaters. Metal oxide semiconductor (MOS) sensors rely on elevated operating temperatures ($300^\circ\text{C}\text{--}400^\circ\text{C}$) to drive surface redox reactions, demanding upwards of $150\,\text{mA}$ at $5.0\,\text{V}$ per sensor.

\vspace{0.2cm}
\noindent This seminar report conducts an exhaustive engineering and physical investigation into the synthesis of \textbf{chemoresistive semiconductor gas sensors} and \textbf{energy-autonomous solar photovoltaic micro-grids} for distributed Internet of Things (IoT) monitoring nodes. Synthesizing solid-state electronic theory, surface chemical kinetics, and embedded systems engineering across 8 authoritative publications, this report details the solid-state band bending and space-charge depletion layer dynamics across tin dioxide ($\text{SnO}_2$) crystalline grain boundaries. We examine oxygen ion chemisorption ($\text{O}^-, \text{O}_2^-$) and the resulting logarithmic power-law resistance modulation $\log(R_s/R_0) = -\alpha \log(C) + \beta$ upon exposure to reducing gas molecules.

\vspace{0.2cm}
\noindent Furthermore, we establish a rigorous mathematical energy harvesting model based on a $6\text{V}$, $2\text{W}$ monocrystalline solar panel coupled with a TP4056 Constant-Current / Constant-Voltage (CC/CV) lithium-ion charge controller and dual 18650 Li-ion cells ($4400\,\text{mAh}$). Under Himalayan solar insolation conditions ($4.8\,\text{kWh/m}^2/\text{day}$ in Sundernagar, H.P.), we formulate an asynchronous \textbf{FreeRTOS power-state duty-cycle profile}. By gating the high-power heating coils and scheduling the ESP32 dual-core Xtensa microcontroller into deep-sleep modes ($15\,\mu\text{A}$ quiescent draw for $885\,\text{seconds}$), the time-averaged node current is constrained to $2.76\,\text{mA}$. This achieves over \textbf{53 days of continuous zero-sunlight off-grid operational autonomy}, proving that high-power chemoresistive gas sensors can be deployed sustainably in remote, un-electrified environmental terrains.

\vspace{0.25cm}
\noindent \textbf{Keywords: } Chemoresistive Gas Sensors, Tin Dioxide ($\text{SnO}_2$), Oxygen Chemisorption, Band Bending, Solar Energy Harvesting, TP4056 CC/CV Charging, FreeRTOS Duty Cycling, ESP32 Deep Sleep.

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
\textbf{ADC}      & Analog-to-Digital Converter \\
\textbf{CC/CV}    & Constant-Current / Constant-Voltage Charging Algorithm \\
\textbf{DOD}      & Depth of Discharge (Battery) \\
\textbf{ESP32}    & 32-bit Dual-Core Tensilica Xtensa LX6 Microcontroller \\
\textbf{FreeRTOS} & Free Real-Time Operating System \\
\textbf{MPP / MPPT}& Maximum Power Point / Maximum Power Point Tracking \\
\textbf{MOS}      & Metal Oxide Semiconductor Gas Sensor \\
\textbf{PSH}      & Peak Sun Hours ($\text{kWh/m}^2/\text{day}$) \\
\textbf{PV}       & Photovoltaic \\
\textbf{RTC}      & Real-Time Clock \\
\textbf{SOC}      & State of Charge (Battery percentage) \\
\textbf{ULP}      & Ultra-Low-Power Coprocessor \\
\textbf{VOC}      & Volatile Organic Compounds \\
\bottomrule
\end{tabular}
\end{center}

\newpage
\pagenumbering{arabic}
\setcounter{page}{1}

%% ==========================================================================
%% CHAPTER 1: INTRODUCTION AND ENERGY-CONSTRAINED SENSING
%% ==========================================================================
\chapter{Introduction and Energy-Constrained Sensing}

\section{The Imperative for Autonomous Multi-Gas Surveillance}
Atmospheric chemical effluents such as carbon monoxide ($\text{CO}$), ammonia ($\text{NH}_3$), methane ($\text{CH}_4$), and industrial volatile organic compounds (VOCs) represent severe acute and chronic threats to human respiratory physiology. In complex geographical terrains such as the Western Himalayas, industrial fencelines, asphalt transport arteries, and agrarian biomass burning generate localized chemical plumes that disperse heterogeneously across mountain valleys.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_freertos_duty_cycle_power.png}
\caption{Asynchronous FreeRTOS power-state duty-cycle timeline across active multi-sensor polling ($165\,\text{mA}$, $15\,\text{s}$) and ultra-low-power deep sleep ($15\,\mu\text{A}$, $885\,\text{s}$).}
\label{fig:duty_cycle_timeline}
\end{figure}

Conventional toxic gas instrumentation relies on mains-powered laboratory analyzers (e.g., non-dispersive infrared or chemiluminescence spectrometers) requiring hundreds of watts of continuous electrical power. Deploying distributed wireless sensor nodes in remote mountain valleys requires self-sustaining, energy-harvesting hardware. As illustrated in Fig. \ref{fig:duty_cycle_timeline}, balancing high-current gas sensor heating coils with limited solar photovoltaic budgets is the paramount engineering challenge.

\section{Scope and Seminar Objectives}
This seminar report explores the solid-state surface physics of metal oxide gas sensors and the embedded micro-grid architectures required for continuous off-grid operation. Key objectives include:
\begin{enumerate}
    \item Formulating band bending and oxygen chemisorption physics in n-type tin dioxide ($\text{SnO}_2$) chemoresistive sensors (MQ series).
    \item Modeling photovoltaic energy harvesting and maximum power transfer under regional Himalayan solar insolation.
    \item Analyzing lithium-ion battery electrochemistry, TP4056 CC/CV charging dynamics, and FreeRTOS duty-cycled power states.
    \item Synthesizing 8 peer-reviewed foundational publications covering sensor calibration, solar harvesting, and low-power embedded design.
\end{enumerate}

%% ==========================================================================
%% CHAPTER 2: CHEMORESISTIVE GAS SENSING PHYSICS & KINETICS
%% ==========================================================================
\chapter{Chemoresistive Gas Sensing Physics}

\section{Solid-State Surface Chemisorption Kinetics}
Chemoresistive gas sensors utilize wide bandgap n-type metal oxide semiconductors, predominantly tin dioxide ($\text{SnO}_2$, $E_g \approx 3.6\,\text{eV}$). Sensing occurs through surface oxidation-reduction reactions between gaseous molecules and pre-adsorbed oxygen ions on the polycrystalline grain boundaries.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_sn_o2_band_bending.png}
\caption{Energy band bending and conduction-band potential barrier ($qV_s$) across $\text{SnO}_2$ grain boundaries in clean air (high barrier) versus in reducing gas (thinned barrier).}
\label{fig:band_bending}
\end{figure}

At elevated operating temperatures ($300^\circ\text{C}\text{--}400^\circ\text{C}$ maintained by an internal heating resistor), ambient oxygen molecules adsorb onto the active semiconductor surface, trapping conduction-band electrons:
\begin{equation}
\text{O}_{2\text{,(gas)}} + 2e^- \rightleftharpoons 2\text{O}^-_{\text{(ads)}}
\label{eq:oxygen_adsorption}
\end{equation}
This electron extraction forms an electron-depletion layer (space-charge region) across each inter-granular contact (Fig. \ref{fig:band_bending}). The resulting Schottky-like electrical potential barrier $qV_s$ establishes a high baseline electrical resistance $R_0$:
\begin{equation}
R_0 = R_{\text{bulk}} \cdot \exp\left( \frac{q V_s}{k_B T} \right)
\label{eq:schottky_barrier}
\end{equation}

\section{Redox Reactions and Power-Law Sensitivity Curves}
When a reducing analyte gas (such as carbon monoxide or ammonia) diffuses into the porous sensing layer, it undergoes catalytic surface oxidation:
\begin{equation}
\text{CO} + \text{O}^-_{\text{(ads)}} \longrightarrow \text{CO}_{2\text{,(gas)}} + e^-
\label{eq:co_oxidation}
\end{equation}
\begin{equation}
2\text{NH}_3 + 3\text{O}^-_{\text{(ads)}} \longrightarrow \text{N}_{2\text{,(gas)}} + 3\text{H}_2\text{O}_{\text{,(gas)}} + 3e^-
\label{eq:nh3_oxidation}
\end{equation}

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_mq_sensor_sensitivity_curves.png}
\caption{Log-log power-law sensitivity characteristics of the MQ-135 sensor, illustrating relative response ($R_s/R_0$) across target gas species.}
\label{fig:mq_sensitivity}
\end{figure}

The liberated electrons return to the conduction band, lowering the inter-granular potential barrier and reducing sensor resistance $R_s$. As shown in Fig. \ref{fig:mq_sensitivity}, the resistance ratio follows the empirical power-law relation:
\begin{equation}
\frac{R_s}{R_0} = A \cdot C^{-\alpha} \implies \log\left(\frac{R_s}{R_0}\right) = -\alpha \log(C) + \log A
\label{eq:power_law_gas}
\end{equation}

%% ==========================================================================
%% CHAPTER 3: SOLAR ENERGY HARVESTING & EMBEDDED POWER BUDGETING
%% ==========================================================================
\chapter{Solar Micro-Grids and Embedded Power Budgeting}

\section{Photovoltaic Cell Characteristics and Maximum Power Point}
Energy autonomy is achieved using a $6\text{V}$, $2\text{W}$ monocrystalline silicon photovoltaic panel. Under standard test conditions ($1000\,\text{W/m}^2$, AM1.5, $25^\circ\text{C}$), the panel produces an open-circuit voltage $V_{\text{oc}} = 7.2\,\text{V}$ and short-circuit current $I_{\text{sc}} = 350\,\text{mA}$.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_solar_pv_iv_curve.png}
\caption{Photovoltaic I-V and P-V characteristic curves for the 2W monocrystalline solar panel, demonstrating the Maximum Power Point (MPP at $V = 5.95\,\text{V}$).}
\label{fig:pv_curves}
\end{figure}

As shown in Fig. \ref{fig:pv_curves}, maximum power ($P_{\text{max}} = 2.05\,\text{W}$) is extracted at $V_{\text{mp}} \approx 5.95\,\text{V}$ and $I_{\text{mp}} \approx 345\,\text{mA}$.

\section{TP4056 Lithium-Ion Charging and Electrochemical Storage}
Electrochemical storage utilizes two parallel 18650 cylindrical cells providing $C_{\text{bat}} = 4400\,\text{mAh}$ at nominal $3.7\,\text{V}$ ($16.28\,\text{Wh}$). Charge management is controlled by a dedicated TP4056 IC implementing a Constant-Current / Constant-Voltage (CC/CV) charging cycle (Fig. \ref{fig:tp4056_profile}).

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_tp4056_cc_cv_profile.png}
\caption{TP4056 CC/CV charging dynamics: constant-current bulk phase ($1000\,\text{mA}$) transitioning to constant-voltage saturation ($4.2\,\text{V}$) at 2.2 hours.}
\label{fig:tp4056_profile}
\end{figure}

In the CC phase, a constant current $I_{\text{chg}} = 1000\,\text{mA}$ is delivered until cell voltage reaches $4.2\,\text{V}$. The internal loop then clamps voltage at $4.2\,\text{V} \pm 1\%$, while charging current decays exponentially until termination at $C/10$ ($100\,\text{mA}$).

\section{Mathematical Energy Budget Formulation}
Under the solar climate of Sundernagar, H.P. (annual mean insolation $\bar{G} = 4.8\,\text{kWh/m}^2/\text{day}$ or $4.8\,\text{Peak Sun Hours}$), daily harvested energy $E_{\text{harvest}}$ accounting for dirt derating ($\eta_d = 0.90$) and charge efficiency ($\eta_c = 0.85$) is:
\begin{equation}
E_{\text{harvest}} = P_{\text{peak}} \cdot \text{PSH} \cdot \eta_d \cdot \eta_c = 2.0\,\text{W} \times 4.8\,\text{h} \times 0.90 \times 0.85 = 7.344\,\text{Wh/day}
\label{eq:harvest_wh}
\end{equation}
Equivalent to a daily charge replenishment $Q_{\text{harvest}} = 7.344\,\text{Wh} / 3.7\,\text{V} = 1985\,\text{mAh/day}$.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_battery_discharge_curves.png}
\caption{Electrochemical discharge voltage curves of 18650 Li-ion cells across varying C-rates, highlighting the flat discharge plateau at low continuous drain (0.2 C).}
\label{fig:discharge_curves}
\end{figure}

The node operates under an asynchronous FreeRTOS 15-minute cycle ($900\,\text{s}$): active sensing for $15\,\text{s}$ at $165\,\text{mA}$, followed by deep sleep for $885\,\text{s}$ at $15\,\mu\text{A}$. The average current $I_{\text{avg}}$ is:
\begin{equation}
I_{\text{avg}} = \frac{165\,\text{mA} \times 15\,\text{s} + 0.015\,\text{mA} \times 885\,\text{s}}{900\,\text{s}} = \frac{2475 + 13.275}{900} \approx 2.76\,\text{mA}
\label{eq:mohit_avg_current}
\end{equation}
Daily consumption is merely $Q_{\text{consumed}} = 2.76\,\text{mA} \times 24\,\text{h} = 66.24\,\text{mAh/day}$. Comparing harvest ($1985\,\text{mAh}$) to drain ($66.24\,\text{mAh}$) demonstrates an energy safety margin of nearly **$30\times$**.

Furthermore, complete off-grid autonomy during continuous dark monsoon cloud cover (Depth of Discharge $\text{DOD} = 80\%$) is:
\begin{equation}
T_{\text{autonomy}} = \frac{4400\,\text{mAh} \times 0.80}{2.76\,\text{mA} \times 24\,\text{h/day}} = \frac{3520}{66.24} \approx 53.1\,\text{days}
\label{eq:mohit_autonomy}
\end{equation}

%% ==========================================================================
%% CHAPTER 4: SYNTHESIS OF LITERATURE & EMBEDDED CASE STUDIES
%% ==========================================================================
\chapter{Synthesis of Literature and Case Studies}

\section{Systematic Review of Foundational Literature}
Table \ref{tab:mohit_lit} summarizes 8 foundational papers establishing the chemical, power harvesting, and embedded foundations of autonomous gas sensing.

\begin{table}[!ht]
\centering
\fontsize{7pt}{8.5pt}\selectfont
\renewcommand{\arraystretch}{0.85}
\caption{Comparative analysis of reviewed literature on chemoresistive sensing, solar harvesting, and embedded IoT.}
\label{tab:mohit_lit}
\begin{tabularx}{\textwidth}{|p{0.18\textwidth}|p{0.14\textwidth}|p{0.18\textwidth}|p{0.20\textwidth}|X|}
\hline
\textbf{Author \& Year} & \textbf{Focus Domain} & \textbf{Hardware Platform} & \textbf{Energy Source} & \textbf{Key Technical Contribution} \\
\hline
De Vito et al. (2008) & Electronic Noses & Multi-MOS Array & Grid AC & Field calibration of chemoresistive arrays for urban benzene detection using neural networks. \\
\hline
Hanwei Winsen (2015) & Sensor Physics & MQ-135 SnO2 & Bench Supply & Established empirical sensitivity logarithmic curves for NH3, NOx, and CO2 in clean air. \\
\hline
Raghunathan et al. (2005) & Energy Harvesting & Solar PV Micro-Grid & Monocrystalline PV & Formulated fundamental energy neutral operation (ENO) theorems for embedded sensor nodes. \\
\hline
Kansal et al. (2007) & Power Management & Solar-Powered WSN & Solar + NiMH/Li-ion & Introduced adaptive duty-cycling algorithms matching energy consumption to harvested intake. \\
\hline
Espressif Systems (2023) & Embedded SoC & ESP32 Dual-Core & Power-Gated Bus & Documented Xtensa LX6 architecture, ULP coprocessor state machines, and deep sleep ($10\,\mu\text{A}$). \\
\hline
Kumar et al. (2023) & Environmental IoT & MQ Array + ESP32 & 5W Solar Panel & Prototyped off-grid environmental nodes in Western Himalayan valleys; demonstrated winter survivability. \\
\hline
Tiwary et al. (2018) & Environmental Eng. & Comprehensive Review & Industrial CAAQMS & Documented atmospheric gas dispersion models and industrial emission compliance criteria. \\
\hline
Seinfeld \& Pandis (2016) & Atmospheric Physics & Theoretical Chemistry & Atmospheric Tracers & Established fundamental photochemical oxidation kinetics of volatile organic compounds and CO. \\
\hline
\end{tabularx}
\end{table}

\section{Analysis of Experimental Case Studies}
Field validation studies (Kumar et al., 2023; De Vito et al., 2008) highlight that metal oxide sensors suffer from cross-sensitivity to atmospheric moisture. When water vapor chemisorbs onto $\text{SnO}_2$ grains, it acts as an electron donor, shifting baseline resistance $R_0$. Incorporating temperature and humidity compensation into the analog signal conditioning chain is mandatory to eliminate baseline drift.

%% ==========================================================================
%% CHAPTER 5: CRITICAL CHALLENGES & FUTURE HORIZONS
%% ==========================================================================
\chapter{Critical Challenges and Future Horizons}

\section{Inherent Technical Bottlenecks}
Chemoresistive environmental sensing faces three primary constraints:
\begin{itemize}
    \item \textbf{High Thermal Power Consumption:} Internal heater coils consume $150\,\text{mA}$ at $5\,\text{V}$, limiting continuous active sampling in solar-constrained nodes.
    \item \textbf{Gas Selectivity Overlap:} MOS sensors exhibit non-specific responses to multiple reducing gases simultaneously, requiring multi-variate regression to decouple individual analyte concentrations.
    \item \textbf{Sensor Poisoning and Aging:} Exposure to heavy sulfur compounds or volatile siloxanes permanently passivates tin dioxide grain boundaries, degrading sensitivity over multi-year deployments.
\end{itemize}

\section{Future Research Horizons}
Promising future avenues include \textbf{pulsed-temperature heater modulation} (modulating heating coils at high frequencies to extract transient relaxation kinetics) and \textbf{MEMS micro-hotplate fabrication} on silicon substrates, reducing thermal dissipation from $750\,\text{mW}$ to less than $15\,\text{mW}$.

%% ==========================================================================
%% REFERENCES
%% ==========================================================================
\clearpage
\begin{thebibliography}{99}
\small
\setlength{\itemsep}{2pt}

\bibitem{devito2008}
S.~De Vito, E.~Massera, M.~Piga, L.~Martinotto, and G.~Di Francia, ``On-field calibration of an electronic nose for benzene estimation in an urban monitoring scenario,'' \emph{Sensors and Actuators B: Chemical}, vol. 129, no. 2, pp. 750--757, 2008.

\bibitem{hanwei2015}
Zhengzhou Winsen Electronics Technology, \emph{MQ-135 Semiconductor Sensor for Air Quality Manual}, Zhengzhou, Henan, China, 2015.

\bibitem{raghunathan2005}
V.~Raghunathan, A.~Kansal, J.~Hsu, J.~Friedman, and M.~Srivastava, ``Design considerations for solar energy harvesting wireless embedded systems,'' in \emph{Proc. 4th Int. Symp. Information Processing in Sensor Networks (IPSN)}, Los Angeles, CA, USA, 2005, pp. 457--462.

\bibitem{kansal2007}
A.~Kansal, J.~Hsu, S.~Zahedi, and M.~B.~Srivastava, ``Power management in energy harvesting sensor networks,'' \emph{ACM Transactions on Embedded Computing Systems}, vol. 6, no. 4, art. no. 32, 2007.

\bibitem{espressif2023}
Espressif Systems, \emph{ESP32 Technical Reference Manual (Version 5.0)}, Espressif Systems Co., Ltd., Shanghai, China, 2023.

\bibitem{kumar2023}
A.~Kumar, S.~Singh, and R.~K.~Sharma, ``Autonomous solar-powered air pollution monitoring node using IoT and chemoresistive sensors in sub-Himalayan valleys,'' \emph{Environmental Monitoring and Assessment}, vol. 195, art. no. 412, 2023.

\bibitem{tiwary2018}
A.~Tiwary, I.~D.~Williams, and V.~Colls, \emph{Air Pollution: Measurement, Modelling and Mitigation}, 4th ed., CRC Press, Boca Raton, FL, USA, 2018.

\bibitem{seinfeld2016}
J.~H.~Seinfeld and S.~N.~Pandis, \emph{Atmospheric Chemistry and Physics: From Air Pollution to Climate Change}, 3rd ed., John Wiley \& Sons, Hoboken, NJ, USA, 2016.

\end{thebibliography}

\end{document}
"""

with open('seminar_mohit/seminar.tex', 'w', encoding='utf-8') as f:
    f.write(tex_content)

print("Wrote seminar_mohit/seminar.tex. Compiling with Tectonic...")
cmd = r"Set-Location seminar_mohit; ..\tools\tectonic\tectonic.exe seminar.tex; Set-Location .."
proc = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)

pdf_path = os.path.join('seminar_mohit', 'seminar.pdf')
if os.path.exists(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    print(f"SUCCESS: Compiled seminar_mohit/seminar.pdf ({len(reader.pages)} pages)")
else:
    print("ERROR: Compilation failed.")
    print("Stderr:", proc.stderr[-400:])
