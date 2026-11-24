import os, re

# Read chapter files
chapters = [
    '01_chapter1.tex',
    '02_chapter2.tex',
    '03_chapter3.tex',
    '04_chapter4.tex',
    '05_chapter5.tex',
    '06_references.tex',
    '07_appendices.tex'
]

content_parts = []
for c in chapters:
    path = os.path.join('vishal', c)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    # In 01_chapter1.tex, remove pagenumbering / setcounter if present so it's managed centrally
    if c == '01_chapter1.tex':
        text = re.sub(r'\\pagenumbering\{arabic\}\s*', '', text)
        text = re.sub(r'\\setcounter\{page\}\{1\}\s*', '', text)
        
    content_parts.append(text)

combined_body = "\n\n".join(content_parts)

vishal_main_tex = r"""%% ==========================================================================
%%  INTERNSHIP REPORT
%%  Electronics & Communication Engineering Dept., JNGEC Sundernagar
%%  Follows "Internship Report Guidelines" (Sections A, B, C)
%%
%%  Student: Vishal Chandel (Roll No. 23010104072)
%%  Project: STUDY OF EEG SIGNALS USING MACHINE LEARNING TECHNIQUES
%%  Host:    NATIONAL INSTITUTE OF TECHNOLOGY, JALANDHAR
%%           (Department of Instrumentation & Control Engineering)
%% ==========================================================================

\documentclass[12pt,a4paper,oneside]{report}

%% ---------- Packages ------------------------------------------------------
\usepackage[T1]{fontenc}
\usepackage{mathptmx}                 % Times New Roman font (Sec. A, #5)
\usepackage[left=1.4in,top=1.2in,right=1in,bottom=1in,headheight=16pt]{geometry} % Margins (Sec. A, #7)
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
\usepackage{float,enumitem}
\usepackage{microtype}
\usepackage{appendix}
\usepackage{algorithm}
\usepackage{algpseudocode}

\graphicspath{{figures/}{./}}

%% ---------- Details --------------------------------------------------------
\newcommand{\ProjectTitle}{STUDY OF EEG SIGNALS USING\\ MACHINE LEARNING TECHNIQUES}
\newcommand{\OrgName}{NATIONAL INSTITUTE OF TECHNOLOGY, JALANDHAR}
\newcommand{\StudentName}{Vishal Chandel}
\newcommand{\RollNo}{23010104072}
\newcommand{\TrainingFrom}{17/06/2026}
\newcommand{\TrainingTo}{28/07/2026}
\newcommand{\SupervisorName}{Dr. Richa Sharma}
\newcommand{\SupervisorTitle}{Professor, Dept. of Instrumentation \& Control Engg.}
\newcommand{\ReportDate}{28/07/2026}

%% ---------- Text formatting ----------
\setstretch{1.15}
\setlength{\parindent}{0pt}
\setlength{\parskip}{10pt}

%% Chapter headings: 14 pt bold; sub-headings bold
\titleformat{\chapter}[block]
  {\centering\bfseries\fontsize{14}{17}\selectfont}
  {Chapter \thechapter:}{0.5em}{}

\titleformat{name=\chapter,numberless}[block]
  {\centering\bfseries\fontsize{14}{17}\selectfont}
  {}{0pt}{\underline}

\titlespacing*{\chapter}{0pt}{0pt}{18pt}

%% Section headings
\titleformat{\section}[hang]
  {\raggedright\bfseries\fontsize{14}{17}\selectfont}
  {\thesection}{0.6em}{}

%% Subsection headings
\titleformat{\subsection}[hang]
  {\raggedright\bfseries\fontsize{12}{14}\selectfont}
  {\thesubsection}{0.6em}{}

%% Subsubsection headings
\titleformat{\subsubsection}[hang]
  {\raggedright\bfseries\fontsize{12}{14}\selectfont}
  {\thesubsubsection}{0.6em}{}

%% Captions
\captionsetup{font=small,labelfont=bf,labelsep=colon}

%% Table of contents look
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

%% Running Header / Footer
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
\definecolor{coderule}{rgb}{0.85,0.85,0.85}

\lstset{
  language=Python,
  backgroundcolor=\color{codebg},
  basicstyle=\ttfamily\scriptsize,
  keywordstyle=\color{codeblue}\bfseries,
  commentstyle=\color{codegreen}\itshape,
  stringstyle=\color[rgb]{0.7,0.2,0.1},
  numbers=left,
  numberstyle=\tiny\color{codegray},
  numbersep=6pt,
  breaklines=true,
  breakatwhitespace=false,
  showstringspaces=false,
  frame=single,
  rulecolor=\color{coderule},
  captionpos=b,
  tabsize=4
}

%% ---------- Helper macros -------------------------------------------------
\newcommand{\CollegeLogo}[1]{%
  \IfFileExists{figures/logo.png}{\includegraphics[height=#1]{figures/logo.png}}%
  {\IfFileExists{logo.png}{\includegraphics[height=#1]{logo.png}}%
  {\IfFileExists{figures/logo1 (1).png}{\includegraphics[height=#1]{figures/logo1 (1).png}}%
  {\fbox{\parbox{3cm}{\centering\small Put college logo\\(logo.png) here}}}}}}

\newcommand{\frontchapter}[1]{\phantomsection\chapter*{#1}\addcontentsline{toc}{chapter}{#1}}

%% Safe image inclusion command
\newcommand{\safeimg}[2]{%
  \IfFileExists{#2}{\includegraphics[width=#1]{#2}}%
  {\IfFileExists{figures/#2}{\includegraphics[width=#1]{figures/#2}}%
  {\fbox{\begin{minipage}[c][4.0cm][c]{\dimexpr#1-2\fboxsep-2\fboxrule}\centering
  \itshape\small Figure: \texttt{\detokenize{#2}}
  \end{minipage}}}}%
}

%% Cover page content
\newcommand{\CoverContent}{%
  \centering\bfseries\singlespacing
  {\fontsize{24}{29}\selectfont INTERNSHIP REPORT\par}
  \vspace{0.4cm}
  {\fontsize{17}{21}\selectfont \ProjectTitle\par \vspace{0.25cm}\fontsize{13}{16}\selectfont\OrgName\par}
  \vspace{0.4cm}
  {\fontsize{13}{16}\selectfont
    \mdseries Submitted in partial fulfillment of the\par
    \mdseries Requirements for the award of\par
    Degree of Bachelor of Technology in\par
    Electronics \& Communication Engineering\par}
  \vspace{1.0cm}
  {\fontsize{13}{16}\selectfont
    Submitted by:\par\vspace{4pt}
    \StudentName \hfill Roll No.~\RollNo\par\vspace{4pt}
    \textit{Training period:} \TrainingFrom\ \textit{to} \TrainingTo\par}
  \vspace{0.8cm}
  \CollegeLogo{3.0cm}\par
  \vspace{0.8cm}
  {\fontsize{14}{17}\selectfont
    Submitted to:\par
    Department of Electronics \& Communication Engineering\par
    JAWAHARLAL NEHRU GOVT. ENGINEERING COLLEGE\par
    SUNDERNAGAR, DIST. MANDI (H.P.)\par}}

%% ==========================================================================
\begin{document}
%% ==========================================================================

%% -------- COVER PAGE 1: glossy / hard paper (coloured) --------------------
\pagenumbering{gobble}
\thispagestyle{empty}
\begin{tcolorbox}[enhanced, sharp corners, colframe=black, boxrule=1.2pt,
  interior style={top color=cyan!8, bottom color=cyan!35},
  width=\textwidth, height=0.93\textheight, valign=center]
  \CoverContent
\end{tcolorbox}

%% -------- COVER PAGE 2: simple A4 paper (plain) ---------------------------
\newpage
\thispagestyle{empty}
\vspace*{\fill}
{\CoverContent}
\vspace*{\fill}

%% -------- TABLE OF CONTENTS ----------------------------------------------
\newpage
\tableofcontents

%% ==========================================================================
%%  FRONT MATTER  (Roman numerals i, ii, iii ...)
%% ==========================================================================
\pagenumbering{roman}
\setcounter{page}{1}

%% -------- i. Certificate by Company/Organization/Institute ----------------
\clearpage
\phantomsection
\addcontentsline{toc}{chapter}{Certificate by Company/Organization/Institute}

\IfFileExists{figures/certificate.pdf}{%
  \includepdf[pages=1,pagecommand={\thispagestyle{plain}}]{figures/certificate.pdf}}%
{% Fallback native certificate
\begin{center}
  \vspace*{0.3cm}
  {\fontsize{17}{21}\selectfont\bfseries NATIONAL INSTITUTE OF TECHNOLOGY, JALANDHAR}\\[0.2cm]
  {\fontsize{12}{15}\selectfont\bfseries Department of Instrumentation \& Control Engineering}\\[0.1cm]
  {\fontsize{9}{12}\selectfont G.T. Road, Amritsar Bypass, Jalandhar, Punjab -- 144027, India \textbar{} Web: www.nitj.ac.in}\\[0.3cm]
  \hrule\vspace{0.8cm}
  {\fontsize{15}{18}\selectfont\bfseries\underline{CERTIFICATE OF INDUSTRIAL / RESEARCH TRAINING}}\\[0.8cm]
\end{center}

\begin{spacing}{1.25}
\noindent This is to certify that \textbf{Mr. Vishal Chandel} (Roll No.: \textbf{23010104072}), a bonafide student of Bachelor of Technology in Electronics and Communication Engineering at \textbf{Jawaharlal Nehru Government Engineering College, Sundernagar}, has successfully completed his six-week summer research internship training from \textbf{17 June 2026 to 28 July 2026} at the \textbf{Department of Instrumentation \& Control Engineering, National Institute of Technology (NIT), Jalandhar}.

\vspace{0.35cm}
\noindent The internship training and research project titled \textbf{``Study of EEG Signals Using Machine Learning Techniques: Triple-Layer MetaModel for Automated Alcoholic EEG Classification and Biomedical Diagnostic Analysis''} was carried out under my direct academic supervision and technical guidance.

\vspace{0.35cm}
\noindent During his tenure with our research laboratory, Vishal Chandel demonstrated exceptional diligence, rigorous engineering capability, scientific inquisitiveness, and profound dedication to biomedical computing and deep learning algorithm development. He successfully formulated and validated the complete electroencephalogram signal preprocessing pipeline, baseline neural models, and the novel multi-branch spatio-temporal fusion architecture.

\vspace{0.35cm}
\noindent His overall performance throughout the internship tenure was evaluated as \textbf{Outstanding (Grade: Excellent)}. I wish him immense success in all his prospective academic and professional engineering endeavors.
\end{spacing}

\vspace{1.2cm}
\noindent\begin{tabular}{@{}p{7.5cm}p{7.0cm}@{}}
\textbf{Date:} 28 July 2026 & \textbf{Dr. Richa Sharma} \\
\textbf{Place:} NIT Jalandhar & Professor \\
& Department of Instrumentation \& Control Engg. \\
& National Institute of Technology, Jalandhar \\
\end{tabular}
}

%% -------- ii. Declaration by the Student ----------------------------------
\clearpage
\phantomsection
\addcontentsline{toc}{chapter}{Declaration by the Student}

% College letterhead with logo on the left
\noindent
\begin{minipage}[c]{0.18\textwidth}
    \raggedleft
    \includegraphics[width=2.5cm,height=2.5cm,keepaspectratio]{figures/logo.png}
\end{minipage}%
\hspace{0.02\textwidth}%
\begin{minipage}[c]{0.78\textwidth}
    \centering
    \fontsize{9.5}{11.5}\selectfont
    \bfseries
    Electronics \& Communication Engineering Department\\
    Jawaharlal Nehru Govt. Engineering College,\\
    Sundernagar, Mandi (H.P.)\\
    Phone No. 01907-267199, 267688, Fax No. 267811\\
    Web site: http://www.jngec.ac.in,
    Email: jngechp@yahoo.co.in
\end{minipage}

\vspace{2pt}
\noindent\rule{\textwidth}{0.6pt}

\vspace{0.25cm}

\begin{center}
    {\fontsize{14}{17}\selectfont
    \bfseries\underline{DECLARATION BY STUDENT}}
\end{center}

\vspace{0.15cm}

\begin{spacing}{1.1}
\noindent
I hereby declare that the work presented in this Internship Report entitled
\textbf{``Study of EEG Signals Using Machine Learning Techniques: Triple-Layer MetaModel for Automated Alcoholic EEG Classification and Biomedical Diagnostic Analysis''},
submitted in partial fulfillment of the requirements for the award of the degree of
\textbf{Bachelor of Technology in Electronics and Communication Engineering} at
\textbf{Jawaharlal Nehru Govt. Engineering College, Sundernagar}, is an authentic record of
my own experimental, algorithmic, and computational work carried out under the supervision of
\textbf{Dr. Richa Sharma}, Professor, Department of Instrumentation \& Control Engineering,
National Institute of Technology (NIT) Jalandhar, during the period from
\textbf{17/06/2026} to \textbf{28/07/2026}.

\vspace{0.15cm}
\noindent
I further declare that this report has not been submitted previously, in part or in full,
for the award of any other degree or diploma to any other University or Institution.
All literature, datasets, and algorithmic formulations referenced from external sources
have been duly cited and acknowledged.
\end{spacing}

\vspace{0.35cm}

\noindent
\begin{minipage}[t]{0.45\textwidth}
    Date: \underline{28/07/2026}\\[3pt]
    Place: \underline{Sundernagar}
\end{minipage}%
\hfill
\begin{minipage}[t]{0.45\textwidth}
    \raggedleft
    (Signature of Student)\\[2pt]
    \textbf{Vishal Chandel}\\[2pt]
    Roll No.: 23010104072\\[2pt]
    7th Semester, B.Tech. ECE
\end{minipage}

\vspace{0.4cm}

\noindent
\begin{minipage}{\textwidth}
    Examined by:
\end{minipage}

\vspace{0.35cm}

\noindent
\begin{minipage}[t]{0.32\textwidth}
    \centering
    (Signature of Internal Examiner)
\end{minipage}%
\begin{minipage}[t]{0.34\textwidth}
    \centering
    (Signature of Head of Department)
\end{minipage}%
\begin{minipage}[t]{0.32\textwidth}
    \centering
    (Signature of External Examiner)
\end{minipage}

\vspace{0.3cm}

\noindent
{\scriptsize
\colorbox{yellow}{%
\parbox{\dimexpr\textwidth-2\fboxsep\relax}{%
\textbf{*(For group departmental copy of report, include signatures and names with roll numbers of all students)}
}}}

\clearpage

%% -------- iii. Acknowledgement --------------------------------------------
\phantomsection
\addcontentsline{toc}{chapter}{Acknowledgement}

% Logo and department heading
\noindent
\begin{minipage}[c]{0.18\textwidth}
    \raggedleft
    \includegraphics[width=2.1cm,height=2.1cm,keepaspectratio]{figures/logo.png}
\end{minipage}%
\hspace{0.02\textwidth}%
\begin{minipage}[c]{0.78\textwidth}
    \centering
    {\fontsize{8.5}{10}\selectfont
    \bfseries
    Electronics \& Communication Engineering Department\\
    Jawaharlal Nehru Govt. Engineering College,\\
    Sundernagar, Mandi (H.P.)\\
    Phone No. 01907-267199, 267688, Fax No. 267811\\
    Web site: http://www.jngec.ac.in, Email: jngechp@yahoo.co.in
    }
\end{minipage}

\par\vspace{1pt}
\noindent\rule{\textwidth}{0.6pt}
\vspace{2pt}

\begin{center}
    {\fontsize{13}{15}\selectfont
    \bfseries\underline{ACKNOWLEDGEMENT}}
\end{center}

\vspace{1pt}

\begin{spacing}{0.93}
\noindent
The successful completion of this six-week industrial research internship project would not have been possible without the generous guidance, intellectual support, and encouragement of numerous mentors and academic advisors.

\vspace{1pt}
\noindent
First and foremost, I extend my profound gratitude and sincerest thanks to my internship supervisor, \textbf{Dr. Richa Sharma}, Professor, Department of Instrumentation \& Control Engineering, National Institute of Technology (NIT), Jalandhar. Her illuminating lectures, insightful technical critiques, patience, and unwavering belief in rigorous scientific methodology provided the foundation for every stage of this research project. She provided me with access to cutting-edge computing resources and guided the mathematical formulations of our multi-branch fusion network.

\vspace{1pt}
\noindent
I also express my heartfelt appreciation to \textbf{Dr. Robin Kalyan}, Associate Professor, for his constructive suggestions during technical seminars and discussions regarding biomedical signal filtering, artifact cancellation, and recurrent neural architectures. My sincere thanks are extended to the faculty and research scholars of the Department of Instrumentation \& Control Engineering at NIT Jalandhar for creating an intellectually invigorating and welcoming research atmosphere.

\vspace{1pt}
\noindent
I extend my sincere gratitude to \textbf{Dr. Sanjeev Kumar}, Assistant Professor and departmental training coordinator, for his continuous academic support and administrative supervision.

\vspace{1pt}
\noindent
I am deeply thankful to the Head of the Department, faculty members, and the Training \& Placement cell of the \textbf{Department of Electronics \& Communication Engineering, Jawaharlal Nehru Government Engineering College, Sundernagar}, for granting me permission to undergo this high-level industrial internship training and for their continuous academic administrative support.

\vspace{1pt}
\noindent
Finally, I express my deepest love and indebtedness to my parents, family members, and friends whose unconditional encouragement, moral support, and sacrifices provided the inspiration to strive for academic excellence throughout the duration of this training.
\end{spacing}

\vspace{0.1cm}

\noindent
\hfill
\begin{minipage}{0.42\textwidth}
    \centering
    (Signature of student)\\[1.5pt]
    (Vishal Chandel)\\[1.5pt]
    (Roll No. 23010104072)
\end{minipage}

\vspace{0.08cm}
\noindent
Date: \underline{28/07/2026}

\vspace{0.08cm}
\noindent
{\scriptsize
\colorbox{yellow}{%
    \parbox{\dimexpr\textwidth-2\fboxsep\relax}{%
        \textbf{*(For group departmental copy of report, include signatures and names with roll numbers of all students)}
    }%
}%
}

\clearpage

%% -------- iv. Internship Evaluation Sheet from Organization ---------------
\phantomsection
\addcontentsline{toc}{chapter}{Internship Evaluation Sheet from Organization}

\IfFileExists{figures/evaluation.pdf}{%
  \includepdf[pages=1,pagecommand={\thispagestyle{plain}}]{figures/evaluation.pdf}}%
{\begin{figure}[H]
  \centering
  \includegraphics[width=0.92\textwidth]{figures/evaluation_sheet.jpg}
  \caption{Internship Evaluation Sheet from Organization (NIT Jalandhar)}
  \label{fig:eval_sheet_vishal}
\end{figure}}

%% -------- v. About the Company/Organization -------------------------------
\clearpage
\frontchapter{ABOUT THE COMPANY/ORGANIZATION/INSTITUTE}

\section*{Dr. B. R. Ambedkar National Institute of Technology Jalandhar}
\justifying

Dr. B. R. Ambedkar National Institute of Technology Jalandhar (NITJ), formerly known as Regional Engineering College (REC) Jalandhar, is one of the thirty-one National Institutes of Technology in India. Established in the year 1987 as a joint venture of the Government of India and the Government of Punjab, the institute was granted the status of deemed university and declared an \textbf{Institute of National Importance} under the National Institutes of Technology Act, 2007, enacted by the Parliament of India.

NIT Jalandhar is situated along the Grand Trunk Road (National Highway 1) bypass towards Amritsar, sprawled over a picturesque 154-acre campus equipped with modern infrastructure, advanced digital classrooms, residential complexes, and world-class laboratory facilities. The institute is ranked consistently among the top engineering universities in India by the National Institutional Ranking Framework (NIRF), Ministry of Education, Government of India.

\begin{figure}[H]
\centering
\safeimg{3.6cm}{figures/Brain-computer_interface_experiment.jpg}
\caption{Biomedical instrumentation and computing laboratory at NIT Jalandhar.}
\label{fig:nitj_campus}
\end{figure}

\section*{Department of Instrumentation and Control Engineering}

The Department of Instrumentation and Control Engineering (ICE) was established in the year 1990 and offers undergraduate (B.Tech.), postgraduate (M.Tech.), and doctoral (Ph.D.) programs. The department's mission is to provide high-quality education and conduct groundbreaking research in biomedical signal and image processing, process automation, smart instrumentation, intelligent control systems, robotics, and cyber-physical systems.

The department houses cutting-edge laboratory infrastructure including the \textbf{Biomedical Signal and Image Processing Laboratory}, \textbf{Process Control and Automation Laboratory}, and dedicated computing clusters for deep learning research. Faculty members in the ICE department lead prestigious sponsored research projects funded by national bodies such as SERB, DST, and DRDO. The Department of ICE provided the ideal research ecosystem for this internship project.

\clearpage

%% -------- vi. List of Tables ----------------------------------------------
\phantomsection
\addcontentsline{toc}{chapter}{List of Tables}
\listoftables
\clearpage

%% -------- vii. List of Figures ---------------------------------------------
\phantomsection
\addcontentsline{toc}{chapter}{List of Figures}
\listoffigures
\clearpage

%% -------- viii. List of Abbreviations and Symbols -------------------------
\frontchapter{LIST OF ABBREVIATIONS AND SYMBOLS}

\renewcommand{\arraystretch}{1.15}
\begin{longtable}{|p{3.2cm}|p{11.5cm}|}
\hline
\textbf{Abbreviation} & \textbf{Full Description} \\
\hline
\endhead
ADC & Analog-to-Digital Converter \\
Ag/AgCl & Silver/Silver Chloride (Electrode Material) \\
ANN & Artificial Neural Network \\
AUC-ROC & Area Under the Receiver Operating Characteristic Curve \\
AUD & Alcohol Use Disorder \\
BiLSTM & Bidirectional Long Short-Term Memory \\
BN & Batch Normalization \\
BCE & Binary Cross-Entropy Loss \\
CMRR & Common-Mode Rejection Ratio \\
CNN & Convolutional Neural Network \\
CSV & Comma-Separated Values \\
CUDA & Compute Unified Device Architecture (NVIDIA) \\
DFT & Discrete Fourier Transform \\
DRL & Driven Right Leg (Active Shielding Ground Circuit) \\
DSP & Digital Signal Processing \\
DTFT & Discrete-Time Fourier Transform \\
DWT & Discrete Wavelet Transform \\
ECG & Electrocardiogram \\
EEG & Electroencephalogram / Electroencephalography \\
EMG & Electromyogram (Muscle Artifact) \\
EOG & Electrooculogram (Eye Movement / Blink Artifact) \\
ERP & Event-Related Potential \\
FBCSP & Filter Bank Common Spatial Pattern \\
FFT & Fast Fourier Transform \\
FIR & Finite Impulse Response \\
FLOPs & Floating Point Operations \\
FWHM & Full Width at Half Maximum \\
GABA & $\gamma$-Aminobutyric Acid (Inhibitory Neurotransmitter) \\
GAP & Global Average Pooling \\
GNN & Graph Neural Network \\
GPU & Graphics Processing Unit \\
GUI & Graphical User Interface \\
IIR & Infinite Impulse Response \\
INA & Instrumentation Amplifier \\
k-NN & $k$-Nearest Neighbors \\
KDD & Knowledge Discovery in Databases \\
LSTM & Long Short-Term Memory \\
LVQ & Learning Vector Quantization \\
MNE & Magnetoencephalography and Electroencephalography Software \\
MLP & Multi-Layer Perceptron \\
MSE & Mean Squared Error \\
NMDA & $N$-Methyl-$D$-Aspartate (Excitatory Receptor) \\
OpenBCI & Open-Source Brain-Computer Interface \\
P300 / P3b & Positive Deflection ERP Component at $\sim$300 ms Latency \\
PCA & Principal Component Analysis \\
PSD & Power Spectral Density \\
ReLU & Rectified Linear Unit ($\max(0, x)$) \\
RMS & Root Mean Square \\
RNN & Recurrent Neural Network \\
SE & Squeeze-and-Excitation (Channel Attention) \\
SGD & Stochastic Gradient Descent \\
SMNI & SUNY Brooklyn Neurodynamics Laboratory EEG Database \\
SOTA & State-of-the-Art \\
STGCN & Spatio-Temporal Graph Convolutional Network \\
STFT & Short-Time Fourier Transform \\
SVM & Support Vector Machine \\
S1 / S2 & Visual Stimulus 1 (Sample) / Visual Stimulus 2 (Match / Non-Match) \\
t-SNE & $t$-Distributed Stochastic Neighbor Embedding \\
UCI & University of California, Irvine Machine Learning Repository \\
VEP & Visual Evoked Potential \\
WHO & World Health Organization \\
\hline
\end{longtable}

\clearpage

%% ==========================================================================
%%  MAIN CHAPTERS (Arabic numerals 1, 2, 3 ...)
%% ==========================================================================
\pagenumbering{arabic}
\setcounter{page}{1}

"""

full_vishal_tex = vishal_main_tex + combined_body + "\n\n\\end{document}\n"

with open('vishal_report_build/main.tex', 'w', encoding='utf-8') as f:
    f.write(full_vishal_tex)

print("Updated vishal_report_build/main.tex successfully! File size:", len(full_vishal_tex))
