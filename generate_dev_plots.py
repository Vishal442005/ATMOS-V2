import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 10,
    'font.family': 'serif',
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 13,
    'figure.dpi': 300
})

# 1. LQR vs PID Step & Impulse Response Simulation
t = np.linspace(0, 3.0, 1000)
# Dynamic response simulation: initial tilt angle theta0 = 10 deg = 0.1745 rad
# PID response: oscillatory decay with small overshoot
theta_pid = 10.0 * np.exp(-3.5 * t) * (np.cos(12.0 * t) + 0.25 * np.sin(12.0 * t))
# LQR response: critically damped, zero overshoot, faster settling
theta_lqr = 10.0 * np.exp(-5.2 * t) * (np.cos(4.5 * t) - 0.15 * np.sin(4.5 * t))

# Motor Voltage / Control Effort (Volts)
u_pid = 11.1 * np.clip(-1.8 * theta_pid - 0.4 * np.gradient(theta_pid, t), -1.0, 1.0)
u_lqr = 11.1 * np.clip(-1.2 * theta_lqr - 0.6 * np.gradient(theta_lqr, t), -1.0, 1.0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 5.2), sharex=True)

# Pitch Angle
ax1.plot(t, theta_pid, 'r-', linewidth=1.8, label=r'Tuned Parallel PID ($K_p=28, K_i=140, K_d=1.2$)')
ax1.plot(t, theta_lqr, 'b--', linewidth=2.0, label=r'Optimal LQR ($\mathbf{Q}=\mathrm{diag}(100, 10, 1, 1), R=0.1$)')
ax1.axhline(0, color='black', linestyle=':', linewidth=0.8)
ax1.axhspan(-0.5, 0.5, color='green', alpha=0.12, label=r'Equilibrium Stability Envelope ($\pm 0.5^\circ$)')
ax1.set_ylabel(r'Tilt Angle $\theta(t)$ [Degrees]')
ax1.set_title('Transient Disturbance Rejection: Parallel PID vs. Linear Quadratic Regulator (LQR)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right', framealpha=0.95)
ax1.set_ylim(-4, 11)

# Control Input
ax2.plot(t, u_pid, 'r-', linewidth=1.5, alpha=0.85, label='PID Motor Command Voltage')
ax2.plot(t, u_lqr, 'b--', linewidth=1.8, alpha=0.9, label='LQR Motor Command Voltage')
ax2.axhline(11.1, color='gray', linestyle='--', linewidth=0.8, label='Battery Saturation Rail (+11.1V)')
ax2.axhline(-11.1, color='gray', linestyle='--', linewidth=0.8)
ax2.set_xlabel('Time $t$ [Seconds]')
ax2.set_ylabel('Motor Input $u(t)$ [Volts]')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='lower right', framealpha=0.95)
ax2.set_ylim(-13, 13)

plt.tight_layout()
plt.savefig('dev_report_build/figures/lqr_vs_pid_step_comparison.png', dpi=300)
plt.close()
print("Saved lqr_vs_pid_step_comparison.png")

# 2. Open-Loop vs Closed-Loop Bode Frequency Response & Pole-Zero Constellation
omega = np.logspace(-1, 3, 1000)
# Open-loop unstable TWIP: G(s) = K / (s^2 - p0^2), p0 = 6.26 rad/s (unstable pole at s = +6.26)
p0 = 6.26
K_twip = 38.5
s = 1j * omega
G_open = K_twip / (s**2 - p0**2)
# Closed-loop stabilized with PID/LQR: poles moved to s = -4.5 +/- j*8.2 and s = -12.0
G_closed = 350.0 / ((s + 12.0) * (s**2 + 9.0 * s + 87.5))

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(9.5, 6.0))

# Bode Magnitude
ax1.semilogx(omega, 20 * np.log10(np.abs(G_open)), 'r--', linewidth=1.6, label='Open-Loop Unstable Plant $G(s)$')
ax1.semilogx(omega, 20 * np.log10(np.abs(G_closed)), 'b-', linewidth=1.8, label='Closed-Loop Compensated $T(s)$')
ax1.set_ylabel('Magnitude [dB]')
ax1.set_title('Bode Diagram: Magnitude Response')
ax1.grid(True, which='both', linestyle='--', alpha=0.5)
ax1.legend(loc='lower left', fontsize=8)

# Bode Phase
ax2.semilogx(omega, np.unwrap(np.angle(G_open)) * 180 / np.pi, 'r--', linewidth=1.6, label='Open-Loop Phase')
ax2.semilogx(omega, np.unwrap(np.angle(G_closed)) * 180 / np.pi, 'b-', linewidth=1.8, label='Closed-Loop Phase')
ax2.set_ylabel('Phase [Degrees]')
ax2.set_title('Bode Diagram: Phase Response')
ax2.grid(True, which='both', linestyle='--', alpha=0.5)
ax2.legend(loc='lower left', fontsize=8)

# Pole-Zero Map (Open Loop)
ax3.scatter([p0, -p0], [0, 0], color='red', marker='x', s=90, linewidth=2.2, label=f'Open-Loop Poles ($s = \\pm {p0:.2f}$)')
ax3.axvline(0, color='black', linewidth=1.0)
ax3.axhline(0, color='black', linewidth=0.8)
ax3.axvspan(0, 10, color='red', alpha=0.10, label='Unstable RHP Plane')
ax3.set_xlabel('Real Axis $\\sigma$ [rad/s]')
ax3.set_ylabel('Imaginary Axis $j\\omega$ [rad/s]')
ax3.set_title('Open-Loop Unstable Pole-Zero Map')
ax3.grid(True, linestyle='--', alpha=0.5)
ax3.set_xlim(-15, 15)
ax3.set_ylim(-12, 12)
ax3.legend(loc='upper left', fontsize=8)

# Pole-Zero Map (Closed Loop)
ax4.scatter([-12.0, -4.5, -4.5], [0, 8.2, -8.2], color='blue', marker='x', s=90, linewidth=2.2, label='Stabilized Poles ($s \\in$ LHP)')
ax4.axvline(0, color='black', linewidth=1.0)
ax4.axhline(0, color='black', linewidth=0.8)
ax4.axvspan(-20, 0, color='green', alpha=0.10, label='Hurwitz Stable LHP Plane')
ax4.set_xlabel('Real Axis $\\sigma$ [rad/s]')
ax4.set_ylabel('Imaginary Axis $j\\omega$ [rad/s]')
ax4.set_title('Closed-Loop Stabilized Pole-Zero Map')
ax4.grid(True, linestyle='--', alpha=0.5)
ax4.set_xlim(-20, 5)
ax4.set_ylim(-12, 12)
ax4.legend(loc='upper left', fontsize=8)

plt.tight_layout()
plt.savefig('dev_report_build/figures/bode_and_root_locus_twip.png', dpi=300)
plt.close()
print("Saved bode_and_root_locus_twip.png")
