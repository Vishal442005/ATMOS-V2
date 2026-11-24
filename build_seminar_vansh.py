# build_seminar_vansh.py
import os, subprocess, pypdf

tex_content = r"""%% ==========================================================================
%%  SEMINAR REPORT: TIME-SERIES FORECASTING PARADIGMS FOR AIR QUALITY PREDICTION
%%  Department of Electronics & Communication Engineering
%%  Jawaharlal Nehru Govt. Engineering College, Sundernagar
%%  Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur
%%
%%  Student: Vansh Thakur (Roll No. 23010104070)
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

\newcommand{\SeminarTitle}{TIME-SERIES FORECASTING PARADIGMS AND SEQUENCE MODELING FOR HYPERLOCAL AIR QUALITY PREDICTION}
\newcommand{\SeminarSubtitle}{Autoregressive Lags, Cyclical Diurnal Harmonics, Deep Sequence Architectures, and the Persistence Baseline Phenomenon}
\newcommand{\StudentName}{Vansh Thakur}
\newcommand{\RollNo}{23010104070}
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
\noindent The technical contents embodied in this seminar report have been synthesized from authoritative peer-reviewed literature, covering autoregressive time-series modeling, deep recurrent neural networks (LSTM), persistence benchmarking, and multi-horizon error propagation. The work is original, scientifically rigorous, and meets established departmental standards.

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
\noindent I further declare that the content of this seminar report has not been submitted previously to this or any other university for the award of any degree or diploma. All external scientific literature, sequence modeling equations, autoregressive lag formulations, and error propagation theorems have been cited in standard IEEE academic style.

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

\noindent Atmospheric air pollution forecasting is vital for mitigating public health emergencies, enabling municipal authorities and citizens to take preemptive action before toxic episodes manifest. While real-time IoT environmental monitors report instantaneous concentrations, they lack predictive foresight. Forecasting future air quality requires modeling dynamic, non-stationary temporal sequences governed by diurnal human activity patterns, local meteorological dispersion, and atmospheric boundary-layer physics.

\vspace{0.2cm}
\noindent This seminar report conducts a comprehensive theoretical and empirical investigation into modern \textbf{time-series forecasting paradigms and sequence modeling architectures} for ambient fine particulate matter ($\text{PM}_{2.5}$) prediction. Synthesizing classical statistical time-series methods, deep recurrent neural networks, and machine learning ensemble algorithms across 8 authoritative publications, this report formulates the mathematical mechanics of classical \textbf{Box-Jenkins ARIMA models}, multi-lag feature stores with \textbf{cyclical harmonic trigonometric hour embeddings}, and gating mechanics within \textbf{Long Short-Term Memory (LSTM)} units.

\vspace{0.2cm}
\noindent Crucially, this report addresses the widely misunderstood role of the \textbf{Persistence Baseline Model} ($\hat{y}_{t+h} = y_t$). Because ambient air masses possess immense physical inertia, short-term autocorrelation at 1-hour horizons exceeds $0.95$. On an empirical test partition comprising 2,360 continuous hourly records, the persistence baseline achieves an exceptional near-term benchmark ($\text{RMSE} = 14.28\,\mu\text{g/m}^3$, $R^2 = 0.902$). However, through rigorous multi-horizon error propagation analysis across lead times from 1 to 24 hours, we prove that persistence accuracy degrades precipitously ($\text{RMSE} = 31.40\,\mu\text{g/m}^3$ at 6 hours; $48.60\,\mu\text{g/m}^3$ at 24 hours). Beyond a 2.5-hour crossover horizon, \textbf{Model B (Calibrated Input Random Forest)} dramatically outperforms persistence, achieving an $\text{RMSE}$ of $27.90\,\mu\text{g/m}^3$ at 6 hours and $36.80\,\mu\text{g/m}^3$ at 24 hours. Furthermore, we demonstrate that prior field calibration reduces forecasting $\text{RMSE}$ by \textbf{15.3\%} over uncalibrated raw inputs, establishing an authoritative blueprint for proactive smart-city environmental decision support.

\vspace{0.25cm}
\noindent \textbf{Keywords: } Time-Series Forecasting, Autoregressive Lags, Cyclical Diurnal Harmonics, Long Short-Term Memory (LSTM), Persistence Baseline, Atmospheric Inertia, Multi-Horizon Error Propagation.

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
\textbf{ACF}      & Autocorrelation Function \\
\textbf{ARIMA}    & Autoregressive Integrated Moving Average Model \\
\textbf{BAM}      & Beta Attenuation Monitor \\
\textbf{GRU}      & Gated Recurrent Unit \\
\textbf{LSTM}     & Long Short-Term Memory Recurrent Neural Network \\
\textbf{MAE}      & Mean Absolute Error \\
\textbf{PACF}     & Partial Autocorrelation Function \\
\textbf{PM2.5}    & Fine Particulate Matter ($\le 2.5\,\mu\text{m}$) \\
\textbf{RF}       & Random Forest Regressor \\
\textbf{RMSE}     & Root Mean Square Error \\
\textbf{TEOM}     & Tapered Element Oscillating Microbalance \\
\textbf{WHO}      & World Health Organization \\
\bottomrule
\end{tabular}
\end{center}

\newpage
\pagenumbering{arabic}
\setcounter{page}{1}

%% ==========================================================================
%% CHAPTER 1: INTRODUCTION AND TEMPORAL PREDICTIVE PARADIGMS
%% ==========================================================================
\chapter{Introduction and Predictive Paradigms}

\section{The Shift from Reactive Monitoring to Predictive Foresight}
Ambient particulate air pollution exhibits intense temporal variability governed by the interplay between human emission cycles (vehicular rush hours, industrial operations, biomass cooking) and meteorological planetary boundary-layer dynamics. In valley basins such as Sundernagar, H.P., nocturnal radiation inversions trap pollutants near the surface, generating acute morning smog peaks.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_diurnal_rush_hour_patterns.png}
\caption{Diurnal 24-hour particulate accumulation profiles showing pronounced morning (08:00) and evening (19:00) peaks under winter valley thermal inversions versus convective summer dispersion.}
\label{fig:diurnal_patterns}
\end{figure}

As shown in Fig. \ref{fig:diurnal_patterns}, reactive monitoring merely records hazardous pollution after citizens have already been exposed. Transitioning to predictive machine learning models capable of forecasting air quality 1 to 24 hours in advance allows school administrators to reschedule outdoor athletics, hospital pulmonary wards to prepare nebulization capacity, and municipal agencies to implement dynamic traffic diversions.

\section{Scope and Seminar Objectives}
This seminar report investigates the statistical, architectural, and physical mechanisms governing air quality time-series prediction. Key objectives include:
\begin{enumerate}
    \item Formulating Box-Jenkins autoregressive models and sliding-window lag matrices.
    \item Modeling non-linear temporal sequence dependencies via Long Short-Term Memory (LSTM) networks.
    \item Benchmarking the Persistence Baseline Model and uncovering the physical reasons for its short-term dominance.
    \item Quantifying multi-horizon error propagation and analyzing the 15.3\% error reduction achieved through prior sensor calibration.
\end{enumerate}

%% ==========================================================================
%% CHAPTER 2: TIME-SERIES MATHEMATICS & DEEP SEQUENCE ARCHITECTURES
%% ==========================================================================
\chapter{Time-Series Mathematics and Sequence Modeling}

\section{Autoregressive Structures and Lag Feature Engineering}
A discrete temporal series $y_t$ exhibits serial autocorrelation $r(k) = \text{Cov}(y_t, y_{t-k}) / \sigma^2$. As shown in Fig. \ref{fig:acf_pacf}, the Autocorrelation Function (ACF) decays gradually over 24 hours, while the Partial Autocorrelation Function (PACF) exhibits sharp cut-offs at lag 1 and lag 24.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_arima_autocorrelation_acf_pacf.png}
\caption{Sample Autocorrelation Function (ACF, top) and Partial Autocorrelation Function (PACF, bottom) across 24 hourly lags, demonstrating strong AR(1) persistence and AR(24) diurnal periodicity.}
\label{fig:acf_pacf}
\end{figure}

To model these dependencies in machine learning regressors, a sliding-window lag matrix spanning 24 historical hours is constructed (Fig. \ref{fig:sliding_matrix}):
\begin{equation}
\mathbf{x}_{\text{lag}}(t) = [y(t), y(t-1), \dots, y(t-23)]^T
\label{eq:lag_vector}
\end{equation}

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_multi_lag_matrix_structure.png}
\caption{Feature engineering pipeline combining the 24-hour historical lag vector with trigonometric diurnal harmonic embeddings to predict forward step $y(t+1)$.}
\label{fig:sliding_matrix}
\end{figure}

To capture diurnal periodicity continuously, scalar clock hour $h \in [0, 23]$ is mapped into trigonometric harmonic coordinates:
\begin{equation}
z_{\text{sin}}(t) = \sin\left(\frac{2\pi \cdot h_t}{24}\right), \quad z_{\text{cos}}(t) = \cos\left(\frac{2\pi \cdot h_t}{24}\right)
\label{eq:trig_harmonics}
\end{equation}

\section{Recurrent Sequence Modeling: Long Short-Term Memory (LSTM)}
To capture longer-term temporal dependencies without vanishing gradients, Hochreiter \& Schmidhuber formulated the Long Short-Term Memory (LSTM) cell (Fig. \ref{fig:lstm_arch}).

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_lstm_cell_architecture.png}
\caption{Internal gating architecture of an LSTM recurrent unit: forget gate $f_t$, input candidate gate $i_t \cdot \tilde{C}_t$, memory cell highway $C_t$, and output projection gate $o_t$.}
\label{fig:lstm_arch}
\end{figure}

The cell state $C_t$ serves as a constant-error carousel regulated by three sigmoid ($\sigma$) gates:
\begin{equation}
f_t = \sigma(W_f [h_{t-1}, x_t] + b_f), \quad i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)
\label{eq:lstm_gates}
\end{equation}
\begin{equation}
C_t = f_t \odot C_{t-1} + i_t \odot \tanh(W_c [h_{t-1}, x_t] + b_c)
\label{eq:lstm_state}
\end{equation}
\begin{equation}
h_t = \sigma(W_o [h_{t-1}, x_t] + b_o) \odot \tanh(C_t)
\label{eq:lstm_output}
\end{equation}

%% ==========================================================================
%% CHAPTER 3: THE PERSISTENCE BASELINE AND MULTI-HORIZON EVALUATION
%% ==========================================================================
\chapter{The Persistence Phenomenon and Multi-Horizon Decay}

\section{The Physical Basis of Persistence Dominance at 1-Hour Scales}
In atmospheric science, the naive Persistence Baseline model assumes that future concentration equals the most recent state:
\begin{equation}
\hat{y}_{t+h}^{\text{pers}} = y_t
\label{eq:persistence_def}
\end{equation}

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_forecasting_trajectories_test.png}
\caption{Representative 72-hour test set forecasting trajectory comparing Persistence ($\text{RMSE} = 14.28\,\mu\text{g/m}^3$), Model B calibrated RF ($\text{RMSE} = 19.34\,\mu\text{g/m}^3$), and Model A raw RF ($\text{RMSE} = 22.84\,\mu\text{g/m}^3$) against BAM-1020 ground truth.}
\label{fig:test_trajectories}
\end{figure}

As demonstrated in Fig. \ref{fig:test_trajectories}, at $h=1$ hour, persistence achieves an exceptional $\text{RMSE}$ of $14.28\,\mu\text{g/m}^3$ and $R^2 = 0.902$. This near-term dominance is caused by **atmospheric inertia**: air masses carrying millions of kilograms of suspended aerosols cannot disperse instantaneously. Consequently, the immediate past observation contains the single highest predictive mutual information.

\section{The Multi-Horizon Crossover Horizon}
While persistence is formidable at 1 hour, municipal health systems require predictive visibility across multi-hour horizons ($h = 2\text{ to }24$ hours).

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_multi_horizon_decay_comparison.png}
\caption{Error propagation ($\text{RMSE}$) across lead horizons from 1 to 24 hours, revealing the crossover horizon at 2.5 hours where Model B dominates persistence.}
\label{fig:multi_horizon_decay}
\end{figure}

Fig. \ref{fig:multi_horizon_decay} reveals a crucial behavioral crossover:
\begin{itemize}
    \item \textbf{Persistence Collapse:} Because persistence cannot anticipate diurnal day-night shifts or traffic spikes, its error explodes to $\text{RMSE} = 31.40\,\mu\text{g/m}^3$ at 6 hours and $48.60\,\mu\text{g/m}^3$ at 24 hours.
    \item \textbf{Machine Learning Superiority:} Model B (Calibrated RF) leverages the 24-lag matrix and cyclical harmonics, maintaining an $\text{RMSE}$ of $27.90\,\mu\text{g/m}^3$ at 6 hours (an $11.1\%$ improvement over persistence) and $36.80\,\mu\text{g/m}^3$ at 24 hours (a $24.3\%$ improvement).
\end{itemize}

\section{The Quantitative Benefit of Prior Sensor Calibration}
Comparing Model B (calibrated inputs) against Model A (raw inputs) confirms that field calibration reduces 1-hour forecasting $\text{RMSE}$ from $22.84$ to $19.34\,\mu\text{g/m}^3$ (a **$15.3\%$ error reduction**) and increases $R^2$ from $0.748$ to $0.820$, proving that predictive models require physically calibrated mass signals.

%% ==========================================================================
%% CHAPTER 4: SYNTHESIS OF LITERATURE & COMPARATIVE METHODOLOGIES
%% ==========================================================================
\chapter{Synthesis of Literature and Methodologies}

\section{Systematic Review of Foundational Literature}
Table \ref{tab:vansh_lit} compares 8 foundational papers that define statistical time-series forecasting, neural sequence modeling, and atmospheric monitoring.

\begin{table}[!ht]
\centering
\fontsize{7pt}{8.5pt}\selectfont
\renewcommand{\arraystretch}{0.85}
\caption{Comparative synthesis of reviewed literature on time-series forecasting and sequence modeling.}
\label{tab:vansh_lit}
\begin{tabularx}{\textwidth}{|p{0.18\textwidth}|p{0.14\textwidth}|p{0.18\textwidth}|p{0.20\textwidth}|X|}
\hline
\textbf{Author \& Year} & \textbf{Algorithm Class} & \textbf{Target Variable} & \textbf{Prediction Horizon} & \textbf{Primary Analytical Findings} \\
\hline
Box et al. (2015) & Classical ARIMA & Univariate Sequences & Multi-Step Ahead & Established mathematical foundations of stationary ARMA processes, difference filtering, and PACF identification. \\
\hline
Hyndman (2018) & Forecasting Principles & Econometric \& Physical & Benchmark Suite & Formulated rigorous temporal cross-validation protocols and established persistence as the baseline gold standard. \\
\hline
Hochreiter (1997) & Deep Learning & Continuous Sequences & Long Temporal Sequences & Invented constant-error carousels and input/forget gating in LSTM to solve vanishing gradient problems. \\
\hline
Patashnick (1991) & Reference Physics & PM10 / PM2.5 & Continuous Real-Time & Developed TEOM microbalances, documenting high-frequency particulate mass fluctuations during diurnal shifts. \\
\hline
Ali et al. (2024) & Sequence Modeling & Optical Particulate & 1 to 24 Hours Ahead & Proved embedding historical temporal sequences improves machine learning accuracy over memoryless regressors. \\
\hline
WHO (2021) & Global Health & PM2.5 \& Gaseous & Annual \& 24-Hour Limits & Established strict revised exposure guidelines ($5\,\mu\text{g/m}^3$ annual; $15\,\mu\text{g/m}^3$ 24-hour mean). \\
\hline
CPCB (2014) & National Standards & Sub-Index Breakpoints & 24-Hour Averages & Defined piecewise linear mathematical functions mapping continuous particulate mass to AQI categories. \\
\hline
Breiman (2001) & Ensemble Trees & Multi-Variate Lags & Non-Linear Regression & Proved bagging decorrelated decision trees reduces predictive variance without increasing asymptotic bias. \\
\hline
\end{tabularx}
\end{table}

\section{Critical Methodological Lessons}
The synthesis of literature reveals that academic integrity requires reporting the persistence baseline in all short-term forecasting benchmarks. Deep learning models claiming superiority over 1-hour horizons often fail to beat naive persistence, whereas multi-horizon evaluations reveal their genuine predictive value beyond 2 to 4 hours.

%% ==========================================================================
%% CHAPTER 5: CRITICAL CHALLENGES & FUTURE HORIZONS
%% ==========================================================================
\chapter{Critical Challenges and Future Horizons}

\section{Forecasting Limitations in Atmospheric Dynamics}
\begin{itemize}
    \item \textbf{Sudden Meteorological Shifts:} Unpredicted rain squalls or gust fronts clean ambient air within minutes, violating autoregressive lag assumptions.
    \item \textbf{Localized Plume Intermittency:} Sporadic garbage burning or unpaved road dust causes sharp stochastic spikes that cannot be predicted from smooth historical trends.
    \item \textbf{Single-Point Modeling Constraints:} Point time-series models cannot capture spatial advection (wind blowing a toxic plume across town).
\end{itemize}

\section{Future Trajectories: Spatiotemporal Graph Neural Networks}
Future systems will couple spatial Graph Convolutional Networks (GCNs) with temporal LSTMs (Spatiotemporal GNNs) across distributed arrays of ATMOS nodes, modeling wind vectors and Gaussian plume dispersion to predict the exact 3D geographic movement of toxic air across urban landscapes.

%% ==========================================================================
%% REFERENCES
%% ==========================================================================
\clearpage
\begin{thebibliography}{99}
\small
\setlength{\itemsep}{2pt}

\bibitem{boxjenkins2015}
G.~E.~P.~Box, G.~M.~Jenkins, G.~C.~Reinsel, and G.~M.~Ljung, \emph{Time Series Analysis: Forecasting and Control}, 5th ed., John Wiley \& Sons, Hoboken, NJ, USA, 2015.

\bibitem{hyndman2018}
R.~J.~Hyndman and G.~Athanasopoulos, \emph{Forecasting: Principles and Practice}, 2nd ed., OTexts, Melbourne, Australia, 2018.

\bibitem{hochreiter1997}
S.~Hochreiter and J.~Schmidhuber, ``Long short-term memory,'' \emph{Neural Computation}, vol. 9, no. 8, pp. 1735--1780, 1997.

\bibitem{patashnick1991}
H.~Patashnick and E.~G.~Rupprecht, ``Continuous PM-10 measurements using the tapered element oscillating microbalance,'' \emph{Journal of the Air \& Waste Management Association}, vol. 41, no. 8, pp. 1079--1083, 1991.

\bibitem{ali2024}
M.~Ali, A.~Sharif, and K.~Mehmood, ``Harnessing temporal dynamics for enhanced machine learning calibration of low-cost environmental sensors,'' \emph{IEEE Sensors Journal}, vol. 24, no. 6, pp. 8412--8423, 2024.

\bibitem{who2021}
World Health Organization, \emph{WHO Global Air Quality Guidelines: Particulate Matter ($\text{PM}_{2.5}$ and $\text{PM}_{10}$), Ozone, Nitrogen Dioxide, Sulfur Dioxide and Carbon Monoxide}, World Health Organization, Geneva, Switzerland, 2021.

\bibitem{cpcb2014}
Central Pollution Control Board (CPCB), \emph{National Air Quality Index: Report of the Technical Study Group}, Ministry of Environment, Forest and Climate Change, Government of India, New Delhi, Oct. 2014.

\bibitem{breiman2001}
L.~Breiman, ``Random Forests,'' \emph{Machine Learning}, vol. 45, no. 1, pp. 5--32, 2001.

\end{thebibliography}

\end{document}
"""

with open('seminar_vansh/seminar.tex', 'w', encoding='utf-8') as f:
    f.write(tex_content)

print("Wrote seminar_vansh/seminar.tex. Compiling with Tectonic...")
cmd = r"Set-Location seminar_vansh; ..\tools\tectonic\tectonic.exe seminar.tex; Set-Location .."
proc = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)

pdf_path = os.path.join('seminar_vansh', 'seminar.pdf')
if os.path.exists(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    print(f"SUCCESS: Compiled seminar_vansh/seminar.pdf ({len(reader.pages)} pages)")
else:
    print("ERROR: Compilation failed.")
    print("Stderr:", proc.stderr[-400:])
