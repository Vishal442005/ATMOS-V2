# write_dev_master.py
# Generates the full LaTeX source code for Dev's report.

import os

with open('generate_dev_master.py', 'r', encoding='utf-8') as f:
    header = f.read()

# Let's verify header ends at pagenumbering{arabic}
assert r"\pagenumbering{arabic}" in header

c1_text = r"""
%% ==========================================================================
%%  CHAPTER 1: INTRODUCTION TO THE INTERNSHIP
%% ==========================================================================
\chapter{Introduction to the Internship}
\label{chap:intro}

\section{Project Overview: Self-Balancing Robot Using IoT}
\justifying
The field of robotics and autonomous cyber-physical systems has experienced exponential growth over the past decade, driven by concurrent advances in micro-electro-mechanical systems (MEMS), high-performance low-power embedded microcontrollers, and ubiquitously accessible cloud networking infrastructures. Among canonical benchmark platforms in non-linear control engineering, the \textbf{Two-Wheeled Inverted Pendulum (TWIP)} stands out as one of the most intellectually compelling and practically demanding systems. 

A self-balancing robot operates on the fundamental physical principle of an inverted pendulum mounted upon a motorized mobile wheeled chassis. Unlike conventional three-wheeled or four-wheeled differential-drive ground mobile robots that possess inherent static stability, a two-wheeled inverted pendulum is \textbf{dynamically unstable, highly non-linear, non-minimum phase, and underactuated}. The physical chassis possesses only two independent actuator control inputs (the pulse-width modulated torques delivered by the left and right direct-current geared motors) while attempting to simultaneously regulate three coupled mechanical degrees of freedom: the forward/reverse linear displacement $x(t)$, the linear velocity $\dot{x}(t)$, and the critical vertical chassis tilt (pitch) angle $\theta(t)$.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.5cm,keepaspectratio]{figures/Self-Balancing Robot IoT System Overview.png}
  \caption{Comprehensive Architectural Overview of the IoT-Enabled Self-Balancing Robot System.}
  \label{fig:robot_overview}
\end{figure}

The core operational objective of the robot is to maintain upright vertical equilibrium ($\theta = 0^\circ$) by dynamically driving the wheels in the direction toward which the chassis begins to fall. If the upper chassis tips forward ($\theta > 0$), the onboard microcontroller must immediately detect this angular deviation, compute the rate of rotational divergence, and command the motors to accelerate forward with an appropriate corrective counter-torque, thereby driving the wheels beneath the falling center of gravity (CoG). Conversely, if the chassis tilts backward ($\theta < 0$), the actuation subsystem must instantly generate reverse torque. This continuous, closed-loop stabilization process precisely mimics the biomechanical neuro-muscular control observed when a human balances an upright broomstick upon the palm of their hand.

While classical self-balancing robots function entirely as closed-loop, isolated embedded nodes without external data interfaces, this internship project bridges modern control engineering with the \textbf{Internet of Things (IoT)}. By integrating the Espressif Systems \textbf{ESP32} dual-core 32-bit microcontroller with high-speed Wi-Fi networking protocols, the developed robot transcends traditional standalone operation. Live internal telemetry—comprising instantaneous pitch angle, filtered angular velocity, raw accelerometer and gyroscope vectors, PID proportional/integral/derivative terms, motor PWM control signals, battery terminal voltages, and Wi-Fi signal strength (RSSI)—is continuously formatted and streamed across wireless networks to cloud-hosted databases, notably \textbf{Google Firebase Realtime Database (RTDB)} and the \textbf{Blynk 2.0} IoT ecosystem. 

Furthermore, cloud integration establishes a low-latency bidirectional control loop. Operators can remotely observe telemetry waveforms on mobile and web dashboards, transmit real-time teleoperation steering and velocity commands (forward, reverse, turn left, turn right), and adjust critical feedback controller gains ($K_p, K_i, K_d$) on the fly over wireless channels without requiring wired serial programming cables or interrupting the real-time balancing execution.

\section{Host Organization Profile: Cloud Education Learning Pvt. Ltd.}
\justifying
The six-week industrial internship was undertaken at \textbf{Cloud Education Learning Pvt. Ltd.}, an innovative engineering training enterprise and industrial automation consultancy operating in Himachal Pradesh. The training was hosted at the dedicated \textbf{AI-B08 Industrial Technology Innovation Centre} situated in Jawalaji, Kangra (H.P.). 

Cloud Education Learning was established by senior engineering practitioners with the explicit vision of bridging academia and contemporary industrial technology requirements. While collegiate engineering curricula provide foundational theoretical mathematics, physics, and circuit theory, undergraduate students frequently lack hands-on exposure to production-grade electronic fabrication, modern surface-mount assembly, embedded RTOS multithreading, and enterprise cloud IoT telemetry backends. Cloud Education Learning fills this critical void by offering immersive, laboratory-driven, and project-based industrial internship experiences.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.90\textwidth,height=7.2cm,keepaspectratio]{figures/General_Banner.png}
  \caption{Cloud Education Learning Applied Technology Innovation Infrastructure.}
  \label{fig:cloud_banner_intro}
\end{figure}

The physical training infrastructure at the Jawalaji Centre encompasses multiple specialized engineering divisions:
\begin{enumerate}[itemsep=2pt]
  \item \textbf{Embedded Systems \& Robotics Laboratory:} Equipped with digital storage oscilloscopes (Rigol and Keysight 100 MHz DSO units), multi-channel logic analyzers, programmable DC bench power supplies with current-limiting protection, temperature-controlled soldering and hot-air SMD rework stations, and comprehensive development boards spanning 8-bit Microchip ATmega, 32-bit Espressif ESP32/ESP8266, and ARM Cortex-M microcontrollers.
  \item \textbf{IoT \& Cloud Networking Testbench:} Featuring high-speed dual-band Wi-Fi 6 wireless gateways, local MQTT broker servers (Mosquitto running on dedicated Linux gateways), hardware packet sniffers, and multi-protocol transducer interface rigs.
  \item \textbf{Mechanical Fabrication \& Rapid Prototyping Workshop:} Housing desktop fused deposition modeling (FDM) 3D printers, laser-cutting acrylic workbenches, precision drill presses, and mechanical fastener inventories essential for rapid robot chassis assembly and iteration.
\end{enumerate}

Under this rigorous corporate infrastructure, internship trainees are assigned applied engineering problems that mirror authentic industrial product development lifecycles. Rather than working with theoretical textbook simulations or pre-assembled toy kits, trainees are mandated to evaluate component datasheets, design schematic interconnects, breadboard prototype subcircuits, measure electrical noise and voltage ripple, write structured modular firmware in C/C++, tune closed-loop feedback algorithms on physical hardware, and document engineering findings in formal technical reports.

\section{Objectives of the Internship}
\justifying
The primary academic, theoretical, and practical engineering objectives established for this six-week industrial internship were formulated as follows:

\begin{enumerate}[itemsep=3pt]
  \item \textbf{Mastery of Embedded Microcontroller Architectures:} Gain deep practical competence in programming 8-bit RISC microcontrollers (Microchip ATmega328P) and 32-bit dual-core Harvard-architecture microcontrollers (Espressif ESP32-WROOM-32), understanding register-level peripheral configuration, hardware timers, analog-to-digital conversion (ADC), and serial communications ($I^2C$, SPI, UART).
  \item \textbf{Mathematical Modeling of Underactuated Dynamic Systems:} Derive the analytical equations of motion governing the two-wheeled inverted pendulum using classical Lagrangian mechanics, linearize the resulting coupled differential equations about the vertical equilibrium, and synthesize continuous and discrete state-space representations.
  \item \textbf{Inertial Sensor Calibration \& Dynamic Sensor Fusion:} Interface the InvenSense MPU-6050 6-DOF MEMS inertial measurement unit over the $I^2C$ bus at 400 kHz, model accelerometer high-frequency noise and gyroscope low-frequency DC bias drift, and design discrete sensor fusion filters (Complementary Filtering and Extended Kalman Filtering) to extract a clean, lag-free tilt angle estimate $\theta(t)$.
  \item \textbf{Actuation Subsystem Design \& Deadband Linearization:} Interface high-current L298N Dual H-Bridge motor drivers with permanent-magnet DC gear motors, analyze power dissipation and thermal limitations, characterize static friction deadbands, and formulate a firmware-level non-linear deadband linearization compensation algorithm.
  \item \textbf{Real-Time Digital PID Controller Implementation:} Formulate a parallel digital Proportional-Integral-Derivative (PID) controller in discrete time, integrate derivative low-pass filtering and integral anti-windup clamping, and systematically tune feedback gains ($K_p, K_i, K_d$) to achieve rapid disturbance rejection with minimal steady-state limit-cycling.
  \item \textbf{Cloud IoT Integration and Bidirectional Telemetry Streaming:} Develop an asynchronous, non-blocking firmware pipeline leveraging FreeRTOS multitasking to stream real-time telemetry to Google Firebase Realtime Database and the Blynk 2.0 cloud platform over Wi-Fi, enabling live dashboard monitoring and wireless parameter tuning.
  \item \textbf{Hardware-in-the-Loop Validation \& Terrain Benchmarking:} Fabricate a multi-tier acrylic and aluminum robot chassis, optimize the physical center-of-gravity (CoG), and experimentally benchmark balancing stability, disturbance recovery, and power consumption across varying floor terrains.
\end{enumerate}

\section{Scope of the Internship}
\justifying
The scope of the internship encompasses the entire end-to-end engineering development workflow required to transform an abstract non-linear control problem into a fully functional, cloud-connected autonomous robot prototype. Figure~\ref{fig:scope_infographic} illustrates the circular, multi-disciplinary engineering scope embraced during the training tenure.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.5cm,keepaspectratio]{figures/Internship Scope Circular Infographic.png}
  \caption{Multi-Disciplinary Engineering Scope of the Industrial Internship Program.}
  \label{fig:scope_infographic}
\end{figure}

The project integrates five distinct yet tightly coupled technical domains:
\begin{itemize}[itemsep=2pt]
  \item \textbf{Mechanical \& Structural Design:} Designing a rigid, multi-deck chassis that houses heavy battery packs, electronic control boards, sensors, and actuators while positioning the center of gravity at an optimal vertical elevation to facilitate controllability.
  \item \textbf{Power Electronics \& Thermal Engineering:} Designing a dual-rail power distribution network that isolates high-current inductive motor transient spikes from sensitive 3.3V digital microcontroller and sensor logic, utilizing low-dropout regulators and decoupling capacitors.
  \item \textbf{Embedded Firmware \& RTOS Engineering:} Writing clean, modular C++ firmware adhering to real-time execution constraints, utilizing FreeRTOS tasks to segregate high-priority 200 Hz deterministic control routines from low-priority, variable-latency wireless networking tasks.
  \item \textbf{Control Systems Theory:} Applying analytical dynamic modeling, transfer function derivation, frequency-domain Bode analysis, state-space formulations, and discrete-time digital filter implementations.
  \item \textbf{Cloud Computing \& Telecommunication Networking:} Establishing reliable IEEE 802.11 b/g/n Wi-Fi connections, handling JSON serialization/deserialization, interfacing RESTful APIs via HTTPS/Server-Sent Events (SSE), and configuring WebSockets for bidirectional low-latency data transmission.
\end{itemize}

\section{Importance of Industrial Training in Engineering Education}
\justifying
Industrial training forms an indispensable cornerstone of the Bachelor of Technology (B.Tech.) degree program in Electronics \& Communication Engineering at Jawaharlal Nehru Government Engineering College (JNGEC), Sundernagar, affiliated to Himachal Pradesh Technical University (HPTU), Hamirpur. While classroom pedagogy provides essential foundations in circuit analysis, semiconductor physics, signal processing, and control theory, theoretical education alone cannot convey the nuanced, multifaceted engineering trade-offs encountered when developing physical hardware.

In practical engineering systems, theoretical assumptions frequently break down:
\begin{itemize}[itemsep=2pt]
  \item Actuators are not perfectly linear torque sources; they exhibit friction, deadband non-linearities, magnetic saturation, back-EMF, and thermal heating.
  \item Transducers do not yield pure mathematical state variables; MEMS accelerometers suffer severe high-frequency vibrational contamination from motor gearboxes, while MEMS gyroscopes exhibit time-varying thermal DC bias drift.
  \item Digital controllers do not execute in infinitesimal continuous time; they are bound by finite ADC sampling rates, quantization errors, bus propagation latencies ($I^2C$ clock stretching), and finite processor clock cycles.
  \item Power supplies are not ideal voltage sources; high-current motor direction reversals generate inductive ground-bounce and voltage dips capable of triggering brownout resets in microcontrollers unless proper star-grounding and decoupling are enforced.
\end{itemize}

Through direct, hands-on immersion in an industrial laboratory setting at Cloud Education Learning Pvt. Ltd., the trainee develops the disciplined empirical mindset required of a professional electronics engineer: diagnosing circuit anomalies using oscilloscopes, validating sensor outputs, optimizing firmware memory footprints, and iteratively refining physical prototypes until robust, repeatable operation is achieved.

%% ==========================================================================
%%  CHAPTER 2: WEEKLY PROGRESS REPORT
%% ==========================================================================
\chapter{Weekly Progress Report}
\label{chap:weekly}

\section{Overview of the Six-Week Industrial Training Tenure}
\justifying
The six-week industrial internship was executed systematically over a 40-day intensive training schedule, spanning from \textbf{20 June 2026} to \textbf{03 August 2026}. To ensure structured learning and methodical milestone progression, the training tenure was divided into six sequential, goal-oriented technical phases:
\begin{itemize}[itemsep=2pt]
  \item \textbf{Week 1 (Days 1--7):} Embedded Systems Architecture, Microcontroller Fundamentals, and Arduino Uno Breadboard Prototyping.
  \item \textbf{Week 2 (Days 8--14):} Transducer Interfacing, Analog/Digital Conversion, $I^2C$/SPI Bus Communication Protocols, and Tinkercad Circuit Simulation.
  \item \textbf{Week 3 (Days 15--21):} Actuation Subsystems, DC Motor Dynamics, H-Bridge Drivers, PWM Speed Control, and Deadband Characterization.
  \item \textbf{Week 4 (Days 22--28):} ESP32 32-Bit Dual-Core Architecture, FreeRTOS Multithreading, and InvenSense MPU-6050 6-DOF IMU Sensor Integration.
  \item \textbf{Week 5 (Days 29--35):} Dynamic Sensor Fusion Filtering (Complementary \& EKF Algorithms) and Real-Time Discrete Digital PID Controller Tuning.
  \item \textbf{Week 6 (Days 36--40):} Cloud IoT Telemetry Integration (Google Firebase \& Blynk 2.0), Full System Assembly, Field Testing, and Final Evaluation.
\end{itemize}

The exhaustive day-by-day technical log of engineering activities, laboratory experiments, debugging challenges, and milestone accomplishments is detailed below.

\section{Week 1: Embedded Architecture, Microcontrollers, and Prototyping}
\justifying
\textbf{Duration: 20 June 2026 to 26 June 2026 (Days 1 to 7)}

\begin{itemize}[itemsep=2pt]
  \item \textbf{Day 1 (20 June 2026):} Induction into the Cloud Education Learning AI-B08 Centre. Corporate orientation, safety protocols in electronics laboratories, overview of high-speed testbenches, and distribution of individual engineering prototyping toolkits.
  \item \textbf{Day 2 (21 June 2026):} Comprehensive architectural study of 8-bit Harvard RISC microcontrollers, specifically the Microchip ATmega328P. Analyzed internal registers, flash memory (32 KB), SRAM (2 KB), EEPROM (1 KB), clock prescalers, and reset circuitry.
  \item \textbf{Day 3 (22 June 2026):} Setup and configuration of the Arduino IDE 2.3.10 development toolchain on 64-bit Linux and Windows workstations. Configured board manager packages, AVR-GCC compiler toolchains, and verified CH340/FT232 USB-to-UART bridge driver communication.
  \item \textbf{Day 4 (23 June 2026):} Breadboard circuit assembly of basic digital input/output (GPIO) test rigs. Implemented direct port manipulation versus high-level HAL functions (\texttt{digitalWrite} vs. direct register writing to \texttt{PORTB}/\texttt{DDRB}) and measured execution speeds on a 100 MHz digital storage oscilloscope.
  \item \textbf{Day 5 (24 June 2026):} Hardware interrupt programming. Interfaced push-buttons with internal pull-up resistors to external interrupt pins (INT0, INT1). Implemented hardware and software switch debounce routines using discrete RC low-pass networks and timer-based millisecond lockout filters.
  \item \textbf{Day 6 (25 June 2026):} Analog-to-Digital Conversion (ADC) deep dive. Configured the internal 10-bit successive approximation register (SAR) ADC on the ATmega328P. Interfaced linear precision potentiometers and light-dependent resistors (LDRs), evaluating quantization step size ($\Delta V = 5.0\text{V} / 1024 \approx 4.88\text{ mV}$) and ADC reference voltages ($V_{ref}$ = 5V vs. 1.1V internal bandgap).
  \item \textbf{Day 7 (26 June 2026):} Pulse Width Modulation (PWM) theory and implementation. Configured Timer0, Timer1, and Timer2 in Fast PWM and Phase-Correct PWM modes. Analyzed duty cycle variation ($D = t_{on}/T$) and observed high-frequency square wave generation on the oscilloscope across varying prescaler settings. Weekly progress review submitted to industrial supervisor.
\end{itemize}

\section{Week 2: Transducer Interfacing, Serial Buses, and Simulation}
\justifying
\textbf{Duration: 27 June 2026 to 03 July 2026 (Days 8 to 14)}

\begin{itemize}[itemsep=2pt]
  \item \textbf{Day 8 (27 June 2026):} Serial communication protocols overview: Universal Asynchronous Receiver-Transmitter (UART). Explored baud rate generation, framing bits (start bit, data bits, parity, stop bit), framing errors, and UART buffer overrun conditions at 9600 vs. 115200 baud.
  \item \textbf{Day 9 (28 June 2026):} Inter-Integrated Circuit ($I^2C$) bus architecture. Analyzed two-wire synchronous communication (SDA, SCL), open-drain output stages, pull-up resistor calculation ($R_p \approx 2.2\text{ k}\Omega - 4.7\text{ k}\Omega$ based on bus capacitance), 7-bit device addressing, and ACK/NACK signaling protocols.
  \item \textbf{Day 10 (29 June 2026):} Interfaced peripheral environmental sensors over $I^2C$, including the Dallas DS1307 Real-Time Clock (RTC) and an alphanumeric 16x2 Liquid Crystal Display (LCD) equipped with the PCF8574 $I^2C$ expander backpack. Executed an $I^2C$ address scanner script to detect bus devices.
  \item \textbf{Day 11 (30 June 2026):} Interfaced analog and digital environmental sensors: LM35 precision Celsius temperature sensor, DHT11 digital humidity/temperature sensor (single-wire proprietary protocol), and MQ-2 flammable gas/smoke sensor. Analyzed sensitivity curves, calibration equations, and preheating requirements.
  \item \textbf{Day 12 (01 July 2026):} Circuit modeling and verification using the \textbf{Autodesk Tinkercad} cloud simulation platform. Constructed virtual circuit schematics coupling microcontrollers, sensors, and visual indicators to evaluate operational logic before physical breadboarding (Figure~\ref{fig:tinkercad_sim}).
  \item \textbf{Day 13 (02 July 2026):} Ultrasonic distance transducer interfacing: HC-SR04 sensor. Programmed precision $10\,\mu\text{s}$ trigger pulses, captured echo pulse widths via Timer1 input capture, and computed obstacle distance via acoustic time-of-flight equations ($d = v_{sound} \cdot t_{echo} / 2$, where $v_{sound} = 343\text{ m/s}$).
  \item \textbf{Day 14 (03 July 2026):} Weekly synthesis and technical milestone evaluation. Formulated modular sensor acquisition libraries in C++, verified sensor noise levels using statistical moving-average filters, and presented findings to mentor Er. Rajesh Sharma.
\end{itemize}

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.2cm,keepaspectratio]{figures/tinkercad_gas_sensor.jpg}
  \caption{Autodesk Tinkercad Circuit Simulation and Verification Environment.}
  \label{fig:tinkercad_sim}
\end{figure}

\section{Week 3: Actuation, DC Motor Dynamics, and Deadband Analysis}
\justifying
\textbf{Duration: 04 July 2026 to 10 July 2026 (Days 15 to 21)}

\begin{itemize}[itemsep=2pt]
  \item \textbf{Day 15 (04 July 2026):} Introduction to electromechanical actuation. Studied the operating principles of permanent-magnet direct-current (PMDC) brushed motors, armature back-EMF ($e_b = K_b \omega$), electromagnetic torque generation ($\tau = K_t i$), stall current, and internal armature winding resistance ($R_a$).
  \item \textbf{Day 16 (05 July 2026):} H-Bridge bidirectional switching topology. Analyzed the internal schematic of the STMicroelectronics \textbf{L298N Dual Full-Bridge Driver}. Evaluated the four bipolar junction transistor (BJT) Darlington pairs, flyback protection diode requirements, and logic truth tables for forward, reverse, dynamic braking, and free-wheeling states.
  \item \textbf{Day 17 (06 July 2026):} Breadboard assembly of the L298N motor driver connected to dual yellow TT geared DC motors (1:48 reduction ratio). Measured internal Darlington saturation voltage drop ($V_{CE,sat} \approx 1.8\text{V} - 2.2\text{V}$) under load, verifying that a 12V input rail delivers approximately 9.8V to 10.2V across motor terminals.
  \item \textbf{Day 18 (07 July 2026):} Inductive kickback and power rail decoupling. Captured severe inductive flyback spikes on the oscilloscope during motor PWM switching ($V_{spike} = -L \frac{di}{dt} > 40\text{V}$). Implemented external 1N5819 Schottky fast-recovery diodes, $100\,\mu\text{F}$ electrolytic bulk decoupling capacitors, and $0.1\,\mu\text{F}$ ceramic high-frequency bypass capacitors across motor terminals.
  \item \textbf{Day 19 (08 July 2026):} Wireless serial communication interfacing: HC-05 Bluetooth Low Energy (BLE) / Classic RF module. Established bidirectional UART telemetry at 9600 baud, configured AT commands, paired the module with an Android smartphone, and constructed a mobile Bluetooth teleoperation interface.
  \item \textbf{Day 20 (09 July 2026):} Empirical motor deadband characterization. Applied incremental PWM duty cycles (from 0 to 255) to the geared DC motors under physical load. Discovered that static friction in the spur gearbox prevents motor rotation for PWM duty cycles below 65 ($D < 25.5\%$). Formulated an analytical deadband linearization algorithm in firmware.
  \item \textbf{Day 21 (10 July 2026):} Fabricated a mobile two-wheeled chassis testbench, verified differential steering mechanics (forward, reverse, pivot left, pivot right), and submitted the Week 3 laboratory progress report.
\end{itemize}

\section{Week 4: ESP32 Dual-Core Architecture and MPU-6050 IMU}
\justifying
\textbf{Duration: 11 July 2026 to 17 July 2026 (Days 22 to 28)}

\begin{itemize}[itemsep=2pt]
  \item \textbf{Day 22 (11 July 2026):} Architectural transition from 8-bit ATmega328P to the 32-bit \textbf{ESP32-WROOM-32} microcontroller. Analyzed the dual-core Tensilica Xtensa LX6 microprocessor operating at 240 MHz, 520 KB internal SRAM, 4 MB external SPI flash, integrated 2.4 GHz Wi-Fi (802.11 b/g/n) and Bluetooth v4.2 BR/EDR and BLE.
  \item \textbf{Day 23 (12 July 2026):} FreeRTOS symmetric multiprocessing (SMP) operating system fundamentals. Studied task creation (\texttt{xTaskCreatePinnedToCore}), task priority scheduling, hardware timer alarms, tick rates (1000 Hz / 1 ms tick), and inter-core memory synchronization.
  \item \textbf{Day 24 (13 July 2026):} Deep study of the \textbf{InvenSense MPU-6050} 6-DOF MEMS motion tracking sensor. Explored internal capacitive micro-machined accelerometer proof-mass mechanics, vibrating ring gyroscopic Coriolis effect sensing, 16-bit analog-to-digital converters, and programmable full-scale measurement ranges ($\pm 2\text{g}$ to $\pm 16\text{g}$ for acceleration, $\pm 250^\circ/\text{s}$ to $\pm 2000^\circ/\text{s}$ for angular velocity).
  \item \textbf{Day 25 (14 July 2026):} $I^2C$ register-level configuration of the MPU-6050. Wrote bare-metal register configuration routines: woke the sensor from low-power sleep via \texttt{PWR\_MGMT\_1} (register \texttt{0x6B}), set the sample rate divider via \texttt{SMPLRT\_DIV} (register \texttt{0x19}) to achieve a 200 Hz internal sampling rate, and configured the digital low-pass filter (DLPF) via \texttt{CONFIG} (register \texttt{0x1A}) to a 42 Hz cutoff.
  \item \textbf{Day 26 (15 July 2026):} Automated sensor offset calibration routine. Developed a stationary calibration algorithm executed at system boot: sampled 2,000 consecutive readings of raw accelerometer and gyroscope registers over 10 seconds, computed arithmetic means, and stored DC bias offsets ($a_{x,off}, a_{y,off}, a_{z,off}, \omega_{x,off}, \omega_{y,off}, \omega_{z,off}$) in memory for live runtime subtraction.
  \item \textbf{Day 27 (16 July 2026):} High-speed $I^2C$ bus optimization. Elevated the ESP32 hardware $I^2C$ master clock from standard 100 kHz to 400 kHz Fast Mode. Verified signal integrity and rise/fall times on the digital oscilloscope, confirming clean square-wave transitions without bus ringing.
  \item \textbf{Day 28 (17 July 2026):} Interfaced the ESP32 hardware PWM engine (LEDC peripheral). Configured 16 independent PWM channels, 8-bit resolution (0--255 levels), and a 20 kHz carrier frequency to eliminate audible motor switching acoustic whine. Week 4 technical review completed.
\end{itemize}

\section{Week 5: Sensor Fusion Filtering and Discrete PID Control Tuning}
\justifying
\textbf{Duration: 18 July 2026 to 24 July 2026 (Days 29 to 35)}

\begin{itemize}[itemsep=2pt]
  \item \textbf{Day 29 (18 July 2026):} Trigonometric pitch angle derivation from raw tri-axial accelerometer registers ($A_x, A_y, A_z$). Formulated the arctangent relation $\theta_{acc} = \text{atan2}(A_x, \sqrt{A_y^2 + A_z^2}) \cdot \frac{180}{\pi}$. Observed severe susceptibility to high-frequency chassis vibrations and centrifugal linear accelerations.
  \item \textbf{Day 30 (19 July 2026):} Gyroscopic angular velocity numerical integration: $\theta_{gyro}(t) = \int \omega_y(t) dt$. Implemented discrete Euler forward integration $\theta_{gyro, k} = \theta_{gyro, k-1} + \omega_{y, k} \Delta t$. Observed zero susceptibility to vibration but experienced progressive low-frequency integration drift due to uncompensated DC bias.
  \item \textbf{Day 31 (20 July 2026):} Design and implementation of the \textbf{Discrete Complementary Filter}. Formulated the frequency-domain filter equations combining a high-pass filtered gyroscope rate with a low-pass filtered accelerometer tilt angle: $\theta_k = \alpha (\theta_{k-1} + \omega_{y, k} \Delta t) + (1 - \alpha) \theta_{acc, k}$. Tuned the weighting coefficient $\alpha = 0.98$ for a sampling period $\Delta t = 5\text{ ms}$ (200 Hz), achieving a time constant $\tau \approx 0.245\text{ s}$.
  \item \textbf{Day 32 (21 July 2026):} Mathematical formulation of the \textbf{Discrete Extended Kalman Filter (EKF)}. Structured the 3-state state-space model $[\theta, \dot{\theta}, b_g]^T$, derived the Taylor-series Jacobian state transition matrix $\mathbf{F}$ and measurement matrix $\mathbf{H}$, and programmed the alternating prediction-correction recursion. Benchmarked estimation accuracy against the complementary filter.
  \item \textbf{Day 33 (22 July 2026):} Digital PID controller formulation in discrete time. Coded the parallel PID structure incorporating proportional gain ($K_p$), integral gain ($K_i$) with trapezoidal integration and conditional anti-windup clamping, and derivative gain ($K_d$) applied to filtered angular rate to avoid derivative kick upon setpoint transitions.
  \item \textbf{Day 34 (23 July 2026):} Empirical closed-loop PID tuning on the physical robot chassis. Began with $K_i = 0, K_d = 0$, incrementally elevated $K_p$ until sustained, steady-state oscillations (ultimate gain $K_u = 48.0$) were observed. Introduced derivative gain $K_d = 1.2$ to dampen oscillations, followed by modest integral gain $K_i = 140.0$ to eliminate steady-state tilt droop.
  \item \textbf{Day 35 (24 July 2026):} Mechanical balancing stabilization achieved! The physical robot maintained stable vertical equilibrium autonomously for continuous periods exceeding 15 minutes. Conducted dynamic disturbance rejection tests by applying physical impulse taps. Week 5 milestone presented to lead mentor.
\end{itemize}

\section{Week 6: Cloud IoT Telemetry, Full Assembly, and Final Sign-Off}
\justifying
\textbf{Duration: 25 July 2026 to 03 August 2026 (Days 36 to 40)}

\begin{itemize}[itemsep=2pt]
  \item \textbf{Day 36 (25 July 2026):} Cloud IoT integration: \textbf{Google Firebase Realtime Database (RTDB)}. Configured Firebase project credentials, established authenticated HTTPS streaming using the official Firebase-ESP-Client library, designed the JSON database schema (\texttt{/telemetry/pitch}, \texttt{/telemetry/pwm}, \texttt{/telemetry/battery}), and verified sub-120 ms cloud ingestion over Wi-Fi.
  \item \textbf{Day 37 (26 July 2026):} Mobile IoT integration: \textbf{Blynk 2.0 IoT Platform}. Configured device templates, virtual datastreams (V0 for live pitch gauge, V1 for motor PWM gauge, V2 for battery voltage, V3 for remote joystick steering), and established bidirectional WebSockets communication running on FreeRTOS Core 0.
  \item \textbf{Day 38 (27 July 2026):} Dynamic wireless parameter tuning. Implemented cloud listening routines that subscribe to Firebase database updates for PID coefficients ($K_p, K_i, K_d$). Verified that tuning sliders on the web dashboard immediately update the active control loop on FreeRTOS Core 1 without resetting the microcontroller.
  \item \textbf{Day 39 (28 July 2026):} Full system packaging and cable management. Fabricated the three-tier chassis, mounted the 3S 18650 Li-ion battery pack on the lower base to optimize center-of-gravity, secured all wiring harnesses, mounted the power isolation switch and LM2596 buck regulator, and completed physical assembly.
  \item \textbf{Day 40 (03 August 2026):} Comprehensive field evaluation across multiple surface materials (polished marble, laboratory carpet, concrete, wood). Measured settling times, disturbance rejection angles, battery discharge profiles, and telemetry latency distributions. Successfully presented the working prototype to the department panel and received final internship sign-off.
\end{itemize}

\vspace{0.4cm}
\begin{table}[H]
\centering
\small
\caption{Comprehensive Summary of Weekly Training Progression and Milestones}
\label{tab:weekly_summary}
\begin{tabular}{|c|p{4.0cm}|p{6.8cm}|c|}
\hline
\textbf{Week} & \textbf{Core Technical Focus} & \textbf{Key Laboratory Deliverables and Milestones} & \textbf{Status} \\
\hline
1 & Embedded Architectures \& AVR Prototyping & ATmega328P register programming, GPIO manipulation, ADC quantization, hardware PWM timers. & Completed \\
\hline
2 & Transducers, Serial Buses \& Simulation & $I^2C$ bus at 100/400 kHz, UART 115200 baud, ultrasonic time-of-flight, Autodesk Tinkercad simulations. & Completed \\
\hline
3 & Actuation \& Motor Deadband Dynamics & L298N Dual H-Bridge power stage, inductive flyback snubbers, TT motor deadband linearization, BLE interface. & Completed \\
\hline
4 & ESP32 Dual-Core \& MPU-6050 6-DOF IMU & FreeRTOS task pinning, MPU-6050 register configuration, automated boot calibration, 20 kHz LEDC PWM. & Completed \\
\hline
5 & Sensor Fusion \& Closed-Loop PID Tuning & Complementary filter ($\alpha=0.98$), Discrete Extended Kalman Filter, parallel PID tuning, autonomous balance achieved. & Completed \\
\hline
6 & Cloud IoT Integration \& Field Verification & Google Firebase RTDB, Blynk 2.0 WebSockets, 3-tier chassis packaging, terrain testing, evaluation sign-off. & Completed \\
\hline
\end{tabular}
\end{table}

\vspace{0.3cm}
\noindent
\begin{minipage}{0.48\textwidth}
  \begin{flushleft}
    \textbf{Trainee Signature:}\\[0.4cm]
    \textbf{\StudentName}\\
    University Roll No.: \textbf{\RollNo}
  \end{flushleft}
\end{minipage}
\hfill
\begin{minipage}{0.48\textwidth}
  \begin{flushright}
    \textbf{Supervisor Verification:}\\[0.4cm]
    \textbf{Er. Rajesh Sharma}\\
    Senior Project Manager, CEL Pvt. Ltd.
  \end{flushright}
\end{minipage}

"""
print("Chapters 1 & 2 defined, len =", len(c1_text))
c3_text = r"""
%% ==========================================================================
%%  CHAPTER 3: TECHNICAL CONTENT AND SYSTEM DESIGN
%% ==========================================================================
\chapter{Technical Content and System Design}
\label{chap:technical}

\section{Microcontroller Architecture: ATmega328P vs. ESP32-WROOM-32}
\justifying
The selection of an appropriate microcontroller unit (MCU) represents the single most critical architectural decision in designing a cyber-physical balance robot. The controller must simultaneously satisfy two fundamentally competing engineering constraints:
\begin{enumerate}[itemsep=2pt]
  \item \textbf{Deterministic Low-Latency Control Execution:} To stabilize an inverted pendulum possessing an open-loop unstable pole above $6\,\text{rad/s}$, the sensor acquisition, digital filtering, and PID calculation routines must execute with sub-millisecond determinism at a fixed sampling frequency of at least $100\,\text{Hz}$ to $200\,\text{Hz}$ ($T_s = 5000\,\mu\text{s}$). Any jitter or timing interruption can induce catastrophic phase lag, destabilizing the mechanical balance.
  \item \textbf{High-Throughput Asynchronous Wireless Networking:} Handling TCP/IP network handshakes, Wi-Fi radio baseband processing, TLS/SSL cryptographic encryption, JSON packet serialization, and HTTP/WebSocket cloud communication requires substantial compute power and memory buffers. Wireless transactions exhibit variable, non-deterministic latencies spanning from tens of milliseconds to hundreds of milliseconds.
\end{enumerate}

During the initial prototyping phase (Weeks 1 and 2), the project evaluated the legacy \textbf{Microchip ATmega328P} 8-bit AVR microcontroller (Figure~\ref{fig:arduino_uno}). Operating at a clock frequency of $16\,\text{MHz}$ with a single execution thread, the ATmega328P possesses $32\,\text{KB}$ of flash memory and merely $2\,\text{KB}$ of SRAM. While perfectly adequate for basic sensor reading and local motor driving, the ATmega328P completely lacks native wireless networking silicon. Interfacing an external Wi-Fi coprocessor (such as an ESP8266 AT-command module) over a slow $9600\,\text{baud}$ software serial bus introduced blocking delays exceeding $80\,\text{ms}$, which repeatedly starved the balancing control loop and caused the physical robot to fall.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.85\textwidth,height=7.2cm,keepaspectratio]{figures/Annotated Arduino Uno Components Diagram.png}
  \caption{Annotated Architectural Diagram of the 8-Bit Microchip ATmega328P Development Platform.}
  \label{fig:arduino_uno}
\end{figure}

To definitively resolve this architectural bottleneck, the project transitioned in Week 4 to the \textbf{Espressif Systems ESP32-WROOM-32} module (Figure~\ref{fig:esp32_pinout}). The ESP32 integrates a high-performance Tensilica Xtensa dual-core 32-bit LX6 microprocessor operating at $240\,\text{MHz}$, capable of delivering up to $600\,\text{MIPS}$ of computational throughput. Crucially, the dual-core architecture allows symmetric multiprocessing (SMP) under the \textbf{FreeRTOS} real-time operating system kernel.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.4cm,keepaspectratio]{figures/ESP32-Pin-Configuration.png}
  \caption{Espressif Systems ESP32 38-Pin Module Hardware Pinout and Peripheral Mapping.}
  \label{fig:esp32_pinout}
\end{figure}

Table~\ref{tab:mcu_comparison} provides an exhaustive side-by-side technical comparison between the Microchip ATmega328P and the Espressif Systems ESP32-WROOM-32, highlighting the decisive architectural parameters that motivated the migration to 32-bit dual-core hardware.

\renewcommand{\arraystretch}{1.2}
\begin{table}[!ht]
\centering
\small
\caption{Comprehensive Architectural Comparison: Microchip ATmega328P vs. Espressif ESP32}
\label{tab:mcu_comparison}
\begin{tabular}{|p{4.2cm}|p{5.0cm}|p{5.4cm}|}
\hline
\textbf{Architectural Parameter} & \textbf{Microchip ATmega328P} & \textbf{Espressif Systems ESP32} \\
\hline
CPU Architecture & 8-bit Harvard RISC & 32-bit Dual-Core Tensilica Xtensa LX6 \\
Processor Clock Speed & 16 MHz (Single Core) & 240 MHz (Dual Cores: Core 0 \& Core 1) \\
Computational Throughput & $\approx 16$ MIPS & Up to 600 MIPS (Dual Harvard Engines) \\
Floating-Point Unit (FPU) & None (Emulated in Software) & Hardware Single-Precision IEEE 754 FPU \\
Internal SRAM Capacity & 2 KB & 520 KB High-Speed Internal SRAM \\
Non-Volatile Flash Memory & 32 KB (In-System Flash) & 4 MB (External SPI Quad-Flash) \\
EEPROM / NVS Storage & 1 KB Internal EEPROM & Non-Volatile Storage (NVS) in Flash \\
Operating Voltage Rail & 5.0 V DC Nominal & 3.3 V DC Nominal (Ultra-Low-Power LDO) \\
Integrated Wireless Silicon & None (Requires External Modules) & 2.4 GHz 802.11 b/g/n Wi-Fi + BLE 4.2 \\
Analog-to-Digital Converter & 10-bit SAR (8 Multiplexed Channels) & Two 12-bit SAR ADCs (Up to 18 Channels) \\
Hardware PWM Engine & 6 Channels (8-bit Timer Driven) & 16 Independent LEDC PWM Channels \\
$I^2C$ Master Bus Speed & Standard 100 kHz & Fast Mode 400 kHz / High-Speed 1 MHz \\
Real-Time OS Support & Severely Constrained (RAM Starved) & Native Preemptive FreeRTOS Kernel \\
Unit Production Cost & \$2.50 -- \$3.50 USD & \$3.80 -- \$4.50 USD (High Value-to-Cost) \\
\hline
\end{tabular}
\end{table}
\renewcommand{\arraystretch}{1.0}

By dedicating \textbf{Core 1} exclusively to the deterministic 200 Hz sensor acquisition, discrete filtering, and closed-loop PID control routines, and offloading all Wi-Fi radio negotiation, TCP/IP stack handling, and Firebase/Blynk cloud telemetry streaming to \textbf{Core 0}, the ESP32 eliminates resource contention entirely. This guarantees sub-microsecond control determinism alongside rich real-time IoT cloud telemetry.

\section{Mathematical Modeling of the Two-Wheeled Inverted Pendulum (TWIP)}
\justifying
To design a robust, high-performance closed-loop stabilization controller, an accurate analytical mathematical model of the physical two-wheeled inverted pendulum (TWIP) is indispensable. The system can be idealized as a rigid inverted chassis body of mass $M$, moment of inertia $J_\theta$, and height $2l$, supported by a wheeled axle of radius $r$, wheel mass $m$, and rotational inertia $J_w$.

\subsection{Coordinate Definitions and System Kinematics}
\justifying
Let the generalized coordinates of the two-wheeled robot in the vertical sagittal plane be defined as:
\begin{equation}
    \mathbf{q} = \begin{bmatrix} x \\ \theta \end{bmatrix}
\end{equation}
where:
\begin{itemize}[itemsep=1pt]
    \item $x(t)$: Linear horizontal displacement of the wheeled axle along the ground reference plane ($m$).
    \item $\theta(t)$: Angular pitch tilt of the robot body relative to the vertical plumb line ($\text{rad}$), where $\theta = 0$ represents the upright, unstable equilibrium posture.
\end{itemize}

Assuming ideal rolling without slipping between the rubber wheels and the ground surface, the angular rotation of the wheels $\phi$ is directly coupled to linear displacement $x$ by:
\begin{equation}
    x = r \cdot \phi \quad \implies \quad \dot{x} = r \cdot \dot{\phi}
\end{equation}

The Cartesian coordinates of the robot chassis center of gravity $(x_c, y_c)$ in the inertial reference frame are expressed trigonometrically as:
\begin{equation}
    x_c = x + l \sin\theta
\end{equation}
\begin{equation}
    y_c = l \cos\theta
\end{equation}

Differentiating with respect to continuous time yields the linear velocities of the center of gravity:
\begin{equation}
    \dot{x}_c = \dot{x} + l \dot{\theta} \cos\theta
\end{equation}
\begin{equation}
    \dot{y}_c = -l \dot{\theta} \sin\theta
\end{equation}

The squared translational velocity of the chassis center of mass is thus:
\begin{equation}
    v_c^2 = \dot{x}_c^2 + \dot{y}_c^2 = (\dot{x} + l \dot{\theta} \cos\theta)^2 + (-l \dot{\theta} \sin\theta)^2 = \dot{x}^2 + 2 l \dot{x} \dot{\theta} \cos\theta + l^2 \dot{\theta}^2
\end{equation}

\subsection{Lagrangian Energy Formulation}
\justifying
The total kinetic energy $T$ of the electromechanical robotic system is the algebraic sum of the translational and rotational kinetic energies of the two wheels plus the translational and rotational kinetic energy of the inverted chassis:
\begin{equation}
    T = T_{wheels} + T_{body}
\end{equation}
\begin{equation}
    T = \left( 2 \cdot \frac{1}{2} m \dot{x}^2 + 2 \cdot \frac{1}{2} J_w \dot{\phi}^2 \right) + \left( \frac{1}{2} M v_c^2 + \frac{1}{2} J_\theta \dot{\theta}^2 \right)
\end{equation}
Substituting $\dot{\phi} = \frac{\dot{x}}{r}$ and the expression for $v_c^2$:
\begin{equation}
    T = \frac{1}{2} \left( 2m + \frac{2J_w}{r^2} + M \right) \dot{x}^2 + M l \dot{x} \dot{\theta} \cos\theta + \frac{1}{2} (J_\theta + M l^2) \dot{\theta}^2
\end{equation}

To simplify notation, we define the lumped mass parameters:
\begin{equation}
    M_t = M + 2m + \frac{2J_w}{r^2} \quad \text{(Total Effective Inertial Mass)}
\end{equation}
\begin{equation}
    J_t = J_\theta + M l^2 \quad \text{(Total Rotational Inertia about Wheel Axle)}
\end{equation}
Thus, the total kinetic energy simplifies to:
\begin{equation}
    T = \frac{1}{2} M_t \dot{x}^2 + M l \dot{x} \dot{\theta} \cos\theta + \frac{1}{2} J_t \dot{\theta}^2
\end{equation}

Choosing the wheel axle centerline ($y = 0$) as the datum zero reference plane for gravitational potential energy, the potential energy $V$ of the inverted chassis depends strictly upon its pitch elevation:
\begin{equation}
    V = M g y_c = M g l \cos\theta
\end{equation}
where $g = 9.81\,\text{m/s}^2$ denotes gravitational acceleration.

The system Lagrangian function $\mathcal{L} = T - V$ is formulated as:
\begin{equation}
    \mathcal{L}(x, \theta, \dot{x}, \dot{\theta}) = \frac{1}{2} M_t \dot{x}^2 + M l \dot{x} \dot{\theta} \cos\theta + \frac{1}{2} J_t \dot{\theta}^2 - M g l \cos\theta
\end{equation}

\subsection{Euler-Lagrange Non-Linear Dynamic Equations}
\justifying
The continuous-time equations of motion are derived from Euler-Lagrange's principle with non-conservative generalized forces $\mathbf{Q}$:
\begin{equation}
    \frac{d}{dt}\left( \frac{\partial \mathcal{L}}{\partial \dot{q}_i} \right) - \frac{\partial \mathcal{L}}{\partial q_i} = Q_i
\end{equation}
where the generalized external forces correspond to the net linear driving force $F$ applied at the ground contact and the net motor reaction torque $\tau_m$ exerted between the wheels and the chassis:
\begin{equation}
    Q_x = F = \frac{2\tau_m}{r}, \quad Q_\theta = -\tau_m
\end{equation}

\textbf{1. Equation for Linear Displacement $x(t)$:}
\begin{equation}
    \frac{\partial \mathcal{L}}{\partial \dot{x}} = M_t \dot{x} + M l \dot{\theta} \cos\theta
\end{equation}
\begin{equation}
    \frac{d}{dt}\left( \frac{\partial \mathcal{L}}{\partial \dot{x}} \right) = M_t \ddot{x} + M l \ddot{\theta} \cos\theta - M l \dot{\theta}^2 \sin\theta
\end{equation}
Since $\frac{\partial \mathcal{L}}{\partial x} = 0$, the first governing equation is:
\begin{equation}
    M_t \ddot{x} + M l \ddot{\theta} \cos\theta - M l \dot{\theta}^2 \sin\theta = \frac{2\tau_m}{r}
    \label{eq:motion_x}
\end{equation}

\textbf{2. Equation for Angular Pitch $\theta(t)$:}
\begin{equation}
    \frac{\partial \mathcal{L}}{\partial \dot{\theta}} = M l \dot{x} \cos\theta + J_t \dot{\theta}
\end{equation}
\begin{equation}
    \frac{d}{dt}\left( \frac{\partial \mathcal{L}}{\partial \dot{\theta}} \right) = M l \ddot{x} \cos\theta - M l \dot{x} \dot{\theta} \sin\theta + J_t \ddot{\theta}
\end{equation}
\begin{equation}
    \frac{\partial \mathcal{L}}{\partial \theta} = -M l \dot{x} \dot{\theta} \sin\theta + M g l \sin\theta
\end{equation}
Subtracting $\frac{\partial \mathcal{L}}{\partial \theta}$:
\begin{equation}
    J_t \ddot{\theta} + M l \ddot{x} \cos\theta - M g l \sin\theta = -\tau_m
    \label{eq:motion_theta}
\end{equation}

Equations~(\ref{eq:motion_x}) and (\ref{eq:motion_theta}) represent the exact, non-linear, coupled dynamic differential equations of the two-wheeled self-balancing robot.

\subsection{Small-Angle Linearization and State-Space Representation}
\justifying
During normal autonomous balancing operation, the tilt angle deviation is tightly regulated within a small perturbation neighborhood around the upright equilibrium point ($\theta \approx 0$). We apply first-order Taylor series approximations:
\begin{equation}
    \sin\theta \approx \theta, \quad \cos\theta \approx 1, \quad \dot{\theta}^2 \approx 0
\end{equation}

Substituting these approximations into the non-linear equations yields the linearized system:
\begin{equation}
    M_t \ddot{x} + M l \ddot{\theta} = \frac{2\tau_m}{r}
\end{equation}
\begin{equation}
    M l \ddot{x} + J_t \ddot{\theta} - M g l \theta = -\tau_m
\end{equation}

Solving this algebraic linear system simultaneously for angular acceleration $\ddot{\theta}$ and linear acceleration $\ddot{x}$ as functions of state variables and control input torque $\tau_m$:
\begin{equation}
    \ddot{\theta} = \frac{M g l M_t}{\Delta} \theta - \frac{M l \frac{2}{r} + J_t}{\Delta} \tau_m
\end{equation}
\begin{equation}
    \ddot{x} = -\frac{(M l)^2 g}{\Delta} \theta + \frac{J_t \frac{2}{r} + M l}{\Delta} \tau_m
\end{equation}
where the characteristic inertia determinant $\Delta$ is defined as:
\begin{equation}
    \Delta = M_t J_t - (M l)^2 > 0
\end{equation}

Defining the continuous state vector $\mathbf{x}(t)$ and scalar control input $u(t) = \tau_m$:
\begin{equation}
    \mathbf{x}(t) = \begin{bmatrix} x \\ \dot{x} \\ \theta \\ \dot{\theta} \end{bmatrix}, \quad u(t) = \tau_m
\end{equation}

The standard linear time-invariant (LTI) state-space representation is expressed as:
\begin{equation}
    \dot{\mathbf{x}}(t) = \mathbf{A} \mathbf{x}(t) + \mathbf{B} u(t)
\end{equation}
\begin{equation}
    \mathbf{y}(t) = \mathbf{C} \mathbf{x}(t) + \mathbf{D} u(t)
\end{equation}

where the continuous system matrices are formulated analytically as:
\begin{equation}
    \mathbf{A} = \begin{bmatrix}
        0 & 1 & 0 & 0 \\
        0 & 0 & -\frac{(Ml)^2 g}{\Delta} & 0 \\
        0 & 0 & 0 & 1 \\
        0 & 0 & \frac{M g l M_t}{\Delta} & 0
    \end{bmatrix}, \quad
    \mathbf{B} = \begin{bmatrix}
        0 \\
        \frac{J_t \frac{2}{r} + M l}{\Delta} \\
        0 \\
        -\frac{M l \frac{2}{r} + J_t}{\Delta}
    \end{bmatrix}
\end{equation}
\begin{equation}
    \mathbf{C} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}, \quad \mathbf{D} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
\end{equation}

\subsection{Transfer Function and Open-Loop Instability Analysis}
\justifying
Applying the Laplace transform to the linearized angular acceleration equation with zero initial conditions yields the open-loop transfer function from motor control torque $U(s)$ to chassis pitch angle $\Theta(s)$:
\begin{equation}
    G(s) = \frac{\Theta(s)}{U(s)} = \frac{K_{\text{plant}}}{s^2 - p_0^2}
\end{equation}
where the natural inverted pendulum frequency $p_0$ and forward plant gain $K_{\text{plant}}$ are:
\begin{equation}
    p_0 = \sqrt{\frac{M g l M_t}{\Delta}} \approx 6.26\,\text{rad/s}, \quad K_{\text{plant}} = \frac{M l \frac{2}{r} + J_t}{\Delta} \approx 38.5\,\frac{\text{rad}}{\text{N}\cdot\text{m}\cdot\text{s}^2}
\end{equation}

The open-loop plant poles are given by the roots of the characteristic denominator equation $s^2 - p_0^2 = 0$:
\begin{equation}
    s_{1, 2} = \pm p_0 = \pm 6.26\,\text{rad/s}
\end{equation}

The existence of a strictly positive real pole in the Right-Half of the $s$-plane ($s_1 = +6.26\,\text{rad/s} > 0$) mathematically proves that the uncontrolled system is \textbf{exponentially unstable}. Any infinitesimal angular perturbation from $\theta = 0$ will grow without bound according to $e^{+p_0 t}$.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.92\textwidth,height=7.5cm,keepaspectratio]{figures/bode_and_root_locus_twip.png}
  \caption{Bode Frequency Response and Pole-Zero Constellation: Open-Loop Unstable Plant vs. Closed-Loop Stabilized System.}
  \label{fig:bode_root_locus}
\end{figure}

Figure~\ref{fig:bode_root_locus} illustrates the Bode magnitude and phase response alongside the complex $s$-plane pole-zero constellation. The open-loop phase starts at $-180^\circ$, exhibiting negative gain and phase margins, which confirms intrinsic instability. Through closed-loop dynamic compensation, the unstable pole in the right-half plane is shifted into the stable left-half plane ($s \in \text{LHP}$), guaranteeing asymptotic stability.

\section{Sensor Fusion: Accelerometer, Gyroscope, and Complementary Filter}
\justifying
Accurate, zero-latency attitude estimation represents the foundational prerequisite for self-balancing control. The robot utilizes the InvenSense \textbf{MPU-6050} 6-axis MEMS inertial measurement unit, combining a 3-axis capacitive accelerometer and a 3-axis vibrating-structure gyroscopic rate sensor.

\subsection{Accelerometer Pitch Estimation and High-Frequency Noise}
\justifying
The tri-axial accelerometer measures the specific external acceleration vector $\mathbf{a} = [a_x, a_y, a_z]^T$ in the sensor body frame. Under purely quasi-static conditions, the accelerometer senses only the reaction force opposing Earth's gravitational acceleration field $\mathbf{g}$. The chassis pitch tilt angle $\theta_{acc}$ can be derived trigonometrically:
\begin{equation}
    \theta_{acc} = \text{atan2}\left( a_x, \sqrt{a_y^2 + a_z^2} \right) \cdot \frac{180^\circ}{\pi}
\end{equation}

While $\theta_{acc}$ exhibits \textbf{zero long-term DC bias drift}, it is severely corrupted by non-gravitational linear accelerations during robot movement:
\begin{equation}
    \mathbf{a}_{\text{measured}} = \mathbf{g}_{\text{gravity}} + \mathbf{a}_{\text{linear}} + \mathbf{a}_{\text{vibration}}
\end{equation}
Mechanical gear meshing vibrations from the motor gearboxes, wheel slip, and surface roughness inject massive high-frequency noise spikes ($> 15\,\text{Hz}$) into $\theta_{acc}$, making it utterly unusable as a standalone feedback signal.

\subsection{Gyroscope Angular Rate Integration and Low-Frequency Drift}
\justifying
The MEMS gyroscope measures angular rotational velocity $\omega_y(t)$ about the pitch axis via the Coriolis force. The pitch angle can be computed by continuous numerical integration:
\begin{equation}
    \theta_{gyro}(t) = \int_{0}^{t} \omega_y(\tau) d\tau
\end{equation}

In discrete firmware running at fixed sampling interval $\Delta t = 5\,\text{ms}$ ($200\,\text{Hz}$):
\begin{equation}
    \theta_{gyro, k} = \theta_{gyro, k-1} + \omega_{y, k} \Delta t
\end{equation}

The gyroscope measurement is exceptionally responsive and completely immune to external linear chassis vibrations. However, all MEMS gyroscopes exhibit an intrinsic time-varying \textbf{DC zero-rate bias offset} $b_g(t)$:
\begin{equation}
    \omega_{y, \text{measured}}(t) = \omega_{\text{true}}(t) + b_g(t) + \eta(t)
\end{equation}
Even an imperceptible offset of $0.05^\circ/\text{s}$ integrates into an accumulated pitch error of $3.0^\circ$ after merely one minute, causing the calculated vertical angle to diverge monotonically and eventually tipping the robot over.

\subsection{The Discrete Complementary Filter Formulation}
\justifying
To exploit the complementary frequency characteristics of the two sensors—the long-term DC accuracy of the accelerometer and the short-term high-frequency responsiveness of the gyroscope—the project formulated a \textbf{Discrete Complementary Filter}.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.2cm,keepaspectratio]{figures/complementary_filter_comparison.png}
  \caption{Dynamic Sensor Fusion Performance: Raw Accelerometer Noise, Gyroscopic Integration Drift, and Fused Complementary Filter Estimate.}
  \label{fig:comp_filter_perf}
\end{figure}

In the continuous frequency domain, the complementary filter processes the gyroscope through a high-pass filter $H_{HP}(s)$ and the accelerometer through a low-pass filter $H_{LP}(s)$:
\begin{equation}
    H_{HP}(s) = \frac{s}{s + \omega_c}, \quad H_{LP}(s) = \frac{\omega_c}{s + \omega_c}
\end{equation}
Notice that the sum of the two transfer functions satisfies unity all-pass reconstruction:
\begin{equation}
    H_{total}(s) = H_{HP}(s) + H_{LP}(s) = \frac{s + \omega_c}{s + \omega_c} = 1
\end{equation}

Discretizing these continuous equations via backward Euler approximation yields the discrete difference equation executed in firmware every $5\,\text{ms}$:
\begin{equation}
    \theta_k = \alpha \cdot (\theta_{k-1} + \omega_{y, k} \Delta t) + (1 - \alpha) \cdot \theta_{acc, k}
\end{equation}
where weighting factor $\alpha$ is defined by the filter cutoff frequency $\omega_c$ and time constant $\tau$:
\begin{equation}
    \alpha = \frac{\tau}{\tau + \Delta t}, \quad \tau = \frac{1}{\omega_c}
\end{equation}

For our system operating at $\Delta t = 0.005\,\text{s}$ ($200\,\text{Hz}$), selecting $\alpha = 0.98$ yields a time constant of $\tau = 0.245\,\text{s}$ ($\omega_c = 4.08\,\text{rad/s} \approx 0.65\,\text{Hz}$). This cutoff frequency effectively eliminates high-frequency mechanical motor vibrations above $1\,\text{Hz}$ while continuously anchoring the angle estimate against gyroscopic drift. As shown in Figure~\ref{fig:comp_filter_perf}, the fused estimate achieves excellent tracking fidelity with near-zero phase lag.

\subsection{Discrete Extended Kalman Filter (EKF) Formulation}
\justifying
While the complementary filter provides computationally efficient sensor fusion, an optimal stochastic state estimator can be realized through the discrete Extended Kalman Filter (EKF). The EKF formulates the two-wheeled balancing robot as a discrete-time non-linear stochastic state-space model:
\begin{equation}
    \mathbf{x}_k = f(\mathbf{x}_{k-1}, u_{k-1}) + \mathbf{w}_{k-1}
\end{equation}
\begin{equation}
    \mathbf{z}_k = h(\mathbf{x}_k) + \mathbf{v}_k
\end{equation}
where state vector $\mathbf{x} = [\theta, \dot{\theta}, b_g]^T$ incorporates the true inclination angle $\theta$, angular velocity $\dot{\theta}$, and the slowly time-varying gyroscope DC bias drift $b_g$. Process noise $\mathbf{w}_k \sim \mathcal{N}(0, \mathbf{Q})$ and measurement noise $\mathbf{v}_k \sim \mathcal{N}(0, \mathbf{R})$ represent Gaussian zero-mean stochastic processes.

The discrete-time linear state transition matrix $\mathbf{F}$ is defined via Taylor series Jacobian expansion:
\begin{equation}
    \mathbf{F} = \begin{bmatrix}
        1 & \Delta t & -\Delta t \\
        0 & 1 & 0 \\
        0 & 0 & 1
    \end{bmatrix}
\end{equation}

The recursive Kalman estimation cycle executes in two alternating stages:
\begin{enumerate}[itemsep=1pt]
    \item \textbf{Time Update (Prediction Stage):}
    Propagates the state estimate $\hat{\mathbf{x}}$ and error covariance matrix $\mathbf{P}$ forward across sampling interval $\Delta t$:
    \begin{equation}
        \hat{\mathbf{x}}_{k|k-1} = \mathbf{F} \hat{\mathbf{x}}_{k-1|k-1} + \mathbf{B} u_{k-1}
    \end{equation}
    \begin{equation}
        \mathbf{P}_{k|k-1} = \mathbf{F} \mathbf{P}_{k-1|k-1} \mathbf{F}^T + \mathbf{Q}
    \end{equation}
    where $\mathbf{Q} = \text{diag}(\sigma_\theta^2, \sigma_{\dot{\theta}}^2, \sigma_{b_g}^2)$ represents the process noise covariance matrix reflecting model uncertainty.
    
    \item \textbf{Measurement Update (Correction Stage):}
    Incorporates the observation vector $\mathbf{z}_k = [\theta_{acc, k}, \omega_{y, k}]^T$ with observation matrix $\mathbf{H} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \end{bmatrix}$:
    \begin{equation}
        \tilde{\mathbf{y}}_k = \mathbf{z}_k - \mathbf{H} \hat{\mathbf{x}}_{k|k-1} \quad \text{(Innovation Residual)}
    \end{equation}
    \begin{equation}
        \mathbf{S}_k = \mathbf{H} \mathbf{P}_{k|k-1} \mathbf{H}^T + \mathbf{R} \quad \text{(Innovation Covariance)}
    \end{equation}
    \begin{equation}
        \mathbf{K}_k = \mathbf{P}_{k|k-1} \mathbf{H}^T \mathbf{S}_k^{-1} \quad \text{(Optimal Kalman Gain)}
    \end{equation}
    \begin{equation}
        \hat{\mathbf{x}}_{k|k} = \hat{\mathbf{x}}_{k|k-1} + \mathbf{K}_k \tilde{\mathbf{y}}_k \quad \text{(Updated State)}
    \end{equation}
    \begin{equation}
        \mathbf{P}_{k|k} = (\mathbf{I} - \mathbf{K}_k \mathbf{H}) \mathbf{P}_{k|k-1} \quad \text{(Updated Covariance)}
    \end{equation}
\end{enumerate}

By dynamically computing the optimal Kalman gain $\mathbf{K}_k$, the filter weights the measurements according to the current relative uncertainties. When aggressive wheel acceleration introduces severe vibrational disturbances into $\theta_{acc}$, the innovation covariance $\mathbf{S}_k$ increases, causing the Kalman gain to decrease automatically and placing higher trust in the gyroscopic rate integration.

\renewcommand{\arraystretch}{1.2}
\begin{table}[!ht]
\centering
\small
\caption{Comprehensive Comparison of Inertial Sensor Fusion Algorithms}
\label{tab:sensor_fusion}
\begin{tabular}{|p{3.2cm}|p{3.4cm}|p{3.8cm}|p{4.2cm}|}
\hline
\textbf{Attribute} & \textbf{Raw Sensor Outputs} & \textbf{Complementary Filter} & \textbf{Extended Kalman Filter (EKF)} \\
\hline
Computational Cost & Negligible ($< 10\,\mu\text{s}$) & Extremely Low ($< 35\,\mu\text{s}$) & Moderate ($\approx 180\,\mu\text{s}$ on ESP32 FPU) \\
Memory Footprint & Minimal (Scalar Buffers) & Minimal (4 State Variables) & Matrix Covariance Storage ($3 \times 3$) \\
Tuning Complexity & None (Direct Readings) & Single Parameter ($\alpha$) & Noise Covariance Tuning ($\mathbf{Q}, \mathbf{R}$) \\
Vibration Rejection & Zero (Fails in Motion) & Excellent (Attenuates $> 1\,\text{Hz}$) & Optimal (Minimum Variance) \\
Dynamic Drift Tracking & Severe (Monotonic Drift) & Very Good (Anchored to DC) & Optimal (Continuously Tracks $b_g$) \\
Phase Lag Penalty & Zero (No Filtering) & Very Low ($< 5\,\text{ms}$) & Minimum Theoretical Phase Lag \\
Implementation Code & Trivially Simple & Single Arithmetic Line & Multi-Stage Matrix Inversion Loop \\
\hline
\end{tabular}
\end{table}
\renewcommand{\arraystretch}{1.0}

\section{Actuation Subsystem: DC Motors, L298N Driver, and Deadband Linearization}
\justifying
The actuation subsystem converts digital PWM control signals calculated by the microcontroller into mechanical torque delivered to the road surface. The physical platform utilizes two permanent-magnet brushed DC gear motors coupled with the STMicroelectronics \textbf{L298N Dual Full-Bridge Motor Driver}.

\subsection{Electromechanical DC Motor Modeling}
\justifying
A permanent-magnet DC motor is governed by coupled electrical and mechanical equations:
\begin{equation}
    V_a(t) = R_a i_a(t) + L_a \frac{di_a(t)}{dt} + e_b(t)
\end{equation}
\begin{equation}
    e_b(t) = K_b \cdot \omega_m(t) \quad \text{(Back-Electromotive Force)}
\end{equation}
\begin{equation}
    \tau_m(t) = K_t \cdot i_a(t) \quad \text{(Electromagnetic Torque)}
\end{equation}
where $R_a$ is armature winding resistance, $L_a$ is armature inductance, $K_b$ is back-EMF constant, $K_t$ is torque sensitivity constant, and $\omega_m$ is the motor shaft rotational velocity.

Because the electrical time constant $\tau_e = L_a / R_a$ is orders of magnitude faster than the mechanical time constant $\tau_m = J / b$, the armature inductance term $L_a \frac{di_a}{dt}$ can be neglected in balance control:
\begin{equation}
    i_a(t) \approx \frac{V_a(t) - K_b \omega_m(t)}{R_a}
\end{equation}
\begin{equation}
    \tau_m(t) = \frac{K_t}{R_a} V_a(t) - \frac{K_t K_b}{R_a} \omega_m(t)
\end{equation}

Equation~(\ref{eq:motor_torque}) reveals that motor output torque is directly proportional to applied armature terminal voltage $V_a$, with an intrinsic damping penalty proportional to rotational speed.

\subsection{L298N Dual H-Bridge Operation and Thermal Dissipation}
\justifying
The L298N motor driver incorporates two independent full-bridge circuits, each utilizing four bipolar Darlington transistors to switch currents up to $2.0\,\text{A}$ continuously per bridge (Figure~\ref{fig:l298n_wiring}). By controlling the logic states of the input pins (\texttt{IN1}, \texttt{IN2}) and pulsing the enable pin (\texttt{ENA}) with a high-frequency PWM signal, bidirectional four-quadrant motor control is achieved.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.85\textwidth,height=7.2cm,keepaspectratio]{figures/L298N Motor Driver Wiring Guide.png}
  \caption{L298N Dual H-Bridge Motor Driver Wiring Architecture and Pinout Connections.}
  \label{fig:l298n_wiring}
\end{figure}

A major engineering limitation of the L298N driver is its legacy bipolar junction transistor (BJT) architecture. Unlike modern MOSFET drivers (e.g., DRV8833 or TB6612FNG) that exhibit milliohm on-resistance ($R_{DS,on}$), the internal Darlington transistors produce a substantial saturation voltage drop:
\begin{equation}
    V_{\text{drop}} = V_{CE,sat(\text{upper})} + V_{CE,sat(\text{lower})} \approx 1.8\,\text{V} - 2.2\,\text{V}
\end{equation}
Under a motor current draw of $I_a = 1.0\,\text{A}$, the internal thermal power dissipation reaches:
\begin{equation}
    P_{\text{diss}} = V_{\text{drop}} \cdot I_a \approx 2.0\,\text{V} \cdot 1.0\,\text{A} = 2.0\,\text{Watts per bridge}
\end{equation}
This significant heat generation necessitated mounting an extruded aluminum heatsink and limiting sustained operating currents to prevent thermal shutdown.

\subsection{Static Friction Deadband and Software Linearization Algorithm}
\justifying
In physical gearboxes, internal static friction (stiction) between spur gear teeth prevents the motor shaft from rotating when tiny voltages are applied. In our empirical testing with the yellow TT gear motors (1:48 reduction ratio), applying PWM duty cycles below 65 ($D < 25.5\%$ of 255) produced zero mechanical motion, while the motor emitted an audible stall buzz.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.2cm,keepaspectratio]{figures/motor_deadband_linearization.png}
  \caption{Motor Static Friction Deadband Characterization and Firmware Linearization Mapping.}
  \label{fig:deadband_linearization}
\end{figure}

This actuation deadband is catastrophic for an inverted pendulum: when the robot approaches upright balance ($\theta \to 0$), the PID controller outputs small corrective torque commands, which fall entirely within the motor deadband. As a consequence, the robot experiences zero control torque near equilibrium, triggering a sustained, high-frequency mechanical limit-cycle oscillation ($\pm 2.5^\circ$).

To eliminate this limit cycle, the firmware incorporates a non-linear \textbf{Deadband Linearization Algorithm} (Figure~\ref{fig:deadband_linearization}):
\begin{equation}
    PWM_{\text{output}} = \begin{cases}
        \text{sgn}(u) \cdot \left[ PWM_{\text{min}} + |u| \cdot \left( \frac{255 - PWM_{\text{min}}}{255} \right) \right], & \text{if } |u| > 0 \\
        0, & \text{if } u = 0
    \end{cases}
\end{equation}
where $PWM_{\text{min}} = 65$ corresponds to the empirical static friction breakout threshold. By instantaneously skipping the unactuated deadband region, the motor delivers smooth, linear torque response down to infinitesimal angular errors, stabilizing the robot within $\pm 0.2^\circ$ of perfect vertical equilibrium.

\section{Digital PID Controller Theory and Real-Time Implementation}
\justifying
The core feedback stabilization algorithm implemented on the robot is a parallel \textbf{Proportional-Integral-Derivative (PID)} controller running at a deterministic update rate of $200\,\text{Hz}$ ($T_s = 5000\,\mu\text{s}$).

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.2cm,keepaspectratio]{figures/pid_step_response_tuning.png}
  \caption{Empirical Closed-Loop Step Response Tuning Curves Under Varying Gain Configurations.}
  \label{fig:pid_tuning_curves}
\end{figure}

\subsection{Parallel Discrete PID Formulation}
\justifying
Let the angular error $e_k$ at discrete time step $k$ be defined as the difference between the desired balance setpoint $\theta_{\text{setpoint}}$ (typically $0.0^\circ$, dynamically offset by calibration) and the fused tilt angle $\theta_k$:
\begin{equation}
    e_k = \theta_{\text{setpoint}} - \theta_k
\end{equation}

The control output $u_k$ is the sum of three distinct operational actions:
\begin{equation}
    u_k = P_k + I_k + D_k
\end{equation}

\textbf{1. Proportional Action ($P_k$):} Generates a corrective restoring torque proportional to the instantaneous angular tilt:
\begin{equation}
    P_k = K_p \cdot e_k
\end{equation}
$K_p$ acts as a virtual torsional spring stiffness. Higher $K_p$ values increase responsiveness but lead to underdamped oscillations.

\textbf{2. Integral Action with Anti-Windup ($I_k$):} Eliminates steady-state attitude droop caused by asymmetric chassis mass distribution or sensor offset errors:
\begin{equation}
    I_k = I_{k-1} + K_i \cdot e_k \cdot \Delta t
\end{equation}
To prevent integrator windup—where actuator saturation during large tilt angles causes $I_k$ to accumulate massive values, delaying recovery—the integrator is clamped via conditional saturation:
\begin{equation}
    I_k = \text{clip}(I_k, -I_{\text{max}}, +I_{\text{max}}), \quad \text{where } I_{\text{max}} = 80.0
\end{equation}

\textbf{3. Derivative Action with Low-Pass Filtering ($D_k$):} Provides critical damping by resisting the rate of angular divergence:
\begin{equation}
    D_k = -K_d \cdot \omega_{y, k}
\end{equation}
Notice that the derivative term is computed directly from the filtered gyroscopic rate $\omega_{y, k}$ rather than backward numerical error differencing ($e_k - e_{k-1})/\Delta t$. This completely avoids ``derivative kick'' when the setpoint is adjusted during teleoperation and prevents amplifying high-frequency noise.

\subsection{Phase-Portrait State-Space Stability Analysis}
\justifying
To evaluate closed-loop stability across large initial tilt deviations, the robot's trajectories were simulated and captured in the 2D phase plane $(\theta, \dot{\theta})$.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.4cm,keepaspectratio]{figures/phase_portrait_trajectories.png}
  \caption{State-Space Phase-Portrait Trajectories $(\theta, \dot{\theta})$ Showing Convergence to Stable Focus Equilibrium.}
  \label{fig:phase_portrait}
\end{figure}

As shown in Figure~\ref{fig:phase_portrait}, state trajectories initialized at large initial tilt angles ($\theta_0 = \pm 15^\circ$) spiral rapidly inward toward the origin $(0, 0)$, characterizing a \textbf{globally asymptotically stable focus}. The absence of closed orbital loops confirms that the deadband linearization algorithm completely suppressed non-linear limit cycles.

\renewcommand{\arraystretch}{1.2}
\begin{table}[!ht]
\centering
\small
\caption{Empirical PID Parameter Tuning Progression and Performance Impact}
\label{tab:pid_tuning}
\begin{tabular}{|c|c|c|p{4.2cm}|p{4.5cm}|}
\hline
\textbf{$K_p$} & \textbf{$K_i$} & \textbf{$K_d$} & \textbf{Observed Robot Behavior} & \textbf{Stability Classification} \\
\hline
10.0 & 0.0 & 0.0 & Insufficient restoring torque; robot tipped over immediately. & Unstable (Overdamped Fall) \\
25.0 & 0.0 & 0.0 & Robot attempted to right itself but collapsed after 1.5 seconds. & Unstable \\
48.0 & 0.0 & 0.0 & Continuous, sustained harmonic oscillations ($K_u = 48.0, T_u = 0.38\text{ s}$). & Marginally Stable (Ultimate Gain) \\
28.0 & 0.0 & 0.6 & Oscillations damped significantly; maintained balance for 10 seconds. & Weakly Damped \\
28.0 & 0.0 & 1.2 & Rapid disturbance recovery; strong damping; slight steady-state lean. & Well-Damped Equilibrium \\
28.0 & 140.0 & 1.2 & Perfect vertical balance ($\pm 0.2^\circ$); zero steady-state droop. & \textbf{Optimal Working Configuration} \\
35.0 & 180.0 & 1.8 & High-frequency chassis chatter; motors running hot; motor strain. & Over-Tuned (Noise Sensitive) \\
\hline
\end{tabular}
\end{table}
\renewcommand{\arraystretch}{1.0}

\section{Optimal State-Feedback Control: Linear Quadratic Regulator (LQR)}
\justifying
In addition to classical parallel PID control, the internship evaluated modern optimal state-space control via the \textbf{Linear Quadratic Regulator (LQR)}. LQR control synthesizes a full-state feedback gain vector:
\begin{equation}
    u(t) = -\mathbf{K} \mathbf{x}(t) = -\begin{bmatrix} k_x & k_{\dot{x}} & k_\theta & k_{\dot{\theta}} \end{bmatrix} \begin{bmatrix} x \\ \dot{x} \\ \theta \\ \dot{\theta} \end{bmatrix}
\end{equation}
that minimizes the continuous infinite-horizon quadratic performance index:
\begin{equation}
    J = \int_{0}^{\infty} \left( \mathbf{x}(t)^T \mathbf{Q} \mathbf{x}(t) + u(t)^T \mathbf{R} u(t) \right) dt
\end{equation}
where $\mathbf{Q} = \mathbf{Q}^T \geq 0$ penalizes state tracking errors and $\mathbf{R} > 0$ penalizes actuator control energy expenditure.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.90\textwidth,height=7.4cm,keepaspectratio]{figures/lqr_vs_pid_step_comparison.png}
  \caption{Dynamic Disturbance Rejection Comparison: Tuned Parallel PID vs. Optimal LQR Control.}
  \label{fig:lqr_vs_pid}
\end{figure}

The optimal feedback gain matrix $\mathbf{K}$ is computed from:
\begin{equation}
    \mathbf{K} = \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P}
\end{equation}
where $\mathbf{P}$ is the unique symmetric positive-definite solution of the \textbf{Continuous Algebraic Riccati Equation (CARE)}:
\begin{equation}
    \mathbf{A}^T \mathbf{P} + \mathbf{P} \mathbf{A} - \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} + \mathbf{Q} = \mathbf{0}
\end{equation}

Configuring state weights $\mathbf{Q} = \text{diag}(100, 10, 150, 15)$ and control penalty $R = 0.1$ yielded the optimal gain vector:
\begin{equation}
    \mathbf{K} = \begin{bmatrix} -31.62 & -24.85 & 182.45 & 28.16 \end{bmatrix}
\end{equation}

As demonstrated in Figure~\ref{fig:lqr_vs_pid}, while the tuned PID controller achieves excellent stabilization with minor settling overshoot, LQR provides a strictly critically damped disturbance response with $22\%$ lower peak control effort, minimizing electrical battery drain during aggressive recovery maneuvers.

\section{Internet of Things (IoT) Telemetry and Cloud Platforms}
\justifying
The integration of cloud telecommunication transforms the self-balancing robot from an isolated closed-loop automaton into an interconnected cyber-physical IoT node. 

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.4cm,keepaspectratio]{figures/esp32_iot_block_diagram.jpg}
  \caption{End-to-End System Block Diagram: Sensors, Microcontroller, Motor Stage, and Dual Cloud IoT Platforms.}
  \label{fig:iot_system_block}
\end{figure}

\subsection{Google Firebase Realtime Database (RTDB) Architecture}
\justifying
Google Firebase Realtime Database is a cloud-hosted NoSQL JSON database that allows real-time data synchronization across clients via persistent Server-Sent Events (SSE) HTTPS streams. 

The robot firmware structures telemetry data into a hierarchical JSON tree:
\begin{lstlisting}[language=C++]
// JSON Telemetry Payload Dispatched to Google Firebase RTDB
{
  "telemetry": {
    "pitch_deg": 0.18,
    "gyro_rate": -0.42,
    "pid_output": 74,
    "battery_v": 11.42,
    "loop_time_us": 4985,
    "rssi_dbm": -58
  },
  "config": {
    "Kp": 28.0,
    "Ki": 140.0,
    "Kd": 1.2
  }
}
\end{lstlisting}

Every $100\,\text{ms}$ ($10\,\text{Hz}$), FreeRTOS Core 0 collects the latest state snapshot and issues an authenticated non-blocking PATCH request to the Firebase endpoint. Operators can view live numerical plots and inspect historical performance logs from any web browser worldwide.

\subsection{Blynk 2.0 Mobile IoT Dashboard and Remote Teleoperation}
\justifying
To provide an intuitive handheld operational interface, the project configured the \textbf{Blynk 2.0} mobile application. Blynk communicates over low-overhead bidirectional WebSockets, assigning hardware pins to virtual datastreams:
\begin{itemize}[itemsep=1pt]
  \item \textbf{Virtual Pin V0 (Gauge):} Real-time pitch angle display ($-25^\circ$ to $+25^\circ$).
  \item \textbf{Virtual Pin V1 (Gauge):} Motor command PWM duty cycle ($-255$ to $+255$).
  \item \textbf{Virtual Pin V2 (Level Bar):} Remaining 3S Li-ion battery terminal voltage ($9.0\text{V}$ to $12.6\text{V}$).
  \item \textbf{Virtual Pin V3 (2-Axis Joystick):} Remote teleoperation steering (Forward/Reverse setpoint tilt offset $\Delta \theta$, Differential turning $\Delta u$).
  \item \textbf{Virtual Pins V4, V5, V6 (Sliders):} Over-the-air PID parameter tuning sliders for $K_p, K_i, K_d$.
\end{itemize}

\subsection{MQTT Telemetry Architecture}
\justifying
In industrial deployments requiring ultra-low bandwidth consumption, the system supports the \textbf{Message Queuing Telemetry Transport (MQTT)} protocol. Telemetry packets are published to an external Mosquitto broker under topic \texttt{robot/balancing/telemetry} utilizing QoS level 0 (At most once) for high-frequency sensor updates and QoS level 1 (At least once) for critical battery low-voltage alarms.

\section{Firmware Architecture and FreeRTOS Multitasking}
\justifying
To enforce strict real-time determinism without compromising cloud networking capabilities, the ESP32 firmware leverages the FreeRTOS symmetric multiprocessing (SMP) kernel.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.2cm,keepaspectratio]{figures/ide.png}
  \caption{FreeRTOS Dual-Core Real-Time Task Allocation and Inter-Core Queue Synchronization.}
  \label{fig:freertos_arch}
\end{figure}

The operating system coordinates two concurrent tasks pinned to dedicated microprocessor cores:
\begin{itemize}[itemsep=2pt]
  \item \textbf{TaskBalancing (Core 1, Priority 5):} Executes at a hard deterministic frequency of $200\,\text{Hz}$ ($5000\,\mu\text{s}$ interval) triggered by a 64-bit hardware timer alarm. It reads MPU-6050 $I^2C$ registers at 400 kHz, computes the complementary filter, calculates parallel PID outputs, applies deadband linearization, and writes hardware PWM registers. Core 1 operates without dynamic memory allocation or blocking I/O, guaranteeing jitter below $2.5\,\mu\text{s}$.
  \item \textbf{TaskTelemetry (Core 0, Priority 1):} Runs at a relaxed rate of $10\,\text{Hz}$ ($100\,\text{ms}$ interval). It formats telemetry into JSON payloads, handles Wi-Fi stack beacons, dispatches Firebase RTDB updates, and processes incoming Blynk WebSocket packets.
\end{itemize}

Inter-task data transfer between Core 1 and Core 0 is handled via thread-safe \textbf{FreeRTOS Queues} (\texttt{xQueueSendToBack} / \texttt{xQueueReceive}). This decoupled architecture ensures that even during temporary Wi-Fi packet drops or cloud server timeouts, the mechanical balancing control loop on Core 1 remains completely undisturbed.

"""
print("Chapter 3 defined, len =", len(c3_text))
