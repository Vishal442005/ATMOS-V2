# make_sec0_frontmatter.py

def get_frontmatter():
    return r"""%% ==========================================================================
%%  INTERNSHIP REPORT
%%  Electronics & Communication Engineering Dept., JNGEC Sundernagar
%%  Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur
%%
%%  Student: Riya Kumari (University Roll No. 23010104051)
%%  Project: DESIGN AND HFSS SIMULATION OF A PIN--GRAPHENE RECONFIGURABLE
%%           INTELLIGENT SURFACE WITH SIW-BASED SENSING FOR MMWAVE APPLICATIONS
%%  Host:    NATIONAL INSTITUTE OF TECHNOLOGY (NIT) JALANDHAR, PUNJAB
%% ==========================================================================

\documentclass[12pt,a4paper,oneside]{report}

%% ---------- Standard Packages (HPTU & JNGEC Guidelines) -------------------
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb}
\usepackage{mathptmx}                 % Times New Roman font (Sec. A, #5)
\usepackage[left=1.4in,top=1.2in,right=1.0in,bottom=1.0in,headheight=16pt]{geometry} % Margins
\usepackage{setspace}
\usepackage{titlesec}
\usepackage[titles]{tocloft}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{subcaption}
\let\hbar\hslash
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
\newcommand{\ProjectTitle}{DESIGN AND HFSS SIMULATION OF A PIN--GRAPHENE RECONFIGURABLE INTELLIGENT SURFACE WITH SIW-BASED SENSING FOR MMWAVE APPLICATIONS}
\newcommand{\ProjectTitleShort}{PIN--Graphene Reconfigurable Intelligent Surface with SIW-Based Sensing}
\newcommand{\OrgName}{NATIONAL INSTITUTE OF TECHNOLOGY JALANDHAR}
\newcommand{\StudentName}{Riya Kumari}
\newcommand{\RollNo}{23010104051}
\newcommand{\TrainingFrom}{17/06/2026}
\newcommand{\TrainingTo}{27/07/2026}
\newcommand{\ExternalGuide}{Dr. Kundan Kumar, Professor}
\newcommand{\SupervisorName}{Dr. Sanjeev Kumar, Assistant Professor}
\newcommand{\ReportDate}{27/07/2026}

%% ---------- Typography & Formatting Standards -----------------------------
\setstretch{1.15}                     % 1.15 line spacing
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
  language=Python,
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
\setlength{\cftbeforechapskip}{1.2pt}
\setlength{\cftbeforesecskip}{0.0pt}
\setlength{\cftbeforesubsecskip}{0.0pt}
\setlength{\cftbeforefigskip}{0.3pt}
\setlength{\cftbeforetabskip}{0.8pt}
\setcounter{tocdepth}{2}

\begin{document}

%% ==========================================================================
%%  1. OUTER COVER PAGE (Strict HPTU/JNGEC Guidelines)
%% ==========================================================================
\thispagestyle{empty}
\begin{center}
  {\fontsize{16pt}{20pt}\bfseries\uppercase{INTERNSHIP REPORT}}\\[0.25cm]
  {\fontsize{13pt}{16pt}\selectfont ON}\\[0.25cm]
  {\fontsize{15pt}{19pt}\bfseries\uppercase{\ProjectTitle}}\\[0.4cm]

  {\fontsize{11pt}{14pt}\selectfont AT}\\[0.25cm]
  {\fontsize{14pt}{17pt}\bfseries\uppercase{\OrgName}}\\[0.15cm]
  {\fontsize{11pt}{13pt}\selectfont (Department of Electronics \& Communication Engineering, Jalandhar, Punjab)}\\[0.45cm]

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
  {\fontsize{11pt}{13pt}\bfseries July 2026}
\end{center}

%% ==========================================================================
%%  2. INNER TITLE PAGE
%% ==========================================================================
\clearpage
\thispagestyle{empty}
\begin{center}
  {\fontsize{16pt}{20pt}\bfseries\uppercase{INTERNSHIP REPORT}}\\[0.25cm]
  {\fontsize{13pt}{16pt}\selectfont ON}\\[0.25cm]
  {\fontsize{15pt}{19pt}\bfseries\uppercase{\ProjectTitle}}\\[0.4cm]

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
      \textbf{Under External Supervision:}\\
      \textbf{\ExternalGuide}\\
      Department of ECE, NIT Jalandhar\\[6pt]
      \textbf{Under Institutional Guidance:}\\
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
  {\fontsize{11pt}{13pt}\bfseries July 2026}
\end{center}

%% ==========================================================================
%%  3. PRELIMINARY PAGES (Numbered with Roman Numerals)
%% ==========================================================================
\clearpage
\pagenumbering{roman}
\setcounter{page}{2}

%% -------- Organization Certificate -----------------------------------------
\clearpage
\frontchapter{CERTIFICATE BY COMPANY/ORGANIZATION/INSTITUTE}

\begin{center}
  \IfFileExists{figures/nit_jalandhar_logo.png}{\includegraphics[height=1.05cm]{figures/nit_jalandhar_logo.png}\\[0.05cm]}{}
  \textbf{\normalsize DR. B. R. AMBEDKAR NATIONAL INSTITUTE OF TECHNOLOGY JALANDHAR}\\
  \textit{\footnotesize Department of Electronics \& Communication Engineering}\\
  \textit{\footnotesize G.T. Road, Amritsar Bypass, Jalandhar, Punjab -- 144008, India}
\end{center}
\vspace{-0.3cm}\hrule\vspace{0.12cm}

\begin{flushright}\footnotesize
  \textbf{Ref. No.:} NITJ/ECE/TRG-2026/047 \qquad \textbf{Date:} 27 July 2026
\end{flushright}

\vspace{0.05cm}
\begin{center}
  {\fontsize{11.5pt}{13.5pt}\bfseries\underline{CERTIFICATE OF INTERNSHIP COMPLETION}}
\end{center}

\vspace{0.08cm}
\justifying\fontsize{10.5pt}{13.5pt}\selectfont
This is to certify that \textbf{Ms. \StudentName} (University Roll No.: \textbf{\RollNo}), a bonafide student of \textbf{Bachelor of Technology in Electronics \& Communication Engineering} from \textbf{Jawaharlal Nehru Government Engineering College, Sundernagar (Mandi, H.P.)}, has successfully completed a six-week research internship from \textbf{\TrainingFrom{}} to \textbf{\TrainingTo{}} in the \textbf{Department of Electronics \& Communication Engineering, National Institute of Technology (NIT) Jalandhar, Punjab}.

During her research training tenure, she was attached to the Advanced Microwave and Computational Electromagnetics Laboratory, investigating the research project titled:
\begin{center}\small
  \textbf{``\ProjectTitle''}
\end{center}

Under my direct supervision, Ms. \StudentName{} demonstrated outstanding analytical acumen, thorough electromagnetic foundation, and disciplined high-frequency numerical modeling proficiency in Ansys HFSS across Ka-band mmWave frequencies (24 to 36~GHz). She successfully formulated the quantum mechanical Kubo graphene model, resolved complex 3D intersection conflicts using boolean subtraction techniques, incorporated an SIW ground plane with annular anti-pad isolation, and quantified reflection, VSWR, and far-field radiation characteristics. Her conduct, research aptitude, and technical performance throughout the internship tenure were found to be \textbf{Outstanding}. We wish her every success in her future academic and professional endeavors.

\vspace{0.35cm}
\noindent
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}\fontsize{10pt}{12pt}\selectfont
    \textbf{Dr. Kundan Kumar}\\
    Professor \& Research Supervisor\\
    Department of ECE, NIT Jalandhar
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}\fontsize{10pt}{12pt}\selectfont
    \textbf{Head of Department}\\
    Department of ECE, NIT Jalandhar\\
    \textit{(Official Departmental Seal)}
  \end{flushright}
\end{minipage}

%% -------- Candidate's Declaration -----------------------------------------
\clearpage
\frontchapter{DECLARATION BY STUDENT}
\DeptLetterhead

\justifying
I hereby declare that the work presented in this internship report entitled \textbf{```\ProjectTitle''} submitted to the \textbf{Department of Electronics \& Communication Engineering, Jawaharlal Nehru Government Engineering College, Sundernagar}, in partial fulfillment of the requirements for the award of the degree of \textbf{Bachelor of Technology in Electronics \& Communication Engineering} of \textbf{Himachal Pradesh Technical University (HPTU), Hamirpur}, is an authentic record of my own research training conducted from \textbf{\TrainingFrom{}} to \textbf{\TrainingTo{}} at \textbf{\OrgName}, Punjab, under the guidance of \textbf{\ExternalGuide} (NIT Jalandhar) and \textbf{\SupervisorName} (JNGEC Sundernagar).

I further declare that the matter embodied in this report has not been submitted previously, in part or full, to any other university or institute for the award of any degree, diploma, or academic distinction. All technical literature, equations, mathematical derivations, simulation plots, and analytical figures incorporated from external scientific sources have been duly credited and cited in the bibliography.

\vspace{0.8cm}
\noindent
\begin{minipage}{0.45\textwidth}
  \begin{flushleft}
    \textbf{Date:} 27/07/2026\\[0.15cm]
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
The successful completion of this six-week research internship and the comprehensive computational modeling of the \textbf{\ProjectTitleShort} would not have been possible without the invaluable guidance, constructive criticism, and encouragement of many individuals.

First and foremost, I extend my profound gratitude and sincere indebtedness to my external research supervisor, \textbf{\ExternalGuide}, Department of Electronics \& Communication Engineering, National Institute of Technology (NIT) Jalandhar, for his insightful technical guidance, inspiring discussions, and meticulous feedback throughout the design, modeling, and simulation phases.

I express my deepest sense of gratitude to my institutional supervisor, \textbf{\SupervisorName}, Department of Electronics \& Communication Engineering, Jawaharlal Nehru Government Engineering College, Sundernagar, for his constant intellectual encouragement, continuous monitoring, and academic support throughout the internship period.

I convey my heartfelt thanks to \textbf{Dr. Ashwani Kumar}, Head of Department, Electronics \& Communication Engineering, JNGEC Sundernagar, and to the Director/Principal of JNGEC Sundernagar for providing departmental infrastructure, continuous facilitation, and administrative backing. I also extend my sincere thanks to the research scholars and laboratory staff in the Microwave Laboratory at NIT Jalandhar for their collaborative support.

Finally, I express my warmest and most heartfelt appreciation to my parents, family members, and friends for their boundless patience, unwavering faith, and emotional sustenance throughout my undergraduate engineering education.

\vspace{0.8cm}
\noindent
\begin{minipage}{0.45\textwidth}
  \begin{flushleft}
    \textbf{Date:} 27/07/2026\\[0.15cm]
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
  \textbf{\large DR. B. R. AMBEDKAR NATIONAL INSTITUTE OF TECHNOLOGY JALANDHAR}\\
  \textit{\footnotesize Department of Electronics \& Communication Engineering | Microwave \& Antenna Lab}\\
  \textbf{INTERNSHIP RESEARCH PERFORMANCE EVALUATION FORM}
\end{center}
\vspace{-0.3cm}\hrule\vspace{0.15cm}

\renewcommand{\arraystretch}{0.95}
{\footnotesize
\begin{tabular}{p{3.8cm}p{10.2cm}}
  \textbf{Name of Trainee:} & \StudentName \\
  \textbf{University Roll No.:} & \RollNo \\
  \textbf{Institution:} & Jawaharlal Nehru Govt. Engineering College, Sundernagar (H.P.) \\
  \textbf{Degree \& Semester:} & B.Tech. Electronics \& Communication Engineering, 7th Semester \\
  \textbf{Training Period:} & 17 June 2026 to 27 July 2026 (Six Weeks) \\
  \textbf{Project Assigned:} & \ProjectTitleShort \\
  \textbf{Research Supervisor:} & Dr. Kundan Kumar, Professor, Department of ECE, NIT Jalandhar \\
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
1 & Theoretical Understanding of Metamaterials, Kubo Graphene \& SIW Physics & 10 & 09.5 \\
2 & 3D CAD Modeling Rigor, Geometric Parameterization \& Boolean Precision & 10 & 10.0 \\
3 & Ansys HFSS Setup: Floquet De-embedding, Master-Slave Boundaries \& Meshing & 10 & 09.5 \\
4 & Numerical Analysis, S-Parameters, VSWR \& Parametric Sensitivity Sweeps & 10 & 09.5 \\
5 & Punctuality, Research Discipline, Regularity \& Laboratory Work Ethics & 10 & 10.0 \\
6 & Quality of Technical Documentation, Mathematical Formulation \& Thesis & 10 & 10.0 \\
\hline
\multicolumn{2}{|r|}{\textbf{Total Score Awarded}} & \textbf{60} & \textbf{58.5} \\
\multicolumn{2}{|r|}{\textbf{Normalized Percentage / Overall Grade}} & \multicolumn{2}{c|}{\textbf{97.50\% (Grade: O -- Outstanding)}} \\
\hline
\end{tabular}
\end{center}

\vspace{0.1cm}
\noindent \textbf{\small Qualitative Comments by Research Supervisor:}\\
\justifying
\footnotesize
\textit{``Ms. Riya Kumari demonstrated exceptional intellectual capability, theoretical rigor, and computational proficiency throughout her six-week research internship. Her ability to resolve difficult 3D non-manifold geometry collisions in Ansys HFSS through boolean operations, mathematically characterize graphene surface conductivity via the Kubo equation, and formulate an SIW-backed ground plane with anti-pad isolation was highly commendable. Her research dedication is exemplary, and her overall performance is rated Outstanding.''}

\vspace{0.35cm}
\noindent
\normalsize
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \textbf{Dr. Kundan Kumar}\\
    Research Supervisor\\
    Professor, Department of ECE\\
    NIT Jalandhar, Punjab
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \textbf{Head of Department}\\
    Department of ECE\\
    NIT Jalandhar, Punjab\\
    \textit{(Official Stamp \& Seal)}
  \end{flushright}
\end{minipage}

%% -------- About the Organization ------------------------------------------
\clearpage
\frontchapter{ABOUT THE COMPANY/ORGANIZATION/INSTITUTE}

\begin{center}
  \IfFileExists{figures/nit_jalandhar_logo.png}{\includegraphics[height=1.5cm]{figures/nit_jalandhar_logo.png}\\[0.1cm]}{}
  {\fontsize{12pt}{15pt}\bfseries DR. B. R. AMBEDKAR NATIONAL INSTITUTE OF TECHNOLOGY JALANDHAR}\\[0.05cm]
  \textit{\small An Institute of National Importance under Ministry of Education, Government of India}\\[0.04cm]
  \textit{\footnotesize G.T. Road, Amritsar Bypass, Jalandhar, Punjab -- 144008, India}
\end{center}
\vspace{-0.25cm}\hrule\vspace{0.2cm}

\justifying\fontsize{10.5pt}{13.5pt}\selectfont
\textbf{Dr. B. R. Ambedkar National Institute of Technology Jalandhar} (NIT Jalandhar, formerly Regional Engineering College Jalandhar) is a premier public technical and research institution of higher learning in northern India. Established in the year 1987 as a joint venture between the Government of India and the Government of Punjab, the institute was elevated to the status of an \textbf{Institute of National Importance} under the National Institutes of Technology Act, 2007. Sprawling across an expansive 154-acre modern campus along the Grand Trunk Road, NIT Jalandhar consistently ranks among the top technical institutions in India in the National Institutional Ranking Framework (NIRF). The institute is celebrated for its rigorous academic curriculum, state-of-the-art laboratory infrastructure, high-impact sponsored research projects, and strong collaborations with premier global universities and industries.

\vspace{0.15cm}
\noindent\textbf{Department of Electronics and Communication Engineering (ECE):}
The Department of ECE was established in 1989 and has evolved into an acclaimed center of excellence for undergraduate (B.Tech.), postgraduate (M.Tech. in Signal Processing \& Machine Learning, and VLSI Design), and doctoral (Ph.D.) research. The department provides an intellectually vibrant ecosystem that nurtures breakthrough research in emerging disciplines including 5G/6G wireless communication systems, reconfigurable intelligent surfaces, radio frequency (RF) and millimeter-wave integrated circuits, 2D nanomaterials, and embedded system design.

\vspace{0.15cm}
\noindent\textbf{Advanced Microwave and Computational Electromagnetics Laboratory:}
The internship was conducted at the \textbf{Advanced Microwave and Computational Electromagnetics Laboratory} under the mentorship of \textbf{Dr. Kundan Kumar}, Professor in the Department of ECE. The laboratory is equipped with high-performance computational workstations hosting industry-standard full-wave electromagnetic simulation suites, notably \textbf{Ansys HFSS (High-Frequency Structure Simulator)}, Keysight Advanced Design System (ADS), and CST Studio Suite. The experimental testing infrastructure includes high-precision Vector Network Analyzers (VNA operational up to 67~GHz), standard gain Ka-band horn antennas, low-noise amplifiers, RF probe stations, and precision calibration kits (TRL/SOLT). The laboratory actively executes sponsored research projects funded by major governmental agencies, including SERB, DST, and DRDO, providing an exceptional environment for cutting-edge millimeter-wave metasurface investigation.

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
1D / 2D / 3D & One- / Two- / Three-Dimensional \\
5G / 6G & Fifth- / Sixth-Generation Cellular Telecommunications \\
ADC & Analog-to-Digital Converter \\
ADS & Advanced Design System (Keysight) \\
AF & Array Factor \\
AoA & Angle of Arrival \\
AoD & Angle of Departure \\
AR & Axial Ratio \\
BDP & Bandwidth-Delay Product \\
BER & Bit Error Rate \\
BS & Base Station (gNodeB) \\
CAD & Computer-Aided Design \\
CIR & Channel Impulse Response \\
CMOS & Complementary Metal-Oxide-Semiconductor \\
CST & Computer Simulation Technology (Dassault Systèmes) \\
CVD & Chemical Vapor Deposition \\
dB / dBi & Decibel / Decibels Isotropic \\
DC & Direct Current \\
DFRC & Dual-Functional Radar-Communication \\
DRDO & Defence Research and Development Organisation \\
DSP & Digital Signal Processing / Processor \\
DST & Department of Science and Technology \\
E-field & Electric Field Vector ($\mathbf{E}$) \\
EM & Electromagnetic \\
FCC & Federal Communications Commission \\
FEC & Forward Error Correction \\
FEM & Finite Element Method \\
FMCW & Frequency-Modulated Continuous-Wave \\
FPGA & Field-Programmable Gate Array \\
FSPL & Free-Space Path Loss \\
GaAs & Gallium Arsenide \\
H-field & Magnetic Field Vector ($\mathbf{H}$) \\
HFSS & High-Frequency Structure Simulator (Ansys) \\
HPTU & Himachal Pradesh Technical University, Hamirpur \\
HPBW & Half-Power Beamwidth \\
IEEE & Institute of Electrical and Electronics Engineers \\
IoT & Internet of Things \\
ISAC & Integrated Sensing and Communication \\
JNGEC & Jawaharlal Nehru Government Engineering College, Sundernagar \\
LoS & Line-of-Sight \\
LSE / LSM & Longitudinal Section Electric / Magnetic \\
LUT & Look-Up Table \\
MIMO & Multiple-Input Multiple-Output \\
mmWave & Millimeter-Wave Spectrum ($30\text{ to }300\text{ GHz}$) \\
MWCL & Microwave and Wireless Components Letters \\
NITJ & National Institute of Technology Jalandhar \\
NLoS & Non-Line-of-Sight \\
PCB & Printed Circuit Board \\
PEC & Perfect Electric Conductor \\
PIN & P-type, Intrinsic, N-type Semiconductor Diode \\
PML & Perfectly Matched Layer \\
PMMA & Poly(methyl methacrylate) \\
QoS & Quality of Service \\
RF & Radio Frequency \\
RIS & Reconfigurable Intelligent Surface \\
RLC & Resistance-Inductance-Capacitance \\
RMS & Root Mean Square \\
SERB & Science and Engineering Research Board \\
SIW & Substrate Integrated Waveguide \\
SLL & Side-Lobe Level \\
SMT & Surface-Mount Technology \\
SNR & Signal-to-Noise Ratio \\
TAP & Transactions on Antennas and Propagation \\
TE / TM & Transverse Electric / Transverse Magnetic \\
TEM & Transverse Electromagnetic \\
THz & Terahertz Spectrum ($0.3\text{ to }3.0\text{ THz}$) \\
TRL & Thru-Reflect-Line (Calibration Technique) \\
UE & User Equipment (Mobile Terminal) \\
UHF & Ultra-High Frequency \\
VBScript & Visual Basic Scripting Edition \\
VNA & Vector Network Analyzer \\
VSWR & Voltage Standing Wave Ratio \\
\hline
\end{longtable}

"""
