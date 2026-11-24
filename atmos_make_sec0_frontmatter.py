# atmos_make_sec0_frontmatter.py

def get_frontmatter():
    return r"""%% ==========================================================================
%%  MAJOR PROJECT REPORT (ECEEE-611P)
%%  Electronics & Communication Engineering Dept., JNGEC Sundernagar
%%  Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur
%%
%%  Project: SOLAR-POWERED HYPERLOCAL AQI MONITORING AND AI-BASED TREND PREDICTION
%%  Authors: Akshit (23010104009), Mohit Negi (23010104043),
%%           Swapnil Sehgal (23010104064), Vansh Thakur (23010104070)
%% ==========================================================================

\documentclass[12pt,a4paper,oneside]{report}

%% ---------- Standard Packages (HPTU & JNGEC Guidelines) -------------------
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage{mathptmx}                 % Times New Roman font
\usepackage[left=1.4in,top=1.0in,right=1.0in,bottom=1.0in,headheight=15pt]{geometry} % Margins
\usepackage{setspace}
\usepackage{titlesec}
\usepackage[titles]{tocloft}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{longtable,tabularx,array,booktabs,multirow}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage[hidelinks]{hyperref}
\usepackage{listings}
\usepackage{ragged2e}
\usepackage{float}
\usepackage{microtype}
\usepackage{enumitem}

\graphicspath{{figures/}{./}}

%% ---------- Float and Page Optimization Parameters ------------------------
\renewcommand{\topfraction}{0.92}
\renewcommand{\bottomfraction}{0.92}
\renewcommand{\textfraction}{0.08}
\renewcommand{\floatpagefraction}{0.88}
\setlength{\floatsep}{6pt plus 2pt minus 2pt}
\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
\setlength{\intextsep}{6pt plus 2pt minus 2pt}

%% ---------- Project Details -----------------------------------------------
\newcommand{\ProjectTitle}{SOLAR-POWERED HYPERLOCAL AQI MONITORING AND AI-BASED TREND PREDICTION}
\newcommand{\ProjectTitleShort}{Solar-Powered Hyperlocal AQI Monitoring}
\newcommand{\CourseCode}{ECEEE-611P}
\newcommand{\SupervisorName}{Er. Nitasha Bisht}
\newcommand{\CoordinatorName}{Er. Akshay Kanwar}
\newcommand{\HODName}{Dr. Ajeet Thakur}
\newcommand{\DeptName}{Department of Electronics and Communication Engineering}
\newcommand{\CollegeName}{Jawaharlal Nehru Government Engineering College Sundernagar}
\newcommand{\UnivName}{Himachal Pradesh Technical University, Hamirpur}
\newcommand{\ReportDate}{MAY, 2026}

%% ---------- Typography & Formatting Standards -----------------------------
\setstretch{1.12}                     % 1.12 line spacing for crisp fitting
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt plus 1pt minus 1pt}

%% Chapter Headings (14pt Bold Centered)
\titleformat{\chapter}[block]
  {\centering\bfseries\fontsize{14pt}{17pt}\selectfont}
  {Chapter \thechapter:}{0.5em}{}

\titleformat{name=\chapter,numberless}[block]
  {\centering\bfseries\fontsize{14pt}{17pt}\selectfont}
  {}{0pt}{\underline}

\titlespacing*{\chapter}{0pt}{0pt}{12pt}

%% Section Headings (13pt Bold Left)
\titleformat{\section}[hang]
  {\raggedright\bfseries\fontsize{13pt}{16pt}\selectfont}
  {\thesection}{0.6em}{}
\titlespacing*{\section}{0pt}{8pt}{3pt}

%% Subsection Headings (12pt Bold Left)
\titleformat{\subsection}[hang]
  {\raggedright\bfseries\fontsize{12pt}{15pt}\selectfont}
  {\thesubsection}{0.6em}{}
\titlespacing*{\subsection}{0pt}{6pt}{2pt}

%% Subsubsection Headings (11pt Bold Left)
\titleformat{\subsubsection}[hang]
  {\raggedright\bfseries\fontsize{11pt}{14pt}\selectfont}
  {\thesubsubsection}{0.6em}{}
\titlespacing*{\subsubsection}{0pt}{5pt}{2pt}

%% Captions
\captionsetup{font=small,labelfont=bf,labelsep=colon,skip=3pt}

%% Table of Contents Styling (TOC depth 2 to keep TOC clean)
\renewcommand{\contentsname}{TABLE OF CONTENTS}
\renewcommand{\listfigurename}{LIST OF FIGURES}
\renewcommand{\listtablename}{LIST OF TABLES}
\renewcommand{\cftchappresnum}{Chapter~}
\renewcommand{\cftchapaftersnum}{:}
\setlength{\cftchapnumwidth}{6.2em}
\renewcommand{\cftchapfont}{\normalfont}
\renewcommand{\cftchappagefont}{\normalfont}
\renewcommand{\cftchapleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftchapdotsep}{\cftdotsep}
\setlength{\cftbeforechapskip}{1.5pt}
\setlength{\cftbeforesecskip}{0.5pt}
\setlength{\cftbeforesubsecskip}{0pt}
\setlength{\cftbeforefigskip}{0.5pt}
\setlength{\cftbeforetabskip}{0.5pt}
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{3}

%% Running Header & Footer
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}

%% Code Listing Configuration
\lstset{
  basicstyle=\ttfamily\scriptsize,
  breaklines=true,
  frame=single,
  numbers=left,
  numberstyle=\tiny\color{gray},
  keywordstyle=\color{blue}\bfseries,
  commentstyle=\color{teal}\itshape,
  stringstyle=\color{purple},
  backgroundcolor=\color{gray!5},
  showspaces=false,
  showstringspaces=false
}

\begin{document}

%% ==========================================================================
%%  1. COVER PAGE (STRICTLY 1 PAGE)
%% ==========================================================================
\begin{titlepage}
\thispagestyle{empty}
\begin{center}
\vspace*{-0.5cm}
{\fontsize{15pt}{18pt}\bfseries \ProjectTitle \par}
\vspace{0.4cm}
{\fontsize{12pt}{15pt}\bfseries A PROJECT REPORT ON \par}
{\fontsize{11pt}{14pt}\bfseries PROJECT (\CourseCode) \par}
\vspace{0.2cm}
{\fontsize{10.5pt}{13.5pt}\itshape Submitted in partial fulfillment of the requirements for the award of the degree of \par}
\vspace{0.2cm}
{\fontsize{13pt}{16pt}\bfseries BACHELOR OF TECHNOLOGY \par}
{\fontsize{11pt}{14pt}\bfseries in \par}
{\fontsize{12pt}{15pt}\bfseries ELECTRONICS AND COMMUNICATION ENGINEERING \par}
\vspace{0.3cm}
\begin{figure}[H]
\centering
\includegraphics[width=2.5cm]{jngec_logo.png}
\end{figure}
\vspace{-0.3cm}
{\fontsize{10.5pt}{13pt}\bfseries SUBMITTED BY: \par}
\vspace{0.1cm}
\begin{table}[H]
\centering
\footnotesize
\begin{tabular}{llr}
\textbf{AKSHIT} & & \textbf{University Roll No.: 23010104009} \\
\textbf{MOHIT NEGI} & & \textbf{University Roll No.: 23010104043} \\
\textbf{SWAPNIL SEHGAL} & & \textbf{University Roll No.: 23010104064} \\
\textbf{VANSH THAKUR} & & \textbf{University Roll No.: 23010104070} \\
\end{tabular}
\end{table}

\vspace{-0.2cm}
\begin{table}[H]
\centering
\footnotesize
\begin{tabular}{p{0.48\textwidth}p{0.48\textwidth}}
\textbf{Under the Supervision of:} & \textbf{Project Coordinator:} \\
\textbf{\SupervisorName} & \textbf{\CoordinatorName} \\
Assistant Professor, Dept. of ECE & Assistant Professor, Dept. of ECE \\
\end{tabular}
\end{table}

\vspace{0.1cm}
{\fontsize{10pt}{13pt}\bfseries \DeptName \par}
{\fontsize{11pt}{14pt}\bfseries \CollegeName \par}
{\fontsize{10pt}{13pt} Sundernagar, District Mandi (H.P.) -- 175018 \par}
{\fontsize{9pt}{12pt} (Affiliated to \UnivName) \par}
\vspace{0.1cm}
{\fontsize{10.5pt}{13pt}\bfseries \ReportDate \par}
\end{center}
\end{titlepage}

\pagenumbering{roman}
\setcounter{page}{2}

%% ==========================================================================
%%  2. SUPERVISOR'S CERTIFICATE (STRICTLY 1 PAGE)
%% ==========================================================================
\thispagestyle{plain}
\begin{center}
{\fontsize{12pt}{15pt}\bfseries \CollegeName \par}
{\fontsize{11pt}{14pt}\bfseries \DeptName \par}
Sundernagar, District Mandi, Himachal Pradesh -- 175018
\vspace{0.5cm}

{\fontsize{14pt}{17pt}\bfseries \underline{CERTIFICATE} \par}
\end{center}
\vspace{0.4cm}

This is to certify that the project report entitled \textbf{``\ProjectTitle''} is a bonafide record of the authentic work carried out by:
\begin{center}
\small
\begin{tabular}{ll}
\textbf{Akshit} & (University Roll No.: 23010104009) \\
\textbf{Mohit Negi} & (University Roll No.: 23010104043) \\
\textbf{Swapnil Sehgal} & (University Roll No.: 23010104064) \\
\textbf{Vansh Thakur} & (University Roll No.: 23010104070) \\
\end{tabular}
\end{center}

under my supervision and guidance in the \DeptName, \CollegeName, Sundernagar, in partial fulfillment of the requirements for the award of the degree of \textbf{Bachelor of Technology in Electronics and Communication Engineering} affiliated to \UnivName, during the academic period January 2025 to May 2026.

The results embodied in this report have not been submitted to any other Institute or University for the award of any degree or diploma.

\vspace{1.2cm}
\noindent
\begin{tabular}{p{0.48\textwidth}p{0.48\textwidth}}
\textbf{Signature of Supervisor / Mentor} & \textbf{Signature of Head of Department} \\
\textbf{\SupervisorName} & \textbf{\HODName} \\
Assistant Professor, Dept. of ECE & Professor \& Head, Dept. of ECE \\
JNGEC Sundernagar & JNGEC Sundernagar \\
Date: \rule{3cm}{0.4pt} & Date: \rule{3cm}{0.4pt} \\
\end{tabular}

\vspace{1.0cm}
\noindent
\begin{tabular}{p{0.48\textwidth}p{0.48\textwidth}}
\textbf{Project Coordinator} & \textbf{External Examiner} \\
\textbf{\CoordinatorName} & \\
Assistant Professor, Dept. of ECE & Signature: \rule{4cm}{0.4pt} \\
JNGEC Sundernagar & Name: \rule{4.5cm}{0.4pt} \\
Date: \rule{3cm}{0.4pt} & Date: \rule{3cm}{0.4pt} \\
\end{tabular}

\newpage

%% ==========================================================================
%%  3. CANDIDATE'S DECLARATION (STRICTLY 1 PAGE)
%% ==========================================================================
\thispagestyle{plain}
\begin{center}
{\fontsize{14pt}{17pt}\bfseries \underline{CANDIDATE'S DECLARATION} \par}
\end{center}
\vspace{0.5cm}

We hereby declare that the work presented in this project report entitled \textbf{``\ProjectTitle''} submitted to the \DeptName, \CollegeName, Sundernagar, affiliated to \UnivName, in partial fulfillment of the requirements for the degree of \textbf{Bachelor of Technology in Electronics and Communication Engineering}, is an authentic record of our own research and experimental work carried out under the supervision of \textbf{\SupervisorName}, Assistant Professor, Department of ECE.

We further confirm that:
\begin{enumerate}[label=(\alph*),leftmargin=2em,itemsep=2pt]
    \item The matter contained in this report has not been submitted by us for the award of any other degree, diploma, or certificate in this or any other university or institute.
    \item All hardware designs, embedded code, machine learning pipelines, cloud services, and experimental results described herein represent our collaborative engineering work, except where explicitly referenced and credited to prior published literature.
    \item Proper citations and references have been provided in standard IEEE academic style for all external literature, datasets, APIs, and libraries utilized during this project.
    \item We accept full institutional responsibility for the integrity and academic authenticity of the data and findings reported in this document.
\end{enumerate}

\vspace{1.2cm}
\noindent
\begin{tabular}{p{0.48\textwidth}p{0.48\textwidth}}
\textbf{Akshit} & \textbf{Mohit Negi} \\
University Roll No.: 23010104009 & University Roll No.: 23010104043 \\
Signature: \rule{3.8cm}{0.4pt} & Signature: \rule{3.8cm}{0.4pt} \\
\vspace{0.6cm} & \vspace{0.6cm} \\
\textbf{Swapnil Sehgal} & \textbf{Vansh Thakur} \\
University Roll No.: 23010104064 & University Roll No.: 23010104070 \\
Signature: \rule{3.8cm}{0.4pt} & Signature: \rule{3.8cm}{0.4pt} \\
\end{tabular}

\vspace{0.8cm}
\noindent
Date: \rule{3.5cm}{0.4pt} \hfill Place: Sundernagar (Mandi), H.P.

\newpage

%% ==========================================================================
%%  4. ACKNOWLEDGEMENTS (STRICTLY 1 PAGE)
%% ==========================================================================
\thispagestyle{plain}
\begin{center}
{\fontsize{14pt}{17pt}\bfseries \underline{ACKNOWLEDGEMENTS} \par}
\end{center}
\vspace{0.4cm}

It is our privilege to express our sincere regards to our project mentor, \textbf{\SupervisorName}, Assistant Professor, Department of Electronics and Communication Engineering, for her valuable inputs, able guidance, encouragement, whole-hearted cooperation, and constructive critiques throughout the duration of our project. Her profound insights into embedded system design, signal acquisition, and sensor calibration frameworks served as an indispensable guiding light during challenging phases of hardware debugging and machine learning model validation.

We convey our gratitude to \textbf{\CoordinatorName}, Assistant Professor and Project Coordinator, for his support, structural feedback, administrative assistance, and constructive evaluation sessions during project milestone assessments.

We deeply express our sincere thanks to our Head of Department, \textbf{\HODName}, for encouraging and allowing us to present this project on \textbf{``\ProjectTitle''} at our department, and for providing the necessary laboratory resources and technical infrastructure.

The success and final outcome of this project required a lot of guidance and assistance from many people, and we are extremely fortunate to have got this all during our project. We take this opportunity to thank all our faculty members, laboratory staff, and peers who have directly or indirectly assisted us.

Finally, we pay our respects and love to our parents and friends for their love, patience, and encouragement throughout this work.

\vspace{0.8cm}
\noindent
\textbf{Akshit} (23010104009) \hfill \textbf{Mohit Negi} (23010104043) \\
\textbf{Swapnil Sehgal} (23010104064) \hfill \textbf{Vansh Thakur} (23010104070)

\vspace{0.3cm}
\noindent
Department of Electronics and Communication Engineering \\
Jawaharlal Nehru Government Engineering College Sundernagar, Mandi (H.P.)

\newpage

%% ==========================================================================
%%  5. EVALUATION SHEET (STRICTLY 1 PAGE)
%% ==========================================================================
\thispagestyle{plain}
\begin{center}
{\fontsize{12pt}{15pt}\bfseries \CollegeName \par}
{\fontsize{11pt}{14pt}\bfseries \DeptName \par}
\vspace{0.2cm}
{\fontsize{13pt}{16pt}\bfseries \underline{PROJECT EVALUATION SHEET} \par}
{\fontsize{10.5pt}{13.5pt}\bfseries Project Course Code: \CourseCode \par}
\end{center}
\vspace{0.2cm}

\noindent
\small
\textbf{Project Title:} \ProjectTitle \\
\textbf{Academic Session:} 2025 -- 2026 \hfill \textbf{Semester:} B.Tech ECE 6th / 8th Semester

\vspace{0.1cm}
\begin{table}[H]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{|c|X|c|c|c|}
\hline
\textbf{S.No.} & \textbf{Evaluation Criteria / Parameter} & \textbf{Max} & \textbf{Internal} & \textbf{External} \\
\hline
1 & Novelty, Literature Survey \& Problem Formulation & 15 & & \\
\hline
2 & System Architecture, Hardware Design \& Prototyping & 25 & & \\
\hline
3 & Embedded Firmware, IoT Cloud Backend \& Web Dashboard & 20 & & \\
\hline
4 & Data Curation, Sensor Calibration \& Machine Learning & 20 & & \\
\hline
5 & Quality of Results, Comparative Analysis \& Practical Impact & 10 & & \\
\hline
6 & Technical Documentation, Report Quality \& Viva-Voce & 10 & & \\
\hline
\multicolumn{2}{|r|}{\textbf{Total Marks}} & \textbf{100} & & \\
\hline
\end{tabularx}
\end{table}

\vspace{-0.2cm}
\begin{table}[H]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{|c|l|c|c|c|c|}
\hline
\textbf{S.No.} & \textbf{Candidate Name} & \textbf{Roll Number} & \textbf{Internal (50)} & \textbf{External (50)} & \textbf{Total (100)} \\
\hline
1 & Akshit & 23010104009 & & & \\
\hline
2 & Mohit Negi & 23010104043 & & & \\
\hline
3 & Swapnil Sehgal & 23010104064 & & & \\
\hline
4 & Vansh Thakur & 23010104070 & & & \\
\hline
\end{tabularx}
\end{table}

\vspace{-0.1cm}
\noindent
\footnotesize
\textbf{Remarks:} \hrulefill \\[4pt]
\hrulefill

\vspace{0.6cm}
\noindent
\begin{tabular}{p{0.31\textwidth}p{0.31\textwidth}p{0.31\textwidth}}
\textbf{Supervisor} & \textbf{Coordinator} & \textbf{External Examiner} \\
(\SupervisorName) & (\CoordinatorName) & Signature: \rule{2.2cm}{0.4pt} \\
Date: \rule{2.2cm}{0.4pt} & Date: \rule{2.2cm}{0.4pt} & Date: \rule{2.2cm}{0.4pt} \\
\end{tabular}

\newpage

%% ==========================================================================
%%  6. ABSTRACT (STRICTLY 1 PAGE)
%% ==========================================================================
\thispagestyle{plain}
\begin{center}
{\fontsize{14pt}{17pt}\bfseries \underline{ABSTRACT} \par}
\end{center}
\vspace{0.3cm}

{\small
Air pollution constitutes one of the most critical environmental challenges of the modern era, posing severe risks to cardiopulmonary health worldwide. While centralized regulatory Continuous Ambient Air Quality Monitoring Stations (CAAQMS) provide high-precision measurements utilizing gold-standard Beta Attenuation Monitors (BAM-1020), their prohibitive capital and operational expenditures result in sparse spatial coverage, obscuring localized pollution micro-zones caused by complex valley topography and vehicular traffic.

To address these limitations, this project presents \textbf{ATMOS}, an end-to-end, solar-powered, energy-autonomous IoT environmental monitoring node coupled with a two-stage machine learning predictive analytics engine. The physical edge hardware integrates an Espressif ESP32 dual-core microcontroller with a precision laser particulate sensor (Plantower PMS5003), a multi-gas chemoresistive sensor array (MQ-135, MQ-7, MQ-4), a digital temperature and humidity sensor (DHT22), and an SSD1306 OLED display. The node is powered off-grid through an autonomous photovoltaic energy-harvesting subsystem comprising a 6V/2W monocrystalline solar panel, a TP4056 lithium-ion charge controller, and a dual 18650 Li-ion battery pack ($4400\,\text{mAh}$). Analytical energy budgeting under Sundernagar solar irradiance ($4.8\,\text{kWh/m}^2/\text{day}$) demonstrates that cyclical FreeRTOS deep-sleep scheduling reduces average current draw to $2.76\,\text{mA}$, ensuring over **53 days of zero-sunlight off-grid operational autonomy**.

Data telemetry is managed via asynchronous FreeRTOS firmware transmitting JSON payloads to a scalable Python Flask REST cloud backend hosted on Render, which orchestrates live Central Pollution Control Board (CPCB) National Air Quality Index (NAQI) sub-index computation, Leaflet GIS spatial mapping, dynamic Chart.js time-series visualizations, and automated SMTP threshold warning alerts.

To resolve the inherent vulnerability of low-cost optical particle counters to hygroscopic particle swelling and sensor drift, we implement a physics-informed two-stage machine learning architecture validated on a co-located regulatory dataset comprising \textbf{15,755 continuous hourly records} spanning July 2018 to January 2021. In \textbf{Stage 1 (Sensor Calibration)}, ambient temperature, relative humidity, and raw optical particle readings are mapped against regulatory BAM ground truth using Hänel deliquescence corrections. Multivariate Linear Regression demonstrates superior validation generalization ($\text{RMSE} = 12.46\,\mu\text{g/m}^3$, $\text{MAE} = 10.24\,\mu\text{g/m}^3$, $R^2 = 0.178$) compared to non-linear Random Forest ($\text{RMSE} = 13.72\,\mu\text{g/m}^3$, $R^2 = 0.004$), proving that lower-capacity regularized models mitigate overfitting on noisy field drift. In \textbf{Stage 2 (Temporal Forecasting)}, a 24-hour lag matrix with cyclical harmonic hour encoding is evaluated for 1-hour-ahead $\text{PM}_{2.5}$ forecasting on the unobserved test subset. While the Persistence baseline remains a formidable near-term benchmark ($\text{RMSE} = 14.28\,\mu\text{g/m}^3$, $R^2 = 0.902$), \textbf{Model B (Calibrated Input RF)} achieves $\text{RMSE} = 19.34\,\mu\text{g/m}^3$ and $R^2 = 0.820$, delivering a \textbf{15.3\% error reduction} over \textbf{Model A (Raw Input RF)} ($\text{RMSE} = 22.84\,\mu\text{g/m}^3$, $R^2 = 0.748$). Multi-horizon evaluation confirms that Model B dominates persistence beyond two hours, establishing ATMOS as a scientifically rigorous, field-validated solution for public health protection.
\par}

\newpage

%% ==========================================================================
%%  7. TABLE OF CONTENTS, LIST OF FIGURES, LIST OF TABLES, ABBREVIATIONS
%% ==========================================================================
\tableofcontents
\newpage

\listoffigures
\newpage

\listoftables
\newpage

%% List of Abbreviations & Nomenclature (STRICTLY 1 PAGE)
\thispagestyle{plain}
\begin{center}
{\fontsize{13pt}{16pt}\bfseries \underline{LIST OF ABBREVIATIONS AND NOMENCLATURE} \par}
\end{center}
\vspace{0.3cm}

\begin{table}[H]
\centering
\scriptsize
\begin{tabularx}{\textwidth}{p{0.20\textwidth}X}
\toprule
\textbf{Abbreviation} & \textbf{Full Definition / Expansion} \\
\midrule
\textbf{ADC} & Analog-to-Digital Converter \\
\textbf{AI} & Artificial Intelligence \\
\textbf{API} & Application Programming Interface \\
\textbf{AQI} & Air Quality Index \\
\textbf{BAM} & Beta Attenuation Monitor (Regulatory Reference Instrument, e.g., BAM-1020) \\
\textbf{BOM} & Bill of Materials \\
\textbf{CAAQMS} & Continuous Ambient Air Quality Monitoring Station \\
\textbf{CPCB} & Central Pollution Control Board (Government of India) \\
\textbf{CSV} & Comma-Separated Values \\
\textbf{DHT} & Digital Humidity and Temperature Sensor \\
\textbf{EPA} & Environmental Protection Agency (United States) \\
\textbf{ESP32} & Espressif 32-bit Dual-Core Tensilica Xtensa LX6 Microcontroller \\
\textbf{FreeRTOS} & Free Real-Time Operating System \\
\textbf{GIS} & Geographic Information System \\
\textbf{GPIO} & General Purpose Input/Output \\
\textbf{GUI} & Graphical User Interface \\
\textbf{HPTU} & Himachal Pradesh Technical University, Hamirpur \\
\textbf{HTTP / HTTPS} & Hypertext Transfer Protocol / Secure \\
\textbf{I2C} & Inter-Integrated Circuit Serial Bus \\
\textbf{IoT} & Internet of Things \\
\textbf{JNGEC} & Jawaharlal Nehru Government Engineering College, Sundernagar \\
\textbf{JSON} & JavaScript Object Notation \\
\textbf{Li-ion} & Lithium-Ion Rechargeable Electrochemical Cell \\
\textbf{MAE} & Mean Absolute Error \\
\textbf{ML} & Machine Learning \\
\textbf{NAQI} & National Air Quality Index (India) \\
\textbf{OLED} & Organic Light Emitting Diode \\
\textbf{OLS} & Ordinary Least Squares Regression \\
\textbf{OPC} & Optical Particle Counter \\
\textbf{PM2.5 / PM10} & Particulate Matter with Aerodynamic Diameter $\le 2.5\,\mu\text{m}$ / $\le 10\,\mu\text{m}$ \\
\textbf{REST} & Representational State Transfer \\
\textbf{RF} & Random Forest Regressor \\
\textbf{RH} & Relative Humidity (\%) \\
\textbf{RMSE} & Root Mean Square Error \\
\textbf{RTC} & Real-Time Clock \\
\textbf{SOC} & State of Charge (Battery percentage) \\
\textbf{TEOM} & Tapered Element Oscillating Microbalance \\
\textbf{TinyML} & Tiny Machine Learning for Low-Power Microcontrollers \\
\textbf{UART} & Universal Asynchronous Receiver-Transmitter \\
\textbf{VOC} & Volatile Organic Compounds \\
\textbf{WHO} & World Health Organization \\
\bottomrule
\end{tabularx}
\end{table}

\newpage
\pagenumbering{arabic}
\setcounter{page}{1}
"""
