# generate_dev_master.py
# Constructs the complete, flawless, perfectly fitted 82-84 page LaTeX source for Dev's report.

import os

tex_content = r"""%% ==========================================================================
%%  INTERNSHIP REPORT
%%  Electronics & Communication Engineering Dept., JNGEC Sundernagar
%%  Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur
%%
%%  Student: Jyotiraditya Singh (University Roll No. 23010104035)
%%  Project: SELF BALANCING ROBOT USING IOT
%%  Host:    CLOUD EDUCATION LEARNING PVT. LTD. (AI-B08 Centre, Jawalaji)
%% ==========================================================================

\documentclass[12pt,a4paper,oneside]{report}

%% ---------- Standard Packages (HPTU & JNGEC Guidelines) -------------------
\usepackage[T1]{fontenc}
\usepackage{mathptmx}                 % Times New Roman font (Sec. A, #5)
\usepackage[left=1.4in,top=1.2in,right=1.0in,bottom=1.0in,headheight=16pt]{geometry} % Margins (Sec. A, #7)
\usepackage{setspace}
\usepackage{titlesec}
\usepackage[titles]{tocloft}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{amsmath,amssymb}
\usepackage{longtable,tabularx,array,booktabs,multirow}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage{pdfpages}
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
\setlength{\floatsep}{8pt plus 2pt minus 2pt}
\setlength{\textfloatsep}{10pt plus 2pt minus 2pt}
\setlength{\intextsep}{8pt plus 2pt minus 2pt}

%% ---------- Project Details -----------------------------------------------
\newcommand{\ProjectTitle}{SELF BALANCING ROBOT USING IOT}
\newcommand{\OrgName}{CLOUD EDUCATION LEARNING PVT. LTD.}
\newcommand{\StudentName}{Jyotiraditya Singh}
\newcommand{\RollNo}{23010104035}
\newcommand{\TrainingFrom}{20/06/2026}
\newcommand{\TrainingTo}{03/08/2026}
\newcommand{\SupervisorName}{Dr. Sanjeev Kumar, Assistant Professor}
\newcommand{\ReportDate}{03/08/2026}

%% ---------- Typography & Formatting Standards -----------------------------
\setstretch{1.15}                     % 1.15 line spacing (Sec. A, #6)
\setlength{\parindent}{0pt}
\setlength{\parskip}{8pt plus 1pt minus 1pt}

%% Chapter Headings (14pt Bold Centered)
\titleformat{\chapter}[block]
  {\centering\bfseries\fontsize{14pt}{17pt}\selectfont}
  {Chapter \thechapter:}{0.5em}{}

\titleformat{name=\chapter,numberless}[block]
  {\centering\bfseries\fontsize{14pt}{17pt}\selectfont}
  {}{0pt}{\underline}

\titlespacing*{\chapter}{0pt}{0pt}{14pt}

%% Section Headings (14pt Bold Left)
\titleformat{\section}[hang]
  {\raggedright\bfseries\fontsize{14pt}{17pt}\selectfont}
  {\thesection}{0.6em}{}
\titlespacing*{\section}{0pt}{10pt}{4pt}

%% Subsection Headings (12pt Bold Left)
\titleformat{\subsection}[hang]
  {\raggedright\bfseries\fontsize{12pt}{15pt}\selectfont}
  {\thesubsection}{0.6em}{}
\titlespacing*{\subsection}{0pt}{8pt}{3pt}

%% Subsubsection Headings (12pt Bold Left)
\titleformat{\subsubsection}[hang]
  {\raggedright\bfseries\fontsize{12pt}{15pt}\selectfont}
  {\thesubsubsection}{0.6em}{}
\titlespacing*{\subsubsection}{0pt}{6pt}{2pt}

%% Captions
\captionsetup{font=small,labelfont=bf,labelsep=colon,skip=4pt}

%% Table of Contents Styling
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
\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{3}

%% Running Header & Footer
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}

%% Code Listing Formatting
\definecolor{codebg}{rgb}{0.97,0.97,0.97}
\definecolor{codeblue}{rgb}{0.1,0.2,0.7}
\definecolor{codegreen}{rgb}{0.1,0.5,0.2}
\definecolor{codegray}{rgb}{0.4,0.4,0.4}

\lstset{
  language=C++,
  backgroundcolor=\color{codebg},
  basicstyle=\ttfamily\scriptsize,
  keywordstyle=\color{codeblue}\bfseries,
  commentstyle=\color{codegreen}\itshape,
  stringstyle=\color[rgb]{0.7,0.2,0.1},
  numbers=left,
  numberstyle=\tiny\color{codegray},
  numbersep=5pt,
  breaklines=true,
  breakatwhitespace=false,
  showstringspaces=false,
  frame=single,
  captionpos=b,
  tabsize=2
}

%% Helper Macros
\newcommand{\CollegeLogo}[1]{%
  \IfFileExists{figures/jngec_logo.png}{\includegraphics[height=#1]{figures/jngec_logo.png}}%
  {\IfFileExists{figures/logo.png}{\includegraphics[height=#1]{figures/logo.png}}%
  {\fbox{\parbox{3cm}{\centering\small College Logo}}}}%
}

\newcommand{\frontchapter}[1]{%
  \chapter*{#1}%
  \addcontentsline{toc}{chapter}{#1}%
}

\newcommand{\DeptLetterhead}{%
  \begin{center}\normalsize\bfseries\singlespacing
    Electronics \& Communication Engineering Department\\
    Jawaharlal Nehru Govt. Engineering College,\\
    Sundernagar, Mandi (H.P.)\\
    Phone No. 01907-267199, 267688, Fax No. 267811\\
    Web site: http://www.jngec.ac.in, Email: jngechp@yahoo.co.in
  \end{center}
  \vspace{-0.2cm}\hrule\vspace{0.4cm}
}

%% ---------- TOC Spacing Optimization --------------------------------------
\setlength{\cftbeforechapskip}{4.5pt}
\setlength{\cftbeforesecskip}{1.2pt}
\setlength{\cftbeforesubsecskip}{0.8pt}

\begin{document}

%% ==========================================================================
%%  1. OUTER COVER PAGE (Strict HPTU/JNGEC Guidelines)
%% ==========================================================================
\thispagestyle{empty}
\begin{center}
  {\fontsize{16pt}{20pt}\bfseries\uppercase{INTERNSHIP REPORT}}\\[0.25cm]
  {\fontsize{13pt}{16pt}\selectfont ON}\\[0.25cm]
  {\fontsize{17pt}{21pt}\bfseries\uppercase{\ProjectTitle}}\\[0.4cm]

  {\fontsize{11pt}{14pt}\selectfont AT}\\[0.25cm]
  {\fontsize{14pt}{17pt}\bfseries\uppercase{\OrgName}}\\[0.15cm]
  {\fontsize{11pt}{13pt}\selectfont (Industrial Training Centre, Jawalaji, Kangra, H.P.)}\\[0.45cm]

  {\fontsize{11pt}{13pt}\selectfont\textit{Submitted in partial fulfillment of the requirements\\
  for the award of the degree of}}\\[0.25cm]
  {\fontsize{13pt}{16pt}\bfseries\uppercase{Bachelor of Technology}}\\[0.15cm]
  {\fontsize{11pt}{13pt}\selectfont in}\\[0.15cm]
  {\fontsize{13pt}{16pt}\bfseries\uppercase{Electronics \& Communication Engineering}}\\[0.45cm]

  \CollegeLogo{2.6cm}\\[0.45cm]

  \begin{minipage}{0.48\textwidth}
    \begin{flushleft}
      \fontsize{10.5pt}{13pt}\selectfont
      \textbf{Submitted to:}\\
      \textbf{Department of ECE}\\
      JNGEC Sundernagar
    \end{flushleft}
  \end{minipage}
  \hfill
  \begin{minipage}{0.48\textwidth}
    \begin{flushright}
      \fontsize{10.5pt}{13pt}\selectfont
      \textbf{Submitted by:}\\
      \textbf{\StudentName}\\
      University Roll No.: \textbf{\RollNo}\\
      Training: \TrainingFrom{} to \TrainingTo
    \end{flushright}
  \end{minipage}

  \vfill

  {\fontsize{12pt}{14pt}\bfseries\uppercase{Department of Electronics \& Communication Engineering}}\\[0.1cm]
  {\fontsize{12pt}{14pt}\bfseries\uppercase{Jawaharlal Nehru Govt. Engineering College}}\\[0.1cm]
  {\fontsize{10.5pt}{12pt}\selectfont Sundernagar, Dist. Mandi (H.P.) -- 175018}\\[0.1cm]
  {\fontsize{10pt}{12pt}\selectfont\textit{Affiliated to Himachal Pradesh Technical University, Hamirpur}}\\[0.2cm]
  {\fontsize{11pt}{13pt}\bfseries August 2026}
\end{center}

%% ==========================================================================
%%  2. INNER TITLE PAGE
%% ==========================================================================
\clearpage
\thispagestyle{empty}
\begin{center}
  {\fontsize{16pt}{20pt}\bfseries\uppercase{INTERNSHIP REPORT}}\\[0.25cm]
  {\fontsize{13pt}{16pt}\selectfont ON}\\[0.25cm]
  {\fontsize{17pt}{21pt}\bfseries\uppercase{\ProjectTitle}}\\[0.4cm]

  {\fontsize{11pt}{14pt}\selectfont AT}\\[0.25cm]
  {\fontsize{14pt}{17pt}\bfseries\uppercase{\OrgName}}\\[0.45cm]

  {\fontsize{11pt}{13pt}\selectfont\textit{Submitted in partial fulfillment of the requirements\\
  for the award of the degree of}}\\[0.25cm]
  {\fontsize{13pt}{16pt}\bfseries\uppercase{Bachelor of Technology}}\\[0.15cm]
  {\fontsize{11pt}{13pt}\selectfont in}\\[0.15cm]
  {\fontsize{13pt}{16pt}\bfseries\uppercase{Electronics \& Communication Engineering}}\\[0.45cm]

  \CollegeLogo{2.6cm}\\[0.45cm]

  \begin{minipage}{0.48\textwidth}
    \begin{flushleft}
      \fontsize{10.5pt}{13pt}\selectfont
      \textbf{Under Academic Guidance:}\\
      \textbf{\SupervisorName}\\
      Department of ECE, JNGEC
    \end{flushleft}
  \end{minipage}
  \hfill
  \begin{minipage}{0.48\textwidth}
    \begin{flushright}
      \fontsize{10.5pt}{13pt}\selectfont
      \textbf{Submitted by:}\\
      \textbf{\StudentName}\\
      University Roll No.: \textbf{\RollNo}\\
      7th Semester, B.Tech. ECE
    \end{flushright}
  \end{minipage}

  \vfill

  {\fontsize{12pt}{14pt}\bfseries\uppercase{Department of Electronics \& Communication Engineering}}\\[0.1cm]
  {\fontsize{12pt}{14pt}\bfseries\uppercase{Jawaharlal Nehru Govt. Engineering College}}\\[0.1cm]
  {\fontsize{10.5pt}{12pt}\selectfont Sundernagar, Dist. Mandi (H.P.) -- 175018}\\[0.1cm]
  {\fontsize{10pt}{12pt}\selectfont\textit{Affiliated to Himachal Pradesh Technical University, Hamirpur}}\\[0.2cm]
  {\fontsize{11pt}{13pt}\bfseries August 2026}
\end{center}

%% ==========================================================================
%%  3. PRELIMINARY PAGES (Numbered with Roman Numerals)
%% ==========================================================================
\clearpage
\pagenumbering{roman}
\setcounter{page}{2}

%% -------- Company Certificate ---------------------------------------------
\frontchapter{CERTIFICATE BY COMPANY/ORGANIZATION/INSTITUTE}

\begin{center}
  \textbf{\large CLOUD EDUCATION LEARNING PVT. LTD.}\\
  \textit{\small AI-B08 Centre, Industrial Training Division, Jawalaji, Kangra, H.P. -- 176031}\\
  \textit{\small Web: www.cloudeducationlearning.com | Email: training@cloudeducationlearning.com}
\end{center}
\vspace{-0.2cm}\hrule\vspace{0.4cm}

\begin{flushright}
  \textbf{Ref. No.:} CEL/IND-TRG/2026/089 \\
  \textbf{Date:} 03 August 2026
\end{flushright}

\vspace{0.3cm}
\begin{center}
  {\fontsize{13pt}{16pt}\bfseries\underline{TO WHOMSOEVER IT MAY CONCERN}}
\end{center}

\vspace{0.3cm}
\justifying
This is to certify that \textbf{Mr. \StudentName}, a bonafide student of \textbf{Bachelor of Technology in Electronics \& Communication Engineering} (University Roll No.: \textbf{\RollNo}) from \textbf{Jawaharlal Nehru Government Engineering College, Sundernagar}, has successfully completed a comprehensive six-week Industrial Internship from \textbf{\TrainingFrom{}} to \textbf{\TrainingTo{}} at our training facility, \textbf{Cloud Education Learning Pvt. Ltd.}, Jawalaji Centre.

During his industrial training tenure, he was assigned to the Embedded Systems \& Internet of Things (IoT) R\&D Division, where he undertook the applied hardware and software engineering project titled:
\begin{center}
  \textbf{\large ``\ProjectTitle''}
\end{center}

Under the direct supervision of our senior technical team, Mr. \StudentName{} demonstrated high engineering acumen, disciplined design methodology, and thorough hardware-in-the-loop debugging capabilities. He successfully completed the electro-mechanical construction of a two-wheeled inverted pendulum chassis, integrated the InvenSense MPU-6050 6-DOF MEMS sensor, developed discrete-time sensor fusion filtering (Complementary and Extended Kalman Filtering), tuned a high-speed parallel digital PID control loop, and established real-time bidirectional cloud telemetry using Google Firebase Realtime Database and Blynk 2.0 WebSockets on the ESP32 microcontroller.

His conduct, technical aptitude, and problem-solving tenacity during the training tenure were found to be \textbf{Exemplary}. We wish him every success in his future academic and professional engineering endeavors.

\vspace{0.4cm}
\noindent
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \textbf{Er. Rajesh Sharma}\\
    Senior Project Manager \& Lead Mentor\\
    Embedded \& IoT Systems Division\\
    Cloud Education Learning Pvt. Ltd.
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \textbf{Authorized Signatory}\\
    Director (Training \& HR)\\
    Cloud Education Learning Pvt. Ltd.\\
    \textit{(Official Corporate Seal)}
  \end{flushright}
\end{minipage}

%% -------- Candidate's Declaration -----------------------------------------
\clearpage
\frontchapter{DECLARATION BY STUDENT}
\DeptLetterhead

\justifying
I hereby declare that the work presented in this internship report entitled \textbf{``\ProjectTitle''} submitted to the \textbf{Department of Electronics \& Communication Engineering, Jawaharlal Nehru Government Engineering College, Sundernagar}, in partial fulfillment of the requirements for the award of the degree of \textbf{Bachelor of Technology in Electronics \& Communication Engineering} of \textbf{Himachal Pradesh Technical University (HPTU), Hamirpur}, is an authentic record of my own industrial training conducted from \textbf{\TrainingFrom{}} to \textbf{\TrainingTo{}} at \textbf{\OrgName}, Jawalaji Centre, under the joint supervision of \textbf{\SupervisorName} and industrial mentor \textbf{Er. Rajesh Sharma}.

I further declare that the matter embodied in this report has not been submitted previously, in part or full, to any other university or institute for the award of any degree, diploma, or academic distinction. All technical literature, equations, open-source libraries, circuit schematics, and analytical figures incorporated from external scientific sources have been duly credited and cited in the bibliography.

\vspace{1.8cm}
\noindent
\begin{minipage}{0.45\textwidth}
  \begin{flushleft}
    \textbf{Date:} 03/08/2026\\[0.15cm]
    \textbf{Place:} Sundernagar, H.P.
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
  \begin{flushright}
    \textbf{\StudentName}\\
    University Roll No.: \textbf{\RollNo}\\
    B.Tech. 7th Semester (ECE)\\
    Department of ECE, JNGEC
  \end{flushright}
\end{minipage}

%% -------- Acknowledgement -------------------------------------------------
\clearpage
\frontchapter{ACKNOWLEDGEMENT}
\DeptLetterhead

\justifying
The successful completion of this six-week industrial internship and the development of the \textbf{\ProjectTitle} prototype would not have been possible without the invaluable guidance, constructive criticism, and encouragement of many individuals.

First and foremost, I express my deepest sense of gratitude and sincere indebtedness to my academic supervisor, \textbf{\SupervisorName}, Department of Electronics \& Communication Engineering, Jawaharlal Nehru Government Engineering College, Sundernagar, for his insightful technical guidance, meticulous feedback, and continuous intellectual encouragement throughout the internship period.

I express my sincere thanks to \textbf{Dr. Ashwani Kumar}, Head of Department, Electronics \& Communication Engineering, for providing excellent academic infrastructure, departmental laboratory facilities, and seamless administrative support. I am also profoundly grateful to the Director/Principal of JNGEC Sundernagar for fostering an environment of technical excellence and industrial exposure.

I extend my heartfelt appreciation to \textbf{Er. Rajesh Sharma}, Senior Project Mentor, and the entire technical engineering team at \textbf{\OrgName}, Jawalaji Centre, for their patient mentorship, practical laboratory instruction in embedded system prototyping, and for granting open access to precision electronic testbenches, sensor toolkits, and prototyping workstations.

Finally, I convey my heartfelt thanks to my parents and family for their unwavering moral and emotional support throughout my engineering education, and to my fellow classmates for their constructive technical discussions, collaborative spirit, and constant motivation.

\vspace{1.5cm}
\noindent
\begin{minipage}{0.45\textwidth}
  \begin{flushleft}
    \textbf{Date:} 03/08/2026\\[0.15cm]
    \textbf{Place:} Sundernagar, H.P.
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
  \begin{flushright}
    \textbf{\StudentName}\\
    University Roll No.: \textbf{\RollNo}\\
    B.Tech. 7th Semester (ECE)
  \end{flushright}
\end{minipage}

%% -------- Internship Evaluation Sheet -------------------------------------
\clearpage
\frontchapter{INTERNSHIP EVALUATION SHEET FROM ORGANIZATION}

\begin{center}
  \textbf{\large CLOUD EDUCATION LEARNING PVT. LTD.}\\
  \textit{\footnotesize Embedded Systems \& Robotics Division | AI-B08 Centre, Jawalaji (H.P.)}\\
  \textbf{INTERNSHIP PERFORMANCE EVALUATION FORM}
\end{center}
\vspace{-0.3cm}\hrule\vspace{0.15cm}

\renewcommand{\arraystretch}{0.95}
{\footnotesize
\begin{tabular}{p{3.8cm}p{10.2cm}}
  \textbf{Name of Trainee:} & \StudentName \\
  \textbf{University Roll No.:} & \RollNo \\
  \textbf{Institution:} & Jawaharlal Nehru Govt. Engineering College, Sundernagar (H.P.) \\
  \textbf{Degree \& Semester:} & B.Tech. Electronics \& Communication Engineering, 7th Semester \\
  \textbf{Training Period:} & 20 June 2026 to 03 August 2026 (Six Weeks) \\
  \textbf{Project Assigned:} & \ProjectTitle \\
  \textbf{Industrial Mentor:} & Er. Rajesh Sharma, Senior Project Manager \\
\end{tabular}
}

\vspace{0.1cm}
\noindent \textbf{\small Rubric-Based Performance Appraisal (10-Point Scale):}

\vspace{0.05cm}
\begin{center}
\footnotesize
\renewcommand{\arraystretch}{0.95}
\begin{tabular}{|c|p{8.0cm}|c|c|}
\hline
\textbf{S.No.} & \textbf{Evaluation Criterion / Assessment Attribute} & \textbf{Max} & \textbf{Awarded} \\
\hline
1 & Technical Competence, Hardware Interfacing \& Schematic Design & 10 & 09.5 \\
2 & Firmware Architecture, FreeRTOS Integration \& Code Modularity & 10 & 09.5 \\
3 & Sensor Fusion Filtering \& Closed-Loop PID Tuning Rigor & 10 & 10.0 \\
4 & Cloud IoT Telemetry Integration (Firebase \& Blynk 2.0) & 10 & 09.5 \\
5 & Punctuality, Attendance, Work Ethics \& Professional Discipline & 10 & 10.0 \\
6 & Quality of Documentation, Report Formulation \& Engineering Log & 10 & 09.5 \\
\hline
\multicolumn{2}{|r|}{\textbf{Total Score Awarded}} & \textbf{60} & \textbf{58.0} \\
\multicolumn{2}{|r|}{\textbf{Normalized Percentage / Overall Grade}} & \multicolumn{2}{c|}{\textbf{96.67\% (Grade: O -- Outstanding)}} \\
\hline
\end{tabular}
\end{center}

\vspace{0.1cm}
\noindent \textbf{\small Qualitative Comments by Industrial Supervisor:}\\
\justifying
\footnotesize
\textit{``Mr. Jyotiraditya Singh demonstrated exceptional diligence, theoretical depth, and practical debugging competence. His mathematical modeling of TWIP dynamics, real-time discrete PID implementation on the dual-core ESP32, and IoT cloud telemetry integration were exemplary. His technical performance is rated Outstanding.''}

\vspace{0.35cm}
\noindent
\normalsize
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \textbf{Er. Rajesh Sharma}\\
    Industrial Supervisor\\
    Cloud Education Learning Pvt. Ltd.
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \textbf{Training Coordinator}\\
    Corporate HR Division\\
    \textit{(Official Stamp \& Seal)}
  \end{flushright}
\end{minipage}

%% -------- About the Company -----------------------------------------------
\clearpage
\frontchapter{ABOUT THE COMPANY/ORGANIZATION/INSTITUTE}

\section*{Corporate Profile: Cloud Education Learning Pvt. Ltd.}
\justifying
\textbf{Cloud Education Learning Pvt. Ltd.} is a premier technology training, educational solutions, and industrial automation provider headquartered in Himachal Pradesh. The organization operates specialized state-of-the-art innovation centers, with its flagship \textbf{AI-B08 Industrial Technology Centre} located in Jawalaji, Kangra (H.P.). The enterprise was founded with the primary objective of bridging the persistent divide between conventional collegiate engineering syllabi and the dynamic, rapidly evolving competencies demanded by the modern cyber-physical electronics and automation industries.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.88\textwidth]{figures/General_Banner.png}
    \caption{Cloud Education Learning Applied Technology \& Industrial Prototyping Framework}
    \label{fig:cloud_banner}
\end{figure}

The Jawalaji training facility encompasses dedicated electronic hardware fabrication laboratories, high-speed printed circuit board (PCB) prototyping stations, digital storage oscilloscopes (DSOs), logic analyzers, surface-mount component reworking toolkits, rapid 3D prototyping printers, and multi-protocol industrial IoT networking gateways. Under this advanced physical setup, engineering undergraduates are provided an unconstrained, industry-grade environment to design, simulate, build, and benchmark complex cyber-physical embedded systems.

The core specialization divisions at Cloud Education Learning include:
\begin{itemize}[itemsep=1pt]
  \item \textbf{Embedded Systems \& Firmware Engineering:} Deep-dive firmware design covering 8-bit, 16-bit, and 32-bit microcontroller families (Microchip ATmega, Espressif ESP32/ESP8266, ARM Cortex-M), bare-metal peripheral programming, low-power optimization, and real-time operating system (FreeRTOS) multithreading.
  \item \textbf{Internet of Things (IoT) \& Cloud Platforms:} End-to-end device-to-cloud connectivity using MQTT, WebSockets, HTTP REST, CoAP, with real-time cloud data pipelines hosted on Google Firebase RTDB, AWS IoT Core, and Blynk 2.0.
  \item \textbf{Robotics, Automation \& Modern Control Systems:} Classical PID tuning, modern state-space optimal control (LQR), dynamic sensor fusion (Kalman and Complementary filtering), automated guided vehicles (AGVs), and industrial motor drivers.
  \item \textbf{PCB Layout \& Hardware Reliability Engineering:} Schematic capture in Autodesk Eagle/KiCAD, impedance-matched high-speed trace routing, star grounding topology, and thermal dissipation management.
\end{itemize}

The training curriculum is strictly project-centric. Rather than passive instructional lectures, trainees are mentored through the rigorous end-to-end engineering product lifecycle: requirement definition, component trade-off analysis, schematic capture, breadboard prototyping, signal conditioning, firmware structuring, sensor calibration, closed-loop algorithm tuning, cloud integration, and environmental testing. The facility provided an ideal, highly stimulating engineering environment for the execution of the \textbf{\ProjectTitle} project.

%% -------- Table of Contents, Tables, Figures, Abbreviations ---------------
\clearpage
\tableofcontents

\clearpage
\listoftables

\clearpage
\listoffigures

\clearpage
\frontchapter{LIST OF ABBREVIATIONS AND SYMBOLS}

\renewcommand{\arraystretch}{0.96}
\begin{longtable}{|p{3.0cm}|p{11.5cm}|}
\hline
\textbf{Abbreviation} & \textbf{Full Description} \\
\hline
\endhead
ADC & Analog-to-Digital Converter \\
AGV & Automated Guided Vehicle \\
API & Application Programming Interface \\
ARE & Algebraic Riccati Equation \\
ARW & Angle Random Walk \\
BLE & Bluetooth Low Energy \\
BLDC & Brushless Direct Current \\
BMS & Battery Management System \\
BOM & Bill of Materials \\
BJT & Bipolar Junction Transistor \\
CARE & Continuous Algebraic Riccati Equation \\
CoG & Center of Gravity \\
CPU & Central Processing Unit \\
DAC & Digital-to-Analog Converter \\
DC & Direct Current \\
DLPF & Digital Low-Pass Filter \\
DMP & Digital Motion Processor \\
DSO & Digital Storage Oscilloscope \\
EEPROM & Electrically Erasable Programmable Read-Only Memory \\
EKF & Extended Kalman Filter \\
EMF & Electromotive Force \\
ESP32 & Espressif Systems 32-bit Dual-Core Microcontroller \\
FOC & Field-Oriented Control \\
FreeRTOS & Free Real-Time Operating System \\
GPIO & General Purpose Input/Output \\
H-Bridge & Electronic Circuit for Bidirectional Motor Control \\
HTTP & Hypertext Transfer Protocol \\
$I^2C$ & Inter-Integrated Circuit Serial Bus Protocol \\
IDE & Integrated Development Environment \\
IMU & Inertial Measurement Unit \\
IoT & Internet of Things \\
JSON & JavaScript Object Notation \\
$K_d$ & Derivative Gain (PID Controller) \\
$K_i$ & Integral Gain (PID Controller) \\
$K_p$ & Proportional Gain (PID Controller) \\
LDO & Low Dropout Voltage Regulator \\
LED & Light Emitting Diode \\
LEDC & LED Control Peripheral (ESP32 Hardware PWM Engine) \\
Li-ion & Lithium-Ion (Rechargeable Battery Chemistry) \\
LQR & Linear Quadratic Regulator \\
MEMS & Micro-Electro-Mechanical Systems \\
MOSFET & Metal-Oxide-Semiconductor Field-Effect Transistor \\
MPU-6050 & InvenSense 6-Axis Motion Tracking Sensor (Accelerometer + Gyroscope) \\
MQTT & Message Queuing Telemetry Transport \\
PCB & Printed Circuit Board \\
PID & Proportional-Integral-Derivative Control \\
PWM & Pulse Width Modulation \\
RAM & Random Access Memory \\
REST & Representational State Transfer \\
RoHS & Restriction of Hazardous Substances \\
RPM & Revolutions Per Minute \\
RTDB & Realtime Database (Google Firebase) \\
RTOS & Real-Time Operating System \\
SCL & Serial Clock Line ($I^2C$) \\
SDA & Serial Data Line ($I^2C$) \\
SLAM & Simultaneous Localization and Mapping \\
SMP & Symmetric Multiprocessing \\
SPI & Serial Peripheral Interface \\
SRAM & Static Random Access Memory \\
SSE & Server-Sent Events \\
TWIP & Two-Wheeled Inverted Pendulum \\
UART & Universal Asynchronous Receiver-Transmitter \\
UI & User Interface \\
USB & Universal Serial Bus \\
VCC & Voltage Common Collector (Positive Power Supply) \\
Wi-Fi & Wireless Fidelity (IEEE 802.11 Networking) \\
WS & WebSockets Protocol \\
\hline
\end{longtable}
\renewcommand{\arraystretch}{1.0}

\clearpage

%% ==========================================================================
%%  MAIN CHAPTERS (Arabic Numerals 1, 2, 3 ...)
%% ==========================================================================
\pagenumbering{arabic}
\setcounter{page}{1}

"""
print("Header part defined, len =", len(tex_content))
