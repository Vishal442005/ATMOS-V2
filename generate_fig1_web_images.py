import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os

out_dir = r'c:\Users\Visha\Desktop\Project\manuscript_Atmos_V2\figures'
web_prep_dir = r'c:\Users\Visha\Desktop\Project\web_component_images\prepared'
os.makedirs(out_dir, exist_ok=True)

# Typography styling
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def place_image(ax, path, x, y, w, h, border_color="#334155", lw=1.2):
    try:
        im = Image.open(path)
        ax.imshow(im, extent=[x, x + w, y, y + h], zorder=4, aspect='auto')
        rect = patches.Rectangle((x, y), w, h, linewidth=lw, edgecolor=border_color, facecolor='none', zorder=5)
        ax.add_patch(rect)
    except Exception as e:
        print(f"Error loading {path}: {e}")

print("Generating Fig 1 with authentic WEB-DOWNLOADED component images...")
fig, ax = plt.subplots(figsize=(13.2, 6.8), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# 1. Main Container Cards (B&W boxes with crisp black borders)
card_sens = patches.FancyBboxPatch((2, 50.5), 28.5, 47.0, boxstyle="round,pad=0.8", ec="black", fc="white", lw=2.2, zorder=1)
card_pwr  = patches.FancyBboxPatch((2, 2.5), 28.5, 44.5, boxstyle="round,pad=0.8", ec="black", fc="white", lw=2.2, zorder=1)
card_mcu  = patches.FancyBboxPatch((35.0, 2.5), 32.5, 95.0, boxstyle="round,pad=0.8", ec="black", fc="white", lw=2.2, zorder=1)
card_cld  = patches.FancyBboxPatch((71.5, 2.5), 27.0, 95.0, boxstyle="round,pad=0.8", ec="black", fc="white", lw=2.2, zorder=1)

for c in [card_sens, card_pwr, card_mcu, card_cld]:
    ax.add_patch(c)

# 2. Section Headers
ax.text(16.25, 95.2, "SENSING TRANSDUCERS", ha="center", va="center", fontsize=11, fontweight="bold", color="#1e3a8a", zorder=3)
ax.plot([4, 28.5], [92.6, 92.6], color="#cbd5e1", lw=1.2, zorder=3)

ax.text(16.25, 44.2, "ENERGY HARVESTING & POWER", ha="center", va="center", fontsize=10.5, fontweight="bold", color="#9a3412", zorder=3)
ax.plot([4, 28.5], [41.6, 41.6], color="#cbd5e1", lw=1.2, zorder=3)

ax.text(51.25, 95.2, "EDGE COMPUTING CORE", ha="center", va="center", fontsize=11.5, fontweight="bold", color="#065f46", zorder=3)
ax.text(51.25, 92.2, "ESP32-WROOM-32D (Dual-Core 240 MHz)", ha="center", va="center", fontsize=8.5, color="#047857", fontweight="semibold", zorder=3)
ax.plot([37, 65.5], [89.6, 89.6], color="#cbd5e1", lw=1.2, zorder=3)

ax.text(85.0, 95.2, "CLOUD & AI PLATFORM", ha="center", va="center", fontsize=11.5, fontweight="bold", color="#5b21b6", zorder=3)
ax.text(85.0, 92.2, "Real-Time Ingestion & Sequence AI", ha="center", va="center", fontsize=8.5, color="#6d28d9", fontweight="semibold", zorder=3)
ax.plot([73.5, 96.5], [89.6, 89.6], color="#cbd5e1", lw=1.2, zorder=3)

# 3. SENSING COMPONENTS (with Web-downloaded images)
# (a) Plantower PMS5003
b_pms = patches.FancyBboxPatch((3.5, 78.5), 25.5, 12.5, boxstyle="round,pad=0.4", ec="#2563eb", fc="#eff6ff", lw=1.3, zorder=2)
ax.add_patch(b_pms)
place_image(ax, os.path.join(web_prep_dir, 'pms5003.png'), 4.2, 79.5, 6.0, 10.5, border_color="#2563eb")
ax.text(11.0, 88.0, "Plantower PMS5003", fontsize=9.0, fontweight="bold", color="#1e40af", zorder=3)
ax.text(11.0, 84.5, "Laser Mie Scattering ($90^\\circ$)", fontsize=7.8, color="#1e3a8a", zorder=3)
ax.text(11.0, 81.5, "PM1.0, PM2.5, PM10 (UART)", fontsize=7.5, color="#2563eb", fontweight="semibold", zorder=3)

# (b) Winsen MQ-135
b_mq = patches.FancyBboxPatch((3.5, 64.5), 25.5, 12.5, boxstyle="round,pad=0.4", ec="#7c3aed", fc="#f5f3ff", lw=1.3, zorder=2)
ax.add_patch(b_mq)
place_image(ax, os.path.join(web_prep_dir, 'mq135.png'), 4.2, 65.5, 6.0, 10.5, border_color="#7c3aed")
ax.text(11.0, 74.0, "Winsen MQ-135 Gas", fontsize=9.0, fontweight="bold", color="#5b21b6", zorder=3)
ax.text(11.0, 70.5, "SnO2 Chemoresistive Film", fontsize=7.8, color="#6d28d9", zorder=3)
ax.text(11.0, 67.5, "15s Dynamic PWM Pulse (ADC)", fontsize=7.5, color="#7c3aed", fontweight="semibold", zorder=3)

# (c) Sensirion SHT31-DIS
b_sht = patches.FancyBboxPatch((3.5, 51.0), 25.5, 12.0, boxstyle="round,pad=0.4", ec="#0d9488", fc="#f0fdfa", lw=1.3, zorder=2)
ax.add_patch(b_sht)
place_image(ax, os.path.join(web_prep_dir, 'sht31.png'), 4.2, 52.0, 6.0, 10.0, border_color="#0d9488")
ax.text(11.0, 60.0, "Sensirion SHT31-DIS", fontsize=9.0, fontweight="bold", color="#0f766e", zorder=3)
ax.text(11.0, 56.5, "Temp (+-0.2 C) & RH (+-2%)", fontsize=7.8, color="#115e59", zorder=3)
ax.text(11.0, 53.5, "I2C Fast-Mode (400 kHz)", fontsize=7.5, color="#0d9488", fontweight="semibold", zorder=3)

# 4. POWER COMPONENTS (with Web-downloaded images)
# (a) Solar Panel
b_pv = patches.FancyBboxPatch((3.5, 29.5), 25.5, 11.0, boxstyle="round,pad=0.4", ec="#d97706", fc="#fffbeb", lw=1.3, zorder=2)
ax.add_patch(b_pv)
place_image(ax, os.path.join(web_prep_dir, 'solar_panel.png'), 4.2, 30.2, 6.0, 9.5, border_color="#d97706")
ax.text(11.0, 37.5, "2.0 W Monocrystalline PV", fontsize=8.8, fontweight="bold", color="#b45309", zorder=3)
ax.text(11.0, 34.2, "6.0 V Voc | 330 mA Isc", fontsize=7.8, color="#d97706", zorder=3)
ax.text(11.0, 31.5, "Solar Micro-Grid Ingestion", fontsize=7.5, color="#b45309", fontweight="semibold", zorder=3)

# (b) TP4056 PMIC
b_pmic = patches.FancyBboxPatch((3.5, 16.5), 25.5, 11.5, boxstyle="round,pad=0.4", ec="#ea580c", fc="#fff7ed", lw=1.3, zorder=2)
ax.add_patch(b_pmic)
place_image(ax, os.path.join(web_prep_dir, 'tp4056.png'), 4.2, 17.5, 6.0, 9.5, border_color="#ea580c")
ax.text(11.0, 25.0, "TP4056 + Load-Sharing", fontsize=8.8, fontweight="bold", color="#c2410c", zorder=3)
ax.text(11.0, 21.8, "AO3401A P-MOS + SS34 Diode", fontsize=7.8, color="#9a3412", zorder=3)
ax.text(11.0, 19.0, "C/10 (33 mA) Safe Cut-off", fontsize=7.5, color="#ea580c", fontweight="semibold", zorder=3)

# (c) 18650 Battery Cell
b_bat = patches.FancyBboxPatch((3.5, 4.0), 25.5, 11.0, boxstyle="round,pad=0.4", ec="#16a34a", fc="#f0fdf4", lw=1.3, zorder=2)
ax.add_patch(b_bat)
place_image(ax, os.path.join(web_prep_dir, 'battery_18650.png'), 4.2, 4.8, 6.0, 9.2, border_color="#16a34a")
ax.text(11.0, 12.2, "18650 Li-ion (3.7 V)", fontsize=8.8, fontweight="bold", color="#15803d", zorder=3)
ax.text(11.0, 9.2, "2600 mAh Protected Cell", fontsize=7.8, color="#16a34a", zorder=3)
ax.text(11.0, 6.5, "MT3608 5V & TPS63020 3.3V", fontsize=7.5, color="#15803d", fontweight="semibold", zorder=3)

# 5. EDGE MCU CORE (with Web-downloaded ESP32 dev board image)
b_mcu_card = patches.FancyBboxPatch((36.5, 72.0), 29.5, 16.0, boxstyle="round,pad=0.5", ec="#059669", fc="#ecfdf5", lw=1.5, zorder=2)
ax.add_patch(b_mcu_card)
place_image(ax, os.path.join(web_prep_dir, 'esp32_dev.png'), 37.5, 73.0, 7.5, 14.0, border_color="#059669")
ax.text(46.2, 84.5, "ESP32 Embedded SoC", fontsize=10.0, fontweight="bold", color="#065f46", zorder=3)
ax.text(46.2, 80.5, "Xtensa Dual-Core 32-bit LX6", fontsize=8.2, color="#047857", zorder=3)
ax.text(46.2, 77.0, "520 KB SRAM | 4 MB SPI Flash", fontsize=8.0, color="#065f46", zorder=3)
ax.text(46.2, 74.0, "FreeRTOS Tickless Low-Power Kernel", fontsize=7.8, color="#059669", fontweight="semibold", zorder=3)

# GBDT Calibrator
b_gbdt = patches.FancyBboxPatch((36.5, 54.5), 29.5, 15.5, boxstyle="round,pad=0.5", ec="#0d9488", fc="#f0fdfa", lw=1.4, zorder=2)
ax.add_patch(b_gbdt)
ax.text(38.0, 66.5, "On-Chip INT8 Monotonic GBDT", fontsize=9.2, fontweight="bold", color="#0f766e", zorder=3)
ax.text(38.0, 63.0, "Physics-Guided Monotonic Decision Trees", fontsize=8.0, color="#115e59", zorder=3)
ax.text(38.0, 59.5, "Aerosol Deliquescence Compensation", fontsize=7.8, color="#0f766e", zorder=3)
ax.text(38.0, 56.5, "Flash: 18.2 KB | Latency: 1.42 ms (<0.01% duty)", fontsize=7.8, color="#0d9488", fontweight="bold", zorder=3)

# 72h Nocturnal Baseline Filter
b_drift = patches.FancyBboxPatch((36.5, 37.5), 29.5, 15.0, boxstyle="round,pad=0.5", ec="#0891b2", fc="#ecfeff", lw=1.4, zorder=2)
ax.add_patch(b_drift)
ax.text(38.0, 49.0, "72h Nocturnal Baseline Filter", fontsize=9.2, fontweight="bold", color="#0e7490", zorder=3)
ax.text(38.0, 45.5, "Zero-Point Dynamic Envelope Tracking", fontsize=7.8, color="#155e75", zorder=3)
ax.text(38.0, 42.5, "180-Day Optical Fouling Re-anchoring", fontsize=7.8, color="#0e7490", zorder=3)
ax.text(38.0, 39.5, "Adaptive 60s / 180s Duty Cycle Switching", fontsize=7.8, color="#0891b2", fontweight="bold", zorder=3)

# Drivers & Power States
b_drv = patches.FancyBboxPatch((36.5, 4.5), 29.5, 31.0, boxstyle="round,pad=0.5", ec="#4f46e5", fc="#eef2ff", lw=1.4, zorder=2)
ax.add_patch(b_drv)
ax.text(51.25, 32.5, "HARDWARE DRIVERS & POWER STATES", ha="center", fontsize=9.0, fontweight="bold", color="#3730a3", zorder=3)
ax.text(51.25, 28.5, "• 12-Bit SAR ADC (MQ-135 Chemoresistive Sampling)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(51.25, 25.0, "• Fast-Mode I2C Master (SHT31 Ambient T/RH)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(51.25, 21.5, "• UART2 Controller (PMS5003 Binary Frame Stream)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(51.25, 18.0, "• 20 kHz Hardware PWM (15s Sensor Heater Ramp)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(51.25, 14.0, "• Wi-Fi 802.11 b/g/n (2.4 GHz TX Telemetry Burst)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(51.25, 9.5, "Power States: Sleep (15 uA) -> Pre-Heat (265 mA)", ha="center", fontsize=7.5, color="#3730a3", fontweight="semibold", zorder=3)
ax.text(51.25, 6.5, "Active Optics (280 mA) -> Wi-Fi Burst (125 mA)", ha="center", fontsize=7.5, color="#3730a3", fontweight="semibold", zorder=3)

# 6. CLOUD PLATFORM (with Web-downloaded Grafana Dashboard image)
b_dash_frame = patches.FancyBboxPatch((72.5, 67.5), 25.0, 20.5, boxstyle="round,pad=0.5", ec="#5b21b6", fc="#f5f3ff", lw=1.4, zorder=2)
ax.add_patch(b_dash_frame)
place_image(ax, os.path.join(web_prep_dir, 'grafana_dashboard.png'), 73.5, 69.0, 11.5, 17.5, border_color="#5b21b6")
ax.text(86.2, 84.5, "Grafana Live UI", fontsize=9.5, fontweight="bold", color="#5b21b6", zorder=3)
ax.text(86.2, 80.5, "Real-Time Telemetry", fontsize=8.0, color="#6d28d9", zorder=3)
ax.text(86.2, 76.5, "Interactive GIS Map", fontsize=8.0, color="#6d28d9", zorder=3)
ax.text(86.2, 72.5, "Public Health Alerts", fontsize=8.0, color="#7c3aed", fontweight="semibold", zorder=3)

# Ingestion
b_mqtt = patches.FancyBboxPatch((72.5, 50.5), 25.0, 15.5, boxstyle="round,pad=0.5", ec="#6366f1", fc="#eef2ff", lw=1.4, zorder=2)
ax.add_patch(b_mqtt)
ax.text(85.0, 62.5, "MQTT Ingestion & Storage", ha="center", fontsize=9.2, fontweight="bold", color="#3730a3", zorder=3)
ax.text(85.0, 58.5, "EMQX Ingestion Broker (TLS 1.3)", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(85.0, 55.0, "InfluxDB Time-Series Engine", ha="center", fontsize=7.8, color="#4338ca", zorder=3)
ax.text(85.0, 52.0, "Synchronous Microclimate Log", ha="center", fontsize=7.5, color="#6366f1", fontweight="semibold", zorder=3)

# BiLSTM Forecaster
b_bilstm = patches.FancyBboxPatch((72.5, 27.0), 25.0, 21.5, boxstyle="round,pad=0.5", ec="#8b5cf6", fc="#f5f3ff", lw=1.5, zorder=2)
ax.add_patch(b_bilstm)
ax.text(85.0, 44.5, "BiLSTM-LSTM Forecaster", ha="center", fontsize=9.5, fontweight="bold", color="#5b21b6", zorder=3)
ax.text(85.0, 40.5, "Bidirectional Encoder (2x128)", ha="center", fontsize=8.0, color="#6d28d9", zorder=3)
ax.text(85.0, 37.0, "Temporal Attention Context Head", ha="center", fontsize=8.0, color="#6d28d9", zorder=3)
ax.text(85.0, 33.5, "Multi-Horizon (t+1h to t+24h)", ha="center", fontsize=8.0, color="#7c3aed", fontweight="bold", zorder=3)
ax.text(85.0, 30.0, "90% Conformal Prediction Bands", ha="center", fontsize=7.8, color="#8b5cf6", fontweight="bold", zorder=3)

# SHAP Engine
b_shap = patches.FancyBboxPatch((72.5, 4.5), 25.0, 20.5, boxstyle="round,pad=0.5", ec="#0284c7", fc="#f0f9ff", lw=1.4, zorder=2)
ax.add_patch(b_shap)
ax.text(85.0, 21.5, "SHAP & Decision Engine", ha="center", fontsize=9.2, fontweight="bold", color="#0369a1", zorder=3)
ax.text(85.0, 17.5, "TreeSHAP Global Attribution", ha="center", fontsize=7.8, color="#0284c7", zorder=3)
ax.text(85.0, 14.0, "Feature Dependency Verification", ha="center", fontsize=7.8, color="#0284c7", zorder=3)
ax.text(85.0, 10.5, "Episodic Plume Detection", ha="center", fontsize=7.8, color="#0ea5e9", zorder=3)
ax.text(85.0, 7.0, "Automated Public Health Triggers", ha="center", fontsize=7.5, color="#0369a1", fontweight="semibold", zorder=3)

# 7. High-Contrast Interconnects
ax.annotate("", xy=(35.0, 84.5), xytext=(29.0, 84.5), arrowprops=dict(arrowstyle="->", color="#2563eb", lw=2.4), zorder=6)
ax.text(32.0, 87.0, "UART", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#2563eb", 
        bbox=dict(boxstyle="round,pad=0.2", ec="#2563eb", fc="white", lw=1.0), zorder=7)

ax.annotate("", xy=(35.0, 70.5), xytext=(29.0, 70.5), arrowprops=dict(arrowstyle="->", color="#7c3aed", lw=2.4), zorder=6)
ax.text(32.0, 73.0, "ADC", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#7c3aed",
        bbox=dict(boxstyle="round,pad=0.2", ec="#7c3aed", fc="white", lw=1.0), zorder=7)

ax.annotate("", xy=(35.0, 57.0), xytext=(29.0, 57.0), arrowprops=dict(arrowstyle="->", color="#0d9488", lw=2.4), zorder=6)
ax.text(32.0, 59.5, "I2C", ha="center", va="center", fontsize=7.5, fontweight="bold", color="#0d9488",
        bbox=dict(boxstyle="round,pad=0.2", ec="#0d9488", fc="white", lw=1.0), zorder=7)

ax.annotate("", xy=(35.0, 20.0), xytext=(29.0, 20.0), arrowprops=dict(arrowstyle="->", color="#ea580c", lw=2.4), zorder=6)
ax.text(32.0, 22.5, "3.3V/5V", ha="center", va="center", fontsize=7.2, fontweight="bold", color="#ea580c",
        bbox=dict(boxstyle="round,pad=0.2", ec="#ea580c", fc="white", lw=1.0), zorder=7)

ax.annotate("", xy=(71.5, 58.0), xytext=(67.5, 58.0), arrowprops=dict(arrowstyle="->", color="#059669", lw=2.6), zorder=6)
ax.text(69.5, 61.2, "Wi-Fi\nMQTT", ha="center", va="center", fontsize=7.8, fontweight="bold", color="#059669",
        bbox=dict(boxstyle="round,pad=0.2", ec="#059669", fc="white", lw=1.0), zorder=7)

plt.tight_layout()
fig.savefig(os.path.join(out_dir, 'fig1_system_architecture.png'), dpi=300, bbox_inches='tight')
plt.close(fig)
print("Fig 1 generated successfully with web component images!")
