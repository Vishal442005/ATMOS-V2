import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageOps
import numpy as np
import os

out_dir = r'c:\Users\Visha\Desktop\Project\manuscript_Atmos_V2\figures'
img_dir = r'c:\Users\Visha\Desktop\Project\atmos_figures'
os.makedirs(out_dir, exist_ok=True)

# Typography settings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['font.size'] = 9.5
plt.rcParams['axes.linewidth'] = 1.2

print("Generating Fig 1 with small hardware images and high visual clarity...")
fig, ax = plt.subplots(figsize=(12.5, 6.6), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Helper function to place framed thumbnail images
def place_image(path, x, y, w, h, border_color="#334155"):
    try:
        im = Image.open(path)
        # Add subtle frame
        ax.imshow(im, extent=[x, x + w, y, y + h], zorder=4, aspect='auto')
        rect = patches.Rectangle((x, y), w, h, linewidth=1.2, edgecolor=border_color, facecolor='none', zorder=5)
        ax.add_patch(rect)
    except Exception as e:
        print(f"Error loading {path}: {e}")

# ==============================================================================
# 1. MAIN DOMAIN CONTAINER BOXES (Black & White outer boxes, ec='black', fc='white')
# ==============================================================================
# Domain 1: Sensing Transducers (Top Left)
card_sens = patches.FancyBboxPatch((2, 49.5), 28, 48, boxstyle="round,pad=0.8", ec="black", fc="white", lw=2.2, zorder=1)
# Domain 2: Energy Harvesting & Power Management (Bottom Left)
card_pwr  = patches.FancyBboxPatch((2, 2.5),  28, 44.5, boxstyle="round,pad=0.8", ec="black", fc="white", lw=2.2, zorder=1)
# Domain 3: Edge Computing Core (Center)
card_mcu  = patches.FancyBboxPatch((34.5, 2.5), 32.5, 95, boxstyle="round,pad=0.8", ec="black", fc="white", lw=2.2, zorder=1)
# Domain 4: Cloud & AI Analytics (Right)
card_cld  = patches.FancyBboxPatch((71, 2.5), 27.5, 95, boxstyle="round,pad=0.8", ec="black", fc="white", lw=2.2, zorder=1)

for c in [card_sens, card_pwr, card_mcu, card_cld]:
    ax.add_patch(c)

# ==============================================================================
# 2. DOMAIN HEADERS
# ==============================================================================
# Sensing Header
ax.text(16, 95.0, "SENSING TRANSDUCERS", ha="center", va="center", fontsize=11, fontweight="bold", color="#1e3a8a", zorder=3)
ax.plot([4, 28], [92.5, 92.5], color="#cbd5e1", lw=1.2, zorder=3)

# Power Header
ax.text(16, 44.0, "ENERGY HARVESTING & POWER", ha="center", va="center", fontsize=10.5, fontweight="bold", color="#9a3412", zorder=3)
ax.plot([4, 28], [41.5, 41.5], color="#cbd5e1", lw=1.2, zorder=3)

# Edge Core Header
ax.text(50.7, 95.0, "EDGE COMPUTING CORE", ha="center", va="center", fontsize=11.5, fontweight="bold", color="#065f46", zorder=3)
ax.text(50.7, 92.0, "ESP32-WROOM-32D (Dual-Core 240 MHz)", ha="center", va="center", fontsize=8.5, color="#047857", fontweight="semibold", zorder=3)
ax.plot([36.5, 65], [89.5, 89.5], color="#cbd5e1", lw=1.2, zorder=3)

# Cloud Header
ax.text(84.7, 95.0, "CLOUD & AI PLATFORM", ha="center", va="center", fontsize=11.5, fontweight="bold", color="#5b21b6", zorder=3)
ax.text(84.7, 92.0, "Real-Time Ingestion & Sequence AI", ha="center", va="center", fontsize=8.5, color="#6d28d9", fontweight="semibold", zorder=3)
ax.plot([73, 96.5], [89.5, 89.5], color="#cbd5e1", lw=1.2, zorder=3)

# ==============================================================================
# 3. SENSING ENGINE COMPONENTS (With Small Hardware Images)
# ==============================================================================
# (a) PMS5003
b_pms = patches.FancyBboxPatch((3.5, 78.5), 25, 12.5, boxstyle="round,pad=0.4", ec="#2563eb", fc="#eff6ff", lw=1.3, zorder=2)
ax.add_patch(b_pms)
place_image(os.path.join(img_dir, 'page_20_09_Image171.jpg'), 4.2, 79.5, 5.8, 10.5, border_color="#2563eb")
ax.text(10.8, 88.0, "Plantower PMS5003", fontsize=9.0, fontweight="bold", color="#1e40af", zorder=3)
ax.text(10.8, 84.5, "Laser Mie Scattering ($90^\\circ$)", fontsize=7.8, color="#1e3a8a", zorder=3)
ax.text(10.8, 81.5, "PM1.0, PM2.5, PM10 (UART)", fontsize=7.5, color="#2563eb", fontweight="semibold", zorder=3)

# (b) MQ-135
b_mq = patches.FancyBboxPatch((3.5, 64.5), 25, 12.5, boxstyle="round,pad=0.4", ec="#7c3aed", fc="#f5f3ff", lw=1.3, zorder=2)
ax.add_patch(b_mq)
place_image(os.path.join(img_dir, 'page_18_06_Image166.jpg'), 4.2, 65.5, 5.8, 10.5, border_color="#7c3aed")
ax.text(10.8, 74.0, "Winsen MQ-135 Gas", fontsize=9.0, fontweight="bold", color="#5b21b6", zorder=3)
ax.text(10.8, 70.5, "SnO2 Chemoresistive Film", fontsize=7.8, color="#6d28d9", zorder=3)
ax.text(10.8, 67.5, "15s Dynamic PWM Pulse (ADC)", fontsize=7.5, color="#7c3aed", fontweight="semibold", zorder=3)

# (c) SHT31-DIS (Vector illustration of Thermo-Hygrometer)
b_sht = patches.FancyBboxPatch((3.5, 51.0), 25, 12.0, boxstyle="round,pad=0.4", ec="#0d9488", fc="#f0fdfa", lw=1.3, zorder=2)
ax.add_patch(b_sht)
# Miniature vector icon for SHT31
sht_icon_box = patches.Rectangle((4.2, 52.0), 5.8, 10.0, facecolor="#ccfbf1", edgecolor="#0d9488", lw=1.2, zorder=3)
ax.add_patch(sht_icon_box)
# Thermometer stem & bulb
ax.plot([6.2, 6.2], [54.5, 59.5], color="#ef4444", lw=2.5, zorder=4)
ax.add_patch(patches.Circle((6.2, 53.8), 0.8, color="#ef4444", zorder=4))
# Droplet icon for humidity
ax.add_patch(patches.Circle((8.0, 56.5), 0.7, color="#0284c7", zorder=4))
ax.text(7.1, 52.6, "T/RH", fontsize=6.0, fontweight="bold", color="#0f766e", ha="center", zorder=4)

ax.text(10.8, 60.0, "Sensirion SHT31-DIS", fontsize=9.0, fontweight="bold", color="#0f766e", zorder=3)
ax.text(10.8, 56.5, "Temp (+-0.2 C) & RH (+-2%)", fontsize=7.8, color="#115e59", zorder=3)
ax.text(10.8, 53.5, "I2C Fast-Mode (400 kHz)", fontsize=7.5, color="#0d9488", fontweight="semibold", zorder=3)

# ==============================================================================
# 4. ENERGY HARVESTING COMPONENTS (With Small Hardware Images)
# ==============================================================================
# (a) Solar PV Panel
b_pv = patches.FancyBboxPatch((3.5, 29.5), 25, 11.0, boxstyle="round,pad=0.4", ec="#d97706", fc="#fffbeb", lw=1.3, zorder=2)
ax.add_patch(b_pv)
place_image(os.path.join(img_dir, 'page_23_14_Image179.jpg'), 4.2, 30.5, 6.0, 9.0, border_color="#d97706")
ax.text(11.0, 37.5, "2.0 W Monocrystalline PV", fontsize=8.8, fontweight="bold", color="#b45309", zorder=3)
ax.text(11.0, 34.2, "6.0 V Voc | 330 mA Isc", fontsize=7.8, color="#d97706", zorder=3)
ax.text(11.0, 31.5, "Solar Micro-Grid Ingestion", fontsize=7.5, color="#b45309", fontweight="semibold", zorder=3)

# (b) TP4056 + Power-Path
b_pmic = patches.FancyBboxPatch((3.5, 16.5), 25, 11.5, boxstyle="round,pad=0.4", ec="#ea580c", fc="#fff7ed", lw=1.3, zorder=2)
ax.add_patch(b_pmic)
place_image(os.path.join(img_dir, 'page_24_15_Image181.jpg'), 4.2, 17.5, 6.0, 9.5, border_color="#ea580c")
ax.text(11.0, 25.0, "TP4056 + Load-Sharing", fontsize=8.8, fontweight="bold", color="#c2410c", zorder=3)
ax.text(11.0, 21.8, "AO3401A P-MOS + SS34 Diode", fontsize=7.8, color="#9a3412", zorder=3)
ax.text(11.0, 19.0, "C/10 (33 mA) Safe Cut-off", fontsize=7.5, color="#ea580c", fontweight="semibold", zorder=3)

# (c) 18650 Battery Pack & Regulators
b_bat = patches.FancyBboxPatch((3.5, 4.0), 25, 11.0, boxstyle="round,pad=0.4", ec="#16a34a", fc="#f0fdf4", lw=1.3, zorder=2)
ax.add_patch(b_bat)
place_image(os.path.join(img_dir, 'page_22_13_Image177.jpg'), 4.2, 4.8, 6.0, 9.2, border_color="#16a34a")
ax.text(11.0, 12.2, "18650 Li-ion (3.7 V)", fontsize=8.8, fontweight="bold", color="#15803d", zorder=3)
ax.text(11.0, 9.2, "2600 mAh Protected Cell", fontsize=7.8, color="#16a34a", zorder=3)
ax.text(11.0, 6.5, "MT3608 5V & TPS63020 3.3V", fontsize=7.5, color="#15803d", fontweight="semibold", zorder=3)

# ==============================================================================
# 5. EDGE COMPUTING CORE (ESP32) (With MCU Image & Architectural Blocks)
# ==============================================================================
# ESP32 Physical Board Image & Info Card
b_mcu_card = patches.FancyBboxPatch((36.0, 72.0), 29.5, 16.0, boxstyle="round,pad=0.5", ec="#059669", fc="#ecfdf5", lw=1.5, zorder=2)
ax.add_patch(b_mcu_card)
place_image(os.path.join(img_dir, 'page_17_05_Image164.jpg'), 37.0, 73.2, 7.5, 13.5, border_color="#059669")
ax.text(46.0, 84.5, "ESP32 Embedded SoC", fontsize=10.0, fontweight="bold", color="#065f46", zorder=3)
ax.text(46.0, 80.5, "Xtensa Dual-Core 32-bit LX6", fontsize=8.2, color="#047857", zorder=3)
ax.text(46.0, 77.0, "520 KB SRAM | 4 MB SPI Flash", fontsize=8.0, color="#065f46", zorder=3)
ax.text(46.0, 74.0, "FreeRTOS Tickless Low-Power Kernel", fontsize=7.8, color="#059669", fontweight="semibold", zorder=3)

# On-Chip GBDT Calibrator Box
b_gbdt = patches.FancyBboxPatch((36.0, 54.5), 29.5, 15.5, boxstyle="round,pad=0.5", ec="#0d9488", fc="#f0fdfa", lw=1.4, zorder=2)
ax.add_patch(b_gbdt)
# Miniature Tree Graphic on left
ax.plot([38.5, 37.5, 39.5], [66.0, 63.5, 63.5], color="#0d9488", lw=1.5, zorder=4)
ax.plot([37.5, 37.0, 38.0], [63.5, 61.0, 61.0], color="#0d9488", lw=1.2, zorder=4)
ax.plot([39.5, 39.0, 40.0], [63.5, 61.0, 61.0], color="#0d9488", lw=1.2, zorder=4)
ax.add_patch(patches.Circle((38.5, 66.0), 0.45, color="#0d9488", zorder=5))
ax.add_patch(patches.Circle((37.5, 63.5), 0.35, color="#0d9488", zorder=5))
ax.add_patch(patches.Circle((39.5, 63.5), 0.35, color="#0d9488", zorder=5))

ax.text(42.0, 66.5, "On-Chip INT8 Monotonic GBDT", fontsize=9.2, fontweight="bold", color="#0f766e", zorder=3)
ax.text(42.0, 63.0, "Physics-Guided Monotonic Trees", fontsize=8.0, color="#115e59", zorder=3)
ax.text(42.0, 59.5, "Aerosol Deliquescence Compensation", fontsize=7.8, color="#0f766e", zorder=3)
ax.text(42.0, 56.5, "Flash: 18.2 KB | Latency: 1.42 ms", fontsize=7.8, color="#0d9488", fontweight="bold", zorder=3)

# 72h Sliding Nocturnal Baseline Filter Box
b_drift = patches.FancyBboxPatch((36.0, 37.5), 29.5, 15.0, boxstyle="round,pad=0.5", ec="#0891b2", fc="#ecfeff", lw=1.4, zorder=2)
ax.add_patch(b_drift)
# Miniature Waveform on left
w_t = np.linspace(37.0, 40.5, 30)
w_y = 44.5 + 1.2 * np.sin(np.linspace(0, 3*np.pi, 30))
ax.plot(w_t, w_y, color="#0891b2", lw=1.6, zorder=4)
ax.axhline(44.5, xmin=0.37, xmax=0.405, color="#ef4444", linestyle="--", lw=1.0, zorder=4)

ax.text(42.0, 49.0, "72h Nocturnal Baseline Filter", fontsize=9.2, fontweight="bold", color="#0e7490", zorder=3)
ax.text(42.0, 45.5, "Zero-Point Dynamic Envelope Tracking", fontsize=7.8, color="#155e75", zorder=3)
ax.text(42.0, 42.5, "180-Day Optical Fouling Re-anchoring", fontsize=7.8, color="#0e7490", zorder=3)
ax.text(42.0, 39.5, "Adaptive 60s / 180s Duty Cycler", fontsize=7.8, color="#0891b2", fontweight="bold", zorder=3)

# Hardware Drivers & Power States
b_drv = patches.FancyBboxPatch((36.0, 4.5), 29.5, 31.0, boxstyle="round,pad=0.5", ec="#4f46e5", fc="#eef2ff", lw=1.4, zorder=2)
ax.add_patch(b_drv)
ax.text(50.7, 32.5, "HARDWARE DRIVERS & POWER STATES", ha="center", fontsize=9.0, fontweight="bold", color="#3730a3", zorder=3)
ax.text(50.7, 28.5, "• 12-Bit SAR ADC (MQ-135 Sampling)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(50.7, 25.0, "• Fast-Mode I2C Master (SHT31 T/RH)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(50.7, 21.5, "• UART2 Controller (PMS5003 Stream)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(50.7, 18.0, "• 20 kHz Hardware PWM (15s Heater Ramp)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(50.7, 14.0, "• Wi-Fi 802.11 b/g/n (2.4 GHz TX Burst)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(50.7, 9.5, "Power States: Sleep (15uA) -> Heat (265mA)", ha="center", fontsize=7.5, color="#3730a3", fontweight="semibold", zorder=3)
ax.text(50.7, 6.5, "Active Optics (280mA) -> Wi-Fi Burst (125mA)", ha="center", fontsize=7.5, color="#3730a3", fontweight="semibold", zorder=3)

# ==============================================================================
# 6. CLOUD & AI ANALYTICS PLATFORM (With Dashboard Image & AI Blocks)
# ==============================================================================
# Cloud Dashboard Viewport Image
b_dash_frame = patches.FancyBboxPatch((72.5, 68.0), 24.5, 20.0, boxstyle="round,pad=0.5", ec="#5b21b6", fc="#f5f3ff", lw=1.4, zorder=2)
ax.add_patch(b_dash_frame)
place_image(os.path.join(img_dir, 'page_37_24_Image208.png'), 73.5, 69.2, 11.5, 17.5, border_color="#5b21b6")
ax.text(86.0, 84.5, "Grafana Live UI", fontsize=9.5, fontweight="bold", color="#5b21b6", zorder=3)
ax.text(86.0, 80.5, "Real-Time Telemetry", fontsize=8.0, color="#6d28d9", zorder=3)
ax.text(86.0, 76.5, "Interactive GIS Map", fontsize=8.0, color="#6d28d9", zorder=3)
ax.text(86.0, 72.5, "Public Health Alerts", fontsize=8.0, color="#7c3aed", fontweight="semibold", zorder=3)

# MQTT Broker & Database Box
b_mqtt = patches.FancyBboxPatch((72.5, 50.5), 24.5, 15.5, boxstyle="round,pad=0.5", ec="#6366f1", fc="#eef2ff", lw=1.4, zorder=2)
ax.add_patch(b_mqtt)
ax.text(84.7, 62.5, "MQTT Ingestion & Storage", ha="center", fontsize=9.2, fontweight="bold", color="#3730a3", zorder=3)
ax.text(84.7, 58.5, "EMQX Ingestion Broker (TLS 1.3)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(84.7, 55.0, "InfluxDB Time-Series Engine", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(84.7, 52.0, "Synchronous Microclimate Log", ha="center", fontsize=7.5, color="#6366f1", fontweight="semibold", zorder=3)

# BiLSTM Sequence Forecaster Box
b_bilstm = patches.FancyBboxPatch((72.5, 27.0), 24.5, 21.5, boxstyle="round,pad=0.5", ec="#8b5cf6", fc="#f5f3ff", lw=1.5, zorder=2)
ax.add_patch(b_bilstm)
ax.text(84.7, 44.5, "BiLSTM-LSTM Forecaster", ha="center", fontsize=9.5, fontweight="bold", color="#5b21b6", zorder=3)
ax.text(84.7, 40.5, "Bidirectional Encoder (2x128)", ha="center", fontsize=8.0, color="#6d28d9", zorder=3)
ax.text(84.7, 37.0, "Temporal Attention Context Head", ha="center", fontsize=8.0, color="#6d28d9", zorder=3)
ax.text(84.7, 33.5, "Multi-Horizon (t+1h to t+24h)", ha="center", fontsize=8.0, color="#7c3aed", fontweight="bold", zorder=3)
ax.text(84.7, 30.0, "90% Conformal Prediction Bands", ha="center", fontsize=7.8, color="#8b5cf6", fontweight="bold", zorder=3)

# Explainability & Decision Support Box
b_shap = patches.FancyBboxPatch((72.5, 4.5), 24.5, 20.5, boxstyle="round,pad=0.5", ec="#0284c7", fc="#f0f9ff", lw=1.4, zorder=2)
ax.add_patch(b_shap)
ax.text(84.7, 21.5, "SHAP & Decision Engine", ha="center", fontsize=9.2, fontweight="bold", color="#0369a1", zorder=3)
ax.text(84.7, 17.5, "TreeSHAP Global Attribution", ha="center", fontsize=7.8, color="#0284c7", zorder=3)
ax.text(84.7, 14.0, "Feature Dependency Verification", ha="center", fontsize=7.8, color="#0284c7", zorder=3)
ax.text(84.7, 10.5, "Episodic Plume Detection", ha="center", fontsize=7.8, color="#0ea5e9", zorder=3)
ax.text(84.7, 7.0, "Automated Public Health Triggers", ha="center", fontsize=7.5, color="#0369a1", fontweight="semibold", zorder=3)

# ==============================================================================
# 7. HIGH-CONTRAST INTERCONNECT ARROWS WITH PROTOCOL BADGES
# ==============================================================================
# PMS5003 -> ESP32 (UART)
ax.annotate("", xy=(34.5, 84.5), xytext=(28.5, 84.5), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=2.4), zorder=6)
ax.text(31.5, 86.8, "UART", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#2563eb", 
        bbox=dict(boxstyle="round,pad=0.2", ec="#2563eb", fc="white", lw=1.0), zorder=7)

# MQ-135 -> ESP32 (ADC / PWM)
ax.annotate("", xy=(34.5, 70.5), xytext=(28.5, 70.5), arrowprops=dict(arrowstyle="->", color="#7c3aed", lw=2.4), zorder=6)
ax.text(31.5, 72.8, "ADC", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#7c3aed",
        bbox=dict(boxstyle="round,pad=0.2", ec="#7c3aed", fc="white", lw=1.0), zorder=7)

# SHT31 -> ESP32 (I2C)
ax.annotate("", xy=(34.5, 57.0), xytext=(28.5, 57.0), arrowprops=dict(arrowstyle="->", color="#0d9488", lw=2.4), zorder=6)
ax.text(31.5, 59.3, "I2C", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#0d9488",
        bbox=dict(boxstyle="round,pad=0.2", ec="#0d9488", fc="white", lw=1.0), zorder=7)

# Power Subsystem -> ESP32 & Sensors (Power Rails)
ax.annotate("", xy=(34.5, 20.0), xytext=(28.5, 20.0), arrowprops=dict(arrowstyle="->", color="#ea580c", lw=2.4), zorder=6)
ax.text(31.5, 22.3, "3.3V/5V", ha="center", va="center", fontsize=7.2, fontweight="bold", color="#ea580c",
        bbox=dict(boxstyle="round,pad=0.2", ec="#ea580c", fc="white", lw=1.0), zorder=7)

# ESP32 -> Cloud (Wi-Fi / MQTT)
ax.annotate("", xy=(71.0, 58.0), xytext=(67.0, 58.0), arrowprops=dict(arrowstyle="->", color="#059669", lw=2.6), zorder=6)
ax.text(69.0, 61.0, "Wi-Fi\nMQTT", ha="center", va="center", fontsize=7.8, fontweight="bold", color="#059669",
        bbox=dict(boxstyle="round,pad=0.2", ec="#059669", fc="white", lw=1.0), zorder=7)

plt.tight_layout()
out_path = os.path.join(out_dir, 'fig1_system_architecture.png')
fig.savefig(out_path, dpi=300, bbox_inches='tight')
plt.close(fig)
print(f"Fig 1 with small hardware images generated and saved to {out_path} successfully!")
