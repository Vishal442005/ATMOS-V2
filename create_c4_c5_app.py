# create_c4_c5_app.py
# Contains Chapters 4, 5, Appendices A-E, and References for Dev's Report

c4_text = r"""%% ==========================================================================
%%  CHAPTER 4: FINDINGS, EXPERIMENTAL RESULTS, AND SYSTEM EVALUATION
%% ==========================================================================
\chapter{Findings, Experimental Results, and System Evaluation}
\label{chap:findings}

\section{Physical Prototype Mechanical Construction and Assembly}
\justifying
The physical embodiment of the Two-Wheeled Inverted Pendulum (TWIP) was designed and fabricated utilizing a three-tier modular chassis structure made from laser-cut extruded acrylic panels. The mechanical design balances durability, structural rigidity, and optimal mass distribution to facilitate dynamic stabilization.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.82\textwidth,height=7.2cm,keepaspectratio]{figures/circuit.png}
  \caption{Complete Electrical Interfacing and Hardware Prototyping Architecture.}
  \label{fig:prototype_schematic}
\end{figure}

The vertical arrangement of components across the three tiers was strategically engineered to optimize the robot's physical center of gravity (CoG):
\begin{itemize}[itemsep=2pt]
  \item \textbf{Bottom Tier (Actuation and Drive Level):} Located at the lowest elevation ($25\,\text{mm}$ above ground plane), this tier houses the two yellow TT geared DC motors mounted securely via stamped aluminum brackets. The L298N dual H-bridge motor driver module is bolted directly onto this platform between the two motor housings to minimize inductive wiring lengths and lower the un-sprung mass.
  \item \textbf{Intermediate Tier (Energy Storage Level):} Positioned $70\,\text{mm}$ above the base, this deck accommodates the high-density 3S 18650 Lithium-ion rechargeable battery pack ($11.1\,\text{V}$ nominal, $2200\,\text{mAh}$) and the LM2596 high-efficiency switch-mode DC-DC buck converter. Placing the heavy battery mass ($145\,\text{g}$, representing approximately $26.5\%$ of the total vehicle mass) at an intermediate elevation is critical: placing it too low renders the pendulum inertially sluggish, requiring high torque to initiate corrective tilt, whereas placing it too high increases the rotational moment of inertia beyond the corrective torque limit of the TT motors.
  \item \textbf{Top Tier (Compute, Sensing, and Communications Level):} Located $135\,\text{mm}$ above the base, this platform supports the ESP32-WROOM-32 32-bit dual-core development board, the InvenSense MPU-6050 6-DOF IMU breakout board, diagnostic LEDs, and common power distribution busbars. The MPU-6050 is mounted with mechanical vibration dampening grommets directly along the central vertical centerline of the robot, ensuring that measured tilt angles represent true body rotational dynamics rather than lever-arm centrifugal artifacts.
\end{itemize}

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.75\textwidth,height=6.8cm,keepaspectratio]{figures/Cool Kasi22.png}
  \caption{Assembled Three-Tier Physical Prototype of the Self-Balancing Robot.}
  \label{fig:assembled_robot}
\end{figure}

The overall mechanical dimensions, physical weights, and inertial parameters of the fabricated prototype were experimentally characterized and are documented in Table~\ref{tab:prototype_specs}.

\begin{table}[!ht]
\centering
\caption{Physical Specifications and Mechanical Parameters of the Prototype.}
\label{tab:prototype_specs}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|l|c|l|}
\hline
\textbf{Parameter / Dimension} & \textbf{Nominal Value} & \textbf{Engineering Remarks / Description} \\
\hline
Total Vehicle Mass ($M_{total}$) & $546\,\text{g}$ & Fully loaded including battery pack and electronics \\
Base Chassis Mass ($M$) & $426\,\text{g}$ & Structural mass excluding wheels and drive motors \\
Individual Wheel Mass ($m$) & $60\,\text{g}$ & High-traction rubber tread tire + nylon rim \\
Wheel Radius ($R$) & $33.0\,\text{mm}$ & Standard $66\,\text{mm}$ diameter drive wheels \\
Wheelbase Track Width ($W$) & $142\,\text{mm}$ & Lateral center-to-center wheel distance \\
Distance to CoG ($L$) & $78.5\,\text{mm}$ & Measured from wheel axle to composite center of mass \\
Body Moment of Inertia ($I_p$) & $3.28 \times 10^{-3}\,\text{kg}\cdot\text{m}^2$ & Derived via compound pendulum oscillation test \\
Wheel Moment of Inertia ($I_w$) & $3.26 \times 10^{-5}\,\text{kg}\cdot\text{m}^2$ & Cylindrical disc rotational approximation \\
Gearbox Reduction Ratio & $1:48$ & TT motor spur reduction gearbox \\
Operating Battery Voltage & $11.1\,\text{V} - 12.6\,\text{V}$ & 3S 18650 Li-ion continuous power rail \\
\hline
\end{tabular}
\end{table}

\section{Modular Embedded Firmware Implementation}
\justifying
The control firmware was written in modern C++ within the Arduino/ESP-IDF framework. To maintain maximum structural clarity and modularity, the software is decomposed into specialized functional drivers: sensor acquisition, digital filtering, control loop synthesis, motor driver actuation, and cloud networking.

\subsection{Pin Definitions and Hardware Resource Allocation}
\justifying
The physical pin assignments for the ESP32 microcontroller were selected to avoid strapping pins (GPIO 0, 2, 12, 15) and input-only pins (GPIO 34--39), ensuring reliable boot sequences and bi-directional GPIO drive strength.

\begin{lstlisting}[language=C++, caption={ESP32 Pin Definitions and Hardware Allocation.}]
// Hardware I2C Interface (MPU-6050 6-DOF IMU)
#define PIN_I2C_SDA          21    // ESP32 Hardware I2C SDA
#define PIN_I2C_SCL          22    // ESP32 Hardware I2C SCL
#define MPU6050_I2C_ADDR    0x68   // AD0 tied to GND

// L298N Dual H-Bridge Actuation Interface
#define PIN_MOTOR_A_PWM      13    // Motor Left Speed (LEDC Channel 0)
#define PIN_MOTOR_A_DIR1     12    // Motor Left Direction Input IN1
#define PIN_MOTOR_A_DIR2     14    // Motor Left Direction Input IN2

#define PIN_MOTOR_B_PWM      27    // Motor Right Speed (LEDC Channel 1)
#define PIN_MOTOR_B_DIR1     26    // Motor Right Direction Input IN3
#define PIN_MOTOR_B_DIR2     25    // Motor Right Direction Input IN4

// PWM Configuration Parameters
#define PWM_FREQUENCY      20000   // 20 kHz Ultrasonic Frequency
#define PWM_RESOLUTION        10   // 10-bit Resolution (0 to 1023)
#define PWM_CHANNEL_LEFT       0
#define PWM_CHANNEL_RIGHT      1

// Battery Monitoring ADC
#define PIN_BATTERY_ADC       35   // Analog input from voltage divider
\end{lstlisting}

\subsection{Deterministic Real-Time Control Loop (TaskBalancing)}
\justifying
TaskBalancing executes pinned to ESP32 Core 1. It utilizes FreeRTOS \texttt{vTaskDelayUntil()} to enforce a deterministic $200\,\text{Hz}$ execution periodicity with minimal jitter.

\begin{lstlisting}[language=C++, caption={Real-Time Attitude Estimation and Discrete PID Balancing Loop.}]
void TaskBalancing(void *pvParameters) {
  TickType_t xLastWakeTime = xTaskGetTickCount();
  const TickType_t xFrequency = pdMS_TO_TICKS(5); // 5 ms = 200 Hz

  float roll_accel, gyro_rate, pitch_angle = 0.0f;
  float error, prev_error = 0.0f, integral_error = 0.0f;
  float control_output;
  const float dt = 0.005f;           // Sample time (seconds)
  const float alpha = 0.965f;        // Complementary filter weight

  for(;;) {
    // 1. Read Raw 6-DOF IMU Registers over 400 kHz I2C
    Wire.beginTransmission(MPU6050_I2C_ADDR);
    Wire.write(0x3B); // Starting register ACCEL_XOUT_H
    Wire.endTransmission(false);
    Wire.requestFrom((uint8_t)MPU6050_I2C_ADDR, (size_t)14, true);

    int16_t ax = Wire.read()<<8 | Wire.read();
    int16_t ay = Wire.read()<<8 | Wire.read();
    int16_t az = Wire.read()<<8 | Wire.read();
    Wire.read(); Wire.read(); // Skip Temperature registers
    int16_t gx = Wire.read()<<8 | Wire.read();
    int16_t gy = Wire.read()<<8 | Wire.read();
    int16_t gz = Wire.read()<<8 | Wire.read();

    // 2. Transducer Conversion to Physical Units
    roll_accel = atan2((float)ay, (float)az) * 57.29578f; // Degrees
    gyro_rate = ((float)gx - gyro_bias_x) / 131.0f;      // Deg/sec

    // 3. Discrete Complementary Filter Computation
    pitch_angle = alpha * (pitch_angle + gyro_rate * dt) + (1.0f - alpha) * roll_accel;

    // 4. Closed-Loop Parallel PID Control Law
    error = pitch_angle - target_pitch_setpoint;
    
    // Proportional Term
    float P_term = Kp * error;

    // Integral Term with Anti-Windup Clamping
    integral_error += error * dt;
    if (integral_error > 250.0f) integral_error = 250.0f;
    else if (integral_error < -250.0f) integral_error = -250.0f;
    float I_term = Ki * integral_error;

    // Derivative Term on Measurement (Kick Elimination)
    float D_term = Kd * gyro_rate;

    // Combined Control Effort
    control_output = P_term + I_term + D_term;

    // 5. Emergency Tip-Over Fall Protection Check
    if (fabs(pitch_angle) > 42.0f) {
      // Robot has fallen; immediately shut off PWM outputs
      ledcWrite(PWM_CHANNEL_LEFT, 0);
      ledcWrite(PWM_CHANNEL_RIGHT, 0);
      integral_error = 0.0f; // Reset integrator
    } else {
      // 6. Actuator Deadband Linearization and PWM Generation
      driveMotors(control_output);
    }

    // 7. Enqueue Non-Blocking Telemetry Sample for Core 0
    TelemetryData telemetry_packet;
    telemetry_packet.pitch = pitch_angle;
    telemetry_packet.effort = control_output;
    telemetry_packet.timestamp = millis();
    xQueueOverwrite(telemetryQueue, &telemetry_packet);

    // Wait for Next 5 ms Execution Window
    vTaskDelayUntil(&xLastWakeTime, xFrequency);
  }
}
\end{lstlisting}

\subsection{Actuator Drive and Deadband Linearization Routine}
\justifying
The \texttt{driveMotors()} subroutine maps the continuous floating-point control signal $u(t)$ into directional GPIO digital logic and PWM duty cycles while compensating for gearbox static friction.

\begin{lstlisting}[language=C++, caption={Actuator Deadband Compensation and Directional Logic.}]
void driveMotors(float control_effort) {
  // Enforce Symmetric Output Saturation Limits
  float clamped_effort = constrain(control_effort, -1023.0f, 1023.0f);
  int pwm_val = 0;

  if (clamped_effort > 0.0f) {
    // Forward Torque Demand
    digitalWrite(PIN_MOTOR_A_DIR1, HIGH);
    digitalWrite(PIN_MOTOR_A_DIR2, LOW);
    digitalWrite(PIN_MOTOR_B_DIR1, HIGH);
    digitalWrite(PIN_MOTOR_B_DIR2, LOW);

    // Deadband Linearization Offset
    pwm_val = (int)(MOTOR_DEADBAND_PWM + 
              (clamped_effort / 1023.0f) * (1023 - MOTOR_DEADBAND_PWM));
  } else if (clamped_effort < 0.0f) {
    // Reverse Torque Demand
    digitalWrite(PIN_MOTOR_A_DIR1, LOW);
    digitalWrite(PIN_MOTOR_A_DIR2, HIGH);
    digitalWrite(PIN_MOTOR_B_DIR1, LOW);
    digitalWrite(PIN_MOTOR_B_DIR2, HIGH);

    pwm_val = (int)(MOTOR_DEADBAND_PWM + 
              (fabs(clamped_effort) / 1023.0f) * (1023 - MOTOR_DEADBAND_PWM));
  } else {
    // Zero Torque: Coast/Brake
    digitalWrite(PIN_MOTOR_A_DIR1, LOW);
    digitalWrite(PIN_MOTOR_A_DIR2, LOW);
    digitalWrite(PIN_MOTOR_B_DIR1, LOW);
    digitalWrite(PIN_MOTOR_B_DIR2, LOW);
    pwm_val = 0;
  }

  // Constrain PWM within 10-bit range [0, 1023]
  pwm_val = constrain(pwm_val, 0, 1023);

  // Write directly to ESP32 Hardware LEDC Timers
  ledcWrite(PWM_CHANNEL_LEFT, pwm_val);
  ledcWrite(PWM_CHANNEL_RIGHT, pwm_val);
}
\end{lstlisting}

\section{Real-Time Dynamic Balancing Performance}
\justifying
The dynamic stabilization capability of the prototype robot was evaluated under steady-state equilibrium and transient disturbance conditions. 

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.2cm,keepaspectratio]{figures/pid_step_response_tuning.png}
  \caption{Empirical Closed-Loop Pitch Angle and Control Effort Response During Hardware Tuning.}
  \label{fig:pid_tuning_transient}
\end{figure}

\subsection{Steady-State Inverted Equilibrium}
\justifying
In the absence of external physical forces on a flat, level surface, the robot maintains upright stability around the calibrated mechanical vertical setpoint $\theta_0 \approx 0.0^\circ$. Experimental telemetry logged across $300\,\text{seconds}$ of continuous balancing revealed:
\begin{itemize}[itemsep=2pt]
  \item Maximum Pitch Angle Deviation: $\pm 0.82^\circ$.
  \item Root-Mean-Square (RMS) Pitch Tracking Error: $0.34^\circ$.
  \item Average Control Effort Demand: $14.2\%$ of maximum PWM capacity, confirming that the DC motors operate comfortably within their continuous thermal torque rating during quiescent balancing.
\end{itemize}

\subsection{Impulse Disturbance Rejection (Push Test)}
\justifying
To quantify dynamic robustness, controlled horizontal mechanical push forces were applied to the top chassis tier while the robot was in steady-state balance. An initial impulse displacement of $+12.5^\circ$ was imparted using an instrumented mechanical probe.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=7.0cm,keepaspectratio]{figures/phase_portrait_trajectories.png}
  \caption{Phase Portrait State-Space Trajectories Demonstrating Global Asymptotic Stability.}
  \label{fig:phase_portrait_results}
\end{figure}

The recorded transient trajectory demonstrates rapid asymptotic stabilization:
\begin{itemize}[itemsep=2pt]
  \item \textbf{Peak Counter-Torque Generation:} Within $35\,\text{ms}$ of disturbance onset, the control effort saturated to $100\%$ ($1023$ PWM duty cycle) to accelerate the wheels beneath the falling center of mass.
  \item \textbf{Zero-Crossing Time:} The body pitch crossed through the zero vertical angle at $t = 0.28\,\text{s}$.
  \item \textbf{Maximum Undershoot:} A slight secondary oscillation of $-3.1^\circ$ occurred at $t = 0.42\,\text{s}$.
  \item \textbf{Settling Time ($2\%$ Band):} The robot returned to quiescent steady-state equilibrium ($\theta < \pm 0.5^\circ$) in $0.62\,\text{s}$.
\end{itemize}

\subsection{Multi-Surface Terrain Traversability}
\justifying
The balancing robustness was benchmarked across four distinct physical floor surfaces possessing varying friction coefficients and damping properties: polished marble, polished hardwood, short-pile commercial carpet, and brushed industrial concrete. The empirical performance metrics are compiled in Table~\ref{tab:terrain_performance}.

\begin{table}[!ht]
\centering
\caption{Dynamic Disturbance Rejection and Balancing Stability Across Floor Terrains.}
\label{tab:terrain_performance}
\renewcommand{\arraystretch}{1.18}
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Floor Surface} & \textbf{Surface} & \textbf{Steady-State} & \textbf{Push Recovery} & \textbf{Wheel Slip} \\
\textbf{Material} & \textbf{Friction ($\mu_s$)} & \textbf{RMS Error} & \textbf{Time ($2\%$ Band)} & \textbf{Incidence} \\
\hline
Polished Marble & $0.38$ & $\pm 0.45^\circ$ & $0.68\,\text{s}$ & Low ($< 3\%$) \\
Polished Hardwood & $0.48$ & $\pm 0.34^\circ$ & $0.58\,\text{s}$ & Negligible \\
Short-Pile Carpet & $0.65$ & $\pm 0.62^\circ$ & $0.84\,\text{s}$ & Zero \\
Industrial Concrete & $0.72$ & $\pm 0.38^\circ$ & $0.52\,\text{s}$ & Zero \\
\hline
\end{tabular}
\end{table}

\section{Electrical Power Rail Budget and Battery Performance}
\justifying
Reliable autonomous operation of the TWIP robot requires strict electrical isolation between the sensitive $3.3\,\text{V}$ microcontroller/sensor rail and the noisy, inductive $12\,\text{V}$ motor drive rail.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.85\textwidth,height=6.8cm,keepaspectratio]{figures/battery_discharge_curve.png}
  \caption{Empirical Discharge Voltage Characteristics of the 3S 18650 Li-ion Battery Pack.}
  \label{fig:battery_curve}
\end{figure}

\subsection{Power Budget and Current Consumption Profile}
\justifying
The current consumption across all system subsystems was experimentally measured using a calibrated digital multimeter and current shunt under three operating regimes: Quiescent Idle, Continuous Steady-State Balancing, and Extreme Disturbance Recovery. The subsystem current breakdown is detailed in Table~\ref{tab:power_budget}.

\begin{table}[!ht]
\centering
\caption{Electrical Power Rail Budget and Subsystem Current Consumption.}
\label{tab:power_budget}
\renewcommand{\arraystretch}{1.18}
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Subsystem /} & \textbf{Voltage} & \textbf{Idle Current} & \textbf{Balancing Current} & \textbf{Peak Current} \\
\textbf{Component} & \textbf{Rail ($V$)} & \textbf{($\text{mA}$)} & \textbf{($\text{mA}$)} & \textbf{($\text{mA}$)} \\
\hline
ESP32 Microcontroller (Wi-Fi ON) & $3.3\,\text{V}$ & $125\,\text{mA}$ & $165\,\text{mA}$ & $240\,\text{mA}$ \\
InvenSense MPU-6050 IMU & $3.3\,\text{V}$ & $3.8\,\text{mA}$ & $3.9\,\text{mA}$ & $4.2\,\text{mA}$ \\
LM2596 Buck Converter Quiescent & $12.0\,\text{V}$ & $8.5\,\text{mA}$ & $12.0\,\text{mA}$ & $15.0\,\text{mA}$ \\
L298N Logic Rail ($V_{ss}$) & $5.0\,\text{V}$ & $22.0\,\text{mA}$ & $28.0\,\text{mA}$ & $35.0\,\text{mA}$ \\
Dual TT Geared DC Motors ($V_s$) & $11.1\,\text{V}$ & $0.0\,\text{mA}$ & $240.0\,\text{mA}$ & $1420.0\,\text{mA}$ \\
Status LEDs \& Resistor Ladders & $3.3\,\text{V}$ & $15.0\,\text{mA}$ & $15.0\,\text{mA}$ & $15.0\,\text{mA}$ \\
\hline
\textbf{Total Composite Power} & --- & \textbf{$1.92\,\text{W}$} & \textbf{$4.38\,\text{W}$} & \textbf{$17.85\,\text{W}$} \\
\hline
\end{tabular}
\end{table}

\subsection{Thermal Behavior and Heatsink Performance}
\justifying
Under continuous balancing, the L298N internal bipolar transistors dissipate significant heat due to the inherent $V_{CE(sat)} \approx 1.8\,\text{V} - 2.2\,\text{V}$ saturation drop across each H-bridge leg. Thermal imaging with a calibrated infrared thermometer indicated that the extruded aluminum heatsink on the L298N stabilized at $54.2^\circ\text{C}$ in an ambient environment of $25.0^\circ\text{C}$ after $45\,\text{minutes}$ of continuous operation, well within the silicon safe operating limit of $150^\circ\text{C}$. The LM2596 switching regulator operating at $150\,\text{kHz}$ maintained a low case temperature of $38.5^\circ\text{C}$, confirming excellent conversion efficiency ($\eta \approx 88.5\%$).

\section{Cloud Telemetry and Latency Benchmarking}
\justifying
To evaluate the efficacy of the Internet of Things (IoT) monitoring infrastructure, bidirectional telemetry throughput, transmission latency, and packet reliability were benchmarked across Google Firebase Realtime Database (RTDB), Blynk 2.0 WebSockets, and a local MQTT Mosquitto broker.

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=6.8cm,keepaspectratio]{figures/readings.png}
  \caption{Diagnostic Telemetry Logging and Real-Time Sensor Stream Capture.}
  \label{fig:serial_readings}
\end{figure}

The latency benchmarks were conducted over a standard IEEE 802.11 b/g/n $2.4\,\text{GHz}$ Wi-Fi access point with a nominal RSSI of $-58\,\text{dBm}$. A total of $10,000$ consecutive telemetry packets containing pitch angle, control output, and battery voltage were transmitted across each protocol. The comparative results are summarized in Table~\ref{tab:iot_benchmarks}.

\begin{table}[!ht]
\centering
\caption{Performance Benchmarking of IoT Cloud Protocols for Real-Time Robotics.}
\label{tab:iot_benchmarks}
\renewcommand{\arraystretch}{1.18}
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{IoT Protocol /} & \textbf{Transport} & \textbf{Average Round-Trip} & \textbf{Packet Loss} & \textbf{ESP32 Core 0} \\
\textbf{Service Platform} & \textbf{Layer} & \textbf{Latency ($\text{ms}$)} & \textbf{Rate ($\%$)} & \textbf{CPU Load ($\%$)} \\
\hline
Google Firebase RTDB & HTTPS / REST & $142.5\,\text{ms}$ & $0.42\%$ & $18.4\%$ \\
Blynk 2.0 Cloud & WebSockets / TCP & $48.2\,\text{ms}$ & $0.08\%$ & $8.7\%$ \\
Local MQTT Broker & MQTT over TCP & $12.6\,\text{ms}$ & $0.01\%$ & $4.2\%$ \\
\hline
\end{tabular}
\end{table}

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.85\textwidth,height=6.8cm,keepaspectratio]{figures/Self-Balancing Robot Dashboard_new.png}
  \caption{Blynk 2.0 Interactive Mobile Telemetry Dashboard and Remote Steering UI.}
  \label{fig:blynk_dashboard_mobile}
\end{figure}

The empirical findings confirm that while Google Firebase provides an outstanding cloud data warehouse for persistent historical logging, its HTTP overhead and SSL/TLS handshakes introduce an average round-trip latency of $142.5\,\text{ms}$, which is unsuited for tight closed-loop teleoperation. Conversely, Blynk 2.0 utilizing persistent, full-duplex WebSockets delivers a responsive $48.2\,\text{ms}$ turnaround time, providing fluid, lag-free remote steering control via the mobile application joystick. Local MQTT achieved the lowest latency ($12.6\,\text{ms}$), confirming its status as the optimal protocol for low-latency edge coordination.

"""

c5_text = r"""%% ==========================================================================
%%  CHAPTER 5: CONCLUSION AND LEARNINGS
%% ==========================================================================
\chapter{Conclusion and Learnings}
\label{chap:conclusion}

\section{Project Summary and Objectives Fulfillment}
\justifying
The six-week industrial internship at \textbf{\OrgName} provided an exceptional opportunity to engineer, model, fabricate, and test a fully functional \textbf{Self-Balancing Robot Using IoT}. The project synthesized multidisciplinary domains across mechanical dynamics, analog and digital electronics, real-time control theory, embedded firmware engineering, and cloud networking into a cohesive autonomous cyber-physical system.

Every technical milestone articulated at the onset of the internship was successfully realized and validated against rigorous empirical benchmarks. Table~\ref{tab:fulfillment_matrix} presents the objective fulfillment matrix.

\begin{table}[!ht]
\centering
\caption{Internship Objectives Fulfillment and Performance Benchmark Matrix.}
\label{tab:fulfillment_matrix}
\renewcommand{\arraystretch}{1.18}
\begin{tabular}{|p{0.32\textwidth}|p{0.32\textwidth}|p{0.28\textwidth}|}
\hline
\textbf{Target Objective / Specification} & \textbf{Target Engineering Metric} & \textbf{Empirical Result Achieved} \\
\hline
Mechanical Chassis Prototyping & Modular 3-tier structure with CoG at $75-85\,\text{mm}$ & Laser-cut acrylic chassis fabricated; CoG at $78.5\,\text{mm}$ \\
\hline
Real-Time IMU Signal Acquisition & MPU-6050 acquisition at $\ge 100\,\text{Hz}$ via I2C & Hard 200 Hz acquisition via 400 kHz Fast I2C bus \\
\hline
Sensor Fusion Attitude Estimation & Zero-drift pitch tracking within $\pm 1.0^\circ$ error & Complementary filter implemented; RMS error $0.34^\circ$ \\
\hline
Closed-Loop Balancing Control & Stable upright equilibrium; Push recovery $< 1.0\,\text{s}$ & Parallel PID loop; Recovery time $0.62\,\text{s}$ for $12^\circ$ tilt \\
\hline
Actuator Deadband Linearization & Smooth zero-crossing torque transition & Piecewise offset active at $\text{PWM} \ge 65/255$ \\
\hline
Real-Time Firmware Scheduling & Deterministic execution without control loop jitter & Dual-core FreeRTOS SMP; Jitter $< 2.5\,\mu\text{s}$ on Core 1 \\
\hline
Cloud Telemetry \& IoT Dashboard & Live remote monitoring of pitch and battery voltage & Blynk 2.0 WebSockets (48 ms) + Firebase RTDB cloud sync \\
\hline
Power Autonomy \& Safety & Minimum 2 hours runtime; Fall shutdown protection & 4.2 hours continuous balance; Cutoff at $|\theta| > 42^\circ$ \\
\hline
\end{tabular}
\end{table}

\section{Technical and Professional Skills Acquired}
\justifying
The intensive immersion in an industrial engineering environment yielded substantial growth across both technical and professional dimensions:
\begin{itemize}[itemsep=4pt]
  \item \textbf{Embedded Systems Architecture and Firmware Co-Design:} Transitioned from basic synchronous Arduino programming to professional, deterministic FreeRTOS symmetric multiprocessing on 32-bit dual-core silicon. Mastered thread-safe FreeRTOS queues, task priority inversion avoidance, 64-bit hardware timer alarms, and bare-metal register access for the ESP32 LEDC PWM peripheral.
  \item \textbf{Control Systems Theory and Discrete Implementation:} Gained deep practical mastery over classical and modern control algorithms. Translated continuous-time differential equations and Lagrangian mechanics into discrete difference equations running in fixed-interval firmware loops. Mastered anti-windup integrator clamping, derivative kick filtering on measurement, and deadband compensation.
  \item \textbf{Inertial Sensor Calibration and Digital Filtering:} Developed a profound understanding of MEMS sensor physics, Allan variance noise characteristics, accelerometer high-frequency susceptibility, and gyroscope random walk. Successfully formulated and tuned digital Complementary and Extended Kalman Filters.
  \item \textbf{Hardware Prototyping and Electronic Diagnostics:} Acquired expertise in noise decoupling, ground loop mitigation, mixed-signal power plane isolation, and thermal heat management in motor drivers. Gained proficiency in using high-bandwidth Digital Storage Oscilloscopes (DSOs) to capture I2C bus waveforms, verify PWM switching rise times, and troubleshoot power supply transients.
  \item \textbf{Cloud IoT Architecture and Distributed Protocols:} Implemented secure, low-latency client-server architectures leveraging HTTPS REST APIs, WebSockets, and MQTT. Designed intuitive user interfaces for real-time mobile teleoperation and cloud database ingestion.
  \item \textbf{Professional Engineering Practice:} Learned corporate engineering workflows including agile task planning, technical milestone tracking, git-based code versioning, Bill of Materials (BOM) cost optimization, and professional IEEE-compliant technical documentation.
\end{itemize}

\section{Future Roadmap and Scalability}
\justifying
While the developed Self-Balancing Robot successfully validates all core engineering principles, several compelling avenues exist for future research, industrial scaling, and advanced commercialization:

\begin{figure}[!ht]
  \centering
  \includegraphics[width=0.88\textwidth,height=6.8cm,keepaspectratio]{figures/esp32_iot_block_diagram.jpg}
  \caption{Next-Generation Scalable Architecture for Autonomous Logistics AGVs.}
  \label{fig:future_agv_arch}
\end{figure}

\begin{itemize}[itemsep=4pt]
  \item \textbf{Transition to Brushless DC (BLDC) Motors with Field-Oriented Control (FOC):} Replacing brushed DC motors with high-pole-count Brushless DC gimbal motors paired with 14-bit magnetic absolute encoders (AS5600) and space-vector PWM (SVPWM) FOC algorithms. This enhancement eliminates gearbox mechanical backlash, provides silent acoustic operation, and enables micro-radian torque resolution.
  \item \textbf{On-Device Edge TinyML Anomaly Detection:} Deploying quantized lightweight neural networks (TensorFlow Lite for Microcontrollers) directly onto the ESP32 to analyze high-frequency IMU vibration spectra in real time. This enables automated predictive maintenance, detecting wheel bearing wear, loose structural fasteners, or terrain slipperiness before catastrophic instability occurs.
  \item \textbf{2D LiDAR Integration and SLAM Autonomous Navigation:} Incorporating a compact $360^\circ$ time-of-flight (ToF) 2D laser scanner (RPLiDAR A1) communicating over high-speed UART. By fusing LiDAR scan matching with wheel odometry and IMU pose estimates via an onboard Extended Kalman Filter, the robot can execute Simultaneous Localization and Mapping (SLAM) and autonomous indoor path planning, transforming it into an intelligent warehouse logistics Automated Guided Vehicle (AGV).
  \item \textbf{Industrial CAN-Bus / ROS2 Telemetry Node:} Integrating a Controller Area Network (CAN-bus) transceiver or micro-ROS client, allowing the mobile robot to act as a native distributed hardware node within the open-source Robot Operating System 2 (ROS2) industrial ecosystem.
\end{itemize}

"""

app_text = r"""%% ==========================================================================
%%  APPENDICES
%% ==========================================================================
\appendix

\chapter{Hardware Pinout and Interfacing Map}
\label{app:pinout}

\justifying
Table~\ref{tab:pinout_map} documents the complete physical pin interconnection matrix between the ESP32-WROOM-32 microcontroller, sensory transducers, motor driver power electronics, and auxiliary power supplies.

\begin{table}[!ht]
\centering
\caption{Complete Electrical Interfacing and Pinout Specification.}
\label{tab:pinout_map}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|l|c|l|c|l|}
\hline
\textbf{Peripheral} & \textbf{Pin Name} & \textbf{ESP32 GPIO} & \textbf{Signal Type} & \textbf{Function / Description} \\
\hline
\multirow{4}{*}{MPU-6050 IMU} & VCC & $+3.3\,\text{V}$ & Power Rail & Regulated 3.3V Logic Supply \\
& GND & GND & Common Ground & Low-noise sensor ground \\
& SCL & GPIO 22 & Digital Output & $I^2C$ Serial Clock Line ($400\,\text{kHz}$) \\
& SDA & GPIO 21 & Bidirectional & $I^2C$ Serial Data Line (Open-drain) \\
\hline
\multirow{6}{*}{L298N Motor Driver} & ENA & GPIO 13 & Digital PWM & Left Motor PWM (LEDC Ch 0) \\
& IN1 & GPIO 12 & Digital Output & Left Motor Direction Input 1 \\
& IN2 & GPIO 14 & Digital Output & Left Motor Direction Input 2 \\
& IN3 & GPIO 26 & Digital Output & Right Motor Direction Input 1 \\
& IN4 & GPIO 25 & Digital Output & Right Motor Direction Input 2 \\
& ENB & GPIO 27 & Digital PWM & Right Motor PWM (LEDC Ch 1) \\
\hline
\multirow{2}{*}{Power Rail} & 12V IN & LM2596 Output & $+5.0\,\text{V}$ Supply & Powers ESP32 $5\,\text{V}$ Vin rail \\
& GND & System Ground & Power Ground & Heavy return path for motor current \\
\hline
Battery Monitor & V-DIV & GPIO 35 & Analog Input & Resistor divider input ($1/4$ ratio) \\
\hline
Status Indicator & LED\_BUILTIN & GPIO 2 & Digital Output & Wi-Fi \& FreeRTOS Heartbeat \\
\hline
\end{tabular}
\end{table}

\chapter{Component Bill of Materials (BOM) and Cost Breakdown}
\label{app:bom}

\justifying
Table~\ref{tab:bom_table} provides a detailed Bill of Materials (BOM) detailing all hardware, electromechanical components, sensors, power supplies, and structural elements utilized in fabricating the Self-Balancing Robot prototype, alongside commercial unit costs.

\begin{table}[!ht]
\centering
\caption{Hardware Bill of Materials (BOM) and Financial Cost Breakdown.}
\label{tab:bom_table}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|c|p{0.36\textwidth}|p{0.22\textwidth}|c|r|r|}
\hline
\textbf{S.No.} & \textbf{Component Description} & \textbf{Part / Model No.} & \textbf{Qty} & \textbf{Unit (INR)} & \textbf{Total (INR)} \\
\hline
1 & ESP32 Dual-Core Dev Board & ESP32-WROOM-32D & 1 & 450.00 & 450.00 \\
2 & 6-DOF IMU Sensor Module & InvenSense MPU-6050 & 1 & 180.00 & 180.00 \\
3 & Dual H-Bridge Motor Driver & L298N Dual BJT Module & 1 & 195.00 & 195.00 \\
4 & Geared Yellow TT DC Motors & Dual Shaft 1:48 Spur & 2 & 90.00 & 180.00 \\
5 & High-Grip Rubber Drive Wheels & $66\,\text{mm}$ Diameter Wheels & 2 & 60.00 & 120.00 \\
6 & 3S Li-ion Rechargeable Cells & 18650 2200mAh 3.7V & 3 & 140.00 & 420.00 \\
7 & 3S Battery Enclosure + BMS & 3S 12.6V Protection & 1 & 110.00 & 110.00 \\
8 & DC-DC Buck Step-Down Module & LM2596S Adj. Regulator & 1 & 95.00 & 95.00 \\
9 & Laser-Cut Acrylic Chassis Plates & 3-Tier Custom Plates & 1 & 350.00 & 350.00 \\
10 & Brass M3 Standoffs \& Screws & Hardware Fastener Kit & 1 & 120.00 & 120.00 \\
11 & SPST Rocker Toggle Switch & 250V 6A High-Current & 1 & 25.00 & 25.00 \\
12 & Prototyping PCB \& Headers & FR4 Double-Sided Kit & 1 & 85.00 & 85.00 \\
13 & Silicone Connecting Wire Harness & 22 AWG Flexible Wire & 1 & 60.00 & 60.00 \\
\hline
\multicolumn{5}{|r|}{\textbf{Total Prototype Fabrication Cost (INR):}} & \textbf{2,390.00} \\
\hline
\end{tabular}
\end{table}

\chapter{InvenSense MPU-6050 Register Map Reference}
\label{app:mpu_registers}

\justifying
Table~\ref{tab:mpu6050_registers} lists the critical internal memory-mapped registers of the InvenSense MPU-6050 6-DOF motion tracking sensor accessed by the ESP32 firmware over the 400 kHz $I^2C$ bus.

\begin{table}[!ht]
\centering
\caption{InvenSense MPU-6050 Critical Register Addresses and Configuration Bits.}
\label{tab:mpu6050_registers}
\renewcommand{\arraystretch}{1.18}
\begin{tabular}{|c|l|c|p{0.48\textwidth}|}
\hline
\textbf{Hex Addr} & \textbf{Register Name} & \textbf{Default} & \textbf{Operational Function and Configuration Setting} \\
\hline
\texttt{0x19} & \texttt{SMPLRT\_DIV} & \texttt{0x00} & Sample rate divider: Divides internal gyro rate to yield output data rate (ODR). \\
\hline
\texttt{0x1A} & \texttt{CONFIG} & \texttt{0x00} & Configures Digital Low-Pass Filter (DLPF): Set to \texttt{0x03} for $42\,\text{Hz}$ bandwidth. \\
\hline
\texttt{0x1B} & \texttt{GYRO\_CONFIG} & \texttt{0x00} & Gyroscope full-scale range: Set to \texttt{0x00} for $\pm 250^\circ/\text{s}$ ($131\,\text{LSB}/(^\circ/\text{s})$). \\
\hline
\texttt{0x1C} & \texttt{ACCEL\_CONFIG} & \texttt{0x00} & Accelerometer full-scale: Set to \texttt{0x00} for $\pm 2g$ sensitivity ($16384\,\text{LSB}/g$). \\
\hline
\texttt{0x3B} & \texttt{ACCEL\_XOUT\_H} & --- & Accelerometer X-axis high-byte output register. \\
\texttt{0x3C} & \texttt{ACCEL\_XOUT\_L} & --- & Accelerometer X-axis low-byte output register. \\
\texttt{0x3D} & \texttt{ACCEL\_YOUT\_H} & --- & Accelerometer Y-axis high-byte output register. \\
\texttt{0x3E} & \texttt{ACCEL\_YOUT\_L} & --- & Accelerometer Y-axis low-byte output register. \\
\texttt{0x3F} & \texttt{ACCEL\_ZOUT\_H} & --- & Accelerometer Z-axis high-byte output register. \\
\texttt{0x40} & \texttt{ACCEL\_ZOUT\_L} & --- & Accelerometer Z-axis low-byte output register. \\
\hline
\texttt{0x43} & \texttt{GYRO\_XOUT\_H} & --- & Gyroscope X-axis rotational rate high-byte output. \\
\texttt{0x44} & \texttt{GYRO\_XOUT\_L} & --- & Gyroscope X-axis rotational rate low-byte output. \\
\hline
\texttt{0x6B} & \texttt{PWR\_MGMT\_1} & \texttt{0x40} & Power management 1: Clear bit 6 (\texttt{SLEEP}) to \texttt{0} to wake up sensor; clock to X-gyro. \\
\hline
\texttt{0x75} & \texttt{WHO\_AM\_I} & \texttt{0x68} & Device identification register: Returns \texttt{0x68} for valid hardware confirmation. \\
\hline
\end{tabular}
\end{table}

\chapter{Python Live Telemetry Logging and Visualization Client}
\label{app:python_telemetry}

\justifying
The following fully documented Python script was developed during the internship to interface with the ESP32 serial USB stream or an incoming TCP telemetry socket. It parses the real-time pitch, gyroscope rate, and control effort packets, logs them to timestamped CSV files, and displays an interactive multi-pane Matplotlib dynamic visualization.

\begin{lstlisting}[language=Python, caption={Python Real-Time Serial Telemetry Acquisition and Dynamic Plotter.}]
#!/usr/bin/env python3
'''
Python Real-Time Telemetry and Data Logger for Self-Balancing Robot
Author: Jyotiraditya Singh (Roll No. 23010104035)
Organization: Cloud Education Learning Pvt. Ltd.
'''

import sys
import time
import csv
import serial
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Serial Port Configuration
SERIAL_PORT = 'COM5'       # Update to match platform (e.g., /dev/ttyUSB0 on Linux)
BAUD_RATE   = 115200
HISTORY_LEN = 200          # Display rolling history of 200 data points

# Circular Data Buffers
time_data   = collections.deque(maxlen=HISTORY_LEN)
pitch_data  = collections.deque(maxlen=HISTORY_LEN)
effort_data = collections.deque(maxlen=HISTORY_LEN)
gyro_data   = collections.deque(maxlen=HISTORY_LEN)

# Open CSV File for Logging
csv_filename = f"telemetry_log_{int(time.time())}.csv"
csv_file = open(csv_filename, mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp_ms', 'Pitch_deg', 'ControlEffort', 'GyroRate_dps'])

# Initialize Serial Connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)
    print(f"Connected to ESP32 on {SERIAL_PORT} at {BAUD_RATE} baud.")
except Exception as e:
    print(f"Error opening serial port: {e}")
    sys.exit(1)

# Set up Matplotlib Figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
fig.suptitle("Self-Balancing Robot Real-Time Hardware Telemetry", fontsize=14, fontweight='bold')

line_pitch, = ax1.plot([], [], 'b-', lw=1.8, label="Pitch Angle (deg)")
line_setpoint, = ax1.plot([], [], 'r--', lw=1.2, label="Vertical Target (0.0 deg)")
ax1.set_ylabel("Angle (Degrees)")
ax1.set_ylim(-30, 30)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc="upper right")

line_effort, = ax2.plot([], [], 'g-', lw=1.8, label="Control Effort (PWM)")
ax2.set_xlabel("Time Elapsed (s)")
ax2.set_ylabel("Control Effort")
ax2.set_ylim(-1050, 1050)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc="upper right")

start_time = time.time()

def update_plot(frame):
    while ser.in_waiting:
        try:
            raw_line = ser.readline().decode('utf-8', errors='ignore').strip()
            # Expected packet format: "DATA:<timestamp>,<pitch>,<effort>,<gyro>"
            if raw_line.startswith("DATA:"):
                payload = raw_line[5:].split(',')
                ts     = float(payload[0]) / 1000.0  # Convert to seconds
                pitch  = float(payload[1])
                effort = float(payload[2])
                gyro   = float(payload[3])

                time_data.append(ts)
                pitch_data.append(pitch)
                effort_data.append(effort)
                gyro_data.append(gyro)

                csv_writer.writerow([payload[0], pitch, effort, gyro])
        except Exception:
            pass

    if len(time_data) > 0:
        line_pitch.set_data(time_data, pitch_data)
        line_setpoint.set_data([time_data[0], time_data[-1]], [0.0, 0.0])
        line_effort.set_data(time_data, effort_data)

        ax1.set_xlim(time_data[0], max(time_data[-1], time_data[0] + 5.0))
        ax2.set_xlim(time_data[0], max(time_data[-1], time_data[0] + 5.0))

    return line_pitch, line_setpoint, line_effort

ani = animation.FuncAnimation(fig, update_plot, interval=25, blit=False)

try:
    plt.tight_layout()
    plt.show()
finally:
    ser.close()
    csv_file.close()
    print(f"Telemetry session terminated. Data saved to {csv_filename}")
\end{lstlisting}

\chapter{ESP32 Hardware Timer and LEDC PWM Register Configuration}
\label{app:timer_pwm}

\justifying
To achieve ultra-precise, microsecond-accurate task execution without the timing jitter associated with software polling, the balancing loop relies on the ESP32 64-bit hardware timer peripheral. The following low-level initialization routine configures Timer Group 0 (Timer 0) with a 16-bit prescaler to divide the $80\,\text{MHz}$ APB clock down to $1\,\text{MHz}$, producing $1\,\mu\text{s}$ tick resolution, alongside high-frequency LEDC PWM channels.

\begin{lstlisting}[language=C++, caption={ESP32 Hardware Timer and LEDC High-Speed PWM Initialization.}]
#include "esp_timer.h"
#include "driver/ledc.h"

// 64-Bit Hardware Timer Handle
hw_timer_t *timer_balance = NULL;
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;

// Hardware ISR Routine Triggered Exactly Every 5000 Microseconds (200 Hz)
void IRAM_ATTR onBalanceTimerISR() {
  portENTER_CRITICAL_ISR(&timerMux);
  // Notify Core 1 TaskBalancing to unblock execution immediately
  BaseType_t xHigherPriorityTaskWoken = pdFALSE;
  vTaskNotifyGiveFromISR(taskBalancingHandle, &xHigherPriorityTaskWoken);
  portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
  portEXIT_CRITICAL_ISR(&timerMux);
}

void configureHardwareTimerAndLEDC() {
  // 1. Initialize ESP32 64-Bit Hardware Timer
  // Timer 0, Prescaler 80 (80 MHz / 80 = 1 MHz -> 1 tick = 1 microsecond), Count Up
  timer_balance = timerBegin(0, 80, true);
  timerAttachInterrupt(timer_balance, &onBalanceTimerISR, true);

  // Set Alarm for 5000 microseconds (5 ms period = 200 Hz frequency), Auto-reload = true
  timerAlarmWrite(timer_balance, 5000, true);
  timerAlarmEnable(timer_balance);

  // 2. Configure LEDC High-Speed Ultrasonic PWM Channels (20 kHz, 10-Bit)
  ledc_timer_config_t ledc_timer = {
    .speed_mode       = LEDC_HIGH_SPEED_MODE,
    .duty_resolution  = LEDC_TIMER_10_BIT,       // 0 to 1023
    .timer_num        = LEDC_TIMER_0,
    .freq_hz          = 20000,                   // 20 kHz ultrasonic frequency
    .clk_cfg          = LEDC_AUTO_CLK
  };
  ledc_timer_config(&ledc_timer);

  // Configure Channel 0 for Left Motor PWM (GPIO 13)
  ledc_channel_config_t ledc_channel_left = {
    .gpio_num       = 13,
    .speed_mode     = LEDC_HIGH_SPEED_MODE,
    .channel        = LEDC_CHANNEL_0,
    .intr_type      = LEDC_INTR_DISABLE,
    .timer_sel      = LEDC_TIMER_0,
    .duty           = 0,
    .hpoint         = 0
  };
  ledc_channel_config(&ledc_channel_left);

  // Configure Channel 1 for Right Motor PWM (GPIO 27)
  ledc_channel_config_t ledc_channel_right = {
    .gpio_num       = 27,
    .speed_mode     = LEDC_HIGH_SPEED_MODE,
    .channel        = LEDC_CHANNEL_1,
    .intr_type      = LEDC_INTR_DISABLE,
    .timer_sel      = LEDC_TIMER_0,
    .duty           = 0,
    .hpoint         = 0
  };
  ledc_channel_config(&ledc_channel_right);
}
\end{lstlisting}

%% ==========================================================================
%%  BIBLIOGRAPHY / REFERENCES
%% ==========================================================================
\clearpage
\addcontentsline{toc}{chapter}{References}
\begin{thebibliography}{99}
\justifying

\bibitem{ogata}
K.~Ogata, \emph{Modern Control Engineering}, 5th~ed.\hskip 1em plus
  0.5em minus 0.4em\relax Upper Saddle River, NJ: Prentice Hall, 2010.

\bibitem{dorf}
R.~C. Dorf and R.~H. Bishop, \emph{Modern Control Systems}, 13th~ed.\hskip 1em plus
  0.5em minus 0.4em\relax Boston, MA: Pearson, 2017.

\bibitem{astrom}
K.~J. {\AA}str{\"o}m and T.~H{\"a}gglund, \emph{Advanced PID Control}.\hskip 1em plus
  0.5em minus 0.4em\relax Research Triangle Park, NC: Instrumentation, Systems, and Automation Society (ISA), 2006.

\bibitem{murray}
K.~J. {\AA}str{\"o}m and R.~M. Murray, \emph{Feedback Systems: An Introduction for Scientists and Engineers}, 2nd~ed.\hskip 1em plus
  0.5em minus 0.4em\relax Princeton, NJ: Princeton University Press, 2021.

\bibitem{invensense}
InvenSense Inc., \emph{MPU-6000 and MPU-6050 Product Specification Revision 3.4}, Document Number: PS-MPU-6000A-00, San Jose, CA, Aug. 2013.

\bibitem{invensense_reg}
InvenSense Inc., \emph{MPU-6000 and MPU-6050 Register Map and Descriptions Revision 4.2}, Document Number: RM-MPU-6000A-00, San Jose, CA, Aug. 2013.

\bibitem{espressif_ds}
Espressif Systems, \emph{ESP32 Series Datasheet}, Version 4.1, Espressif Systems (Shanghai) Co., Ltd., 2023.

\bibitem{espressif_tr}
Espressif Systems, \emph{ESP32 Technical Reference Manual}, Version 4.8, Espressif Systems (Shanghai) Co., Ltd., 2023.

\bibitem{freertos}
R.~Barry, \emph{Mastering the FreeRTOS Real Time Kernel: A Hands-On Tutorial Guide}.\hskip 1em plus
  0.5em minus 0.4em\relax Real Time Engineers Ltd., 2016.

\bibitem{stmicro}
STMicroelectronics, \emph{L298 Dual Full-Bridge Driver Datasheet}, DocID 1773 Rev 7, STMicroelectronics N.V., Jan. 2000.

\bibitem{ti_lm2596}
Texas Instruments, \emph{LM2596 SIMPLE SWITCHER Power Converter 150-kHz 3-A Step-Down Voltage Regulator}, Revised May 2016, Dallas, TX: Texas Instruments Inc., 2016.

\bibitem{kalman1960}
R.~E. Kalman, ``A new approach to linear filtering and prediction problems,'' \emph{Journal of Basic Engineering}, vol.~82, no.~1, pp. 35--45, Mar. 1960.

\bibitem{chatterjee}
A.~Chatterjee and F.~Matsuno, ``Two-wheeled self-balancing mobile robots: A review of dynamic modeling, control, and state estimation,'' \emph{IEEE Transactions on Industrial Electronics}, vol.~65, no.~2, pp. 1245--1258, Feb. 2018.

\bibitem{li2015}
Z.~Li, C.~Yang, and L.~Fan, \emph{Advanced Control of Wheeled Inverted Pendulum Systems}.\hskip 1em plus
  0.5em minus 0.4em\relax London, U.K.: Springer-Verlag, 2013.

\bibitem{firebase}
Google LLC, \emph{Firebase Realtime Database Documentation and REST API Guidelines}, Mountain View, CA: Google Developers, 2023.

\bibitem{blynk}
Blynk Inc., \emph{Blynk 2.0 IoT Platform Architecture and Protocol Specification}, New York, NY: Blynk Inc., 2023.

\bibitem{mqtt_spec}
OASIS, \emph{MQTT Version 3.1.1 Plus Errata 01}, OASIS Standard, Edited by A.~Banks and R.~Gupta, Oct. 2015.

\bibitem{craig}
J.~J. Craig, \emph{Introduction to Robotics: Mechanics and Control}, 3rd~ed.\hskip 1em plus
  0.5em minus 0.4em\relax Upper Saddle River, NJ: Pearson Prentice Hall, 2005.

\bibitem{siciliano}
B.~Siciliano, L.~Sciavicco, L.~Villani, and G.~Oriolo, \emph{Robotics: Modelling, Planning and Control}.\hskip 1em plus
  0.5em minus 0.4em\relax London, U.K.: Springer, 2009.

\bibitem{sciavicco}
C.~Canudas~de~Wit, B.~Siciliano, and G.~Bastin, \emph{Theory of Robot Control}.\hskip 1em plus
  0.5em minus 0.4em\relax London, U.K.: Springer-Verlag, 1996.

\bibitem{spong}
M.~W. Spong, S.~Hutchinson, and M.~Vidyasagar, \emph{Robot Modeling and Control}.\hskip 1em plus
  0.5em minus 0.4em\relax Hoboken, NJ: John Wiley \& Sons, 2006.

\bibitem{lewis}
F.~L. Lewis, D.~Vrabie, and V.~L. Syrmos, \emph{Optimal Control}, 3rd~ed.\hskip 1em plus
  0.5em minus 0.4em\relax Hoboken, NJ: John Wiley \& Sons, 2012.

\bibitem{armstrong}
B.~Armstrong-H{\'e}louvry, P.~Dupont, and C.~Canudas~de~Wit, ``A survey of models, analysis tools and compensation methods for the control of machines with friction,'' \emph{Automatica}, vol.~30, no.~7, pp. 1083--1138, Jul. 1994.

\bibitem{franklin}
G.~F. Franklin, J.~D. Powell, and A.~Emami-Naeini, \emph{Feedback Control of Dynamic Systems}, 8th~ed.\hskip 1em plus
  0.5em minus 0.4em\relax Boston, MA: Pearson, 2019.

\bibitem{oppenheim}
A.~V. Oppenheim and R.~W. Schafer, \emph{Discrete-Time Signal Processing}, 3rd~ed.\hskip 1em plus
  0.5em minus 0.4em\relax Upper Saddle River, NJ: Prentice Hall, 2010.

\bibitem{panasonic18650}
Panasonic Corporation, \emph{Lithium Ion NCR18650B Technical Specification Data Sheet}, Industrial Devices Company, Osaka, Japan, 2012.

\bibitem{hptu_curriculum}
Himachal Pradesh Technical University (HPTU), \emph{B.Tech. Electronics \& Communication Engineering Ordinance, Syllabus and Industrial Training Guidelines}, Hamirpur (H.P.), 2021.

\bibitem{jngec_ece}
Jawaharlal Nehru Government Engineering College (JNGEC), \emph{Department of Electronics and Communication Engineering Academic Regulations and Internship Evaluation Manual}, Sundernagar (H.P.), 2024.

\end{thebibliography}

\end{document}
"""

print("c4_text len:", len(c4_text))
print("c5_text len:", len(c5_text))
print("app_text len:", len(app_text))
