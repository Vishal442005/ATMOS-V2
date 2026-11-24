import os

with open('make_sec0_frontmatter.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_toc = text.find('%% -------- Table of Contents, Tables, Figures, Abbreviations ---------------')
pos_end_table = text.find(r'\end{longtable}', pos_toc)
clean_end = pos_end_table + len(r'\end{longtable}') + 1

# Cut everything after clean_end and add \n"""\n
trimmed = text[:clean_end] + '\n"""\n'

# Now replace the About Organization section inside trimmed
abt_marker = '%% -------- About the Organization ------------------------------------------'
pos_abt = trimmed.find(abt_marker)
pos_toc2 = trimmed.find('%% -------- Table of Contents', pos_abt)

new_abt_section = r'''%% -------- About the Organization ------------------------------------------
\clearpage
\frontchapter{ABOUT THE COMPANY/ORGANIZATION/INSTITUTE}

\begin{center}
  \IfFileExists{figures/nit_jalandhar_logo.png}{\includegraphics[height=1.8cm]{figures/nit_jalandhar_logo.png}\\[0.15cm]}{}
  {\fontsize{13pt}{16pt}\bfseries DR. B. R. AMBEDKAR NATIONAL INSTITUTE OF TECHNOLOGY JALANDHAR}\\[0.08cm]
  \textit{\small An Institute of National Importance under Ministry of Education, Government of India}\\[0.05cm]
  \textit{\footnotesize G.T. Road, Amritsar Bypass, Jalandhar, Punjab -- 144008, India}
\end{center}
\vspace{-0.2cm}\hrule\vspace{0.3cm}

\justifying
\textbf{Dr. B. R. Ambedkar National Institute of Technology Jalandhar} (NIT Jalandhar, formerly Regional Engineering College Jalandhar) is a premier public technical and research institution of higher learning in northern India. Established in the year 1987 as a joint venture between the Government of India and the Government of Punjab, the institute was elevated to the status of an \textbf{Institute of National Importance} under the National Institutes of Technology Act, 2007. Sprawling across an expansive 154-acre modern campus along the historic Grand Trunk Road, NIT Jalandhar consistently ranks among the top technical institutions in India in the National Institutional Ranking Framework (NIRF). The institute is celebrated for its rigorous academic curriculum, world-class infrastructure, high-impact sponsored research projects, and strong collaborations with premier global universities and industries.

\subsection*{Department of Electronics and Communication Engineering (ECE)}
The Department of Electronics and Communication Engineering at NIT Jalandhar was established in 1989 and has evolved into an acclaimed center of excellence for undergraduate (B.Tech.), postgraduate (M.Tech. in Signal Processing \& Machine Learning, and VLSI Design), and doctoral (Ph.D.) research. The department provides an intellectually vibrant ecosystem that nurtures breakthrough research in emerging disciplines including 5G/6G wireless communication systems, reconfigurable intelligent surfaces, radio frequency (RF) and millimeter-wave integrated circuits, 2D nanomaterials, embedded systems, and machine learning for physical-layer processing.

\subsection*{Advanced Microwave and Computational Electromagnetics Laboratory}
The internship was conducted at the \textbf{Advanced Microwave and Computational Electromagnetics Laboratory} under the mentorship of \textbf{Dr. Kundan Kumar}, Professor in the Department of ECE. The laboratory is equipped with high-end computational workstations hosting industry-standard full-wave electromagnetic simulation suites, notably \textbf{Ansys HFSS (High-Frequency Structure Simulator)}, Keysight Advanced Design System (ADS), and CST Studio Suite. The experimental testing infrastructure includes high-precision Vector Network Analyzers (VNA operational up to 67~GHz), standard gain Ka-band horn antennas, low-noise amplifiers, RF probe stations, and precision mechanical calibration kits (TRL/SOLT). The laboratory actively executes sponsored research projects funded by major governmental agencies, including the Science and Engineering Research Board (SERB), the Department of Science and Technology (DST), and the Defence Research and Development Organisation (DRDO), providing an exceptional environment for cutting-edge millimeter-wave metasurface investigation.

'''

final_text = trimmed[:pos_abt] + new_abt_section + trimmed[pos_toc2:]

with open('make_sec0_frontmatter.py', 'w', encoding='utf-8') as f:
    f.write(final_text)

print('Cleaned make_sec0_frontmatter.py successfully. Length:', len(final_text))
