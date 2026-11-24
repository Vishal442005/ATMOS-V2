# generate_beamer_slides.py
# Generates the complete LaTeX Beamer presentation (16:9 widescreen) for Vishal's seminar.

import os
import subprocess

beamer_tex = r"""\documentclass[aspectratio=169,10pt]{beamer}

\usepackage[T1]{fontenc}
\usepackage{mathptmx}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{amsmath,amssymb}
\usepackage{tabularx,array,booktabs,multirow}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{tcolorbox}

\graphicspath{{figures/}{./}}

%% ---------- Color Palette (Deep Space Theme) -----------------------------
\definecolor{spaceblue}{RGB}{11,27,61}
\definecolor{navyaccent}{RGB}{22,46,98}
\definecolor{accentblue}{RGB}{0,119,182}
\definecolor{cyancolor}{RGB}{0,180,216}
\definecolor{goldcolor}{RGB}{255,183,3}
\definecolor{cardbg}{RGB}{248,249,252}
\definecolor{textdark}{RGB}{30,41,59}

%% ---------- Beamer Theme Customization -----------------------------------
\usetheme{Madrid}
\usecolortheme{default}

\setbeamercolor{palette primary}{bg=spaceblue,fg=white}
\setbeamercolor{palette secondary}{bg=navyaccent,fg=white}
\setbeamercolor{palette tertiary}{bg=accentblue,fg=white}
\setbeamercolor{structure}{fg=accentblue}
\setbeamercolor{frametitle}{bg=spaceblue,fg=white}
\setbeamercolor{title}{bg=spaceblue,fg=goldcolor}
\setbeamercolor{subtitle}{fg=cyancolor}
\setbeamercolor{author}{fg=white}
\setbeamercolor{institute}{fg=white!85}
\setbeamercolor{date}{fg=goldcolor}
\setbeamercolor{block title}{bg=navyaccent,fg=white}
\setbeamercolor{block body}{bg=cardbg,fg=textdark}
\setbeamercolor{block title alerted}{bg=red!70!black,fg=white}
\setbeamercolor{block body alerted}{bg=red!5!white,fg=textdark}
\setbeamercolor{block title example}{bg=accentblue,fg=white}
\setbeamercolor{block body example}{bg=accentblue!5!white,fg=textdark}

\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{
  \leavevmode%
  \hbox{%
  \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,left]{author in head/foot}%
    \usebeamerfont{author in head/foot}\hspace*{2ex}Vishal Chandel (23010104072)
  \end{beamercolorbox}%
  \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,center]{title in head/foot}%
    \usebeamerfont{title in head/foot}Delay Tolerant Networks in Space
  \end{beamercolorbox}%
  \begin{beamercolorbox}[wd=.333333\paperwidth,ht=2.25ex,dp=1ex,right]{date in head/foot}%
    \usebeamerfont{date in head/foot}\insertframenumber{} / \inserttotalframenumber\hspace*{2ex}
  \end{beamercolorbox}}%
  \vskip0pt%
}

%% ---------- Title & Author Metadata --------------------------------------
\title[Delay Tolerant Networks in Space Communications]{\Large\textbf{DELAY TOLERANT NETWORKS IN SPACE COMMUNICATIONS}}
\subtitle{\small Architectural Genesis, Protocol Evolution, and Deterministic Routing from Deep Impact to Artemis}
\author[\textbf{Vishal Chandel}]{\textbf{Vishal Chandel} (Roll No.: \textbf{23010104072})\\[2pt]
\footnotesize Under the Guidance of: \textbf{Dr. Sanjeev Kumar}, Assistant Professor}
\institute[JNGEC]{\footnotesize Department of Electronics \& Communication Engineering\\
\textbf{Jawaharlal Nehru Government Engineering College, Sundernagar}\\
\textit{Affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur}}
\date[2026--2027]{B.Tech. Technical Seminar \quad | \quad Academic Year 2026--2027}
\titlegraphic{\includegraphics[height=1.2cm]{figures/logo.png}}

\begin{document}

%% =========================================================================
%% SLIDE 1: TITLE SLIDE
%% =========================================================================
\begin{frame}[plain]
  \titlepage
\end{frame}

%% =========================================================================
%% SLIDE 2: PRESENTATION AGENDA
%% =========================================================================
\begin{frame}{Seminar Presentation Roadmap}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{block}{1. Physical & Theoretical Foundations}
    \begin{itemize}
      \item The Space Communication Dilemma
      \item Fatal Breakdown of Terrestrial TCP/IP
      \item Store-Carry-and-Forward Paradigm
    \end{itemize}
  \end{block}
  \begin{block}{2. Architecture & The Bundle Protocol}
    \begin{itemize}
      \item BPv7 Overlay Architecture (RFC 9171)
      \item Evolution: BPv6 to BPv7 & CBOR Encoding
      \item Recursive DTN & BIBE Encapsulation
    \end{itemize}
  \end{block}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{block}{3. Transport & Deterministic Routing}
    \begin{itemize}
      \item Licklider Transmission Protocol (LTP)
      \item Reinforcement Learning Adaptive FEC
      \item Contact Graph Routing (CGR) Mechanics
      \item Next-Gen Graph Attention MARL AI
    \end{itemize}
  \end{block}
  \begin{block}{4. Frontiers, Missions & Synthesis}
    \begin{itemize}
      \item Deep Space Optical Communications (DSOC)
      \item Bundle Security Protocol (BPSec, RFC 9172)
      \item From DINET (2008) to Artemis LunaNet
    \end{itemize}
  \end{block}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 3: THE DEEP-SPACE COMMUNICATION REALITY
%% =========================================================================
\begin{frame}{The Deep-Space Communication Reality: Physical Extremes}
\begin{columns}[T]
\begin{column}{0.32\textwidth}
  \begin{exampleblock}{Astronomical Latency}
    \begin{itemize}\footnotesize
      \item \textbf{Moon:} $1.28\,\text{s}$ one-way.
      \item \textbf{Mars:} $3.1 \text{ to } 22.3\,\text{min}$ ($6.2 \text{ to } 44.6\,\text{min}$ RTT).
      \item \textbf{Jupiter:} $33 \text{ to } 53\,\text{min}$.
      \item \textbf{Voyager 1:} $> 22.5\,\text{hours}$.
      \item Interactive feedback loops are physically impossible.
    \end{itemize}
  \end{exampleblock}
\end{column}
\begin{column}{0.32\textwidth}
  \begin{alertblock}{Link Intermittency}
    \begin{itemize}\footnotesize
      \item \textbf{Planetary Rotation:} Disconnects ground antennas every $12\text{--}24\,\text{h}$.
      \item \textbf{Orbital Shadowing:} Passing behind moons/planets.
      \item \textbf{Solar Conjunction:} Sun severs Earth-Mars link for $\sim 2\,\text{weeks}$.
      \item Instantaneous end-to-end paths \textbf{never exist}.
    \end{itemize}
  \end{alertblock}
\end{column}
\begin{column}{0.32\textwidth}
  \begin{block}{Severe Path Loss & Noise}
    \begin{itemize}\footnotesize
      \item \textbf{Path Loss ($1/R^2$):} Signal attenuation exceeds $200\,\text{dB}$.
      \item \textbf{High BER:} $10^{-3} \text{ to } 10^{-1}$ during solar storms.
      \item \textbf{Asymmetric Links:} kW DSN uplink vs. $20\text{--}50\,\text{W}$ spacecraft downlink.
    \end{itemize}
  \end{block}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 4: THE COLLAPSE OF TERRESTRIAL TCP/IP IN SPACE
%% =========================================================================
\begin{frame}{The Fatal Breakdown of Terrestrial TCP/IP in Space}
\begin{columns}[T]
\begin{column}{0.52\textwidth}
  \begin{alertblock}{Failure Modes of Standard TCP/IP}
    \begin{itemize}\footnotesize
      \item \textbf{Three-Way Handshake (SYN $\to$ SYN-ACK $\to$ ACK):} On Mars, establishing a connection requires $40\text{--}60\,\text{minutes}$ before sending a single payload byte!
      \item \textbf{Retransmission Timers (RTO):} Standard RTO ($200\,\text{ms} \text{ to } 2\,\text{s}$) fires continuously across interplanetary delays, causing perpetual spurious retransmissions.
      \item \textbf{AIMD Congestion Collapse:} TCP interprets link bit errors as congestion, halving cwnd repeatedly until throughput drops to zero.
      \item \textbf{DNS Resolution:} Interactive name lookups fail across multi-minute links.
    \end{itemize}
  \end{alertblock}
\end{column}
\begin{column}{0.45\textwidth}
  \begin{block}{Terrestrial vs. Space Environment}
    \footnotesize
    \begin{tabular}{|l|p{2.0cm}|p{2.0cm}|}
      \hline
      \textbf{Parameter} & \textbf{Terrestrial} & \textbf{Deep Space} \\
      \hline
      Path Continuity & Continuous & Intermittent \\
      Propagation & $< 100\,\text{ms}$ & Minutes--hours \\
      Primary Loss & Congestion & Path loss, BER \\
      Bandwidth & Symmetric & Asymmetric \\
      \hline
    \end{tabular}
    \vspace{0.3cm}
    \centering
    \color{red!80!black}\textbf{Conclusion: Terrestrial TCP/IP is fundamentally non-viable in deep space.}
  \end{block}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 5: STORE-CARRY-AND-FORWARD PARADIGM
%% =========================================================================
\begin{frame}{The Paradigm Shift: Store-Carry-and-Forward Networking}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{block}{Store-Carry-and-Forward Mechanics}
    \begin{itemize}\footnotesize
      \item \textbf{Bundle-Oriented:} Discards streaming packets in favor of self-contained message bundles containing metadata, lifetime, and routing headers.
      \item \textbf{Persistent Hop-by-Hop Storage:} Nodes store bundles in non-volatile flash memory/NVRAM for hours or days awaiting contact windows.
      \item \textbf{Exploitation of Orbital Motion:} Orbiters and rovers physically transport stored data across orbital space.
    \end{itemize}
  \end{block}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{Custody Transfer Error Isolation}
    \begin{itemize}\footnotesize
      \item \textbf{Custody Request:} Upstream node sends bundle and retains copy.
      \item \textbf{Custody Acceptance:} Downstream node stores bundle, verifies integrity, and emits a \textbf{Custody Signal (CS)}.
      \item \textbf{Local Retransmission:} Upstream node releases its copy only after receiving CS.
      \item \textbf{Hop-by-Hop Reliability:} Eliminates end-to-end multi-hour retransmission timeouts.
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 6: THE SPACE DTN PROTOCOL ARCHITECTURE (BPv7)
%% =========================================================================
\begin{frame}{The Space DTN Protocol Architecture (BPv7, RFC 9171)}
\begin{columns}[T]
\begin{column}{0.52\textwidth}
  \centering
  \includegraphics[width=\textwidth,height=5.6cm,keepaspectratio]{figures/space_dtn_protocol_stack.png}
\end{column}
\begin{column}{0.45\textwidth}
  \begin{block}{Architectural Pillars of BPv7}
    \begin{itemize}\footnotesize
      \item \textbf{Overlay Layer:} Sits between application and heterogeneous lower-layer transports.
      \item \textbf{Convergence Layer Adapters (CLA):} Interfaces BPv7 with LTP, TCPCL, UDPCL, and CCSDS space data links.
      \item \textbf{Endpoint Identifiers (EIDs):} Uniform URI-based naming (\texttt{ipn:node.service} or \texttt{dtn://mars-rover/data}).
      \item \textbf{Interplanetary Gateway:} Unifies terrestrial fiber, lunar mesh, and deep-space RF/laser.
    \end{itemize}
  \end{block}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 7: EVOLUTION: BPv6 TO BPv7
%% =========================================================================
\begin{frame}{Evolution of the Bundle Protocol: From BPv6 to BPv7}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{alertblock}{Legacy BPv6 (RFC 5050, 2007)}
    \begin{itemize}\footnotesize
      \item \textbf{SDNV Encoding:} Self-Delimiting Numeric Values and verbose ASCII text strings.
      \item \textbf{Lloyd Wood's 2009 Critique:} Identified severe custody signal proliferation (each bundle required an individual custody signal, choking reverse links).
      \item \textbf{High Header Overhead:} Significant bandwidth consumed on low-bitrate links.
      \item \textbf{Experimental Security:} Standalone BSP (RFC 6257).
    \end{itemize}
  \end{alertblock}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{Modern BPv7 Standard (RFC 9171, 2022)}
    \begin{itemize}\footnotesize
      \item \textbf{CBOR Serialization:} Concise Binary Object Representation (RFC 8949) shrinks headers by $\mathbf{35\%}$.
      \item \textbf{Compressed Custody Signals (CCS):} Single custody signal acknowledges hundreds of bundles via bit vectors.
      \item \textbf{Decoupled Custody Management:} Handled cleanly via administrative records.
      \item \textbf{Native BPSec (RFC 9172):} Cryptographic integrity and confidentiality.
      \item \textbf{Baseline for Artemis & LunaNet.}
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 8: RECURSIVE DTN & BIBE ENCAPSULATION
%% =========================================================================
\begin{frame}{Recursive DTN: Bundle-in-Bundle Encapsulation (BIBE, RFC 9174)}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{block}{The Multi-Domain Challenge}
    \begin{itemize}\footnotesize
      \item Space missions span heterogeneous subnets:
        \begin{itemize}[leftmargin=10pt]
          \item Lunar Surface Mesh (Low-power RF)
          \item High-Capacity Gateway Relays
          \item Terrestrial DSN Ground Stations
        \end{itemize}
      \item Subnets use different EID formats (IPN vs. DTN) and security policies.
      \item Modifying bundle headers at gateways breaks end-to-end cryptographic signatures!
    \end{itemize}
  \end{block}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{BIBE Tunneling Solution}
    \begin{itemize}\footnotesize
      \item \textbf{Carrier Bundles:} The entire original bundle (headers, security blocks, payload) is packaged inside the payload of an outer carrier bundle.
      \item \textbf{Signature Preservation:} Intermediate nodes route the carrier bundle without touching internal signatures.
      \item \textbf{Aggregation:} Multiple small bundles for the same destination are batched into a single outer bundle.
      \item Standardized in \textbf{RFC 9174 (2022)}.
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 9: TRANSPORT RELIABILITY: LTP (RFC 5326)
%% =========================================================================
\begin{frame}{Transport Layer Reliability: Licklider Transmission Protocol (LTP)}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{block}{Dual Service Classes (RFC 5326)}
    \begin{itemize}\footnotesize
      \item \textbf{Red Data Service (Reliable):}
        \begin{itemize}[leftmargin=8pt]
          \item Guaranteed delivery via Selective Negative Acknowledgement (SNACK) ARQ.
          \item Checkpoint (CP) flags request receiver status.
          \item Report Segments (RS) communicate missing bytes.
          \item Used for flight software, commands, science telemetry.
        \end{itemize}
      \item \textbf{Green Data Service (Unreliable):}
        \begin{itemize}[leftmargin=8pt]
          \item Best-effort transmission without ACK overhead.
          \item Ideal for loss-tolerant video, imagery, real-time sensing.
        \end{itemize}
    \end{itemize}
  \end{block}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{Checkpoint & Report Segment Protocol}
    \begin{itemize}\footnotesize
      \item \textbf{Streaming Transmission:} Red segments are transmitted continuously without waiting for per-packet ACKs.
      \item \textbf{Checkpointing:} Sender marks final segment of Red block with CP bit.
      \item \textbf{Selective Retransmission:} Receiver issues Report Segment indicating exact missing byte ranges; sender retransmits only those bytes!
      \item \textbf{Continuous Transmission:} Next block begins transmitting immediately during the round-trip wait.
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 10: INTELLIGENT TRANSPORT: ADAPTIVE FEC
%% =========================================================================
\begin{frame}{Intelligent Transport Optimizations: Adaptive Forward Error Correction}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{alertblock}{Problem with Static Coding Rates}
    \begin{itemize}\footnotesize
      \item Deep-space links experience dynamic SNR swings due to solar plasma, weather, and antenna pointing.
      \item \textbf{Over-protecting (Rate 1/3):} Wastes channel bandwidth during clear conditions.
      \item \textbf{Under-protecting (Rate 7/8):} Causes block corruption and multi-hour ARQ retransmission delays.
    \end{itemize}
  \end{alertblock}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{Deep Q-Learning Adaptive FEC (Wang \& Li, 2023)}
    \begin{itemize}\footnotesize
      \item \textbf{DQN Agent:} Observes channel SNR, queue backlog, and residual contact duration.
      \item \textbf{Dynamic Code Rate Selection:} Seamlessly switches between Reed-Solomon RS(255, 223) and multi-rate LDPC codes.
      \item \textbf{Performance Milestones:}
        \begin{itemize}[leftmargin=8pt]
          \item $\mathbf{34\%}$ reduction in delivery latency.
          \item $\mathbf{42\%}$ decrease in ARQ retransmissions.
          \item Preserves scarce onboard battery reserves.
        \end{itemize}
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 11: THE ROUTING PARADIGM SHIFT
%% =========================================================================
\begin{frame}{The Routing Paradigm Shift: Stochastic to Deterministic}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{alertblock}{Terrestrial / Epidemic Routing (Stochastic)}
    \begin{itemize}\footnotesize
      \item \textbf{Assumes Random Motion:} Ground vehicles/pedestrians move unpredictably.
      \item \textbf{Epidemic Routing (Vahdat 2000):} Floods duplicate copies to every node encountered.
      \item \textbf{PRoPHET Routing (Lindgren 2003):} Estimates delivery probability from past contacts.
      \item \textbf{Fails in Deep Space:} Flooding exhausts spacecraft storage, consumes battery, and wastes bandwidth.
    \end{itemize}
  \end{alertblock}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{Deep-Space Routing (Deterministic)}
    \begin{itemize}\footnotesize
      \item \textbf{Keplerian Orbital Mechanics:} Spacecraft positions are known months in advance with sub-second precision.
      \item \textbf{Predictable Contacts:} Contact start, end, rate, and distance are completely scheduled.
      \item \textbf{Single-Copy Forwarding:} Deterministic routing delivers a single bundle copy along the optimal path.
      \item \textbf{Foundation for Contact Graph Routing (CGR).}
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 12: CONTACT GRAPH ROUTING (CGR) ARCHITECTURE
%% =========================================================================
\begin{frame}{Contact Graph Routing (CGR) Architecture & Mechanics}
\begin{columns}[T]
\begin{column}{0.52\textwidth}
  \centering
  \includegraphics[width=\textwidth,height=5.6cm,keepaspectratio]{figures/contact_graph_routing_flow.png}
\end{column}
\begin{column}{0.45\textwidth}
  \begin{block}{CGR Algorithmic Mechanics}
    \begin{itemize}\footnotesize
      \item \textbf{Contact Plan:} Pre-computed schedule of contacts:
        $C_i = [t_s, t_e, \text{Node}_A, \text{Node}_B, \text{Rate}]$.
      \item \textbf{Contact Volume:} Maximum bits transferable:
        $V_i = (t_e - t_s) \times \text{Rate}$.
      \item \textbf{Dijkstra Over Time:} Modified shortest-path search computes \textbf{Earliest Delivery Time (EDT)} across time-varying edges.
      \item \textbf{Capacity Tracking:} Deducts bundle sizes from remaining contact volume to avoid oversubscription.
    \end{itemize}
  \end{block}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 13: CGR ENHANCEMENTS: CAPACITY & BUFFER CONSTRAINTS
%% =========================================================================
\begin{frame}{CGR Enhancements: Capacity and Buffer Constraints}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{alertblock}{The Vanilla CGR Overbooking Flaw}
    \begin{itemize}\footnotesize
      \item Independent space nodes select the same optimal high-bandwidth relay simultaneously.
      \item Arrival volume exceeds contact capacity ($V_{arr} > V_i$).
      \item Intermediate relay buffers overflow, causing dropped bundles and expensive retransmissions.
    \end{itemize}
  \end{alertblock}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{Modern Enhanced CGR Variants}
    \begin{itemize}\footnotesize
      \item \textbf{CGR-ATO (Avoid Time Overbooking):} Tracks chronological capacity depletion, preventing bundle collisions.
      \item \textbf{EAR-CGR (Energy & Storage Aware):} Integrates battery state-of-charge and flash storage capacity into path weights.
      \item \textbf{Opportunistic Multi-Pathing:} Splits massive science datasets across parallel orbiters.
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 14: NEXT-GENERATION AI ROUTING: GAT-MARL
%% =========================================================================
\begin{frame}{Next-Generation AI Routing: Graph Attention MARL}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{block}{Challenges in Mega-Constellations}
    \begin{itemize}\footnotesize
      \item Swarms of 50+ lunar/Martian SmallSats create combinatorially massive contact graphs.
      \item Unpredictable orbital drag, solar flare jamming, and ad-hoc rover transmissions disrupt static schedules.
      \item Centralized Dijkstra recomputations overwhelm radiation-hardened spacecraft CPUs.
    \end{itemize}
  \end{block}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{Graph Attention Multi-Agent RL (Zhang 2024)}
    \begin{itemize}\footnotesize
      \item \textbf{Distributed Agents:} Each satellite runs a local neural policy.
      \item \textbf{Graph Attention Networks (GAT):} Dynamically weights neighbor links by SNR, residual contact time, and queue backlog.
      \item \textbf{CTDE Framework:} Centralized training offline, decentralized execution with sub-millisecond inference onboard.
      \item $\mathbf{28\%}$ higher throughput under link jamming.
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 15: DEEP SPACE OPTICAL COMMUNICATIONS (DSOC)
%% =========================================================================
\begin{frame}{Deep Space Optical Communications (DSOC)}
\begin{columns}[T]
\begin{column}{0.52\textwidth}
  \centering
  \includegraphics[width=\textwidth,height=5.6cm,keepaspectratio]{figures/paper1_fig_p8_1.png}
\end{column}
\begin{column}{0.45\textwidth}
  \begin{block}{NASA Psyche DSOC Flight Results}
    \begin{itemize}\footnotesize
      \item \textbf{Gigabit Optical Links:} Demonstrated $267\,\text{Mbps}$ downlinks from $31\,\text{million km}$ (130$\times$ Earth-Moon distance).
      \item \textbf{Weather Vulnerability:} Laser beams are completely blocked by terrestrial clouds and fog.
      \item \textbf{DTN Integration:}
        \begin{itemize}[leftmargin=8pt]
          \item Store-Carry-and-Forward holds gigabit datasets.
          \item Bursts data down during clear optical windows.
          \item Falls back to RF for critical command/telemetry.
        \end{itemize}
    \end{itemize}
  \end{block}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 16: HAPS RELAYS & SMALLSAT MICRO-DTN
%% =========================================================================
\begin{frame}{HAPS Relays & SmallSat Micro-DTN ($\mu$D3TN)}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{block}{High Altitude Pseudo-Satellites (HAPS)}
    \begin{itemize}\footnotesize
      \item \textbf{Stratospheric Solar Drones:} Fly at $20\,\text{km}$ altitude, permanently above clouds and weather.
      \item \textbf{Optical Collectors:} Act as space optical ground stations with zero cloud blockage.
      \item \textbf{Downlink Relay:} Forwards bundles to ground fiber networks via high-frequency millimeter RF.
      \item Boosts optical availability from $60\%$ to $>\mathbf{98\%}$.
    \end{itemize}
  \end{block}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{Software-Defined Micro-DTN ($\mu$D3TN)}
    \begin{itemize}\footnotesize
      \item Developed by DLR / TU Dresden for CubeSats.
      \item \textbf{Ultra-Low Footprint:} RAM $< 100\,\text{KB}$, storage $< 256\,\text{KB}$; runs on bare-metal ARM Cortex-M.
      \item \textbf{Full BPv7 & LTP Compliance:} Implements RFC 9171 and RFC 5326 in memory-safe ANSI C.
      \item Flight-validated on orbital CubeSats (OPS-SAT, SONATE-2).
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 17: DEEP-SPACE CYBER-SECURITY: BPSEC (RFC 9172)
%% =========================================================================
\begin{frame}{Deep-Space Cyber-Security: Bundle Security Protocol (BPSec)}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{alertblock}{Deep-Space Security Hurdles}
    \begin{itemize}\footnotesize
      \item \textbf{No Online Certificate Authority:} OCSP and CRL lookups fail across multi-hour delays.
      \item \textbf{No Interactive TLS Handshakes:} Handshakes are impossible without real-time round trips.
      \item \textbf{Untrusted Relays:} Data transits commercial and coalition orbiters; payloads must remain confidential.
      \item \textbf{Replay Attacks:} Spacecraft command sequences must be strictly protected against delayed replays.
    \end{itemize}
  \end{alertblock}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{BPSec Architecture (RFC 9172, 2022)}
    \begin{itemize}\footnotesize
      \item \textbf{Block Integrity Block (BIB):} Digital signatures (HMAC-SHA256, ECDSA) over target blocks.
      \item \textbf{Block Confidentiality Block (BCB):} Encrypts target blocks with AES-GCM-256 authenticated encryption.
      \item \textbf{Pre-Shared Key (PSK) Infrastructure:} Schedule-based epoch key rotation.
      \item Enables relays to read routing headers while scientific payloads remain fully encrypted end-to-end.
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 18: HISTORICAL FLIGHT VALIDATIONS
%% =========================================================================
\begin{frame}{Historical Flight Validations: From DINET to the ISS}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \centering
  \includegraphics[width=\textwidth,height=5.4cm,keepaspectratio]{figures/paper7_fig_p3_1.png}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{block}{Operational Flight Milestones}
    \begin{itemize}\footnotesize
      \item \textbf{2008 - Deep Impact (DINET):} NASA JPL tested 9-node interplanetary mesh across 15 million miles.
      \item \textbf{2012 - ISS LEGO Rover:} ESA Astronaut Sunita Williams remotely steered a rover in Germany via DTN.
      \item \textbf{2016 - ISS Operational DTN:} Continuous operational deployment on the International Space Station.
      \item \textbf{2022 - Artemis I:} Orion capsule validated DTN/LTP telemetry with the Deep Space Network (DSN).
    \end{itemize}
  \end{block}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 19: THE ARTEMIS ERA: LUNANET & GATEWAY
%% =========================================================================
\begin{frame}{The Artemis Era: LunaNet and the Lunar Gateway Backbone}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{block}{LunaNet Architecture (NASA/TM-2023-0001)}
    \begin{itemize}\footnotesize
      \item Unified framework for lunar surface and orbital infrastructure:
        \begin{itemize}[leftmargin=8pt]
          \item \textbf{Communications:} Disruption-tolerant relay via BPv7.
          \item \textbf{PNT:} Lunar positioning, navigation, and timing.
          \item \textbf{Science Utilization:} Space weather alerts.
        \end{itemize}
      \item Mandates \textbf{BPv7, LTP, and BPSec} across all international lunar landers, rovers, and orbiters.
    \end{itemize}
  \end{block}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{exampleblock}{The Lunar Gateway Interplanetary Hub}
    \begin{itemize}\footnotesize
      \item \textbf{Near-Rectilinear Halo Orbit (NRHO):} Constant Earth line-of-sight and continuous lunar South Pole coverage.
      \item \textbf{Surface Aggregation:} Gateway aggregates low-power rover data via Ka-band proximity links.
      \item \textbf{High-Speed Trunk Downlink:} Blasts bundled science data back to Earth via optical laser links.
      \item Proving ground for future Martian infrastructure.
    \end{itemize}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 20: SYNTHESIS MATRIX OF LITERATURE
%% =========================================================================
\begin{frame}{Comparative Synthesis Matrix of Evaluated Literature}
\centering\footnotesize
\renewcommand{\arraystretch}{1.1}
\begin{tabular}{|l|l|p{4.2cm}|p{3.2cm}|}
\hline
\textbf{Author \& Year} & \textbf{Protocol / Domain} & \textbf{Scientific Contribution} & \textbf{Key Performance Metric} \\
\hline
Cerf et al. (2007) & RFC 4838 (DTN) & Store-Carry-and-Forward overlay architecture & Foundational interplanetary standard \\
Burleigh et al. (2016) & CGR / ION & Deterministic Dijkstra over celestial contacts & 0\% packet drops on scheduled links \\
Blanchet et al. (2022) & BPv7 (RFC 9171) & CBOR binary encoding \& compressed custody & 35\% header size reduction \\
Farrell et al. (2023) & BIBE (RFC 9174) & Recursive bundle encapsulation across subnets & Cross-gateway tunneling \\
Wang \& Li (2023) & Adaptive FEC & Deep Q-Learning code rate adaptation & 42\% fewer ARQ retransmissions \\
Zhang \& Liu (2024) & GAT-MARL AI & Graph Attention Multi-Agent RL & 28\% higher throughput in jamming \\
NASA / ESA (2023) & LunaNet Standard & Mandatory BPv7/BPSec for Artemis & Global international baseline \\
\hline
\end{tabular}
\end{frame}

%% =========================================================================
%% SLIDE 21: CRITICAL OPEN CHALLENGES
%% =========================================================================
\begin{frame}{Critical Open Research Challenges & Future Roadmap}
\begin{columns}[T]
\begin{column}{0.48\textwidth}
  \begin{alertblock}{1. Contact Plan Scalability}
    \begin{itemize}\footnotesize
      \item Mega-constellations (hundreds of CubeSats) make centralized contact distribution intractable.
      \item Requires decentralized, autonomous contact discovery.
    \end{itemize}
  \end{alertblock}
  \begin{alertblock}{2. Quantum Space DTN}
    \begin{itemize}\footnotesize
      \item Merging Quantum Key Distribution (QKD) and quantum repeaters with asynchronous DTN storage.
    \end{itemize}
  \end{alertblock}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{block}{3. Deep-Space AI Security}
    \begin{itemize}\footnotesize
      \item Protecting onboard RL routing policies against adversarial telemetry poisoning and spoofed ephemerides.
    \end{itemize}
  \end{block}
  \begin{block}{4. Energy-Constrained SmallSats}
    \begin{itemize}\footnotesize
      \item Synchronizing deep sleep states and orbital wake-up timers without GPS drift over months.
    \end{itemize}
  \end{block}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 22: CONCLUSION
%% =========================================================================
\begin{frame}{Conclusion & Key Seminar Takeaways}
\begin{exampleblock}{Summary of Contributions}
  \begin{enumerate}\footnotesize
    \item \textbf{Paradigm Validation:} Delay/Disruption Tolerant Networking is the only physically viable protocol suite capable of bridging astronomical propagation delays and orbital occlusions.
    \item \textbf{Maturity of Standards:} Standardized BPv7 (RFC 9171) with CBOR binary serialization and Compressed Custody Signals has resolved legacy scalability bottlenecks.
    \item \textbf{Deterministic Routing:} Contact Graph Routing (CGR) and Graph Attention MARL AI exploit celestial mechanics to achieve optimal forwarding with zero redundant flooding.
    \item \textbf{Operational Reality:} DTN is flight-proven (DINET, ISS, Artemis I) and serves as the mandatory operational backbone for NASA/ESA LunaNet and the Lunar Gateway.
  \end{enumerate}
\end{exampleblock}
\begin{center}
  \color{accentblue}\textbf{Space DTN is the foundational protocol architecture for humanity's interplanetary internet.}
\end{center}
\end{frame}

%% =========================================================================
%% SLIDE 23: REFERENCES & ACKNOWLEDGEMENTS
%% =========================================================================
\begin{frame}{Key References & Academic Acknowledgements}
\begin{columns}[T]
\begin{column}{0.62\textwidth}
  \begin{block}{Key References}
    \tiny
    \begin{itemize}
      \item[1.] V. Cerf et al., ``Delay-Tolerant Networking Architecture,'' \emph{RFC 4838}, 2007.
      \item[2.] K. Fall, ``A delay-tolerant network architecture for challenged internets,'' \emph{ACM SIGCOMM}, 2003.
      \item[3.] S. Burleigh et al., ``Contact Graph Routing: An Overview,'' \emph{IEEE Comm. Mag.}, 2016.
      \item[4.] M. Blanchet et al., ``Bundle Protocol Version 7,'' \emph{RFC 9171}, 2022.
      \item[5.] M. Ramadas et al., ``Licklider Transmission Protocol - Specification,'' \emph{RFC 5326}, 2008.
      \item[6.] E. Birrane et al., ``Bundle Security Protocol Specification (BPSec),'' \emph{RFC 9172}, 2022.
      \item[7.] NASA, ``LunaNet Interoperability Specification,'' \emph{NASA/TM-2023-0001}, 2023.
      \item[8.] L. Wood et al., ``A critique of custody transfer in DTN,'' \emph{IEEE Aerospace Conf.}, 2009.
    \end{itemize}
  \end{block}
\end{column}
\begin{column}{0.35\textwidth}
  \begin{exampleblock}{Acknowledgements}
    \footnotesize
    \textbf{Supervisor:}\\
    Dr. Sanjeev Kumar, Assistant Professor\\
    Dept. of ECE, JNGEC Sundernagar\\[4pt]
    \textbf{Department Head:}\\
    Dr. Ashwani Kumar, HOD ECE\\[4pt]
    \textbf{Director:}\\
    Prof. (Dr.) Rajeshwar Singh\\[4pt]
    \textit{Faculty \& staff of ECE Dept., JNGEC Sundernagar.}
  \end{exampleblock}
\end{column}
\end{columns}
\end{frame}

%% =========================================================================
%% SLIDE 24: CLOSING SLIDE
%% =========================================================================
\begin{frame}[plain]
  \centering
  \vspace{0.8cm}
  \includegraphics[height=1.5cm]{figures/logo.png}\\[0.4cm]
  {\fontsize{26pt}{30pt}\bfseries\color{goldcolor} THANK YOU!}\\[0.3cm]
  {\fontsize{16pt}{20pt}\bfseries\color{spaceblue} Questions \& Discussion}\\[0.4cm]
  {\fontsize{11pt}{14pt}\selectfont\color{accentblue} Delay Tolerant Networks in Space Communications}\\[0.2cm]
  {\fontsize{10pt}{13pt}\selectfont Department of Electronics \& Communication Engineering\\
  Jawaharlal Nehru Government Engineering College, Sundernagar (H.P.)}\\[0.4cm]
  \colorbox{cardbg}{\parbox{0.6\textwidth}{\centering\small
    \textbf{Vishal Chandel} \quad | \quad Roll No.: \textbf{23010104072}\\
    Email: \texttt{vishal.ece@jngec.ac.in}
  }}
\end{frame}

\end{document}
"""

with open(r"seminar_vishal\presentation.tex", "w", encoding="utf-8") as f:
    f.write(beamer_tex)

print("Wrote seminar_vishal/presentation.tex successfully!")
