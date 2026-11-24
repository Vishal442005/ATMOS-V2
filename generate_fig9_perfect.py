import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

out_dir = r'c:\Users\Visha\Desktop\Project\manuscript_Atmos_V2\figures'
os.makedirs(out_dir, exist_ok=True)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

print("Generating Fig 9 with spacious, zero-collision layout...")

# Create figure with 2 columns: left for flowchart, right split into 2 subplots for Memory & Latency
fig = plt.figure(figsize=(13.6, 6.6), dpi=300)
gs = fig.add_gridspec(2, 2, width_ratios=[1.15, 1.0], height_ratios=[1.0, 1.0], hspace=0.38, wspace=0.28)

ax_flow = fig.add_subplot(gs[:, 0])
ax_mem  = fig.add_subplot(gs[0, 1])
ax_time = fig.add_subplot(gs[1, 1])

# ==============================================================================
# SUBPLOT (a): Firmware Execution State Flowchart
# ==============================================================================
ax_flow.set_xlim(0, 100)
ax_flow.set_ylim(0, 100)
ax_flow.axis('off')
ax_flow.set_title("(a) Deterministic Firmware Execution State Machine", fontweight="bold", fontsize=11.5, pad=12)

# Outer boundary card (B&W container)
bg_card = patches.FancyBboxPatch((1, 1), 98, 97.5, boxstyle="round,pad=0.8", ec="black", fc="#fafafa", lw=1.8, zorder=1)
ax_flow.add_patch(bg_card)

# STATE 0: RTC Wakeup
s0 = patches.FancyBboxPatch((18, 88.0), 64, 8.2, boxstyle="round,pad=0.5", ec="black", fc="white", lw=1.6, zorder=2)
ax_flow.add_patch(s0)
ax_flow.text(50, 93.0, "STATE 0: RTC TIMER WAKEUP", ha="center", va="center", fontsize=8.8, fontweight="bold", color="#1e3a8a", zorder=3)
ax_flow.text(50, 89.8, "ULP Wake Event | Enable 3.3V/5V Power Rails via GPIO", ha="center", va="center", fontsize=7.5, color="#2563eb", zorder=3)

# STATE 1: Battery Check
s1 = patches.FancyBboxPatch((18, 75.5), 64, 8.2, boxstyle="round,pad=0.5", ec="black", fc="white", lw=1.6, zorder=2)
ax_flow.add_patch(s1)
ax_flow.text(50, 80.5, "STATE 1: VOLTAGE & POWER-PATH CHECK", ha="center", va="center", fontsize=8.8, fontweight="bold", color="#9a3412", zorder=3)
ax_flow.text(50, 77.3, "Sample Vbat via 12-Bit ADC | Check Solar Load-Sharing", ha="center", va="center", fontsize=7.5, color="#c2410c", zorder=3)

# Arrow State 0 -> State 1
ax_flow.annotate("", xy=(50, 83.7), xytext=(50, 88.0), arrowprops=dict(arrowstyle="->", color="black", lw=1.8), zorder=4)

# DECISION DIAMOND
ax_flow.annotate("", xy=(50, 70.8), xytext=(50, 75.5), arrowprops=dict(arrowstyle="->", color="black", lw=1.8), zorder=4)
dec_poly = patches.Polygon([[50, 70.5], [68, 64.5], [50, 58.5], [32, 64.5]], closed=True, ec="black", fc="white", lw=1.6, zorder=2)
ax_flow.add_patch(dec_poly)
ax_flow.text(50, 65.5, "Vbat >= 3.65 V?", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#111827", zorder=3)
ax_flow.text(50, 62.5, "Battery Health Check", ha="center", va="center", fontsize=7.0, color="#4b5563", zorder=3)

# Decision Branches:
# YES branch (Down to State 2)
ax_flow.annotate("", xy=(50, 50.5), xytext=(50, 58.5), arrowprops=dict(arrowstyle="->", color="#15803d", lw=2.0), zorder=4)
ax_flow.text(51.5, 54.5, "YES: Normal Mode (T = 60 s)", ha="left", va="center", fontsize=7.5, fontweight="bold", color="#15803d",
             bbox=dict(boxstyle="round,pad=0.2", ec="#15803d", fc="#f0fdf4", lw=1.0), zorder=5)

# NO branch (Right around to State 2)
ax_flow.annotate("", xy=(68, 64.5), xytext=(78, 64.5), arrowprops=dict(arrowstyle="-", color="#dc2626", lw=1.8), zorder=4)
ax_flow.annotate("", xy=(78, 46.5), xytext=(78, 64.5), arrowprops=dict(arrowstyle="-", color="#dc2626", lw=1.8), zorder=4)
ax_flow.annotate("", xy=(70, 46.5), xytext=(78, 46.5), arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.8), zorder=4)
ax_flow.text(80.0, 56.0, "NO: Eco Mode\n(T = 180 s)", ha="left", va="center", fontsize=7.2, fontweight="bold", color="#dc2626",
             bbox=dict(boxstyle="round,pad=0.2", ec="#dc2626", fc="#fef2f2", lw=1.0), zorder=5)

# STATE 2: Sensor Sampling
s2 = patches.FancyBboxPatch((14, 42.0), 56, 8.5, boxstyle="round,pad=0.5", ec="black", fc="white", lw=1.6, zorder=2)
ax_flow.add_patch(s2)
ax_flow.text(42, 47.0, "STATE 2: SENSOR TRANSDUCTION & STABILIZATION", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#5b21b6", zorder=3)
ax_flow.text(42, 43.8, "15s PWM MOX Heater | PMS5003 Optics | SHT31 T/RH", ha="center", va="center", fontsize=7.3, color="#6d28d9", zorder=3)

# STATE 3: On-Chip GBDT
ax_flow.annotate("", xy=(42, 37.3), xytext=(42, 42.0), arrowprops=dict(arrowstyle="->", color="black", lw=1.8), zorder=4)
s3 = patches.FancyBboxPatch((14, 28.8), 56, 8.5, boxstyle="round,pad=0.5", ec="black", fc="white", lw=1.6, zorder=2)
ax_flow.add_patch(s3)
ax_flow.text(42, 33.8, "STATE 3: ON-CHIP INT8 MONOTONIC GBDT", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#065f46", zorder=3)
ax_flow.text(42, 30.6, "Inference in 1.42 ms | 72h Nocturnal Zero Re-anchoring", ha="center", va="center", fontsize=7.3, color="#047857", zorder=3)

# STATE 4: Wi-Fi MQTT Burst
ax_flow.annotate("", xy=(42, 24.1), xytext=(42, 28.8), arrowprops=dict(arrowstyle="->", color="black", lw=1.8), zorder=4)
s4 = patches.FancyBboxPatch((14, 15.6), 56, 8.5, boxstyle="round,pad=0.5", ec="black", fc="white", lw=1.6, zorder=2)
ax_flow.add_patch(s4)
ax_flow.text(42, 20.6, "STATE 4: WIRELESS MQTT TELEMETRY BURST", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#0e7490", zorder=3)
ax_flow.text(42, 17.4, "TLS 1.3 Transmission to EMQX | InfluxDB Ingestion", ha="center", va="center", fontsize=7.3, color="#0891b2", zorder=3)

# STATE 5: Deep Sleep Entry
ax_flow.annotate("", xy=(42, 10.9), xytext=(42, 15.6), arrowprops=dict(arrowstyle="->", color="black", lw=1.8), zorder=4)
s5 = patches.FancyBboxPatch((14, 2.5), 56, 8.4, boxstyle="round,pad=0.5", ec="black", fc="white", lw=1.6, zorder=2)
ax_flow.add_patch(s5)
ax_flow.text(42, 7.5, "STATE 5: TICKLESS DEEP SLEEP (15 uA)", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#374151", zorder=3)
ax_flow.text(42, 4.3, "Program RTC Alarm for (T - 16.9s) | Rails Power-Down", ha="center", va="center", fontsize=7.3, color="#4b5563", zorder=3)

# Loop back arrow (Left side: State 5 -> State 0)
ax_flow.annotate("", xy=(14, 6.7), xytext=(6, 6.7), arrowprops=dict(arrowstyle="-", color="#2563eb", lw=1.8), zorder=4)
ax_flow.annotate("", xy=(6, 92.1), xytext=(6, 6.7), arrowprops=dict(arrowstyle="-", color="#2563eb", lw=1.8), zorder=4)
ax_flow.annotate("", xy=(18, 92.1), xytext=(6, 92.1), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=1.8), zorder=4)
ax_flow.text(8.5, 50.0, "Autonomous Cycle Repeat", rotation=90, ha="center", va="center", fontsize=7.2, fontweight="bold", color="#2563eb",
             bbox=dict(boxstyle="round,pad=0.2", ec="#2563eb", fc="white", lw=1.0), zorder=5)

# ==============================================================================
# SUBPLOT (b1): Memory Utilization (SRAM & Flash)
# ==============================================================================
mem_types = ["SRAM Allocation\n(520 KB Total)", "SPI Flash Storage\n(4096 KB Total)"]
used_kb   = [28.4, 18.2]
total_kb  = [520.0, 4096.0]
used_pct  = [u / t * 100.0 for u, t in zip(used_kb, total_kb)]
free_pct  = [100.0 - p for p in used_pct]

y_pos = np.arange(len(mem_types))
bar_h = 0.42

bars_u = ax_mem.barh(y_pos, used_pct, bar_h, color="#10b981", edgecolor="black", lw=1.2, label="Allocated / In Use (%)")
bars_f = ax_mem.barh(y_pos, free_pct, bar_h, left=used_pct, color="#e2e8f0", edgecolor="black", lw=1.2, label="Free Headroom Available (%)")

ax_mem.set_yticks(y_pos)
ax_mem.set_yticklabels(mem_types, fontsize=8.8, fontweight="semibold")
ax_mem.set_xlim(0, 105)
ax_mem.set_xlabel("Hardware Memory Resource Allocation (%)", fontweight="semibold", fontsize=9.0)
ax_mem.set_title("(b) ESP32-WROOM-32D Memory Utilization", fontweight="bold", fontsize=10.5)
ax_mem.grid(True, axis="x", linestyle="--", alpha=0.5)

# Clear text callouts outside or cleanly inside bars
ax_mem.text(12.0, y_pos[0], "Used: 28.4 KB (5.5%)", va="center", ha="left", fontsize=8.0, fontweight="bold", color="#065f46",
            bbox=dict(boxstyle="round,pad=0.2", ec="#059669", fc="#ecfdf5", lw=0.9))
ax_mem.text(65.0, y_pos[0], "Free Heap: 491.6 KB (94.5%)", va="center", ha="center", fontsize=8.0, fontweight="semibold", color="#334155")

ax_mem.text(12.0, y_pos[1], "GBDT: 18.2 KB (0.44%)", va="center", ha="left", fontsize=8.0, fontweight="bold", color="#065f46",
            bbox=dict(boxstyle="round,pad=0.2", ec="#059669", fc="#ecfdf5", lw=0.9))
ax_mem.text(65.0, y_pos[1], "Available Flash: 3.98 MB (99.56%)", va="center", ha="center", fontsize=8.0, fontweight="semibold", color="#334155")

ax_mem.legend(loc="upper right", framealpha=0.9, fontsize=8.0)

# ==============================================================================
# SUBPLOT (b2): Active Cycle Execution Latency Breakdown (16.9s Total)
# ==============================================================================
tasks = [
    "MQ-135 Heater Pulse",
    "PMS5003 Optics Flow",
    "Wi-Fi / TLS / MQTT",
    "SHT31 I2C Readout",
    "INT8 GBDT Calibrator"
]
latencies_sec = [15.00, 0.80, 1.05, 0.05, 0.0014]
colors = ["#f59e0b", "#3b82f6", "#06b6d4", "#10b981", "#8b5cf6"]

y_t = np.arange(len(tasks))
bars_t = ax_time.barh(y_t, latencies_sec, height=0.52, color=colors, edgecolor="black", lw=1.2)
ax_time.set_yticks(y_t)
ax_time.set_yticklabels(tasks, fontsize=8.5, fontweight="semibold")
ax_time.invert_yaxis()
ax_time.set_xlim(0, 18.0)
ax_time.set_xlabel("Execution Time per Active Cycle (Seconds)", fontweight="semibold", fontsize=9.0)
ax_time.set_title("(c) Active Cycle Latency Breakdown ($T_{\\mathrm{active}} = 16.9\\,$s)", fontweight="bold", fontsize=10.5)
ax_time.grid(True, axis="x", linestyle="--", alpha=0.5)

labels = [
    "15.00 s (88.7% duty budget)",
    "0.80 s (4.7%)",
    "1.05 s (6.2%)",
    "0.05 s (0.3%)",
    "1.42 ms (0.0084% - Ultra-Low Edge Overhead)"
]

for bar, txt, col in zip(bars_t, labels, colors):
    w = bar.get_width()
    ax_time.text(w + 0.35, bar.get_y() + bar.get_height()/2.0, txt,
                 va="center", ha="left", fontsize=7.8, fontweight="bold", color="#1f2937")

# Adjust spacing cleanly
plt.subplots_adjust(left=0.05, right=0.97, top=0.92, bottom=0.09, hspace=0.38, wspace=0.28)
fig.savefig(os.path.join(out_dir, 'fig9_edge_firmware_state_machine.png'), dpi=300, bbox_inches='tight')
plt.close(fig)
print("Fig 9 generated successfully with zero text collisions and separated latency panels!")
