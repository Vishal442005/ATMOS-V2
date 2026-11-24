import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

os.makedirs('seminar_vishal/figures', exist_ok=True)

# 1. Space DTN Protocol Stack Comparison
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.5)
ax.axis('off')

# Color palette
c_blue = '#1d3557'
c_light_blue = '#457b9d'
c_teal = '#a8dadc'
c_coral = '#e63946'
c_bg = '#f1faee'
c_box = '#e9ecef'

# Title
ax.text(5, 7.1, "Comparison of Terrestrial Internet, SCPS, and Space DTN Protocol Stacks", 
        fontsize=13, fontweight='bold', ha='center', color=c_blue)

# Column Headers
stacks = [
    ("Standard Terrestrial\nTCP/IP Stack", 1.8),
    ("CCSDS SCPS Stack\n(Early Space Attempts)", 5.0),
    ("Modern Space DTN Stack\n(RFC 9171 / CCSDS Standards)", 8.2)
]

for title, x in stacks:
    ax.text(x, 6.3, title, fontsize=10, fontweight='bold', ha='center', color=c_blue)

# Stack layers definitions (name, y, height, color, textcolor)
# Column 1: TCP/IP
col1_layers = [
    ("Application Layer (HTTP, FTP)", 5.2, 0.7, '#dee2e6', '#212529'),
    ("Transport: TCP / UDP\n(Requires Interactive RTT)", 4.2, 0.8, '#ffccd5', '#9d0208'),
    ("Network: IPv4 / IPv6\n(Assumes Continuous End-to-End Path)", 3.2, 0.8, '#ffccd5', '#9d0208'),
    ("Data Link: Ethernet / 802.11", 2.4, 0.6, '#dee2e6', '#212529'),
    ("Physical: Copper / Fiber / RF", 1.6, 0.6, '#dee2e6', '#212529')
]

for text, y, h, col, tcol in col1_layers:
    rect = patches.FancyBboxPatch((0.5, y), 2.6, h, boxstyle="round,pad=0.04", fc=col, ec='#adb5bd', lw=1.2)
    ax.add_patch(rect)
    ax.text(1.8, y + h/2.0, text, fontsize=7.5, ha='center', va='center', color=tcol, multialignment='center')

# Column 2: CCSDS SCPS
col2_layers = [
    ("Mission Applications", 5.2, 0.7, '#dee2e6', '#212529'),
    ("SCPS-TP (Transport Protocol)\n(TCP extensions: large windows)", 4.2, 0.8, '#ffe5d9', '#d00000'),
    ("SCPS-NP / Compressed IP\n(Breaks on long occultation)", 3.2, 0.8, '#ffe5d9', '#d00000'),
    ("Space Link (TC / TM)", 2.4, 0.6, '#dee2e6', '#212529'),
    ("Deep Space RF Links", 1.6, 0.6, '#dee2e6', '#212529')
]

for text, y, h, col, tcol in col2_layers:
    rect = patches.FancyBboxPatch((3.7, y), 2.6, h, boxstyle="round,pad=0.04", fc=col, ec='#adb5bd', lw=1.2)
    ax.add_patch(rect)
    ax.text(5.0, y + h/2.0, text, fontsize=7.5, ha='center', va='center', color=tcol, multialignment='center')

# Column 3: Space DTN Architecture
col3_layers = [
    ("Space Applications / Science Telemetry", 5.4, 0.5, '#d8f3dc', '#1b4332'),
    ("BUNDLE PROTOCOL (BPv7 - RFC 9171)\n+ BPSec (Security: BIB / BCB)\n[Store-Carry-and-Forward Overlay]", 4.1, 1.1, '#74c69d', '#081c15'),
    ("Convergence Layer Adapters (CLA)", 3.4, 0.55, '#b7e4c7', '#1b4332'),
    ("Transport: LTP (RFC 5326) / TCP / UDP\n(Licklider Protocol: Red/Green Segments)", 2.4, 0.85, '#95d5b2', '#081c15'),
    ("Underlying Space Links:\nProximity-1 RF / Ka-Band / Optical Laser", 1.5, 0.75, '#d8f3dc', '#1b4332')
]

for text, y, h, col, tcol in col3_layers:
    rect = patches.FancyBboxPatch((6.9, y), 2.6, h, boxstyle="round,pad=0.04", fc=col, ec='#2d6a4f', lw=1.5)
    ax.add_patch(rect)
    ax.text(8.2, y + h/2.0, text, fontsize=7.5, fontweight='bold' if 'BUNDLE' in text else 'normal',
            ha='center', va='center', color=tcol, multialignment='center')

# Highlight Arrow on DTN
ax.annotate("Overlay Layer\nSpans Across Heterogeneous\nDisrupted Networks", 
            xy=(6.9, 4.65), xytext=(5.6, 4.65),
            arrowprops=dict(arrowstyle="->", color='#e63946', lw=1.5),
            fontsize=7, fontweight='bold', color='#e63946', va='center', ha='right',
            bbox=dict(boxstyle="round,pad=0.2", fc='#fff', ec='#e63946', lw=1))

plt.tight_layout()
plt.savefig('seminar_vishal/figures/space_dtn_protocol_stack.png', dpi=300)
plt.savefig('seminar_vishal/figures/space_dtn_protocol_stack.pdf')
plt.close()
print("Saved space_dtn_protocol_stack.png and .pdf")

# 2. Contact Graph Routing Principle Diagram
fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.5)
ax.axis('off')

ax.text(5, 5.1, "Deterministic Contact Graph Routing (CGR) in Orbital Space Networks", 
        fontsize=12, fontweight='bold', ha='center', color=c_blue)

# Timeline bar
ax.plot([1.0, 9.0], [1.0, 1.0], color='#6c757d', lw=2)
ax.text(9.1, 1.0, "Time (t)", fontsize=9, va='center', fontweight='bold', color='#495057')

# Time ticks
ticks = [("t0 (Launch)", 1.5), ("t1 (AOS Orbiter)", 3.2), ("t2 (LOS Orbiter)", 5.2), ("t3 (AOS Earth)", 6.8), ("t4 (LOS Earth)", 8.5)]
for label, x in ticks:
    ax.plot([x, x], [0.9, 1.1], color='#343a40', lw=1.5)
    ax.text(x, 0.65, label, fontsize=7, ha='center', color='#343a40')

# Nodes
# Mars Surface Rover
rect_rover = patches.FancyBboxPatch((0.8, 3.8), 2.0, 0.8, boxstyle="round,pad=0.05", fc='#e9ecef', ec='#495057', lw=1.2)
ax.add_patch(rect_rover)
ax.text(1.8, 4.2, "Node 1:\nMars Rover (Source)", fontsize=8, ha='center', va='center', fontweight='bold')

# Mars Relay Orbiter
rect_orbiter = patches.FancyBboxPatch((4.0, 3.8), 2.0, 0.8, boxstyle="round,pad=0.05", fc='#e9ecef', ec='#495057', lw=1.2)
ax.add_patch(rect_orbiter)
ax.text(5.0, 4.2, "Node 2:\nRelay Orbiter", fontsize=8, ha='center', va='center', fontweight='bold')

# Earth Ground Station
rect_earth = patches.FancyBboxPatch((7.2, 3.8), 2.0, 0.8, boxstyle="round,pad=0.05", fc='#e9ecef', ec='#495057', lw=1.2)
ax.add_patch(rect_earth)
ax.text(8.2, 4.2, "Node 3:\nEarth DSN Station", fontsize=8, ha='center', va='center', fontweight='bold')

# Contact Windows (Bands)
# Contact 1: Rover to Orbiter
rect_c1 = patches.Rectangle((3.2, 2.7), 2.0, 0.5, fc='#a8dadc', ec='#457b9d', lw=1.2, alpha=0.9)
ax.add_patch(rect_c1)
ax.text(4.2, 2.95, "Contact Window 1: Rover -> Orbiter\nRate: 2 Mbps, Vol: 30 MB, OWLT: 2 ms", 
        fontsize=7, ha='center', va='center', fontweight='bold', color='#1d3557')

# Intermittent storage / carry phase
ax.annotate("Store & Carry in Buffer\n(Planetary Occultation: No Link)", 
            xy=(5.0, 3.6), xytext=(5.0, 2.0),
            arrowprops=dict(arrowstyle="->", color='#e63946', lw=1.5),
            fontsize=7.5, fontweight='bold', color='#e63946', ha='center',
            bbox=dict(boxstyle="round,pad=0.2", fc='#fff', ec='#e63946'))

# Contact 2: Orbiter to Earth DSN
rect_c2 = patches.Rectangle((6.8, 2.7), 1.7, 0.5, fc='#c7f9cc', ec='#38b000', lw=1.2, alpha=0.9)
ax.add_patch(rect_c2)
ax.text(7.65, 2.95, "Contact Window 2: Orbiter -> Earth\nRate: 150 Mbps, OWLT: 14 min", 
        fontsize=7, ha='center', va='center', fontweight='bold', color='#004b23')

# Route Path Arrows
ax.annotate("", xy=(3.2, 3.8), xytext=(2.8, 3.8), arrowprops=dict(arrowstyle="->", color='#1d3557', lw=2))
ax.annotate("", xy=(7.2, 3.8), xytext=(6.0, 3.8), arrowprops=dict(arrowstyle="->", color='#1d3557', lw=2))

plt.tight_layout()
plt.savefig('seminar_vishal/figures/contact_graph_routing_flow.png', dpi=300)
plt.savefig('seminar_vishal/figures/contact_graph_routing_flow.pdf')
plt.close()
print("Saved contact_graph_routing_flow.png and .pdf")
