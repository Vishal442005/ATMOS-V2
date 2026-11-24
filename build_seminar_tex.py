import os

tex_content = r"""%% ==========================================================================
%%  SEMINAR REPORT: DELAY TOLERANT NETWORKS IN SPACE COMMUNICATIONS
%%  Department of Electronics & Communication Engineering
%%  Jawaharlal Nehru Govt. Engineering College, Sundernagar
%%  Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur
%%
%%  Student: Vishal Chandel (Roll No. 23010104072)
%%  Supervisor / Coordinator: Dr. Sanjeev Kumar, Assistant Professor
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
\usepackage{tabularx,array,booktabs,multirow}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage[hidelinks]{hyperref}
\usepackage{enumitem}
\usepackage{microtype}

%% ---------- Typography & Formatting Standards -----------------------------
\setstretch{1.14}                     % 1.14-1.15 line spacing for dense, clean engineering reports
\setlength{\parskip}{3.5pt}           % Modest paragraph separation
\setlength{\parindent}{0pt}           % Block paragraphs
\graphicspath{{figures/}{./}}

%% Float Placement Tolerances (Allow large half-page images on text pages)
\renewcommand{\topfraction}{0.95}
\renewcommand{\bottomfraction}{0.95}
\renewcommand{\textfraction}{0.05}
\renewcommand{\floatpagefraction}{0.85}

%% Adjust list spacing
\setlist{itemsep=1.0pt,topsep=1.2pt,parsep=0pt,partopsep=0pt}

%% Adjust float & caption spacing
\setlength{\textfloatsep}{6pt plus 2pt minus 2pt}
\setlength{\intextsep}{5pt plus 2pt minus 2pt}
\setlength{\floatsep}{5pt plus 2pt minus 2pt}
\setlength{\abovecaptionskip}{3.5pt}
\setlength{\belowcaptionskip}{1.5pt}

%% Adjust equation spacing
\setlength{\abovedisplayskip}{3.0pt plus 1pt minus 1pt}
\setlength{\belowdisplayskip}{3.0pt plus 1pt minus 1pt}

%% ---------- Title Formatting (14pt Bold Uppercase for Chapters) ----------
\titleformat{\chapter}[hang]
  {\normalfont\fontsize{14pt}{17pt}\bfseries\filcenter\uppercase}
  {\thechapter.\hspace{0.8em}}{0pt}{}
\titlespacing*{\chapter}{0pt}{4pt}{9pt}

\titleformat{\section}[hang]
  {\normalfont\fontsize{12pt}{15pt}\bfseries}
  {\thesection\hspace{0.6em}}{0pt}{}
\titlespacing*{\section}{0pt}{6pt}{2pt}

\titleformat{\subsection}[hang]
  {\normalfont\fontsize{12pt}{14pt}\bfseries\itshape}
  {\thesubsection\hspace{0.6em}}{0pt}{}
\titlespacing*{\subsection}{0pt}{4pt}{2pt}

%% ---------- Header & Footer Configuration ---------------------------------
\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\fontsize{9pt}{11pt}\selectfont\nouppercase{\rightmark}}
\fancyfoot[C]{\fontsize{10pt}{12pt}\selectfont\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyfoot[C]{\fontsize{10pt}{12pt}\selectfont\thepage}
  \renewcommand{\headrulewidth}{0pt}
}

%% ---------- TOC / LOF / LOT Formatting ------------------------------------
\renewcommand{\cftchapleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftsubsecleader}{\cftdotfill{\cftdotsep}}
\setlength{\cftbeforechapskip}{3pt}
\setlength{\cftbeforesecskip}{1.5pt}

%% ---------- Custom Macros & Helpers ---------------------------------------
\newcommand{\SeminarTitle}{DELAY TOLERANT NETWORKS IN SPACE COMMUNICATIONS}
\newcommand{\SeminarSubtitle}{Architectural Genesis, Protocol Evolution, and Deterministic Routing from Deep Impact to Artemis}
\newcommand{\StudentName}{Vishal Chandel}
\newcommand{\RollNo}{23010104072}
\newcommand{\Semester}{7th Semester, B.Tech. ECE}
\newcommand{\SupervisorName}{Dr. Sanjeev Kumar}
\newcommand{\SupervisorDesignation}{Assistant Professor}
\newcommand{\HODName}{Dr. Ashwani Kumar}
\newcommand{\HODDesignation}{Head of Department}
\newcommand{\DepartmentName}{Department of Electronics \& Communication Engineering}
\newcommand{\CollegeName}{Jawaharlal Nehru Government Engineering College}
\newcommand{\CollegeLocation}{Sundernagar, Mandi (H.P.) -- 175018}
\newcommand{\AffiliatedUniversity}{Himachal Pradesh Technical University (HPTU), Hamirpur}
\newcommand{\AcademicYear}{2026--2027}

%% ==========================================================================
\begin{document}
%% ==========================================================================

%% --------------------------------------------------------------------------
%% COVER / TITLE PAGE (HPTU & JNGEC Standard with prominent SEMINAR REPORT)
%% --------------------------------------------------------------------------
\begin{titlepage}
\thispagestyle{empty}
\begin{center}

{\fontsize{24pt}{28pt}\bfseries\uppercase{SEMINAR REPORT}}\\[0.25cm]
{\fontsize{13pt}{16pt}\selectfont\textbf{ON}}\\[0.35cm]
{\fontsize{16pt}{20pt}\bfseries\uppercase{\SeminarTitle}}\\[0.25cm]
{\fontsize{11pt}{14pt}\selectfont\textbf{\SeminarSubtitle}}\\[0.45cm]

{\fontsize{11pt}{13pt}\selectfont\textit{Submitted in Partial Fulfillment of the Requirements\\
for the Award of the Degree of}}\\[0.3cm]

{\fontsize{13pt}{16pt}\bfseries\uppercase{Bachelor of Technology}}\\[0.15cm]
{\fontsize{11pt}{14pt}\selectfont in}\\[0.15cm]
{\fontsize{12pt}{15pt}\bfseries\uppercase{Electronics \& Communication Engineering}}\\[0.55cm]

\includegraphics[height=2.8cm,keepaspectratio]{logo.png}\\[0.55cm]

\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \fontsize{10.5pt}{13pt}\selectfont
    \textbf{Guided by:}\\
    \textbf{\SupervisorName}\\
    \SupervisorDesignation\\
    \DepartmentName
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \fontsize{10.5pt}{13pt}\selectfont
    \textbf{Submitted by:}\\
    \textbf{\StudentName}\\
    University Roll No.: \textbf{\RollNo}\\
    \Semester
  \end{flushright}
\end{minipage}

\vfill

{\fontsize{12pt}{15pt}\bfseries\uppercase{\DepartmentName}}\\[0.15cm]
{\fontsize{12pt}{15pt}\bfseries\uppercase{\CollegeName}}\\[0.1cm]
{\fontsize{10pt}{12pt}\selectfont\CollegeLocation}\\[0.15cm]
{\fontsize{10pt}{12pt}\selectfont\textit{Affiliated to \AffiliatedUniversity}}\\[0.25cm]
{\fontsize{11pt}{13pt}\bfseries November 2026}

\end{center}
\end{titlepage}

%% --------------------------------------------------------------------------
%% PRELIMINARY PAGES (Numbered in lower-case roman numerals)
%% --------------------------------------------------------------------------
\pagenumbering{roman}
\setcounter{page}{2}

%% --------------------------------------------------------------------------
%% CERTIFICATE OF APPROVAL
%% --------------------------------------------------------------------------
\clearpage
\begin{center}
  {\fontsize{12pt}{14pt}\bfseries\uppercase{\CollegeName}}\\[0.05cm]
  {\fontsize{10pt}{12pt}\selectfont\CollegeLocation}\\[0.05cm]
  {\fontsize{11pt}{13pt}\bfseries\uppercase{\DepartmentName}}\\[0.25cm]
  \includegraphics[height=1.7cm,keepaspectratio]{logo.png}\\[0.25cm]
  {\fontsize{13pt}{16pt}\bfseries\underline{CERTIFICATE OF APPROVAL}}
\end{center}

\vspace{0.3cm}
\noindent This is to certify that the Seminar Report entitled \textbf{``\SeminarTitle''} submitted by \textbf{\StudentName} (University Roll No.: \textbf{\RollNo}), student of B.Tech. 7th Semester in Electronics and Communication Engineering, has been completed and presented under my direct academic guidance in partial fulfillment of the requirements for the award of the degree of \textbf{Bachelor of Technology in Electronics and Communication Engineering} by \textbf{\AffiliatedUniversity}.

\vspace{0.25cm}
\noindent The technical contents embodied in this seminar report have been synthesized from authoritative peer-reviewed literature, recent scientific advances, and experimental flight validation records. The work is original, scientifically rigorous, and meets the evaluation standards established by the Department.

\vspace{1.8cm}
\noindent
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \rule{5.0cm}{0.6pt}\\
    \textbf{\SupervisorName}\\
    Supervisor \& Assistant Professor\\
    \DepartmentName\\
    JNGEC Sundernagar
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \rule{5.0cm}{0.6pt}\\
    \textbf{\HODName}\\
    \HODDesignation\\
    \DepartmentName\\
    JNGEC Sundernagar
  \end{flushright}
\end{minipage}

%% --------------------------------------------------------------------------
%% CANDIDATE'S DECLARATION
%% --------------------------------------------------------------------------
\clearpage
\begin{center}
  {\fontsize{12pt}{14pt}\bfseries\uppercase{\CollegeName}}\\[0.05cm]
  {\fontsize{10pt}{12pt}\selectfont\CollegeLocation}\\[0.05cm]
  {\fontsize{11pt}{13pt}\bfseries\uppercase{\DepartmentName}}\\[0.25cm]
  \includegraphics[height=1.7cm,keepaspectratio]{logo.png}\\[0.25cm]
  {\fontsize{13pt}{16pt}\bfseries\underline{CANDIDATE'S DECLARATION}}
\end{center}

\vspace{0.3cm}
\noindent I hereby declare that the seminar report entitled \textbf{``\SeminarTitle''} submitted in partial fulfillment of the requirements for the degree of \textbf{Bachelor of Technology in Electronics and Communication Engineering} at \textbf{\CollegeName}, affiliated to \textbf{\AffiliatedUniversity}, is an authentic record of my own academic research conducted under the supervision of \textbf{\SupervisorName}, Assistant Professor, \DepartmentName.

\vspace{0.25cm}
\noindent I further declare that the content of this seminar report has not been submitted previously, in part or full, to this or any other university or institution for the award of any degree, diploma, or fellowship. All sources of information, published research papers, algorithms, mathematical derivations, and technical figures have been duly cited and acknowledged in accordance with academic integrity guidelines.

\vspace{2.0cm}
\noindent
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \textbf{Date: } 17th November 2026\\[0.1cm]
    \textbf{Place: } Sundernagar, H.P.
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \rule{5.0cm}{0.6pt}\\
    \textbf{\StudentName}\\
    University Roll No.: \textbf{\RollNo}\\
    B.Tech. 7th Semester, ECE
  \end{flushright}
\end{minipage}

%% --------------------------------------------------------------------------
%% ABSTRACT (Acknowledgements removed per user instruction)
%% --------------------------------------------------------------------------
\clearpage
\begin{center}
  {\fontsize{14pt}{17pt}\bfseries\underline{ABSTRACT}}
\end{center}
\vspace{0.35cm}

\noindent Terrestrial telecommunication infrastructures rely entirely on continuous, bidirectional, low-latency connectivity supported by the ubiquitous TCP/IP protocol suite. However, when extended across interplanetary and cis-lunar distances, conventional networking paradigms break down catastrophically due to massive one-way propagation delays (ranging from seconds in cis-lunar orbits to tens of minutes between Earth and Mars), severe channel asymmetry, intermittent line-of-sight occultation, and elevated bit error rates. To overcome these fundamental physical constraints, the space communications community engineered \textbf{Delay-Tolerant Networking (DTN)}, establishing a paradigm shift from persistent circuit- or packet-switched routing to an asynchronous \textbf{Store-Carry-and-Forward} architecture.

\vspace{0.25cm}
\noindent This seminar report presents an exhaustive, evolutionary investigation of space DTN technologies, synthesizing theoretical foundations, international protocol standards, and cutting-edge algorithmic advances across 16 authoritative scientific publications. Rather than presenting an arbitrary chronological record, this report traces the technical narrative through which networking bottlenecks were systematically uncovered and engineered away. We begin with the foundational mathematical formulation of time-varying graphs and the structural failure of TCP/IP, followed by the architectural transition from Consultative Committee for Space Data Systems (CCSDS) SCPS protocols to the IETF Bundle Protocol (BPv6, RFC 5050; BPv7, RFC 9171) and modern recursive Bundle-in-Bundle Encapsulation (BIBE) developed in the REDMARS2 initiative. 

\vspace{0.25cm}
\noindent We examine transport reliability mechanisms, emphasizing the Licklider Transmission Protocol (LTP, RFC 5326) and novel Reinforcement Learning-based Adaptive Forward Error Correction (RL-FEC) designed to eliminate multi-minute retransmission cycles. Furthermore, we trace the routing paradigm shift from stochastic epidemic flooding to deterministic \textbf{Contact Graph Routing (CGR)}, detailing time-space resource contact graph (TSRCG) models, capacity/buffer-constrained graph searches, and decentralized Multi-Agent Reinforcement Learning (MARL) with graph attention networks deployed in NASA JPL lunar scenarios. Finally, cross-layer optimizations in optical satellite downlinks, high-altitude platform (HAPS) atmospheric relays, CubeSat software-defined micro-stacks ($\mu$D3TN), and Bundle Security (BPSec, RFC 9172) are analyzed alongside real-world flight heritage (DINET, ISS, Artemis LunaNet). A comprehensive 16-paper comparative matrix highlights the historical trajectory toward autonomous interplanetary networking.

\vspace{0.35cm}
\noindent \textbf{Keywords: } Delay-Tolerant Networks (DTN), Interplanetary Internet, Bundle Protocol Version 7 (BPv7), Licklider Transmission Protocol (LTP), Contact Graph Routing (CGR), Reinforcement Learning, LunaNet, BPSec.

%% --------------------------------------------------------------------------
%% TABLE OF CONTENTS, LIST OF FIGURES, LIST OF TABLES, LIST OF ABBREVIATIONS
%% --------------------------------------------------------------------------
\clearpage
\tableofcontents

\clearpage
\listoffigures
\vspace{0.5cm}
{\let\clearpage\relax\listoftables}

\clearpage
\begin{center}
  {\fontsize{13pt}{16pt}\bfseries\underline{LIST OF ABBREVIATIONS}}
\end{center}
\vspace{0.25cm}

\begin{center}
\fontsize{9pt}{11pt}\selectfont
\begin{tabular}{p{2.6cm}p{11.4cm}}
\toprule
\textbf{Abbreviation} & \textbf{Full Expansion} \\
\midrule
\textbf{AAS}      & Autonomous Agent Scheduling \\
\textbf{BER}      & Bit Error Rate \\
\textbf{BIBE}     & Bundle-in-Bundle Encapsulation \\
\textbf{BP}       & Bundle Protocol \\
\textbf{BPSec}    & Bundle Protocol Security (RFC 9172) \\
\textbf{BPv6}     & Bundle Protocol Version 6 (RFC 5050) \\
\textbf{BPv7}     & Bundle Protocol Version 7 (RFC 9171) \\
\textbf{CBOR}     & Concise Binary Object Representation (RFC 8949) \\
\textbf{CCSDS}    & Consultative Committee for Space Data Systems \\
\textbf{CGR}      & Contact Graph Routing \\
\textbf{CLA}      & Convergence Layer Adapter \\
\textbf{CSCG}     & Contact-State Contact Graph \\
\textbf{DINET}    & Deep Impact Network Experiment \\
\textbf{DSN}      & Deep Space Network (NASA) \\
\textbf{DTN}      & Delay-Tolerant Networking / Disruption-Tolerant Networking \\
\textbf{EAT}      & Earliest Arrival Time \\
\textbf{EID}      & Endpoint Identifier \\
\textbf{ESA}      & European Space Agency \\
\textbf{FSO}      & Free-Space Optical Communication \\
\textbf{GAT}      & Graph Attention Network \\
\textbf{GNSS}     & Global Navigation Satellite System \\
\textbf{HAPS}     & High-Altitude Platform Station \\
\textbf{ION}      & Interplanetary Overlay Network (NASA JPL) \\
\textbf{ISL}      & Inter-Satellite Link \\
\textbf{LEO}      & Low Earth Orbit \\
\textbf{LTP}      & Licklider Transmission Protocol (RFC 5326) \\
\textbf{MARL}     & Multi-Agent Reinforcement Learning \\
\textbf{MEO}      & Medium Earth Orbit \\
\textbf{NASA}     & National Aeronautics and Space Administration \\
\textbf{OWLT}     & One-Way Light Time \\
\textbf{QoS}      & Quality of Service \\
\textbf{RINA}     & Recursive InterNetwork Architecture \\
\textbf{RL-FEC}   & Reinforcement Learning-Based Forward Error Correction \\
\textbf{RTT}      & Round-Trip Time \\
\textbf{SCPS}     & Space Communications Protocol Specifications \\
\textbf{TSRCG}    & Time-Space Resource Contact Graph \\
\textbf{UDP}      & User Datagram Protocol \\
\bottomrule
\end{tabular}
\end{center}

%% --------------------------------------------------------------------------
%% MAIN CHAPTERS (Numbered 1, 2, 3...)
%% --------------------------------------------------------------------------
\clearpage
\pagenumbering{arabic}
\setcounter{page}{1}

%% ==========================================================================
%% CHAPTER 1: THE SPACE COMMUNICATION DILEMMA AND THEORETICAL FOUNDATIONS
%% ==========================================================================
\chapter{The Space Communication Dilemma and Theoretical Foundations}
\label{chap:dilemma}

\section{Physical Extremes of Deep-Space Channels}
Modern communication engineering is fundamentally grounded in the architectural assumptions of terrestrial packet-switched networking: electromagnetic delays are milliseconds, transmission errors are low, continuous paths connect endpoints, and symmetric feedback is guaranteed. When infrastructure expands across interplanetary dimensions, these assumptions collapse:
\begin{enumerate}[itemsep=1.0pt]
  \item \textbf{Extreme Propagation Delays:} Because electromagnetic signals propagate at $c \approx 3 \times 10^8\text{ m/s}$, the One-Way Light Time (OWLT) produces massive latency. Earth-Moon links experience an OWLT of 1.3 seconds (Round-Trip Time, RTT, of 2.6 seconds). Between Earth and Mars, orbital distances range from $5.5 \times 10^7\text{ km}$ to $4.0 \times 10^8\text{ km}$, resulting in OWLTs spanning 3.1 to 22.2 minutes (RTT of 6.2 to 44.4 minutes). Outer solar system probes experience RTTs of several hours.
  \item \textbf{Frequent and Protracted Link Disruptions:} Space communication paths are severed by celestial mechanics: planetary rotation occludes line-of-sight ground stations, orbital trajectories place orbiters behind moons, and solar conjunctions introduce extreme plasma noise blocking RF links for weeks.
  \item \textbf{Severe Channel Asymmetry:} Deep-space probes operate under strict size, weight, and power (SWaP) constraints. Downlink transmissions from planetary probes utilize low-power transmitters, while uplink signals from Earth's Deep Space Network (DSN) 70-meter dishes provide massive radiated power, producing rate asymmetries exceeding $1000:1$.
  \item \textbf{Elevated Bit Error Rates (BER):} Deep-space RF and Free-Space Optical (FSO) signals suffer free-space path loss ($P_r \propto 1/d^2$), solar background radiation, and atmospheric scintillation, producing high bit error rates.
\end{enumerate}

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.96\textwidth,height=8.4cm,keepaspectratio]{space_dtn_protocol_stack.png}
  \caption{Comprehensive architectural comparison across the traditional Terrestrial TCP/IP stack, the legacy CCSDS SCPS stack, and the Delay-Tolerant Networking (DTN) architecture.}
  \label{fig:stack_comparison}
\end{figure}

\section{The Breakdown of Terrestrial TCP/IP in Deep Space}
The standard Internet protocol suite fails catastrophically in deep space:
\begin{itemize}[itemsep=1.0pt]
  \item \textbf{Connection Handshake Failure:} TCP requires an interactive three-way handshake (\texttt{SYN}, \texttt{SYN-ACK}, \texttt{ACK}) before data transmission can begin. On an Earth-Mars link with an RTT of 40 minutes, 40 minutes of contact time is consumed solely establishing the socket connection before any payload byte is dispatched.
  \item \textbf{Congestion Control Collapse:} TCP interprets unacknowledged segments as buffer congestion. In space, where packet losses stem from channel noise or occultation, TCP repeatedly throttles its congestion window ($cwnd$) to 1 MSS, driving throughput toward zero.
  \item \textbf{Interactive Protocol Overhead:} Standard application protocols (DNS, TLS, HTTP) require multi-RTT exchanges for address resolution and security negotiation, rendering them unusable across long-delay links.
\end{itemize}

\section{Formal Algebraic and Geometric Space Networking Models}
To establish a rigorous mathematical foundation for time-varying deep-space connectivity, Bernardoni et al. \cite{bernardoni2023algebraic} formulated formal algebraic and geometric models for space networks. Rather than treating orbital networks as static graphs with stochastic edge failures, space communication topologies are modeled as deterministic, periodic, time-varying contact graphs.

\clearpage
\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.95\textwidth,height=8.2cm,keepaspectratio]{paper4_fig_p6_1.png}
  \caption{Geometric and algebraic representation of space contact networks, capturing predictable orbital visibility trajectories and state transitions (adapted from Bernardoni et al. \cite{bernardoni2023algebraic}).}
  \label{fig:bernardoni_geom}
\end{figure}

Let the space communication network be represented as a time-varying directed multigraph $\mathcal{G}(t) = (\mathcal{V}, \mathcal{E}(t))$, where $\mathcal{V}$ denotes the set of planetary bodies, satellites, landers, and ground stations, and $\mathcal{E}(t)$ represents the set of directed communication contacts available at time $t$. A contact $c_i \in \mathcal{E}(t)$ is formally defined as an ordered 6-tuple:
\begin{equation}
  c_i = \langle u_i, v_i, t_s^{(i)}, t_e^{(i)}, R_i, D_i \rangle
\end{equation}
where $u_i \in \mathcal{V}$ is the transmitting node, $v_i \in \mathcal{V}$ is the receiving node, $[t_s^{(i)}, t_e^{(i)}]$ defines the active contact interval, $R_i$ is the operational data transmission rate (bps), and $D_i$ denotes the one-way propagation delay across the link. Bernardoni et al. \cite{bernardoni2023algebraic} proved that routing in such deterministic geometric topologies maps onto algebraic path algebras over closed semirings. Building on this formulation, Sun et al. \cite{sun2022modeling} established the \textbf{Time-Space Resource Contact Graph (TSRCG)}, transforming dynamic continuous orbital contacts into discrete, schedulable flow networks. In a TSRCG, storage capacity at intermediate orbital relays is modeled alongside link capacity, enabling polynomial-time multi-commodity flow optimization for space missions.

%% ==========================================================================
%% CHAPTER 2: ARCHITECTURAL GENESIS: THE BUNDLE PROTOCOL EVOLUTION
%% ==========================================================================
\chapter{Architectural Genesis: The Bundle Protocol Evolution}
\label{chap:bundle}

\section{The Store-Carry-and-Forward Paradigm}
To overcome the failure of conversational protocols, Vinton Cerf, Scott Burleigh, and the Delay-Tolerant Networking Research Group (DTNRG) introduced the \textbf{Store-Carry-and-Forward} paradigm (RFC 4838 \cite{cerf2007delay}). In contrast to traditional routers that discard packets if an outgoing link is unavailable, a DTN node buffers data units in persistent non-volatile storage. The node retains custody of the data, physically carries it during orbital transit, and forwards it when the next scheduled contact window opens.

The \textbf{Bundle Protocol (BP)} operates as an overlay layer (Layer 7.5) situated above heterogeneous transport and data-link convergence layers. Application messages are packaged into variable-length contiguous data blocks called \textbf{bundles}. Each bundle consists of a Primary Block (source/destination EIDs, creation timestamp, lifetime, flags), Canonical Extension Blocks (security parameters, QoS classes), and a Payload Block.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.95\textwidth,height=7.2cm,keepaspectratio]{paper2_fig_p1_1.png}
  \caption{Lloyd Wood's architectural assessment and protocol layering model of delay-tolerant networking \cite{wood2012assessing}.}
  \label{fig:wood_layering}
\end{figure}

\section{Lloyd Wood's Critical Assessment and Architectural Realignment}
In 2007, the IETF published \textbf{BPv6 (RFC 5050)} \cite{scott2007bundle}. While BPv6 was hailed as a breakthrough, real-world flight trials and architectural evaluations revealed fundamental engineering deficiencies. In a landmark critique, Lloyd Wood \cite{wood2012assessing} evaluated the Bundle Protocol against classical networking principles.

Wood \cite{wood2012assessing} identified three critical flaws in BPv6:
\begin{enumerate}[itemsep=1.0pt]
  \item \textbf{Conflation of Transport and Network Functions:} BP attempted to serve simultaneously as an end-to-end transport protocol (guaranteeing reliability via custody transfer) and a hop-by-hop network routing protocol. This violated Saltzer's classical \emph{End-to-End Principle}, as custody transfer operated hop-by-hop but lacked mechanisms to ensure true end-to-end delivery when intermediate custodial nodes experienced buffer exhaustion.
  \item \textbf{Custody Transfer Flaws:} In BPv6, custody acceptance generated an administrative custody signal dispatched backward across the high-delay link. Because the upstream custodial node had to maintain the bundle in non-volatile memory until receiving the custody signal, an asymmetric link or lost custody signal caused redundant retransmissions, filling deep-space storage buffers.
  \item \textbf{Encoding Overhead and Parsing Complexity:} BPv6 utilized Self-Delimiting Numeric Values (SDNV) and string-based URI EIDs (e.g., \texttt{dtn:}\allowbreak\texttt{//mars/}\allowbreak\texttt{science}), consuming significant parsing overhead on flight-qualified rad-hardened processors with limited clock speeds.
\end{enumerate}

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=8.8cm,keepaspectratio]{paper1_fig_p8_1.png}
  \caption{Recursive Bundle-in-Bundle Encapsulation (BIBE) architecture developed in the REDMARS2 project, demonstrating scope-based isolation across multi-domain planetary networks (adapted from Feldmann et al. \cite{feldmann2025selected}).}
  \label{fig:redmars_bibe}
\end{figure}

\section{Standardization of BPv7 and Compressed Custody Re-engineering}
The DTN community addressed these architectural shortcomings by releasing \textbf{Bundle Protocol Version 7 (BPv7, RFC 9171)} in 2022 \cite{burleigh2022bundle}. BPv7 completely redesigned data serialization by replacing SDNVs with \textbf{Concise Binary Object Representation (CBOR, RFC 8949)}. CBOR provides compact binary encoding, predictable field offsets, and fast decoding suitable for low-power flight avionics. Furthermore, BPv7 standardized numeric \texttt{ipn} EID formats (e.g., \texttt{ipn:42.1}), drastically reducing primary header byte overhead. Crucially, BPv7 stripped custody transfer out of the core specification, delegating reliability to specialized convergence layers and dedicated extension blocks. Recently, Le Bihan, Flentge, and Fraire \cite{arxiv_custody_bpv7} developed a modernized custody transfer and compressed status reporting framework for BPv7 (to be standardized by CCSDS in 2025). As illustrated in their experimental evaluation, rather than transmitting a single custody acknowledgement per bundle, the new system introduces:
\begin{equation}
  \text{Compressed Custody Signal (CCS)} = \langle \text{Flow ID}, \text{Base Sequence}, \text{Bitmask Range} \rangle
\end{equation}
This allows an orbiter to acknowledge thousands of received telemetry bundles within a single 32-byte administrative record, reducing reverse-channel signaling overhead by over 92\% \cite{arxiv_custody_bpv7}.

\section{Recursive DTN: Bundle-in-Bundle Encapsulation (BIBE)}
As space missions transition from single spacecraft to complex federated architectures (e.g., lunar gateways, rover swarms, and commercial relays), flat DTN addressing becomes unscalable. In the REDMARS2 project, Feldmann et al. \cite{feldmann2025selected} integrated the principles of the \textbf{Recursive InterNetwork Architecture (RINA)} into DTN through \textbf{Bundle-in-Bundle Encapsulation (BIBE)}. BIBE allows a complete customer bundle (including headers, security blocks, and payload) to be encapsulated as the payload of an outer carrier bundle (Figure~\ref{fig:redmars_bibe}). This decouples internal administrative domains: a lunar rover network can utilize local addressing and ephemeral link keys, while the outer carrier bundle navigates Earth-Moon inter-agency relays using standardized CCSDS convergence layers. Flight experiments conducted in collaboration with ESA confirmed that BIBE establishes scalable, policy-isolated, recursive routing across heterogeneous space domains without requiring global EID synchronization \cite{feldmann2025selected}.

%% ==========================================================================
%% CHAPTER 3: TRANSPORT LAYER RELIABILITY: LICKLIDER TRANSMISSION PROTOCOL
%% ==========================================================================
\chapter{Transport Layer Reliability: The Licklider Transmission Protocol}
\label{chap:ltp}

\section{The Need for Long-Delay Convergence Layers}
While the Bundle Protocol operates as an overlay, it cannot transmit raw bits across physical links directly. It requires a \textbf{Convergence Layer Adapter (CLA)} to map bundle transmission onto underlying link technologies. Because TCP collapses in deep space and raw UDP offers no reliability, the IETF and CCSDS developed the \textbf{Licklider Transmission Protocol (LTP, RFC 5326)} \cite{ramadas2008licklider}, named for ARPANET pioneer J.C.R. Licklider. Designed specifically for point-to-point, long-delay, high-BER deep-space radio and optical links, LTP eliminates conversational transactions through automated checkpointing and selective negative acknowledgements.

\begin{figure}[!ht]
  \centering
  \includegraphics[height=6.8cm,keepaspectratio]{paper6_diagram_p1.png}
  \caption{Complete operational state machine and transmission pipeline of the Licklider Transmission Protocol (LTP) augmented with Reinforcement Learning-based Adaptive FEC (adapted from Chen et al. \cite{chen2025reliable}).}
  \label{fig:ltp_rl_fec}
\end{figure}

\section{LTP Operational Mechanics: Red and Green Data}
LTP segments outgoing bundle payloads into an aggregated transmission block. Within this block, LTP defines two orthogonal transmission services:
\begin{itemize}[itemsep=0.5pt]
  \item \textbf{Red Data (Reliable Transmission):} Red segments require positive acknowledgement. When the transmitting node dispatches the final red segment of a block, it sets the \textbf{Checkpoint (CP)} flag. Upon receiving the CP segment, the receiving node evaluates its assembly buffer and returns a \textbf{Report Segment (RS)} containing a compact bitmask of successfully received and missing segment offsets. The sender retransmits only missing segments, dispatches a new checkpoint, and completes the transaction with a Report Acknowledgement (RA).
  \item \textbf{Green Data (Unreliable Transmission):} Green segments are transmitted without checkpoints, acknowledgements, or retransmission timers. Green data is utilized for transient sensor streams, redundant telemetry, or bundles with application-layer forward error correction.
\end{itemize}

The transmission duration of an LTP block over a link with data rate $R$, one-way propagation delay $\tau_{\text{prop}}$, block size $S_{\text{block}}$, and retransmission rounds $N_{\text{retx}}$ is governed by:
\begin{equation}
  T_{\text{total}} = \frac{S_{\text{block}}}{R} + \sum_{k=1}^{N_{\text{retx}}} \left( 2\tau_{\text{prop}} + \frac{S_{\text{missing}}^{(k)}}{R} \right)
\end{equation}
Equation (3.1) highlights the severe penalty of deep-space link errors: each retransmission round incurs a $2\tau_{\text{prop}}$ latency, delaying delivery by up to 40 minutes per Mars pass.

\section{Reinforcement Learning-Based Adaptive FEC for LTP}
To eliminate the devastating delay penalties of iterative ARQ retransmissions, Chen, Song, and Zhao \cite{chen2025reliable} developed a pioneering architecture combining LTP with \textbf{Reinforcement Learning-Based Adaptive Forward Error Correction (RL-FEC)}. Under the RL-FEC framework (Figure~\ref{fig:ltp_rl_fec}), an autonomous agent observes dynamic link states (signal-to-noise ratio $\gamma(t)$, atmospheric attenuation, and recent packet loss distribution) and models the FEC code rate selection as a Markov Decision Process (MDP). At each transmission checkpoint, the agent selects an optimal Reed-Solomon or Luby Transform (LT) erasure coding overhead $\rho_{\text{fec}}$ balancing bandwidth against retransmission risk:
\begin{equation}
  \mathcal{R}_t = - \left[ \alpha \cdot \frac{\text{Payload Size} \times (1 + \rho_{\text{fec}})}{R} + \beta \cdot P_{\text{fail}}(\rho_{\text{fec}}, \text{BER}) \cdot 2\tau_{\text{prop}} \right]
\end{equation}
where $\alpha$ and $\beta$ are weighting factors prioritizing bandwidth efficiency versus delivery latency. Chen et al. \cite{chen2025reliable} demonstrated that RL-FEC cuts block completion time by up to 64\% across deep-space optical and RF links, achieving single-pass delivery in over 98.4\% of contact windows.

\section{Goal-Oriented Deep-Space Bundle Management and Flow Control}
At the interface between LTP and the Bundle Protocol, buffer memory management during protracted disruptions remains critical. Feldmann et al. \cite{arxiv_goal_bundle_rl} developed a \textbf{Goal-Oriented Flow Control and Bundle Management} framework using deep reinforcement learning. By evaluating bundle metadata (priority, expiration time, and science mission value), the autonomous agent dynamically schedules bundle transmission queues and prunes stale data during buffer crises, preventing buffer-overflow cascades across relay orbiters.

%% ==========================================================================
\chapter{The Routing Paradigm Shift: Contact Graph Routing and AI}
\label{chap:cgr}

\section{From Stochastic Epidemic Routing to Deterministic Contacts}
Terrestrial mobile ad-hoc networks (MANETs) utilize reactive or proactive routing protocols (AODV, OLSR) that maintain continuous routing tables. Early DTN terrestrial research explored opportunistic, stochastic algorithms such as \textbf{Epidemic Routing} (flooding bundles to all encountered nodes) and \textbf{PRoPHET} (probabilistic routing based on encounter history). In deep-space communications, stochastic flooding is unacceptable:
\begin{enumerate}[itemsep=1.0pt]
  \item Deep-space transmitters operate under extreme electrical power and amplifier limitations; flooding redundant copies depletes precious spacecraft battery reserves.
  \item Storage capacity on space hardware is strictly bounded; flooding rapidly induces catastrophic buffer exhaustion.
  \item Most importantly, celestial orbital mechanics are completely \textbf{deterministic}. Orbital ephemerides, ground station tracking schedules, and spacecraft trajectories are calculated mathematically years in advance.
\end{enumerate}

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.98\textwidth,height=7.6cm,keepaspectratio]{contact_graph_routing_flow.png}
  \caption{Operational timeline and algorithmic flow of Contact Graph Routing (CGR), illustrating contact plan scheduling, volume-aware reservation, and route construction between planetary nodes.}
  \label{fig:cgr_flow}
\end{figure}

\section{Contact Graph Routing (CGR) Principles}
To exploit predictable orbital trajectories, Scott Burleigh at NASA JPL developed \textbf{Contact Graph Routing (CGR)} \cite{araniti2015contact}. CGR equips every node with a synchronized \textbf{Contact Plan}---a database containing all anticipated future communication opportunities across the network. When a bundle destined for node $D$ arrives at an intermediate node at time $t_{\text{current}}$, CGR performs a specialized Dijkstra shortest-path search over the contact graph to compute the \textbf{Earliest Arrival Time (EAT)}:
\begin{equation}
  \text{EAT}(c_i) = \max\left( t_s^{(i)}, \text{Arr}(u_i) \right) + D_i + \frac{S_{\text{bundle}}}{R_i}
\end{equation}
where $\text{Arr}(u_i)$ is the arrival time of the bundle at the transmitting node of contact $c_i$. Furthermore, modern CGR incorporates \textbf{Volume Reservation}. Because each contact $c_i$ has a finite data volume capacity $V(c_i) = R_i \cdot (t_e^{(i)} - t_s^{(i)})$, routing a bundle through $c_i$ decrements its available capacity:
\begin{equation}
  V_{\text{residual}}(c_i) \leftarrow V_{\text{residual}}(c_i) - S_{\text{bundle}}
\end{equation}
If $V_{\text{residual}}(c_i) < S_{\text{bundle}}$, contact $c_i$ is suppressed for that routing tree, and alternate paths are explored (Figure~\ref{fig:cgr_flow}).

\section{Capacity- and Buffer-Constrained CGR Enhancements}
While classical CGR modeled link transmission volumes, it ignored intermediate storage buffer constraints. When multiple source nodes simultaneously routed traffic through a single relay orbiter, the relay's storage buffer exceeded physical capacity, causing silent bundle drops.

To resolve this limitation, Alhajj and Corlay \cite{alhajj2024improved} designed \textbf{Improved CGR with Capacity and Buffer Constraints}. Their algorithm constructs a dynamic Contact-State Contact Graph (CSCG) that tracks the temporal evolution of storage buffers at every node across future contact epochs:
\begin{equation}
  B_v(t) = B_v(0) + \sum_{c_{\text{in}} \in \mathcal{E}_{\text{in}}(v), t_e \le t} \text{Vol}(c_{\text{in}}) - \sum_{c_{\text{out}} \in \mathcal{E}_{\text{out}}(v), t_e \le t} \text{Vol}(c_{\text{out}})
\end{equation}
By enforcing $B_v(t) \le B_v^{\max}$ as a hard constraint during route computation, their algorithm guarantees 0\% packet drop due to buffer exhaustion, even under 95\% network utilization \cite{alhajj2024improved}. In parallel, Madoery, Kurt, and Yanikomeroglu \cite{madoery2023routing} formulated heterogeneous traffic routing for satellite DTNs, ensuring high-priority emergency command bundles bypass congested queues ahead of bulk science imaging.

\begin{figure}[!ht]
  \centering
  \includegraphics[height=9.2cm,keepaspectratio]{paper8_fig_p3_1.png}
  \caption{Decentralized multi-agent reinforcement learning architecture utilizing Graph Attention Networks (GAT) for lunar surface rovers and orbiters (adapted from Lozano-Cuadra et al., NASA JPL collaboration \cite{lozano2025learning}).}
  \label{fig:lunar_marl}
\end{figure}

\section{Next-Generation Lunar AI Routing: Graph Attention MARL}
As lunar exploration intensifies under the NASA Artemis program, future lunar surface networks will feature swarms of rovers, autonomous landers, and orbiting relays whose movements cannot be entirely pre-computed. In a landmark collaboration between Aarhus University and NASA JPL, Lozano-Cuadra, Soret, and Sanchez Net \cite{lozano2025learning} developed \textbf{Graph Attention-based Multi-Agent Reinforcement Learning (GAT-MARL)} for lunar DTNs.

As shown in Figure~\ref{fig:lunar_marl}, each lunar asset acts as an autonomous reinforcement learning agent. The agent processes local contact status, queue backlog, and neighbor node embeddings using a Graph Attention Network (GAT). Through decentralized training and shared actor-critic objectives, the agents learn cooperative forwarding policies that adapt to unpredicted rover displacements. Their results demonstrated a 47\% reduction in end-to-end delivery latency compared to static CGR in high-dynamic lunar surface topologies \cite{lozano2025learning}. Complementing this approach, Feldmann et al. \cite{arxiv_neural_lunar_dtn} introduced \textbf{NeuraLunaDTNet}, which compresses complex Dijkstra contact lookups into a feedforward neural network executing inference in under 2 milliseconds on flight-grade FPGAs.

\section{Lightweight Onboard Routing for Satellite Constellations}
For large-scale satellite mega-constellations and autonomous Global Navigation Satellite Systems (GNSS), standard CGR graph searches require excessive memory ($O(|\mathcal{V}| \cdot |\mathcal{E}|)$). Yan, Fraire, et al. \cite{arxiv_autonomous_gnss} solved this scalability bottleneck by inventing \textbf{DS-SMFP} (Deterministic Single-Slot Multi-Flow Propagation). By exploiting the structural reality that each satellite communicates with at most one peer per time slot, DS-SMFP performs a single backward sweep across time slots, outputting forwarding decisions in linear time $O(T)$ with working memory independent of the planning horizon. Deployed in a 30-satellite BeiDou constellation simulation, DS-SMFP matched CGR delivery delays while running \textbf{180 times faster} and consuming \textbf{36 times less working memory} \cite{arxiv_autonomous_gnss}.

%% ==========================================================================
%% CHAPTER 5: CROSS-LAYER OPTIMIZATION, OPTICAL LINKS, AND SPACE SECURITY
%% ==========================================================================
\chapter{Cross-Layer Optimization, Optical Links, and Space Security}
\label{chap:cross_layer}

\section{Optical Satellite Downlinks and Energy Scheduling}
To overcome RF spectrum congestion and achieve multi-gigabit throughput, next-generation space missions are adopting \textbf{Free-Space Optical (FSO)} communications. Optical laser downlinks offer bandwidth advantages exceeding $10\text{ Gbps}$ at lower power and mass. However, optical links are acutely vulnerable to cloud obscuration, fog, and atmospheric turbulence.

\begin{figure}[!ht]
  \centering
  \includegraphics[height=9.4cm,keepaspectratio]{paper13_diagram_p1.png}
  \caption{Energy-efficient traffic scheduling and cloud-free line-of-sight tracking for optical LEO satellite downlinks (adapted from Fettes et al. \cite{fettes2026energy}).}
  \label{fig:optical_sched}
\end{figure}

Fettes, Madoery, and Yanikomeroglu \cite{fettes2026energy} developed an \textbf{Energy-Efficient Traffic Scheduling} algorithm for optical Low Earth Orbit (LEO) downlinks (Figure~\ref{fig:optical_sched}). Their framework couples DTN bundle storage with on-board battery state-of-charge ($E_{\text{batt}}(t)$) and cloud-free line-of-sight (CFLOS) probabilities over terrestrial ground stations. By selectively scheduling laser transmissions only when cloud cover is below threshold $\theta_{\text{cloud}}$ and solar panels have recharged battery reserves, their scheduling scheme increased cumulative downloaded payload volume by 41\% while preventing battery exhaustion \cite{fettes2026energy}.

\section{HAPS-Enabled Optical Relays and Planetary Clustering}
To bypass atmospheric cloud disruption entirely, Boualem et al. \cite{arxiv_haps_optical_dtn} proposed integrating \textbf{High-Altitude Platform Stations (HAPS)} operating in the stratosphere ($20\text{ km}$ altitude) as DTN optical relays. Because HAPS float above 95\% of Earth's clouds and turbulent atmosphere, LEO satellites down-link massive science datasets to HAPS via ultra-high-rate optical channels. The HAPS stores the bundles and relays them to ground gateways over weather-resilient RF links or clean-sky optical paths. Boualem et al. demonstrated that HAPS-DTN architectures achieve a 99.1\% delivery ratio compared to just 63.4\% for direct satellite-to-ground optical links during severe weather events \cite{arxiv_haps_optical_dtn}.

In planetary exploration environments (e.g., Mars or Lunar bases), rovers and sensor nodes form local ad-hoc clusters. Boualem et al. \cite{arxiv_clustering_adhoc} established a comprehensive classification of clustering algorithms for space ad-hoc networks, proving that multi-metric cluster-head election (incorporating residual energy, mobility stability, and line-of-sight duration to orbital relays) extends planetary network operational lifetime by over 38\%.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.92\textwidth,height=8.4cm,keepaspectratio]{paper12_fig_p9_1.png}
  \caption{Architectural refinement of the lightweight, software-defined $\mu$D3TN protocol stack for resource-constrained CubeSats and SmallSats (adapted from Walter et al. \cite{arxiv_software_defined_dtn}).}
  \label{fig:mud3tn_arch}
\end{figure}

\section{Software-Defined $\mu$D3TN for CubeSats and SmallSats}
Traditional DTN implementations, such as NASA's Interplanetary Overlay Network (ION), require large memory footprints and POSIX-compliant operating systems, making them difficult to deploy on resource-constrained CubeSats. Walter et al. \cite{arxiv_software_defined_dtn} redesigned the open-source \textbf{$\mu$D3TN} stack into a modular, software-defined DTN architecture (Figure~\ref{fig:mud3tn_arch}).

The refined $\mu$D3TN implementation isolates protocol processing from platform hardware through standardized POSIX/FreeRTOS abstraction layers and Unix domain socket interfaces. The entire BPv7 and LTP stack compiles to an executable smaller than 120 KB, requiring less than 256 KB of RAM. This breakthrough enables low-cost $1\text{U}$--$3\text{U}$ CubeSats to participate directly in international delay-tolerant space networks alongside major agency orbiters.

\section{Deep-Space Security: The Bundle Security Protocol (BPSec)}
Securing communication across delay-tolerant space networks presents unprecedented cryptographic challenges. Terrestrial protocols (TLS, IPsec) depend on continuous end-to-end sessions, synchronized real-time clocks, and instantaneous Certificate Revocation Lists (CRLs). In deep space, an encryption key cannot be validated against a terrestrial Certification Authority (CA) without incurring multi-hour delay.

To resolve these challenges, Birrane and McKeever standardized the \textbf{Bundle Security Protocol (BPSec, RFC 9172)} \cite{birrane2022bundle}. BPSec defines two modular cryptographic extension blocks:
\begin{itemize}[itemsep=1.0pt]
  \item \textbf{Block Confidentiality Block (BCB):} Encrypts designated bundle blocks (e.g., Payload Block) to ensure data confidentiality against unauthorized eavesdropping across public satellite relays.
  \item \textbf{Block Integrity Block (BIB):} Computes a cryptographic digital signature or Message Authentication Code (MAC) across target blocks to guarantee data integrity and source authenticity.
\end{itemize}
Because intermediate nodes must inspect primary and routing blocks to make forwarding decisions, BPSec permits granular, block-level cryptographic protection. Payloads remain encrypted end-to-end, while intermediate routing headers can be authenticated hop-by-hop, preventing malicious nodes from injecting counterfeit bundles or launching buffer-denial-of-service attacks \cite{birrane2022bundle}.

%% ==========================================================================
%% CHAPTER 6: SYNTHESIS OF LITERATURE, FLIGHT VALIDATIONS, AND CONCLUSION
%% ==========================================================================
\chapter{Synthesis of Literature, Flight Validations, and Conclusion}
\label{chap:synthesis}

\section{Comprehensive Comparative Synthesis of Evaluated Literature}
To systematically summarize the technological landscape, Table~\ref{tab:lit_matrix} presents an exhaustive comparative synthesis of the 16 peer-reviewed scientific papers evaluated in this seminar report, detailing their specific operational challenges, proposed algorithmic solutions, target space domains, and key quantitative findings.

\begin{table}[!ht]
\centering
\caption{Comprehensive comparative synthesis of evaluated literature on space delay-tolerant networks.}
\label{tab:lit_matrix}
\vspace{0.12cm}
\resizebox{\textwidth}{!}{%
\begin{tabular}{>{\raggedright}p{2.8cm}>{\raggedright}p{1.0cm}>{\raggedright}p{4.2cm}>{\raggedright}p{4.5cm}>{\raggedright}p{3.0cm}>{\raggedright\arraybackslash}p{4.2cm}}
\toprule
\textbf{Author \& Ref.} & \textbf{Year} & \textbf{Problem Addressed} & \textbf{Core Innovation / Method} & \textbf{Space Domain} & \textbf{Key Result / Advancement} \\
\midrule
Feldmann \emph{et al.} \cite{feldmann2025selected} & 2025 & Domain isolation \& scalability & Bundle-in-Bundle Encapsulation (BIBE) & Interplanetary / UAVs & Verified recursive RINA overlay with ESA \\
Wood \cite{wood2012assessing} & 2012 & BPv6 layering \& custody flaws & Critical architectural evaluation & Deep Space & Exposed transport-layer conflation in BP \\
Le Bihan \emph{et al.} \cite{arxiv_custody_bpv7} & 2025 & High custody signaling overhead & Compressed Custody Signal (CCS) for BPv7 & Lunar / Earth Obs. & 92\% reduction in return-link overhead \\
Bernardoni \emph{et al.} \cite{bernardoni2023algebraic} & 2023 & Lack of formal graph models & Algebraic semirings \& geometric topologies & Space Networks & Proved formal routing convergence bounds \\
Sun \emph{et al.} \cite{sun2022modeling} & 2022 & Dynamic LEO topology changes & Time-Space Resource Contact Graph (TSRCG) & LEO Constellations & Optimal multi-task delivery guarantee \\
Chen \emph{et al.} \cite{chen2025reliable} & 2025 & Devastating LTP ARQ delays & RL-Based Adaptive Forward Error Correction & Deep Space RF/Optical & 64\% reduction in block transfer time \\
Feldmann \emph{et al.} \cite{arxiv_goal_bundle_rl} & 2026 & Buffer overflow during disruptions & Goal-Oriented RL flow control & Deep Space & Autonomous bundle priority scheduling \\
Lozano \emph{et al.} \cite{lozano2025learning} & 2025 & Dynamic lunar rover mobility & Graph Attention Multi-Agent RL (NASA JPL) & Lunar Surface & 47\% latency reduction vs. static CGR \\
Madoery \emph{et al.} \cite{madoery2023routing} & 2023 & Heterogeneous QoS traffic contention & Multi-class QoS priority routing & Satellite DTN & Prevents telecommand starvation \\
Alhajj \emph{et al.} \cite{alhajj2024improved} & 2024 & CGR buffer-exhaustion bundle drops & Dynamic Contact-State Contact Graph & Space DTN & 0\% packet drop under 95\% utilization \\
Feldmann \emph{et al.} \cite{arxiv_neural_lunar_dtn} & 2024 & Excessive CGR search latency & NeuraLunaDTNet feedforward neural routing & Lunar Constellations & Sub-2ms onboard routing decisions \\
Walter \emph{et al.} \cite{arxiv_software_defined_dtn} & 2024 & Heavy POSIX overhead on CubeSats & Software-defined modular $\mu$D3TN stack & CubeSats / SmallSats & Operates in $<$256 KB RAM footprint \\
Fettes \emph{et al.} \cite{fettes2026energy} & 2026 & Weather \& battery limits in FSO & Energy-aware optical downlink scheduling & LEO Optical & 41\% increase in downloaded payload \\
Boualem \emph{et al.} \cite{arxiv_haps_optical_dtn} & 2024 & Cloud blocking of optical links & Stratospheric HAPS DTN optical relay & Satellite-to-Ground & 99.1\% delivery ratio in cloudy weather \\
Boualem \emph{et al.} \cite{arxiv_clustering_adhoc} & 2024 & Energy depletion in space ad-hoc & Multi-metric clustering taxonomy & Planetary Ad-Hoc & 38\% extension in network lifetime \\
Yan \emph{et al.} \cite{arxiv_autonomous_gnss} & 2026 & CGR memory explosion on GNSS & DS-SMFP single backward slot sweep & Autonomous GNSS & 180x speedup, 36x less working memory \\
\bottomrule
\end{tabular}%
}
\end{table}

\section{Historical Flight Validations: From DINET to Artemis}
The theoretical and algorithmic concepts of DTN have undergone rigorous in-flight validation across key historical space missions:
\begin{itemize}[itemsep=1.0pt]
  \item \textbf{Deep Impact Network Experiment (DINET, 2008):} NASA JPL executed the world's first interplanetary DTN flight test using the \emph{Deep Impact} spacecraft located 15 million miles from Earth. Over 27 days, JPL engineers transmitted hundreds of telemetry images using the Bundle Protocol and LTP across a network of 10 nodes (9 on Earth, 1 in deep space), demonstrating autonomous store-carry-and-forward recovery from scheduled occultations \cite{burleigh2003delay}.
  \item \textbf{EPOXI Mission (2010):} Following DINET, the extended EPOXI mission utilized DTN for comet flyby telemetry recovery, proving that bundle-based transmission eliminated manual file-retransmission tracking by ground operators.
  \item \textbf{International Space Station (ISS) Commercial Payloads (2012--Present):} NASA, ESA, and commercial partners deployed DTN payloads on the ISS. The European Space Agency demonstrated remote robotic arm control from the ISS to a ground rover in Germany using DTN, proving protocol stability across mixed space-to-ground links.
  \item \textbf{NASA Artemis Program and LunaNet (2024--2026+):} NASA and international partners established the \textbf{LunaNet Interoperability Specification}. LunaNet mandates the Bundle Protocol (BPv7) and LTP as the official standard for all lunar orbiters, landers, rovers, and astronaut EVA units, establishing the operational foundation of the Solar System Internet.
\end{itemize}

\section{Evolutionary Synthesis: How Space DTN Matured}
The scientific narrative synthesized in this seminar report demonstrates a four-phase evolutionary progression:
\begin{enumerate}[itemsep=1.0pt]
  \item \textbf{Phase 1: Foundational Overlay (1998--2012):} Recognized the fundamental failure of TCP/IP across interplanetary distances and established the Store-Carry-and-Forward architecture via BPv6 (RFC 5050) and LTP (RFC 5326). Rigorous critiques by Lloyd Wood \cite{wood2012assessing} identified layering and custody weaknesses.
  \item \textbf{Phase 2: Deterministic Routing \& Flight Prototyping (2008--2020):} Replaced stochastic flooding with Contact Graph Routing (CGR) to exploit deterministic celestial mechanics. Validated protocols in deep-space flight missions (DINET, EPOXI, ISS).
  \item \textbf{Phase 3: Protocol Standardization \& Resource Awareness (2020--2024):} Standardized BPv7 (RFC 9171) with CBOR serialization, designed capacity- and buffer-constrained CGR \cite{alhajj2024improved}, and implemented lightweight micro-stacks ($\mu$D3TN) for resource-constrained CubeSats \cite{arxiv_software_defined_dtn}.
  \item \textbf{Phase 4: Autonomous AI \& Multi-Domain Inter-Networking (2024--Present):} Integrated deep reinforcement learning for adaptive FEC \cite{chen2025reliable}, deployed Graph Attention MARL for decentralized lunar rovers \cite{lozano2025learning}, and developed recursive Bundle-in-Bundle Encapsulation \cite{feldmann2025selected} for the expanding Artemis Solar System Internet.
\end{enumerate}

\section{Open Research Challenges and Conclusion}
While space DTN has achieved remarkable maturity, several formidable challenges remain open for ongoing investigation:
\begin{enumerate}[itemsep=1.0pt]
  \item \textbf{Autonomous Key Management in BPSec:} Distributing and revoking asymmetric cryptographic keys across multi-hour delay links without relying on centralized terrestrial authorities remains an active security challenge.
  \item \textbf{Unified RF/Optical Dynamic Contact Scheduling:} Incorporating real-time atmospheric weather probabilities into CGR contact plans requires tighter cross-layer integration between optical transceivers and bundle routing engines.
  \item \textbf{Inter-Agency Governance and Policy Routing:} Managing trust, traffic accounting, and policy-based forwarding between competing governmental and commercial space relay providers requires standardized BGP-like policy protocols for DTN \cite{arxiv_bgp_dtn}.
\end{enumerate}

In conclusion, Delay-Tolerant Networking represents the definitive networking architecture for space communications. By replacing conversational handshakes with persistent Store-Carry-and-Forward routing, standardizing BPv7 and LTP, and incorporating artificial intelligence for dynamic link adaptation and lunar routing, DTN enables humanity's transition from isolated point-to-point deep-space links to a permanent, resilient, and autonomous Interplanetary Internet.

%% ==========================================================================
%% REFERENCES (IEEE Style, 25 Authoritative Citations, single-page compact)
%% ==========================================================================
\clearpage
\begingroup
\makeatletter
\renewenvironment{thebibliography}[1]{%
  \chapter*{\bibname}%
  \@mkboth{\MakeUppercase\bibname}{\MakeUppercase\bibname}%
  \addcontentsline{toc}{chapter}{\bibname}%
  \list{\@biblabel{\@arabic\c@enumiv}}%
       {\settowidth\labelwidth{\@biblabel{#1}}%
        \leftmargin\labelwidth
        \advance\leftmargin\labelsep
        \setlength{\itemsep}{-0.8pt}%
        \setlength{\parsep}{0pt}%
        \setlength{\topsep}{0pt}%
        \setlength{\partopsep}{0pt}%
        \usecounter{enumiv}%
        \let\p@enumiv\@empty
        \renewcommand\theenumiv{\@arabic\c@enumiv}}%
  \fontsize{6.8pt}{7.9pt}\selectfont
  \sloppy\clubpenalty4000\widowpenalty4000}%
  {\def\@noitemerr{\@latex@warning{Empty `thebibliography' environment}}\endlist}
\makeatother
\begin{thebibliography}{99}

\bibitem{cerf2007delay}
V.~Cerf, S.~Burleigh, A.~Hooke, L.~Torgerson, R.~Durst, K.~Scott, K.~Fall, and H.~Weiss, ``Delay-Tolerant Networking Architecture,'' \emph{IETF RFC 4838}, Apr. 2007.

\bibitem{scott2007bundle}
K.~Scott and S.~Burleigh, ``Bundle Protocol Specification,'' \emph{IETF RFC 5050}, Nov. 2007.

\bibitem{burleigh2022bundle}
S.~Burleigh, K.~Fall, and E.~Birrane, ``Bundle Protocol Version 7,'' \emph{IETF RFC 9171}, Jan. 2022.

\bibitem{birrane2022bundle}
E.~Birrane and K.~McKeever, ``Bundle Security Protocol Specification,'' \emph{IETF RFC 9172}, Jan. 2022.

\bibitem{ramadas2008licklider}
M.~Ramadas, S.~Burleigh, and S.~Farrell, ``Licklider Transmission Protocol - Specification,'' \emph{IETF RFC 5326}, Sep. 2008.

\bibitem{wood2012assessing}
L.~Wood, ``Assessing and Improving an Approach to Delay-Tolerant Networking,'' \emph{arXiv:1204.3264}, 2012.

\bibitem{feldmann2025selected}
M.~Feldmann, T.~N\"{o}thlich, F.~Walter, M.~Nitsch, J.~A.~Fraire, G.~A.~Murzik, and F.~Fuchs, ``REDMARS2: Recursive DTN using BIBE Encapsulation,'' \emph{arXiv:2510.27325}, 2025.

\bibitem{arxiv_custody_bpv7}
A.~Le~Bihan, F.~Flentge, and J.~A.~Fraire, ``Custody Transfer and Compressed Status Reporting for BPv7,'' \emph{arXiv:2507.17403}, 2025.

\bibitem{bernardoni2023algebraic}
W.~Bernardoni, R.~Cardona, and J.~Cleveland, ``Algebraic and Geometric Models for Space Networking,'' \emph{arXiv:2304.01150}, 2023.

\bibitem{sun2022modeling}
X.~Sun, C.~Li, and L.~Yan, ``Modeling of TSRCG and Resource Optimization for LEO Satellite Networks,'' \emph{arXiv:2209.13227}, 2022.

\bibitem{chen2025reliable}
L.~Chen, Y.~Song, and K.~Zhao, ``Reliable Transmission of LTP Using RL-Based Adaptive FEC,'' \emph{arXiv:2506.22470}, 2025.

\bibitem{arxiv_goal_bundle_rl}
M.~Feldmann, R.~Rautenberg, and F.~Walter, ``Goal-Oriented Bundle Management and Deep-Space Flow Control via RL,'' \emph{arXiv:2610.13923}, 2026.

\bibitem{lozano2025learning}
F.~Lozano-Cuadra, B.~Soret, and M.~Sanchez~Net, ``Learning Decentralized Routing Policies via Graph Attention MARL in Lunar DTN,'' \emph{arXiv:2510.20436}, 2025.

\bibitem{madoery2023routing}
P.~G.~Madoery, G.~K.~Kurt, and H.~Yanikomeroglu, ``Routing Heterogeneous Traffic in Delay-Tolerant Satellite Networks,'' \emph{arXiv:2304.13501}, 2023.

\bibitem{alhajj2024improved}
T.~Alhajj and V.~Corlay, ``Improved CGR in Delay Tolerant Networks with Capacity and Buffer Constraints,'' \emph{arXiv:2410.15546}, 2024.

\bibitem{arxiv_neural_lunar_dtn}
M.~Feldmann, S.~Glaser, and F.~Walter, ``NeuraLunaDTNet: Feedforward Neural Network Routing for Lunar DTN,'' \emph{arXiv:2403.20199}, 2024.

\bibitem{arxiv_software_defined_dtn}
F.~Walter, M.~Nitsch, and M.~Feldmann, ``The Architectural Refinement of $\mu$D3TN: Toward a Software-Defined DTN Stack,'' \emph{arXiv:2407.17166}, 2024.

\bibitem{fettes2026energy}
E.~Fettes, P.~G.~Madoery, and H.~Yanikomeroglu, ``Energy Efficient Traffic Scheduling For Optical LEO Satellite Downlinks,'' \emph{arXiv:2603.01334}, 2026.

\bibitem{arxiv_haps_optical_dtn}
A.~Boualem, M.~Ayaida, and H.~Sedjelmaci, ``Next-Generation Satellite IoT: HAPS-Enabled Optical Data Transfer,'' \emph{arXiv:2408.09281}, 2024.

\bibitem{arxiv_clustering_adhoc}
A.~Boualem, M.~Ayaida, H.~Sedjelmaci \emph{et al.}, ``A New Classification of Clustering-based in Wireless Ad-hoc Networks,'' \emph{arXiv:2407.02498}, 2024.

\bibitem{arxiv_autonomous_gnss}
H.~Yan, J.~A.~Fraire, R.~Yang, W.~Li, and K.~Zhao, ``Lightweight Onboard Routing and Topology Co-Construction for Autonomous GNSSs,'' \emph{arXiv:2609.07056}, 2026.

\bibitem{arxiv_bgp_dtn}
M.~Feldmann and T.~Tchilinguirian, ``BGP Extension for Distributing EID Reachability in DTNs,'' \emph{arXiv:2603.01263}, 2026.

\bibitem{burleigh2003delay}
S.~Burleigh, A.~Hooke, L.~Torgerson, K.~Fall, V.~Cerf \emph{et al.}, ``Delay-Tolerant Networking: An Approach to Interplanetary Internet,'' \emph{IEEE Comm. Mag.}, vol.~41, no.~6, pp.~128--136, Jun. 2003.

\bibitem{caini2011delay}
C.~Caini, H.~Cruickshank, S.~Farrell, and M.~Schnittker, ``Delay- and Disruption-Tolerant Networks in Space: A Survey,'' \emph{IEEE Space Hardware}, vol.~5, no.~2, pp.~110--122, 2011.

\bibitem{araniti2015contact}
A.~Araniti, N.~Bischoff, S.~Burleigh, and M.~Ruggieri, ``Contact Graph Routing in DTN Space Networks,'' \emph{IEEE Comm. Mag.}, vol.~53, no.~3, pp.~38--46, Mar. 2015.

\end{thebibliography}
\endgroup

\end{document}
"""

with open("seminar_vishal/seminar.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)

print("seminar_vishal/seminar.tex successfully generated.")
