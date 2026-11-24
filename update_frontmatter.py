with open('make_sec0_frontmatter.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update TOC and LOF spacing
old_cft = r'''\setlength{\cftbeforechapskip}{1.8pt}
\setlength{\cftbeforesecskip}{0.2pt}
\setlength{\cftbeforesubsecskip}{0.0pt}
\setlength{\cftbeforefigskip}{0.8pt}
\setlength{\cftbeforetabskip}{1.0pt}'''

new_cft = r'''\setlength{\cftbeforechapskip}{1.2pt}
\setlength{\cftbeforesecskip}{0.0pt}
\setlength{\cftbeforesubsecskip}{0.0pt}
\setlength{\cftbeforefigskip}{0.3pt}
\setlength{\cftbeforetabskip}{0.8pt}'''

if old_cft in text:
    text = text.replace(old_cft, new_cft)
else:
    print('Warning: old_cft not found')

# 2. Certificate: make it fit on 1 page strictly
cert_start = text.find('%% -------- Organization Certificate')
cert_end = text.find('%% -------- Candidate\'s Declaration')

new_cert = r'''%% -------- Organization Certificate -----------------------------------------
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

'''

text = text[:cert_start] + new_cert + text[cert_end:]

# 3. About Organization: make it strictly 1 page
abt_start = text.find('%% -------- About the Organization')
abt_end = text.find('%% -------- Table of Contents')

new_abt = r'''%% -------- About the Organization ------------------------------------------
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

'''

text = text[:abt_start] + new_abt + text[abt_end:]

with open('make_sec0_frontmatter.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated frontmatter layout successfully')
