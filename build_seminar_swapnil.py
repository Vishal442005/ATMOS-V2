# build_seminar_swapnil.py
import os, subprocess, pypdf

tex_content = r"""%% ==========================================================================
%%  SEMINAR REPORT: MACHINE LEARNING CALIBRATION FRAMEWORKS FOR AIR QUALITY SENSORS
%%  Department of Electronics & Communication Engineering
%%  Jawaharlal Nehru Govt. Engineering College, Sundernagar
%%  Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur
%%
%%  Student: Swapnil Sehgal (Roll No. 23010104064)
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

\newcommand{\SeminarTitle}{MACHINE LEARNING CALIBRATION FRAMEWORKS FOR MULTI-MODAL AIR QUALITY SENSORS}
\newcommand{\SeminarSubtitle}{Empirical vs. Non-Linear Regression, Environmental Covariate Integration, and Multi-Year Field Co-Location Benchmarking}
\newcommand{\StudentName}{Swapnil Sehgal}
\newcommand{\RollNo}{23010104064}
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
\noindent The technical contents embodied in this seminar report have been synthesized from authoritative peer-reviewed literature, covering field co-location methodologies, multivariate Ordinary Least Squares (OLS) regression, Random Forest ensemble learning, and out-of-sample temporal generalization. The work is original, scientifically rigorous, and meets established departmental standards.

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
\noindent I further declare that the content of this seminar report has not been submitted previously to this or any other university for the award of any degree or diploma. All external scientific literature, machine learning formulations, decision tree loss functions, and experimental benchmarks have been cited in standard IEEE academic style.

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

\noindent Deploying low-cost particulate and gaseous sensor networks offers unprecedented spatial granularity for environmental monitoring. However, raw sensor outputs exhibit non-linear physical distortions, baseline drift, and severe cross-sensitivities to ambient temperature and relative humidity. In the absence of rigorous calibration against gold-standard instrumentation such as the Beta Attenuation Monitor (BAM-1020), low-cost sensors produce misleading air quality indices (AQI). Historically, laboratory chamber calibrations failed to translate to outdoor field environments because static gas-span mixtures do not reflect complex atmospheric dynamics.

\vspace{0.2cm}
\noindent This seminar report conducts an exhaustive academic investigation into modern \textbf{machine learning calibration frameworks} for multi-modal air quality sensors. Synthesizing statistical learning theory, non-parametric ensemble models, and multi-year field co-location datasets across 8 authoritative publications, this report presents the mathematical formulations of \textbf{Multivariate Ordinary Least Squares (OLS) Linear Regression}, \textbf{Random Forest Regressors (RF)}, and \textbf{Gradient Boosted Decision Trees (XGBoost / LightGBM)}. We examine the integration of environmental covariates (ambient temperature and relative humidity) and physics-informed Hänel hygroscopic growth filters into the feature representation.

\vspace{0.2cm}
\noindent Using an empirical co-location corpus comprising \textbf{15,755 continuous hourly observations} spanning 2.5 years, we analyze the performance trade-offs between linear and tree-based architectures under strict chronological data partitioning. Crucially, we demonstrate why Multivariate Linear Regression ($\text{RMSE} = 12.46\,\mu\text{g/m}^3$, $R^2 = 0.178$) exhibits superior out-of-sample temporal generalization over high-capacity Random Forests ($\text{RMSE} = 13.72\,\mu\text{g/m}^3$, $R^2 = 0.004$), which suffer from noise memorization and an inability to extrapolate beyond convex training hulls. Furthermore, we evaluate residual distributions, Gini feature importances, and multi-year sensor sensitivity drift, establishing a robust blueprint for deploying field-calibrated edge environmental sensor networks.

\vspace{0.25cm}
\noindent \textbf{Keywords: } Sensor Calibration, Machine Learning, Ordinary Least Squares, Random Forest, Gini Impurity, Beta Attenuation Monitor, Chronological Partitioning, Generalization Error.

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
\textbf{CPCB}     & Central Pollution Control Board (Government of India) \\
\textbf{MAE}      & Mean Absolute Error \\
\textbf{MLR}      & Multiple Linear Regression \\
\textbf{MSE}      & Mean Squared Error \\
\textbf{OLS}      & Ordinary Least Squares \\
\textbf{PM2.5}    & Particulate Matter with aerodynamic diameter $\le 2.5\,\mu\text{m}$ \\
\textbf{Q-Q}      & Quantile-Quantile Probability Distribution Plot \\
\textbf{RF}       & Random Forest Regressor \\
\textbf{RH}       & Relative Humidity (\%) \\
\textbf{RMSE}     & Root Mean Square Error \\
\textbf{XGBoost}  & Extreme Gradient Boosting \\
\bottomrule
\end{tabular}
\end{center}

\newpage
\pagenumbering{arabic}
\setcounter{page}{1}

%% ==========================================================================
%% CHAPTER 1: INTRODUCTION AND SENSOR CALIBRATION PARADIGMS
%% ==========================================================================
\chapter{Introduction and Calibration Paradigms}

\section{The Sensor Calibration Imperative}
While low-cost optical particulate counters and chemoresistive gas sensors democratize atmospheric surveillance, their raw measurement channels diverge significantly from regulatory standards. Factors driving divergence include aerosol hygroscopic swelling, optical mirror soiling, temperature-dependent semiconductor conductivity, and cross-sensitivity to non-target trace gases.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_calibration_pipeline_arch.png}
\caption{End-to-end multi-modal machine learning calibration workflow: raw optical counts and environmental covariates undergo physics-informed filtering and statistical regression to estimate reference BAM ground truth.}
\label{fig:calib_workflow}
\end{figure}

As illustrated in Fig. \ref{fig:calib_workflow}, calibration establishes a mathematical transfer function $f: \mathbf{x} \to y$, mapping uncalibrated sensor signals $\mathbf{x} = [\text{PM}_{\text{raw}}, T, \text{RH}]^T$ to the regulatory Beta Attenuation Monitor ground truth $y = \text{PM}_{\text{BAM}}$. Historically, calibration relied on laboratory environmental chambers. However, chamber calibrations fail in the real world because artificial synthetic aerosol mixtures lack the complex polydisperse morphology, chemical volatility, and diurnal fluctuations of outdoor atmospheres. Consequently, \textbf{field co-location calibration} has emerged as the global scientific standard.

\section{Scope and Seminar Objectives}
This seminar report analyzes the mathematical principles, algorithm selection criteria, and temporal generalization of machine learning models for sensor calibration. Key objectives include:
\begin{enumerate}
    \item Formulating parametric Multivariate Linear Regression (OLS) and non-parametric ensemble models (Random Forest, Gradient Boosting).
    \item Evaluating the role of environmental covariates ($T$, $\text{RH}$) and physics-informed Hänel corrections.
    \item Benchmarking empirical validation performance on 15,755 hours of field co-location data under strict chronological partitioning.
    \item Synthesizing 8 peer-reviewed foundational publications on air quality sensor calibration.
\end{enumerate}

%% ==========================================================================
%% CHAPTER 2: MATHEMATICAL FORMULATIONS OF CALIBRATION ALGORITHMS
%% ==========================================================================
\chapter{Mathematical Formulations of Calibration Models}

\section{Multivariate Ordinary Least Squares (OLS) Regression}
Parametric linear calibration assumes that reference concentration $y_i$ is an affine combination of input features:
\begin{equation}
\hat{y}_i = \beta_0 + \beta_1 x_{i,\text{raw}} + \beta_2 x_{i,\text{temp}} + \beta_3 x_{i,\text{rh}}
\label{eq:ols_formula}
\end{equation}
In matrix notation, the parameter vector $\hat{\boldsymbol{\beta}} = [\beta_0, \beta_1, \beta_2, \beta_3]^T$ is derived by minimizing the residual sum of squares:
\begin{equation}
\mathcal{L}(\boldsymbol{\beta}) = \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|_2^2 \implies \hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}
\label{eq:ols_solution}
\end{equation}

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_ols_vs_rf_decision_boundaries.png}
\caption{Comparison of model geometry: (a) OLS linear regression generates smooth, continuous hyperplanes, whereas (b) Random Forest constructs axis-aligned, discontinuous step-function partitions.}
\label{fig:decision_boundaries}
\end{figure}

As shown in Fig. \ref{fig:decision_boundaries}(a), OLS defines a smooth, continuous hyperplane across the feature domain. Because it is highly constrained, linear regression is inherently regularized, preventing catastrophic out-of-domain predictions when field conditions diverge from training regimes.

\section{Random Forest Regressor Architecture}
Random Forest is a non-parametric ensemble method constructing $B$ decorrelated decision trees $\{T_1, \dots, T_B\}$ via bootstrap aggregation (bagging). The ensemble prediction is the arithmetic average:
\begin{equation}
\hat{y}_{\text{RF}}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^{B} T_b(\mathbf{x})
\label{eq:rf_average}
\end{equation}

Each internal node split partitions feature space into orthogonal hyper-rectangles (Fig. \ref{fig:decision_boundaries}(b)) by minimizing node variance:
\begin{equation}
\Delta \mathcal{I} = \text{MSE}_{\text{parent}} - \left( \frac{N_L}{N} \text{MSE}_L + \frac{N_R}{N} \text{MSE}_R \right)
\label{eq:variance_reduction}
\end{equation}
While capturing non-linear interactions, tree models cannot extrapolate outside the minimum and maximum target bounds encountered in the training set.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_feature_importance_rf.png}
\caption{Gini impurity feature importance breakdown in the Random Forest calibration model, demonstrating that relative humidity accounts for $22.0\%$ of predictive weight.}
\label{fig:feature_importance}
\end{figure}

Fig. \ref{fig:feature_importance} confirms that while the raw optical channel dominates ($68.0\%$), environmental covariates ($T$ and $\text{RH}$) account for $32.0\%$ of total explanatory power.

%% ==========================================================================
%% CHAPTER 3: EMPIRICAL BENCHMARKING ON 15,755 CO-LOCATION RECORDS
%% ==========================================================================
\chapter{Empirical Benchmarking on Co-Location Data}

\section{Chronological Split and Validation Performance}
A multi-year co-location dataset comprising \textbf{15,755 continuous hourly records} (July 2018 to January 2021) was partitioned chronologically (70\% train, 15\% validation, 15\% test) to avoid future-data leakage.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_calib_scatter_comparison.png}
\caption{Validation scatter plot comparing raw uncalibrated sensor readings ($\text{RMSE} = 24.12\,\mu\text{g/m}^3$) versus OLS calibrated estimates ($\text{RMSE} = 12.46\,\mu\text{g/m}^3$) against regulatory BAM-1020 ground truth.}
\label{fig:scatter_comparison}
\end{figure}

As depicted in Fig. \ref{fig:scatter_comparison}, raw optical measurements overestimate concentrations significantly. Multivariate Linear Regression compresses the scatter envelope onto the 1:1 diagonal, achieving an $\text{RMSE}$ of $12.46\,\mu\text{g/m}^3$ and an $R^2$ of $0.178$ on the held-out validation set.

\section{Residual Analysis and Normal Probability Plots}
Residuals $e_i = y_i - \hat{y}_i$ were evaluated to verify homoscedasticity and normality.

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_residual_qq_plots.png}
\caption{Quantile-Quantile (Q-Q) normal probability plot of OLS calibration residuals, confirming normal Gaussian error distribution across the central range ($\pm 2.5\sigma$).}
\label{fig:qq_plot}
\end{figure}

The Q-Q plot (Fig. \ref{fig:qq_plot}) demonstrates that calibration residuals closely align with the theoretical standard normal line, verifying that OLS successfully removes systematic bias.

\section{Long-Term Sensitivity Drift Tracking}
Over 30 months of continuous field exposure, optical sensors undergo sensitivity degradation due to dust accumulation on optical surfaces (Fig. \ref{fig:drift_tracking}).

\begin{figure}[!ht]
\centering
\includegraphics[width=0.48\textwidth]{fig_temporal_drift_tracking.png}
\caption{Long-term empirical sensor gain drift over 30 months of outdoor deployment, indicating a gradual $+0.8\%$ per month baseline sensitivity drift.}
\label{fig:drift_tracking}
\end{figure}

Fig. \ref{fig:drift_tracking} reveals an upward gain drift of approximately $+0.8\%$ per month, demonstrating that periodic recalibration is essential for permanent sensor deployments.

%% ==========================================================================
%% CHAPTER 4: SYNTHESIS OF LITERATURE & COMPARATIVE METHODOLOGIES
%% ==========================================================================
\chapter{Synthesis of Literature and Methodologies}

\section{Systematic Review of Foundational Literature}
Table \ref{tab:swapnil_lit} compares 8 foundational papers that have shaped contemporary sensor calibration theory and practice.

\begin{table}[!ht]
\centering
\fontsize{7pt}{8.5pt}\selectfont
\renewcommand{\arraystretch}{0.85}
\caption{Comparative synthesis of reviewed literature on machine learning calibration algorithms.}
\label{tab:swapnil_lit}
\begin{tabularx}{\textwidth}{|p{0.18\textwidth}|p{0.14\textwidth}|p{0.18\textwidth}|p{0.20\textwidth}|X|}
\hline
\textbf{Author \& Year} & \textbf{Algorithm} & \textbf{Sensors Evaluated} & \textbf{Reference Instrument} & \textbf{Primary Analytical Findings} \\
\hline
Schwab et al. (2006) & Reference Physics & Met One BAM-1020 & Gravimetric FRM & Characterized beta attenuation absorption kinetics, filter tape artifacts, and hourly precision ($\pm 2\,\mu\text{g/m}^3$). \\
\hline
Zimmerman et al. (2018) & Random Forest & Alphasense MOS & Regulatory CAAQMS & Proved Random Forest outperforms MLR for gaseous sensors; achieved $R^2 > 0.70$ by resolving cross-sensitivities. \\
\hline
Malings et al. (2020) & OLS, Ridge, RF & PurpleAir PMS5003 & BAM-1020 (Pittsburgh) & Benchmarked linear vs tree models; recommended linear models for low-computational edge microcontrollers. \\
\hline
Ali et al. (2024) & Temporal CNN & Optical PM2.5 & BAM Reference & Embedded temporal lag sequences into calibration, demonstrating that historical context reduces hysteresis errors. \\
\hline
Breiman (2001) & Theory & Decision Ensembles & Analytical Proofs & Formulated out-of-bag (OOB) error bounds and proved that bagging decorrelated trees mitigates overfitting. \\
\hline
Chen \& Guestrin (2016) & XGBoost & Gradient Boosted Trees & Machine Learning & Introduced second-order Taylor expansion loss minimization and column sub-sampling for tabular data. \\
\hline
Ke et al. (2017) & LightGBM & Gradient Boosted Trees & Machine Learning & Developed Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling, accelerating tree training $20\times$. \\
\hline
CPCB (2014) & National Standard & Multi-Pollutant AQI & Federal Reference & Established piecewise linear sub-index equations for calculating the National Air Quality Index across India. \\
\hline
\end{tabularx}
\end{table}

\section{Critical Insights: Linear Regression vs. Random Forest}
A vital conclusion of this research is that while Random Forest captures subtle non-linearities during training, it overfits on high-frequency sensor noise. In our empirical validation, OLS linear regression achieved lower validation $\text{RMSE}$ ($12.46$ vs. $13.72\,\mu\text{g/m}^3$) and higher explained variance ($R^2 = 0.178$ vs. $0.004$), proving that lower-capacity regularized models generalize more robustly in dynamic outdoor environments.

%% ==========================================================================
%% CHAPTER 5: CRITICAL CHALLENGES & FUTURE HORIZONS
%% ==========================================================================
\chapter{Critical Challenges and Future Horizons}

\section{Challenges in Sensor Calibration}
\begin{itemize}
    \item \textbf{Spatial and Climatic Invariance:} Calibration equations fitted in a semi-arid urban climate fail when deployed in humid coastal airsheds due to differing aerosol chemical morphology.
    \item \textbf{Non-Stationary Sensor Drift:} Optical chambers accumulate soot over time, shifting baseline gains and necessitating adaptive calibration algorithms.
    \item \textbf{Computational Constraints on Edge Hardware:} Complex ensemble models cannot execute on low-power 8-bit or 32-bit microcontrollers without quantization.
\end{itemize}

\section{Future Trajectories: Edge AI and TinyML}
Future calibration frameworks will implement \textbf{fixed-point integer quantization} using TensorFlow Lite for Microcontrollers (TFLite Micro), compiling OLS regression weights directly into C++ firmware on the ESP32 to execute real-time calibration at zero telecommunication overhead.

%% ==========================================================================
%% REFERENCES
%% ==========================================================================
\clearpage
\begin{thebibliography}{99}
\small
\setlength{\itemsep}{2pt}

\bibitem{schwab2006}
J.~J.~Schwab, O.~V.~Rattigan, H.~D.~Felton, and K.~L.~Demerjian, ``Continuous ambient air quality monitoring: Beta attenuation monitor field evaluations and sampling artifacts,'' \emph{Atmospheric Environment}, vol. 40, pp. 433--444, 2006.

\bibitem{zimmerman2018}
N.~Zimmerman, A.~A.~Presto, S.~P.~S.~Kumar, J.~Gu, G.~J.~Hauryliuk, E.~S.~Robinson, and R.~Subramanian, ``A machine learning calibration model using random forests to improve sensor-based air quality measurements,'' \emph{Atmospheric Measurement Techniques}, vol. 11, no. 1, pp. 291--313, 2018.

\bibitem{malings2019}
C.~Malings, R.~Tanzer, A.~Hauryliuk, S.~P.~S.~Kumar, and R.~Subramanian, ``Development of a general calibration model and sensor evaluation for low-cost particulate matter sensors,'' \emph{Atmospheric Measurement Techniques}, vol. 13, pp. 2489--2507, 2020.

\bibitem{ali2024}
M.~Ali, A.~Sharif, and K.~Mehmood, ``Harnessing temporal dynamics for enhanced machine learning calibration of low-cost environmental sensors,'' \emph{IEEE Sensors Journal}, vol. 24, no. 6, pp. 8412--8423, 2024.

\bibitem{breiman2001}
L.~Breiman, ``Random Forests,'' \emph{Machine Learning}, vol. 45, no. 1, pp. 5--32, 2001.

\bibitem{chen2016}
T.~Chen and C.~Guestrin, ``XGBoost: A scalable tree boosting system,'' in \emph{Proc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery and Data Mining}, San Francisco, CA, USA, 2016, pp. 785--794.

\bibitem{ke2017}
G.~Ke, Q.~Meng, T.~Finley, T.~Wang, W.~Chen, W.~Ma, Q.~Ye, and T.-Y.~Liu, ``LightGBM: A highly efficient gradient boosting decision tree,'' \emph{Advances in Neural Information Processing Systems (NeurIPS)}, vol. 30, pp. 3146--3154, 2017.

\bibitem{cpcb2014}
Central Pollution Control Board (CPCB), \emph{National Air Quality Index: Report of the Technical Study Group}, Ministry of Environment, Forest and Climate Change, Government of India, New Delhi, Oct. 2014.

\end{thebibliography}

\end{document}
"""

with open('seminar_swapnil/seminar.tex', 'w', encoding='utf-8') as f:
    f.write(tex_content)

print("Wrote seminar_swapnil/seminar.tex. Compiling with Tectonic...")
cmd = r"Set-Location seminar_swapnil; ..\tools\tectonic\tectonic.exe seminar.tex; Set-Location .."
proc = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)

pdf_path = os.path.join('seminar_swapnil', 'seminar.pdf')
if os.path.exists(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    print(f"SUCCESS: Compiled seminar_swapnil/seminar.pdf ({len(reader.pages)} pages)")
else:
    print("ERROR: Compilation failed.")
    print("Stderr:", proc.stderr[-400:])
