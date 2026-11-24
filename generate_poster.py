# generate_poster.py
# Generates the complete LaTeX research poster for Vishal's seminar.

import os
import subprocess

poster_tex = r"""\documentclass[11pt]{article}
\usepackage[landscape,a1paper,margin=1.0cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{mathptmx}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{amsmath,amssymb}
\usepackage{tabularx,array,booktabs,multirow}
\usepackage{xcolor}
\usepackage[most]{tcolorbox}
\usepackage{microtype}
\usepackage{enumitem}
\usepackage{ragged2e}

\pagestyle{empty}
\graphicspath{{figures/}{./}}

%% ---------- Color Palette (Deep Space Aerospace Theme) -------------------
\definecolor{spaceblue}{RGB}{11,27,61}         % Deep Navy
\definecolor{navyaccent}{RGB}{22,46,98}        % Mid Navy
\definecolor{accentblue}{RGB}{0,119,182}       % Aerospace Blue
\definecolor{cyancolor}{RGB}{0,180,216}        % Electric Cyan
\definecolor{goldcolor}{RGB}{255,183,3}        % Gold Accent
\definecolor{cardbg}{RGB}{250,252,255}         % Crisp Box Background
\definecolor{cardborder}{RGB}{185,205,230}     % Subtle Border
\definecolor{textdark}{RGB}{25,35,55}          % Body Text
\definecolor{bannerbg}{RGB}{8,18,45}           % Header/Footer Dark

%% ---------- Custom Box Styling -------------------------------------------
\tcbset{
  posterbox/.style={
    colback=cardbg,
    colframe=navyaccent,
    coltitle=white,
    fonttitle=\bfseries\fontsize{13pt}{16pt}\selectfont,
    boxrule=1.5pt,
    arc=3.5mm,
    top=2.5mm, bottom=2.5mm, left=3.0mm, right=3.0mm,
    boxsep=1.5mm,
    enhanced,
    drop shadow=black!15,
    title style={fill=navyaccent},
    attach boxed title to top left={xshift=4mm,yshift=-2.5mm},
    boxed title style={
      boxrule=0.8pt,
      colframe=cyancolor,
      colback=navyaccent,
      arc=2mm,
      top=1.2mm,bottom=1.2mm,left=3mm,right=3mm
    }
  },
  accentbox/.style={
    colback=cardbg,
    colframe=accentblue,
    coltitle=white,
    fonttitle=\bfseries\fontsize{13pt}{16pt}\selectfont,
    boxrule=1.5pt,
    arc=3.5mm,
    top=2.5mm, bottom=2.5mm, left=3.0mm, right=3.0mm,
    boxsep=1.5mm,
    enhanced,
    drop shadow=black!15,
    title style={fill=accentblue},
    attach boxed title to top left={xshift=4mm,yshift=-2.5mm},
    boxed title style={
      boxrule=0.8pt,
      colframe=goldcolor,
      colback=spaceblue,
      arc=2mm,
      top=1.2mm,bottom=1.2mm,left=3mm,right=3mm
    }
  }
}

\setlist{itemsep=1.5pt,topsep=1.5pt,parsep=0pt,partopsep=0pt,leftmargin=14pt}

\begin{document}
\color{textdark}

%% ==========================================================================
%%  HEADER BANNER
%% ==========================================================================
\begin{tcolorbox}[
  colback=bannerbg,
  colframe=spaceblue,
  arc=4mm,
  boxrule=2pt,
  top=4mm, bottom=4mm, left=6mm, right=6mm,
  enhanced,
  drop shadow=black!25
]
\begin{minipage}{0.11\textwidth}
  \centering
  \includegraphics[width=3.6cm,height=3.6cm,keepaspectratio]{figures/logo.png}
\end{minipage}
\hfill
\begin{minipage}{0.64\textwidth}
  \centering
  {\fontsize{14pt}{17pt}\bfseries\color{cyancolor} JAWAHARLAL NEHRU GOVT. ENGINEERING COLLEGE, SUNDERNAGAR}\\[2pt]
  {\fontsize{11pt}{14pt}\color{white!85} Department of Electronics \& Communication Engineering \quad | \quad Affiliated to HPTU Hamirpur}\\[5pt]
  {\fontsize{22pt}{26pt}\bfseries\color{goldcolor} DELAY TOLERANT NETWORKS IN SPACE COMMUNICATIONS}\\[3pt]
  {\fontsize{13pt}{16pt}\bfseries\color{white} Architectural Genesis, Protocol Evolution, and Deterministic Routing from Deep Impact to Artemis}
\end{minipage}
\hfill
\begin{minipage}{0.22\textwidth}
  \fontsize{10.5pt}{13.5pt}\selectfont\color{white}
  \textbf{Author:} Vishal Chandel\\
  \textbf{University Roll No.:} 23010104072\\
  \textbf{Degree:} B.Tech. 7th Semester (ECE)\\
  \textbf{Supervisor:} Dr. Sanjeev Kumar\\
  \textbf{Designation:} Assistant Professor, ECE\\
  \textbf{Academic Year:} 2026--2027
\end{minipage}
\end{tcolorbox}

\vspace{0.35cm}

%% ==========================================================================
%%  3-COLUMN POSTER BODY
%% ==========================================================================
\begin{minipage}[t]{0.322\textwidth}
%% --------------------------------------------------------------------------
%% COLUMN 1: THE PROBLEM, THE PARADIGM, AND THE BUNDLE PROTOCOL
%% --------------------------------------------------------------------------

\begin{tcolorbox}[posterbox, title={1. The Deep-Space Communication Dilemma}]
  \justifying\fontsize{10.2pt}{13pt}\selectfont
  Terrestrial internet standards (\textbf{TCP/IP}) implicitly assume continuous end-to-end paths, negligible propagation delay ($< 100\,\text{ms}$), and low packet loss rates ($< 1\%$). In deep space, fundamental physical laws violate every single assumption:
  \begin{itemize}
    \item \textbf{Astro-Scale Latency:} Light travel time introduces round-trip times (RTT) ranging from $6\,\text{to }44\,\text{minutes}$ for Mars, up to $1.8\,\text{hours}$ for Jupiter, and $2.8\,\text{hours}$ for Saturn.
    \item \textbf{Periodic Line-of-Sight Occlusions:} Celestial body rotation, orbital mechanics, planetary shadowing, and solar conjunctions sever RF/optical links for hours or days.
    \item \textbf{High Bit Error Rates (BER):} Deep-space path loss ($1/R^2$), cosmic microwave noise, and solar flares cause severe frame corruption ($10^{-3} \text{ to } 10^{-1}$).
    \item \textbf{Collapse of TCP:} 3-way handshakes require multiple hours; timers expire continuously; throughput throttles to zero under TCP's AIMD congestion control.
  \end{itemize}
\end{tcolorbox}

\vspace{0.3cm}

\begin{tcolorbox}[posterbox, title={2. The Store-Carry-and-Forward Paradigm}]
  \justifying\fontsize{10.2pt}{13pt}\selectfont
  To overcome the absence of instantaneous end-to-end paths, \textbf{Delay/Disruption Tolerant Networking (DTN)} abandons packet switching in favor of \textbf{Store-Carry-and-Forward message switching}:
  \begin{itemize}
    \item Nodes store message bundles in persistent non-volatile storage (flash/NVRAM) until a planned, future contact window materializes.
    \item Data travels along physical motion vectors (carried by planetary orbiters, rovers, and transit spacecraft) over hours, days, or weeks.
    \item \textbf{Custody Transfer:} Upstream nodes guarantee bundle retransmission until a downstream node explicitly confirms custody acceptance, isolating transmission errors to individual hops.
  \end{itemize}
\end{tcolorbox}

\vspace{0.3cm}

\begin{tcolorbox}[accentbox, title={3. Space DTN Protocol Architecture (BPv7)}]
  \centering
  \includegraphics[width=0.98\textwidth,height=6.2cm,keepaspectratio]{figures/space_dtn_protocol_stack.png}\\[3pt]
  \justifying\fontsize{10pt}{12.5pt}\selectfont
  \textbf{Bundle Protocol Version 7 (BPv7, RFC 9171):} Operates as an overlay layer situated directly above heterogeneous convergence layers:
  \begin{itemize}
    \item \textbf{CBOR Serialization:} Replaces human-readable text with Concise Binary Object Representation, shrinking protocol header overhead by $35\%$.
    \item \textbf{Compressed Custody Signals (CCS):} Resolves Lloyd Wood's critique regarding custody signal amplification; acknowledges hundreds of bundles in single compact bit vectors.
    \item \textbf{BIBE (RFC 9174):} Bundle-in-Bundle Encapsulation enables recursive tunneling across disjoint deep-space subnets without re-encoding original payloads.
  \end{itemize}
\end{tcolorbox}

\end{minipage}
\hfill
%% --------------------------------------------------------------------------
%% COLUMN 2: TRANSPORT RELIABILITY AND DETERMINISTIC ROUTING
%% --------------------------------------------------------------------------
\begin{minipage}[t]{0.322\textwidth}

\begin{tcolorbox}[posterbox, title={4. Transport Layer: LTP (RFC 5326)}]
  \justifying\fontsize{10.2pt}{13pt}\selectfont
  Conventional transport protocols fail across astronomical delays. The \textbf{Licklider Transmission Protocol (LTP)} provides specialized point-to-point convergence reliability over long-delay, error-prone RF and optical links:
  \begin{itemize}
    \item \textbf{Dual Data Service Classes:}
      \begin{itemize}[leftmargin=10pt]
        \item \textit{Red Data (Reliable):} Guaranteed ARQ delivery. Senders emit Checkpoints (CP); receivers acknowledge via Report Segments (RS).
        \item \textit{Green Data (Unreliable):} Best-effort streaming without ACK overhead, ideal for high-rate telemetry, imagery, and loss-tolerant video.
      \end{itemize}
    \item \textbf{RL-Based Adaptive FEC:} Recent research applies Deep Q-Networks (DQN) to dynamically adjust Reed-Solomon / LDPC code rates, minimizing retransmissions under fluctuating space link margins.
  \end{itemize}
\end{tcolorbox}

\vspace{0.3cm}

\begin{tcolorbox}[accentbox, title={5. Deterministic Routing: Contact Graph Routing}]
  \centering
  \includegraphics[width=0.98\textwidth,height=6.0cm,keepaspectratio]{figures/contact_graph_routing_flow.png}\\[3pt]
  \justifying\fontsize{10pt}{12.5pt}\selectfont
  \textbf{Contact Graph Routing (CGR):} Unlike terrestrial stochastic or epidemic routing, deep-space spacecraft trajectories are governed strictly by orbital mechanics:
  \begin{itemize}
    \item \textbf{Contact Plans:} Pre-computed schedules of contact intervals $C_i = [t_s, t_e, \text{Node}_A, \text{Node}_B, \text{Rate}, \text{Range}]$.
    \item \textbf{Dijkstra Over Time:} Finds earliest-delivery-time paths through a directed temporal graph, tracking residual contact volumes to prevent buffer overflow.
    \item \textbf{CGR-ATO \& EAR-CGR:} Enhanced variants dynamically re-route traffic when orbital anomalies or solar flares prematurely terminate a scheduled pass.
  \end{itemize}
\end{tcolorbox}

\vspace{0.3cm}

\begin{tcolorbox}[posterbox, title={6. Next-Generation AI \& SmallSat DTN}]
  \justifying\fontsize{10.2pt}{13pt}\selectfont
  \begin{itemize}
    \item \textbf{Graph Attention Multi-Agent RL (GAT-MARL):} Deployed in lunar constellations to optimize routing under dynamic cross-link jamming and non-deterministic rover demands.
    \item \textbf{Software-Defined Micro-DTN ($\mu$D3TN):} Optimized for resource-constrained CubeSats; written in memory-safe C with a footprint $< 100\,\text{KB}$, enabling inter-satellite mesh routing.
  \end{itemize}
\end{tcolorbox}

\end{minipage}
\hfill
%% --------------------------------------------------------------------------
%% COLUMN 3: OPTICAL LINKS, MISSIONS, AND SYNTHESIS
%% --------------------------------------------------------------------------
\begin{minipage}[t]{0.322\textwidth}

\begin{tcolorbox}[posterbox, title={7. Deep Space Optical Communications (DSOC)}]
  \centering
  \includegraphics[width=0.95\textwidth,height=4.8cm,keepaspectratio]{figures/paper1_fig_p8_1.png}\\[3pt]
  \justifying\fontsize{10pt}{12.5pt}\selectfont
  \textbf{Hybrid RF/Optical Space Downlinks:} NASA's 2023--2024 Psyche DSOC experiment validated gigabit-per-second optical downlinks from deep space:
  \begin{itemize}
    \item Optical channels achieve $100\times$ RF data rates but suffer from cloud attenuation and atmospheric turbulence.
    \item DTN coordinates hybrid RF/Optical scheduling: high-volume bundles buffer until clear optical line-of-sight is established, falling back to S-band RF for command/control.
  \end{itemize}
\end{tcolorbox}

\vspace{0.25cm}

\begin{tcolorbox}[posterbox, title={8. Historical Flight Validations: From DINET to Artemis}]
  \centering
  \fontsize{8.5pt}{10.5pt}\selectfont
  \renewcommand{\arraystretch}{1.12}
  \begin{tabularx}{\textwidth}{|l|l|X|}
    \hline
    \textbf{Year} & \textbf{Flight Mission} & \textbf{Key Technical Milestone Validated} \\
    \hline
    2008 & Deep Impact (DINET) & First interplanetary DTN test; 9-node simulated mesh over 15M miles. \\
    2012 & ISS-to-Earth LEGO & Cosmonaut remotely steered terrestrial rover via DTN from space station. \\
    2016 & ISS ESA Meteor & First continuous operational DTN payload aboard the ISS. \\
    2022 & Artemis I & Orion capsule tested DTN telemetry with Deep Space Network (DSN). \\
    2026+ & Artemis II/III \& Gateway & Full autonomous LunaNet architecture with DTN/BPv7 backbone. \\
    \hline
  \end{tabularx}
\end{tcolorbox}

\vspace{0.25cm}

\begin{tcolorbox}[posterbox, title={9. Cyber-Security \& Open Frontiers}]
  \justifying\fontsize{10pt}{12.5pt}\selectfont
  \textbf{Bundle Security Protocol (BPSec, RFC 9172):}
  \begin{itemize}
    \item Provides Block Integrity (BIB) and Block Confidentiality (BCB) without interactive TLS/PKI handshakes.
    \item \textbf{Open Research Challenges:} Scalability of contact plan distribution across multi-hop constellations; quantum optical key exchange; cross-domain interoperability across international space agencies.
  \end{itemize}
\end{tcolorbox}

\vspace{0.25cm}

\begin{tcolorbox}[posterbox, title={10. Key References \& Acknowledgements}]
  \fontsize{8pt}{10pt}\selectfont
  \textbf{[1]} V.~Cerf et al., ``Delay-Tolerant Networking Architecture,'' \emph{RFC 4838}, 2007. \quad
  \textbf{[2]} S.~Burleigh et al., ``Contact Graph Routing,'' \emph{IEEE Communications Magazine}, 2016. \quad
  \textbf{[3]} M.~Blanchet et al., ``Bundle Protocol Version 7,'' \emph{RFC 9171}, 2022. \quad
  \textbf{[4]} NASA, ``LunaNet Interoperability Specification,'' \emph{NASA/TM-2023-0001}, 2023.\\[2pt]
  \textit{Sincere gratitude to Dr. Sanjeev Kumar and Dept. of ECE, JNGEC Sundernagar for supervision and academic support.}
\end{tcolorbox}

\end{minipage}

\vfill

%% ==========================================================================
%%  FOOTER BANNER
%% ==========================================================================
\begin{tcolorbox}[
  colback=bannerbg,
  colframe=spaceblue,
  arc=3mm,
  boxrule=1.5pt,
  top=2.5mm, bottom=2.5mm, left=5mm, right=5mm,
  enhanced
]
\begin{center}
  \fontsize{10.5pt}{13pt}\selectfont\color{white}
  \textbf{Department of Electronics \& Communication Engineering \quad | \quad Jawaharlal Nehru Government Engineering College, Sundernagar, Mandi (H.P.)}\\
  \color{cyancolor}Himachal Pradesh Technical University (HPTU), Hamirpur \quad | \quad Seminar Technical Series 2026--2027
\end{center}
\end{tcolorbox}

\end{document}
"""

with open(r"seminar_vishal\poster.tex", "w", encoding="utf-8") as f:
    f.write(poster_tex)

print("Wrote seminar_vishal/poster.tex successfully!")
