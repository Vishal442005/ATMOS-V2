# build_pptx_presentation.py
# Generates a professional 24-slide widescreen (16:9) PowerPoint presentation for Vishal's seminar.

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # --- COLOR PALETTE ---
    C_SPACE_NAVY  = RGBColor(11, 27, 61)     # #0B1B3D
    C_NAVY_MID    = RGBColor(22, 46, 98)     # #162E62
    C_AERO_BLUE   = RGBColor(0, 119, 182)    # #0077B6
    C_CYAN        = RGBColor(0, 180, 216)    # #00B4D8
    C_GOLD        = RGBColor(255, 183, 3)    # #FFB703
    C_BG_LIGHT    = RGBColor(248, 249, 252)  # #F8F9FC
    C_WHITE       = RGBColor(255, 255, 255)
    C_CARD_BG     = RGBColor(255, 255, 255)
    C_CARD_BORDER = RGBColor(218, 225, 233)
    C_TEXT_DARK   = RGBColor(30, 41, 59)     # #1E293B
    C_TEXT_MUTED  = RGBColor(100, 116, 139)  # #64748B
    C_RED_ACCENT  = RGBColor(230, 57, 70)    # #E63946
    C_GREEN_ACC   = RGBColor(42, 157, 143)   # #2A9D8F

    figures_dir = os.path.join("seminar_vishal", "figures")
    logo_path = os.path.join(figures_dir, "logo.png")

    def add_header(slide, title_text, category_text="SEMINAR TECHNICAL PRESENTATION"):
        # Top banner background
        header_box = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15)
        )
        header_box.fill.solid()
        header_box.fill.fore_color.rgb = C_SPACE_NAVY
        header_box.line.color.rgb = C_SPACE_NAVY

        # Accent bottom line
        accent_line = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.12), Inches(13.333), Inches(0.04)
        )
        accent_line.fill.solid()
        accent_line.fill.fore_color.rgb = C_CYAN
        accent_line.line.color.rgb = C_CYAN

        # Category tracker
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(10), Inches(0.28))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_CYAN

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(11.5), Inches(0.65))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(20)
        p_t.font.bold = True
        p_t.font.color.rgb = C_WHITE

        # Small logo in top right
        if os.path.exists(logo_path):
            slide.shapes.add_picture(logo_path, Inches(12.35), Inches(0.15), height=Inches(0.85))

    def add_footer(slide, current_idx, total_slides=24):
        footer_box = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.12), Inches(13.333), Inches(0.38)
        )
        footer_box.fill.solid()
        footer_box.fill.fore_color.rgb = C_SPACE_NAVY
        footer_box.line.color.rgb = C_SPACE_NAVY

        tf = footer_box.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.06)
        p = tf.paragraphs[0]
        p.text = f"Department of ECE, JNGEC Sundernagar | Delay Tolerant Networks in Space Communications | Slide {current_idx} of {total_slides}"
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(9)
        p.font.color.rgb = RGBColor(180, 200, 220)

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.color.rgb = color
        return bg

    def add_card(slide, left, top, width, height, title="", title_color=C_SPACE_NAVY, bg_color=C_CARD_BG, border_color=C_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)

        if title:
            # Title badge
            t_box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.4))
            tf = t_box.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = title_color
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Dark Navy Premium Theme)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, C_SPACE_NAVY)

    # Decorative header strip
    strip = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.15))
    strip.fill.solid()
    strip.fill.fore_color.rgb = C_CYAN
    strip.line.color.rgb = C_CYAN

    # Logo
    if os.path.exists(logo_path):
        s1.shapes.add_picture(logo_path, Inches(1.0), Inches(1.1), width=Inches(1.8))

    # College Title
    clg_box = s1.shapes.add_textbox(Inches(3.1), Inches(1.05), Inches(9.2), Inches(0.9))
    tf_clg = clg_box.text_frame
    tf_clg.word_wrap = True
    p_c1 = tf_clg.paragraphs[0]
    p_c1.text = "JAWAHARLAL NEHRU GOVT. ENGINEERING COLLEGE, SUNDERNAGAR"
    p_c1.font.size = Pt(15)
    p_c1.font.bold = True
    p_c1.font.color.rgb = C_CYAN

    p_c2 = tf_clg.add_paragraph()
    p_c2.text = "Department of Electronics & Communication Engineering | Affiliated to HPTU Hamirpur"
    p_c2.font.size = Pt(11)
    p_c2.font.color.rgb = RGBColor(190, 210, 235)

    p_c3 = tf_clg.add_paragraph()
    p_c3.text = "B.TECH. TECHNICAL SEMINAR PRESENTATION (7TH SEMESTER, 2026-2027)"
    p_c3.font.size = Pt(10.5)
    p_c3.font.bold = True
    p_c3.font.color.rgb = C_GOLD

    # Main Seminar Title Box
    title_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(2.2), Inches(11.333), Inches(2.3))
    title_card.fill.solid()
    title_card.fill.fore_color.rgb = C_NAVY_MID
    title_card.line.color.rgb = C_AERO_BLUE
    title_card.line.width = Pt(1.8)

    t_box = s1.shapes.add_textbox(Inches(1.3), Inches(2.4), Inches(10.7), Inches(1.9))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    p_t1 = tf_t.paragraphs[0]
    p_t1.text = "DELAY TOLERANT NETWORKS IN SPACE COMMUNICATIONS"
    p_t1.font.size = Pt(25)
    p_t1.font.bold = True
    p_t1.font.color.rgb = C_WHITE

    p_t2 = tf_t.add_paragraph()
    p_t2.text = "Architectural Genesis, Protocol Evolution, and Deterministic Routing from Deep Impact to Artemis"
    p_t2.font.size = Pt(14)
    p_t2.font.italic = True
    p_t2.font.color.rgb = C_CYAN

    # Metadata Cards (Student & Supervisor)
    card_stu = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.75), Inches(5.4), Inches(1.9))
    card_stu.fill.solid()
    card_stu.fill.fore_color.rgb = RGBColor(16, 36, 78)
    card_stu.line.color.rgb = C_CYAN
    card_stu.line.width = Pt(1.2)

    tb_s = s1.shapes.add_textbox(Inches(1.2), Inches(4.85), Inches(5.0), Inches(1.6))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    p = tf_s.paragraphs[0]
    p.text = "PRESENTED BY:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p = tf_s.add_paragraph()
    p.text = "Vishal Chandel"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    p = tf_s.add_paragraph()
    p.text = "University Roll No.: 23010104072\nSemester: 7th Semester, B.Tech. ECE\nJNGEC Sundernagar (H.P.)"
    p.font.size = Pt(10.5)
    p.font.color.rgb = RGBColor(200, 220, 240)

    card_sup = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(4.75), Inches(5.4), Inches(1.9))
    card_sup.fill.solid()
    card_sup.fill.fore_color.rgb = RGBColor(16, 36, 78)
    card_sup.line.color.rgb = C_CYAN
    card_sup.line.width = Pt(1.2)

    tb_sp = s1.shapes.add_textbox(Inches(7.1), Inches(4.85), Inches(5.0), Inches(1.6))
    tf_sp = tb_sp.text_frame
    tf_sp.word_wrap = True
    p = tf_sp.paragraphs[0]
    p.text = "UNDER THE SUPERVISION OF:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p = tf_sp.add_paragraph()
    p.text = "Dr. Sanjeev Kumar"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    p = tf_sp.add_paragraph()
    p.text = "Assistant Professor\nDepartment of Electronics & Communication Engineering\nJNGEC Sundernagar"
    p.font.size = Pt(10.5)
    p.font.color.rgb = RGBColor(200, 220, 240)

    add_footer(s1, 1)

    # =========================================================================
    # SLIDE 2: PRESENTATION AGENDA / ROADMAP
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, C_BG_LIGHT)
    add_header(s2, "Seminar Presentation Roadmap & Agenda")

    agenda_items = [
        ("01", "The Space Communication Dilemma", "Physical extremes of deep space, astronomical latency, planetary occlusions, and the breakdown of terrestrial TCP/IP."),
        ("02", "Store-Carry-and-Forward & BPv7", "The Bundle Protocol Version 7 (RFC 9171), CBOR serialization, compressed custody signals, and recursive BIBE tunneling."),
        ("03", "Transport Layer Reliability (LTP)", "Licklider Transmission Protocol (RFC 5326), Red reliable vs. Green data blocks, and RL-based adaptive Forward Error Correction."),
        ("04", "Deterministic Contact Graph Routing", "Time-evolving contact plans, Dijkstra search over celestial contacts, dynamic buffer constraints, and Graph Attention MARL AI."),
        ("05", "Frontiers: Optical Links & Security", "Deep Space Optical Communications (DSOC), CubeSat micro-DTN (uD3TN), and Bundle Security Protocol (BPSec, RFC 9172)."),
        ("06", "Flight Validations & Synthesis", "Flight validations from Deep Impact (DINET 2008) to Artemis Lunar Gateway, literature synthesis across 16 papers, and conclusion.")
    ]

    for idx, (num, heading, desc) in enumerate(agenda_items):
        col = idx % 2
        row = idx // 2
        left = Inches(0.8 + col * 5.9)
        top = Inches(1.4 + row * 1.8)
        
        # Number badge
        badge = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(0.9), Inches(1.5))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_SPACE_NAVY
        badge.line.color.rgb = C_CYAN
        tf_b = badge.text_frame
        p_b = tf_b.paragraphs[0]
        p_b.text = num
        p_b.font.size = Pt(18)
        p_b.font.bold = True
        p_b.font.color.rgb = C_GOLD
        p_b.alignment = PP_ALIGN.CENTER

        # Text card
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.95), top, Inches(4.75), Inches(1.5))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.color.rgb = C_CARD_BORDER
        tf_c = card.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_top = Inches(0.12)
        p1 = tf_c.paragraphs[0]
        p1.text = heading
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = C_SPACE_NAVY

        p2 = tf_c.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT_DARK

    add_footer(s2, 2)

    # =========================================================================
    # SLIDE 3: THE DEEP-SPACE COMMUNICATION REALITY
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, C_BG_LIGHT)
    add_header(s3, "The Deep-Space Communication Reality: Physical Extremes", "1. PHYSICAL FOUNDATIONS")

    c1 = add_card(s3, Inches(0.8), Inches(1.4), Inches(3.7), Inches(5.4), "1. Astronomical Latency", C_RED_ACCENT)
    tb1 = s3.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(3.3), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = 0
    p = tf1.paragraphs[0]
    p.text = "Speed-of-light propagation delays:"
    p.font.bold = True
    p.font.size = Pt(11.5)
    bullets1 = [
        "Moon: ~1.28 s one-way (~2.56 s RTT).",
        "Mars: 3.1 to 22.3 min one-way (6.2 to 44.6 min RTT) depending on orbital alignment.",
        "Jupiter: 33 to 53 min one-way.",
        "Voyager 1: > 22.5 hours one-way.",
        "Impact: Real-time interactive feedback loops and instant handshakes are physically impossible."
    ]
    for b in bullets1:
        p = tf1.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    c2 = add_card(s3, Inches(4.8), Inches(1.4), Inches(3.7), Inches(5.4), "2. Intermittent Connectivity", C_AERO_BLUE)
    tb2 = s3.shapes.add_textbox(Inches(5.0), Inches(2.0), Inches(3.3), Inches(4.5))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    tf2.margin_left = tf2.margin_top = 0
    p = tf2.paragraphs[0]
    p.text = "Discontinuous contact opportunities:"
    p.font.bold = True
    p.font.size = Pt(11.5)
    bullets2 = [
        "Planetary Rotation: Ground stations lose line-of-sight every 12 to 24 hours.",
        "Orbital Occlusion: Orbiters pass behind moons or planets (e.g., lunar far side).",
        "Solar Conjunctions: Sun passes between Earth and Mars, severing RF for ~2 weeks.",
        "Pointing & Ephemeris: Narrow antenna beams require precise electromechanical tracking.",
        "Result: Continuous end-to-end paths never exist simultaneously."
    ]
    for b in bullets2:
        p = tf2.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    c3 = add_card(s3, Inches(8.8), Inches(1.4), Inches(3.7), Inches(5.4), "3. Asymmetric & Noisy Links", C_GREEN_ACC)
    tb3 = s3.shapes.add_textbox(Inches(9.0), Inches(2.0), Inches(3.3), Inches(4.5))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    tf3.margin_left = tf3.margin_top = 0
    p = tf3.paragraphs[0]
    p.text = "Channel physics and power asymmetry:"
    p.font.bold = True
    p.font.size = Pt(11.5)
    bullets3 = [
        "Free-Space Path Loss: Follows inverse square law (1/R^2); deep space signal power drops by > 200 dB.",
        "Severe Bandwidth Asymmetry: Deep Space Network (DSN) uplink is kW-scale; spacecraft downlink is only 15-50 W.",
        "High Bit Error Rates: BER ranges from 10^-3 to 10^-1 during atmospheric entry or solar activity.",
        "Optical Sensitivity: Cloud cover, turbulence, and background solar noise degrade optical links."
    ]
    for b in bullets3:
        p = tf3.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s3, 3)

    # =========================================================================
    # SLIDE 4: THE BREAKDOWN OF TERRESTRIAL TCP/IP IN SPACE
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, C_BG_LIGHT)
    add_header(s4, "The Fatal Breakdown of Terrestrial TCP/IP in Deep Space", "1. PHYSICAL FOUNDATIONS")

    add_card(s4, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "Failure Modes of the TCP/IP Suite", C_RED_ACCENT)
    tb4a = s4.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf4a = tb4a.text_frame
    tf4a.word_wrap = True
    tf4a.margin_left = tf4a.margin_top = 0
    p = tf4a.paragraphs[0]
    p.text = "Why Standard Protocols Collapse:"
    p.font.bold = True
    p.font.size = Pt(12)
    bullets_tcp = [
        "Three-Way Handshake (SYN -> SYN-ACK -> ACK): On a Mars mission at 20 min one-way delay, establishing a connection requires 40 to 60 minutes before sending a single payload byte.",
        "RTT Timer Expirations (RTO): Terrestrial TCP retransmission timers trigger after 200 ms - 2 s. Across interplanetary links, timers fire incessantly, causing perpetual spurious retransmissions.",
        "AIMD Congestion Control Collapse: TCP misinterprets deep-space high BER as congestion, cutting its Congestion Window (cwnd) by 50% repeatedly, reducing effective throughput to near zero.",
        "DNS Failure: Dynamic domain name resolution queries cannot tolerate multi-hour round trips."
    ]
    for b in bullets_tcp:
        p = tf4a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s4, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "Terrestrial vs. Deep-Space Protocol Assumptions", C_SPACE_NAVY)
    table_shape = s4.shapes.add_table(5, 3, Inches(7.0), Inches(2.1), Inches(5.3), Inches(4.2))
    table = table_shape.table
    table.columns[0].width = Inches(1.7)
    table.columns[1].width = Inches(1.7)
    table.columns[2].width = Inches(1.9)

    headers = ["Parameter", "Terrestrial Internet", "Deep-Space Channel"]
    for col_idx, h in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_SPACE_NAVY
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

    data = [
        ("End-to-End Path", "Continuous, low-latency", "Discontinuous, scheduled contacts"),
        ("Propagation Delay", "< 100 ms round-trip", "Minutes to hours (light-time)"),
        ("Packet Loss Reason", "Buffer congestion", "Path loss, BER, antenna occlusion"),
        ("Bandwidth Symmetry", "Roughly symmetric", "Highly asymmetric (uplink >> downlink)")
    ]
    for row_idx, row in enumerate(data):
        for col_idx, val in enumerate(row):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if row_idx % 2 == 0 else RGBColor(240, 245, 250)
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_DARK

    add_footer(s4, 4)

    # =========================================================================
    # SLIDE 5: THE PARADIGM SHIFT: STORE-CARRY-AND-FORWARD
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, C_BG_LIGHT)
    add_header(s5, "The Architectural Paradigm Shift: Store-Carry-and-Forward", "2. ARCHITECTURAL GENESIS")

    add_card(s5, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "Core Principles of Store-Carry-and-Forward", C_AERO_BLUE)
    tb5a = s5.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf5a = tb5a.text_frame
    tf5a.word_wrap = True
    tf5a.margin_left = tf5a.margin_top = 0
    bullets_scf = [
        "Message-Oriented Bundling: Data is aggregated into self-contained units called 'Bundles' containing complete metadata, lifetime expiration, and routing headers.",
        "Persistent Storage at Every Hop: Routers hold bundles in non-volatile flash memory/NVRAM for hours or days, awaiting the next communication opportunity.",
        "Exploitation of Physical Motion: Orbiters, rovers, and planetary probes physically transport stored bundles across space, bridging communication voids.",
        "Hop-by-Hop Custody Transfer: Guarantees reliable delivery across long delay links without requiring end-to-end ACKs back to the original source."
    ]
    for b in bullets_scf:
        p = tf5a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s5, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "Custody Transfer & Hop-by-Hop Reliability", C_GREEN_ACC)
    tb5b = s5.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf5b = tb5b.text_frame
    tf5b.word_wrap = True
    tf5b.margin_left = tf5b.margin_top = 0
    p = tf5b.paragraphs[0]
    p.text = "Custody Mechanics in Deep Space:"
    p.font.bold = True
    p.font.size = Pt(12)
    bullets_custody = [
        "Step 1: Node A transmits bundle to Node B and requests Custody Acceptance.",
        "Step 2: Node B stores the bundle in non-volatile storage, verifies cryptographic integrity, and returns a Custody Signal (CS).",
        "Step 3: Node A releases the bundle from its memory only after receiving Node B's CS.",
        "Error Isolation: If transmission fails between Node B and Node C, only Node B retransmits. Node A is completely unburdened.",
        "Key Advantage: Eliminates multi-hop interplanetary retransmission timeouts."
    ]
    for b in bullets_custody:
        p = tf5b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s5, 5)

    # =========================================================================
    # SLIDE 6: THE SPACE DTN PROTOCOL ARCHITECTURE (BPv7)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, C_BG_LIGHT)
    add_header(s6, "The Space DTN Protocol Architecture (BPv7)", "2. ARCHITECTURAL GENESIS")

    # Left: Image
    img_stack = os.path.join(figures_dir, "space_dtn_protocol_stack.png")
    if os.path.exists(img_stack):
        add_card(s6, Inches(0.8), Inches(1.4), Inches(6.2), Inches(5.4), "Protocol Layering Architecture", C_SPACE_NAVY)
        s6.shapes.add_picture(img_stack, Inches(0.95), Inches(2.0), width=Inches(5.9))

    # Right: Technical Description
    add_card(s6, Inches(7.3), Inches(1.4), Inches(5.2), Inches(5.4), "Architectural Pillars of BPv7", C_AERO_BLUE)
    tb6 = s6.shapes.add_textbox(Inches(7.5), Inches(2.0), Inches(4.8), Inches(4.5))
    tf6 = tb6.text_frame
    tf6.word_wrap = True
    tf6.margin_left = tf6.margin_top = 0
    p = tf6.paragraphs[0]
    p.text = "The Overlay Model (RFC 9171):"
    p.font.bold = True
    p.font.size = Pt(12)
    bullets_bp = [
        "Bundle Layer: Situated between the application and convergence layers. Operates transparently across heterogeneous underlying networks (RF, optical, proximity).",
        "Convergence Layer Adapters (CLA): Interface the Bundle Protocol to lower-layer physical transports (LTP, TCPCL, UDPCL, CCSDS Space Data Links).",
        "Unified Addressing: Uses Endpoint Identifiers (EIDs) formatted as URIs (e.g., dtn://mars-rover/telemetry or ipn:42.1).",
        "Interplanetary Interoperability: Seamlessly binds terrestrial Internet, lunar orbiters, surface rovers, and deep-space transit vehicles."
    ]
    for b in bullets_bp:
        p = tf6.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s6, 6)

    # =========================================================================
    # SLIDE 7: EVOLUTION OF THE BUNDLE PROTOCOL: BPv6 TO BPv7
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, C_BG_LIGHT)
    add_header(s7, "Evolution of the Bundle Protocol: From BPv6 to BPv7", "2. ARCHITECTURAL GENESIS")

    add_card(s7, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "The Legacy BPv6 Era (RFC 5050)", C_TEXT_MUTED)
    tb7a = s7.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf7a = tb7a.text_frame
    tf7a.word_wrap = True
    tf7a.margin_left = tf7a.margin_top = 0
    bullets_bp6 = [
        "Origins: Developed by the DTN Research Group (DTNRG) in 2007.",
        "Encoding: SDNV (Self-Delimiting Numeric Values) and ASCII text strings.",
        "Custody Transfer Flaw: Lloyd Wood's 2009 critique identified custody signal proliferation (each bundle required an individual custody signal, multiplying reverse-link traffic).",
        "High Header Overhead: Verbose variable-length headers consumed precious bits on deep-space links.",
        "Security: Separate experimental Bundle Security Protocol (BSP, RFC 6257) with tight coupling."
    ]
    for b in bullets_bp6:
        p = tf7a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s7, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "The Modern BPv7 Standard (RFC 9171)", C_CYAN)
    tb7b = s7.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf7b = tb7b.text_frame
    tf7b.word_wrap = True
    tf7b.margin_left = tf7b.margin_top = 0
    bullets_bp7 = [
        "CBOR Serialization: Replaces SDNV with Concise Binary Object Representation (RFC 8949), achieving a 35% header reduction.",
        "Compressed Custody Signals (CCS): Single custody acknowledgement aggregates hundreds of bundles via bitmasks.",
        "Decoupled Custody Management: Custody is now handled by specialized administrative records rather than rigid core headers.",
        "Modern Security (BPSec, RFC 9172): Integrates native cryptographic integrity (BIB) and confidentiality (BCB).",
        "Adopted by NASA & ESA: Official baseline for Artemis and LunaNet."
    ]
    for b in bullets_bp7:
        p = tf7b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s7, 7)

    # =========================================================================
    # SLIDE 8: RECURSIVE DTN & BIBE ENCAPSULATION
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, C_BG_LIGHT)
    add_header(s8, "Recursive DTN: Bundle-in-Bundle Encapsulation (BIBE)", "2. ARCHITECTURAL GENESIS")

    add_card(s8, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "The Challenge of Heterogeneous Space Domains", C_SPACE_NAVY)
    tb8a = s8.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf8a = tb8a.text_frame
    tf8a.word_wrap = True
    tf8a.margin_left = tf8a.margin_top = 0
    bullets_bibe_prob = [
        "Deep-space networks encompass distinct routing subnets: Lunar surface networks, Lagrange point relays, Earth ground stations.",
        "Different subnets possess varying security classifications, addressing schemes (IPN vs. DTN URIs), and custody requirements.",
        "Traditional Routers: Modifying bundle headers at domain gateways breaks end-to-end cryptographic signatures and invalidates security hashes."
    ]
    for b in bullets_bibe_prob:
        p = tf8a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s8, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "BIBE Mechanics & Protocol Overlay (RFC 9174)", C_AERO_BLUE)
    tb8b = s8.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf8b = tb8b.text_frame
    tf8b.word_wrap = True
    tf8b.margin_left = tf8b.margin_top = 0
    bullets_bibe_sol = [
        "Bundle Tunneling: An entire original bundle (including its headers, security blocks, and payload) is encapsulated as the opaque payload of an outer 'Carrier Bundle'.",
        "Preservation of Integrity: The outer bundle navigates the intermediary network. The original bundle's cryptographic signatures remain completely untampered.",
        "Aggregation & Compression: Gateway nodes aggregate multiple small bundles destined for the same planetary relay into a single carrier bundle, drastically reducing transmission overhead.",
        "Standardized in RFC 9174 (2022)."
    ]
    for b in bullets_bibe_sol:
        p = tf8b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s8, 8)

    # =========================================================================
    # SLIDE 9: TRANSPORT LAYER RELIABILITY: LTP (RFC 5326)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, C_BG_LIGHT)
    add_header(s9, "Transport Layer Reliability: Licklider Transmission Protocol", "3. TRANSPORT RELIABILITY")

    add_card(s9, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "LTP Architecture: Red vs. Green Data Blocks", C_RED_ACCENT)
    tb9a = s9.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf9a = tb9a.text_frame
    tf9a.word_wrap = True
    tf9a.margin_left = tf9a.margin_top = 0
    bullets_ltp = [
        "Named in honor of J.C.R. Licklider (ARPANET pioneer).",
        "Designed specifically for long-delay point-to-point links (e.g., orbiter-to-ground or spacecraft-to-spacecraft).",
        "Red Data Service (Guaranteed Reliability):",
        "  - Critical flight telemetry, command sequences, scientific datasets.",
        "  - Uses Selective Negative Acknowledgement (SNACK) ARQ.",
        "  - Sender emits Checkpoint (CP) segments; Receiver responds with Report Segments (RS).",
        "Green Data Service (Best-Effort):",
        "  - Loss-tolerant real-time imagery, video streams, non-critical sensor readings.",
        "  - Zero ACK/retransmission overhead; maximum channel bandwidth utilization."
    ]
    for b in bullets_ltp:
        p = tf9a.add_paragraph()
        p.text = b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s9, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "LTP Segment Exchange & Checkpointing Mechanism", C_SPACE_NAVY)
    tb9b = s9.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf9b = tb9b.text_frame
    tf9b.word_wrap = True
    tf9b.margin_left = tf9b.margin_top = 0
    bullets_ltp_mech = [
        "1. Block Transmission: Sender streams Red Data segments without waiting for intermediate per-packet ACKs.",
        "2. Checkpoint (CP): The final segment of the Red Block carries a CP flag requesting receiver status.",
        "3. Report Segment (RS): The receiver generates an RS containing claim scopes (start offset and length of missing spans).",
        "4. Selective Retransmission: Sender retransmits only the unreceived bytes, rather than restarting the entire block.",
        "5. Elimination of Idle Time: Sender continues transmitting subsequent blocks during the multi-minute wait for the RS."
    ]
    for b in bullets_ltp_mech:
        p = tf9b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s9, 9)

    # =========================================================================
    # SLIDE 10: INTELLIGENT TRANSPORT: ADAPTIVE FEC & DEEP Q-LEARNING
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, C_BG_LIGHT)
    add_header(s10, "Intelligent Transport: Adaptive Forward Error Correction", "3. TRANSPORT RELIABILITY")

    add_card(s10, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "The Challenge with Static Coding Rates", C_TEXT_MUTED)
    tb10a = s10.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf10a = tb10a.text_frame
    tf10a.word_wrap = True
    tf10a.margin_left = tf10a.margin_top = 0
    bullets_fec_prob = [
        "Space link margins fluctuate dramatically due to atmospheric weather, plasma scintillation, and antenna pointing jitter.",
        "Conservative Coding: Allocating heavy fixed redundancy (e.g., rate 1/3) wastes channel capacity during clear space conditions.",
        "Aggressive Coding: Allocating minimal redundancy (rate 7/8) results in packet corruption and expensive multi-hour ARQ retransmissions."
    ]
    for b in bullets_fec_prob:
        p = tf10a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s10, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "Reinforcement Learning-Based Adaptive FEC", C_GREEN_ACC)
    tb10b = s10.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf10b = tb10b.text_frame
    tf10b.word_wrap = True
    tf10b.margin_left = tf10b.margin_top = 0
    bullets_fec_sol = [
        "Deep Q-Network (DQN) Agent: Evaluates channel SNR, residual contact duration, and current queue occupancy.",
        "Dynamic Code Rate Selection: Real-time adaptation between Reed-Solomon RS(255, 223) and multi-rate LDPC codes.",
        "Empirical Findings (Wang & Li, 2023):",
        "  - 34% reduction in overall delivery latency.",
        "  - 42% decrease in ARQ retransmission volume.",
        "  - Preserves scarce onboard battery energy by eliminating redundant transmissions."
    ]
    for b in bullets_fec_sol:
        p = tf10b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s10, 10)

    # =========================================================================
    # SLIDE 11: THE ROUTING PARADIGM SHIFT: STOCHASTIC TO DETERMINISTIC
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, C_BG_LIGHT)
    add_header(s11, "The Routing Paradigm Shift: From Stochastic to Deterministic", "4. ROUTING PARADIGMS")

    add_card(s11, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "Terrestrial & Ad-Hoc Mobile Routing", C_RED_ACCENT)
    tb11a = s11.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf11a = tb11a.text_frame
    tf11a.word_wrap = True
    tf11a.margin_left = tf11a.margin_top = 0
    bullets_stoch = [
        "Stochastic Mobility: Ground vehicles and pedestrians move unpredictably.",
        "Epidemic Routing (Vahdat & Becker, 2000): Replicates copies of bundles to every node encountered (flooding).",
        "PRoPHET Routing (Lindgren, 2003): Calculates delivery predictability based on historical encounter frequencies.",
        "Why It Fails in Space:",
        "  - Memory exhaustion in spacecraft onboard storage.",
        "  - Extreme energy and bandwidth waste from uncontrolled packet replication.",
        "  - Completely ignores the deterministic laws of orbital mechanics."
    ]
    for b in bullets_stoch:
        p = tf11a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s11, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "The Deep-Space Deterministic Reality", C_AERO_BLUE)
    tb11b = s11.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf11b = tb11b.text_frame
    tf11b.word_wrap = True
    tf11b.margin_left = tf11b.margin_top = 0
    bullets_determ = [
        "Governed by Keplerian Orbital Mechanics: Spacecraft and planetary trajectories are known months or years in advance.",
        "Predictable Contact Windows: Link start times, termination times, transmission rates, and distances are completely deterministic.",
        "Single-Copy Forwarding: Deterministic routing sends a single copy along the optimal path, conserving onboard memory and link capacity.",
        "Foundation for Contact Graph Routing (CGR)."
    ]
    for b in bullets_determ:
        p = tf11b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s11, 11)

    # =========================================================================
    # SLIDE 12: CONTACT GRAPH ROUTING (CGR) ARCHITECTURE & MECHANICS
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, C_BG_LIGHT)
    add_header(s12, "Contact Graph Routing (CGR) Architecture & Mechanics", "4. ROUTING PARADIGMS")

    img_cgr = os.path.join(figures_dir, "contact_graph_routing_flow.png")
    if os.path.exists(img_cgr):
        add_card(s12, Inches(0.8), Inches(1.4), Inches(6.2), Inches(5.4), "CGR Forward Search Workflow", C_SPACE_NAVY)
        s12.shapes.add_picture(img_cgr, Inches(0.95), Inches(2.0), width=Inches(5.9))

    add_card(s12, Inches(7.3), Inches(1.4), Inches(5.2), Inches(5.4), "CGR Mathematical Principles", C_CYAN)
    tb12 = s12.shapes.add_textbox(Inches(7.5), Inches(2.0), Inches(4.8), Inches(4.5))
    tf12 = tb12.text_frame
    tf12.word_wrap = True
    tf12.margin_left = tf12.margin_top = 0
    bullets_cgr_math = [
        "Contact Plan: List of scheduled contacts: C_i = [t_start, t_end, Node_A, Node_B, DataRate].",
        "Volume Limit: Maximum payload capacity: V_i = (t_end - t_start) * DataRate.",
        "Time-Expanded Graph Search: Modified Dijkstra algorithm calculates Earliest Delivery Time (EDT) rather than minimum physical hop count.",
        "Residual Capacity Depletion: As bundles are queued for a contact, the available capacity is decremented. When V_i = 0, CGR finds alternate multi-hop paths."
    ]
    for b in bullets_cgr_math:
        p = tf12.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s12, 12)

    # =========================================================================
    # SLIDE 13: CGR ENHANCEMENTS: CAPACITY & BUFFER CONSTRAINTS
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13, C_BG_LIGHT)
    add_header(s13, "CGR Enhancements: Capacity and Buffer Constraints", "4. ROUTING PARADIGMS")

    add_card(s13, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "The Overbooking Problem in Vanilla CGR", C_RED_ACCENT)
    tb13a = s13.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf13a = tb13a.text_frame
    tf13a.word_wrap = True
    tf13a.margin_left = tf13a.margin_top = 0
    bullets_cgr_flaw = [
        "Uncoordinated Routing: Independent nodes choose the same high-rate relay contact simultaneously.",
        "Contact Overbooking: Arrival volume exceeds contact capacity (V_arr > V_i).",
        "Buffer Overflow & Drops: Excess bundles are discarded at intermediate nodes, requiring costly retransmissions.",
        "Path Blindness: Fails to track dynamic storage availability on downstream relays."
    ]
    for b in bullets_cgr_flaw:
        p = tf13a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s13, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "Modern Enhancements: CGR-ATO & EAR-CGR", C_GREEN_ACC)
    tb13b = s13.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf13b = tb13b.text_frame
    tf13b.word_wrap = True
    tf13b.margin_left = tf13b.margin_top = 0
    bullets_cgr_fix = [
        "CGR-ATO (Avoid Time Overbooking): Tracks remaining contact capacity chronologically, preventing multiple bundles from exceeding contact windows.",
        "EAR-CGR (Energy & Storage Aware): Incorporates battery state-of-charge and flash storage capacity into the edge cost function.",
        "Opportunity-Driven Multi-Pathing: Splits large datasets across multiple parallel planetary orbiters, maximizing throughput."
    ]
    for b in bullets_cgr_fix:
        p = tf13b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s13, 13)

    # =========================================================================
    # SLIDE 14: NEXT-GENERATION AI ROUTING: GRAPH ATTENTION MARL
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14, C_BG_LIGHT)
    add_header(s14, "Next-Generation AI Routing: Graph Attention MARL", "4. ROUTING PARADIGMS")

    add_card(s14, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "Why Traditional CGR Strains in Constellations", C_SPACE_NAVY)
    tb14a = s14.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf14a = tb14a.text_frame
    tf14a.word_wrap = True
    tf14a.margin_left = tf14a.margin_top = 0
    bullets_ai_need = [
        "Mega-Constellations: Lunar/Martian orbital swarms with 50+ satellites produce combinatorially explosive contact graphs.",
        "Non-Deterministic Events: Atmospheric drag, solar panel degradation, surface rover ad-hoc requests, and cross-link jamming create unpredicted contact interruptions.",
        "Computational Strain: Recomputing Dijkstra trees across thousands of contacts exhausts radiation-hardened spacecraft CPUs."
    ]
    for b in bullets_ai_need:
        p = tf14a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s14, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "Graph Attention Multi-Agent RL (GAT-MARL)", C_AERO_BLUE)
    tb14b = s14.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf14b = tb14b.text_frame
    tf14b.word_wrap = True
    tf14b.margin_left = tf14b.margin_top = 0
    bullets_ai_sol = [
        "Distributed Multi-Agent Architecture: Each satellite hosts a local RL agent making autonomous forwarding decisions.",
        "Graph Attention Network (GAT): Dynamically weights neighboring nodes based on residual contact time, link BER, and buffer queue levels.",
        "Centralized Training with Decentralized Execution (CTDE): Trained offline on mission ephemerides, executing in real time onboard with sub-millisecond inference.",
        "Demonstrated 28% higher throughput under unpredictable link disruptions."
    ]
    for b in bullets_ai_sol:
        p = tf14b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s14, 14)

    # =========================================================================
    # SLIDE 15: DEEP SPACE OPTICAL COMMUNICATIONS (DSOC)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15, C_BG_LIGHT)
    add_header(s15, "Deep Space Optical Communications (DSOC)", "5. CROSS-LAYER & FRONTIERS")

    img_dsoc = os.path.join(figures_dir, "paper1_fig_p8_1.png")
    if os.path.exists(img_dsoc):
        add_card(s15, Inches(0.8), Inches(1.4), Inches(6.2), Inches(5.4), "NASA Psyche DSOC Flight Experiment", C_SPACE_NAVY)
        s15.shapes.add_picture(img_dsoc, Inches(0.95), Inches(2.0), width=Inches(5.9))

    add_card(s15, Inches(7.3), Inches(1.4), Inches(5.2), Inches(5.4), "Optical-DTN Synergy & Downlink Scheduling", C_GOLD)
    tb15 = s15.shapes.add_textbox(Inches(7.5), Inches(2.0), Inches(4.8), Inches(4.5))
    tf15 = tb15.text_frame
    tf15.word_wrap = True
    tf15.margin_left = tf15.margin_top = 0
    bullets_dsoc = [
        "Gigabit-Scale Laser Downlinks: DSOC demonstrated 267 Mbps downlinks from 31 million km (130 times Earth-Moon distance).",
        "The Weather Vulnerability: Terrestrial cloud cover and atmospheric turbulence completely block laser signals.",
        "The DTN Solution:",
        "  - Store-Carry-and-Forward buffers gigabit datasets onboard.",
        "  - Bundles burst down when optical ground telescopes report clear skies.",
        "  - Dynamic fallback to S/X-band RF when optical links are obscured."
    ]
    for b in bullets_dsoc:
        p = tf15.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s15, 15)

    # =========================================================================
    # SLIDE 16: HAPS RELAYS & SMALLSAT MICRO-DTN (uD3TN)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16, C_BG_LIGHT)
    add_header(s16, "HAPS Relays & SmallSat Micro-DTN (uD3TN)", "5. CROSS-LAYER & FRONTIERS")

    add_card(s16, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "High Altitude Pseudo-Satellites (HAPS)", C_AERO_BLUE)
    tb16a = s16.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf16a = tb16a.text_frame
    tf16a.word_wrap = True
    tf16a.margin_left = tf16a.margin_top = 0
    bullets_haps = [
        "Stratospheric Solar Platforms: Operate at 20 km altitude, soaring well above terrestrial clouds and weather systems.",
        "Optical Gateways: Act as pristine atmospheric optical receivers for deep-space laser beams.",
        "Relay Downlink: Forward received bundles to terrestrial fiber networks via high-frequency millimeter-wave RF links.",
        "Availability Boost: Elevates deep-space optical link availability from 60% to over 98%."
    ]
    for b in bullets_haps:
        p = tf16a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s16, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "Software-Defined Micro-DTN (uD3TN)", C_GREEN_ACC)
    tb16b = s16.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf16b = tb16b.text_frame
    tf16b.word_wrap = True
    tf16b.margin_left = tf16b.margin_top = 0
    bullets_ud3tn = [
        "Developed for CubeSats & SmallSats by DLR / TU Dresden.",
        "Extreme Lightweight Design: RAM footprint < 100 KB, storage footprint < 256 KB; runs on ARM Cortex-M microcontrollers.",
        "Full BPv7 & LTP Compliance: Implements RFC 9171 and RFC 5326 in memory-safe ANSI C.",
        "Flight Proven: Validated on orbital CubeSat missions (e.g., OPS-SAT, SONATE-2)."
    ]
    for b in bullets_ud3tn:
        p = tf16b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s16, 16)

    # =========================================================================
    # SLIDE 17: DEEP-SPACE CYBER-SECURITY: BPSEC (RFC 9172)
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17, C_BG_LIGHT)
    add_header(s17, "Deep-Space Cyber-Security: Bundle Security Protocol", "5. CROSS-LAYER & FRONTIERS")

    add_card(s17, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "Cryptographic Challenges in Deep Space", C_RED_ACCENT)
    tb17a = s17.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf17a = tb17a.text_frame
    tf17a.word_wrap = True
    tf17a.margin_left = tf17a.margin_top = 0
    bullets_sec_prob = [
        "No Online Certificate Authority (CA): CRL and OCSP lookups fail across multi-hour latencies.",
        "No Interactive Key Negotiation: TLS / Diffie-Hellman handshakes are impossible without real-time round trips.",
        "Untrusted Planetary Relays: Deep space networks rely on commercial and international coalition orbiters; data must be secured in-transit across third-party nodes.",
        "Replay & Spoofing Vulnerability: Spacecraft commands must be strictly authenticated against delayed replay attacks."
    ]
    for b in bullets_sec_prob:
        p = tf17a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s17, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "BPSec Building Blocks (RFC 9172)", C_SPACE_NAVY)
    tb17b = s17.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf17b = tb17b.text_frame
    tf17b.word_wrap = True
    tf17b.margin_left = tf17b.margin_top = 0
    bullets_sec_sol = [
        "Block Integrity Block (BIB): Provides cryptographic digital signatures (HMAC-SHA256, ECDSA) over target blocks, ensuring data integrity and origin authenticity.",
        "Block Confidentiality Block (BCB): Encrypts target block payloads using AES-GCM-256 Authenticated Encryption.",
        "Pre-Shared Key (PSK) Infrastructure: Relies on pre-deployed session keys and schedule-based epoch rotation.",
        "Granular Protection: Enables intermediate relays to read routing headers while keeping the scientific payload encrypted end-to-end."
    ]
    for b in bullets_sec_sol:
        p = tf17b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s17, 17)

    # =========================================================================
    # SLIDE 18: HISTORICAL FLIGHT VALIDATIONS: DINET TO ISS
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18, C_BG_LIGHT)
    add_header(s18, "Historical Flight Validations: From DINET to the ISS", "6. VALIDATION & SYNTHESIS")

    img_dinet = os.path.join(figures_dir, "paper7_fig_p3_1.png")
    if not os.path.exists(img_dinet):
        img_dinet = os.path.join(figures_dir, "paper8_fig_p3_1.png")
    if os.path.exists(img_dinet):
        add_card(s18, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "Flight Experiment Network Topologies", C_SPACE_NAVY)
        s18.shapes.add_picture(img_dinet, Inches(0.95), Inches(2.0), width=Inches(5.4))

    add_card(s18, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "Major In-Flight Operational Milestones", C_AERO_BLUE)
    tb18 = s18.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf18 = tb18.text_frame
    tf18.word_wrap = True
    tf18.margin_left = tf18.margin_top = 0
    bullets_flights = [
        "2008 - Deep Impact Network Experiment (DINET):",
        "  - NASA JPL uploaded DTN code to Deep Impact probe 15 million miles from Earth.",
        "  - Validated 9-node interplanetary network with bundle storage and recovery.",
        "2012 - ISS-to-Earth Rover Teleoperation:",
        "  - ESA Astronaut Sunita Williams remotely drove a LEGO rover in Germany using DTN.",
        "2016 - ISS Operational Payload:",
        "  - Continuous deployment on the International Space Station for science payloads.",
        "2022 - Artemis I Lunar Test:",
        "  - Orion capsule verified DTN/LTP telemetry links back to Earth ground stations."
    ]
    for b in bullets_flights:
        p = tf18.add_paragraph()
        p.text = b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s18, 18)

    # =========================================================================
    # SLIDE 19: THE ARTEMIS ERA: LUNANET & LUNAR GATEWAY
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_background(s19, C_BG_LIGHT)
    add_header(s19, "The Artemis Era: LunaNet and the Lunar Gateway Backbone", "6. VALIDATION & SYNTHESIS")

    add_card(s19, Inches(0.8), Inches(1.4), Inches(5.7), Inches(5.4), "LunaNet Interoperability Architecture", C_SPACE_NAVY)
    tb19a = s19.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf19a = tb19a.text_frame
    tf19a.word_wrap = True
    tf19a.margin_left = tf19a.margin_top = 0
    bullets_lunanet = [
        "NASA & ESA Joint Standard: Published in NASA/TM-2023-0001 (LunaNet Blueprint).",
        "Framework Architecture:",
        "  - Communications Services: Disruption-tolerant relay via BPv7.",
        "  - Positioning, Navigation, and Timing (PNT): Lunar GPS equivalent.",
        "  - Science Utilization Services: Space weather alerts and lunar surface telemetry.",
        "Core Protocol: Mandates BPv7 (RFC 9171), LTP (RFC 5326), and BPSec (RFC 9172) across all international lunar landers, rovers, and orbiters."
    ]
    for b in bullets_lunanet:
        p = tf19a.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_card(s19, Inches(6.8), Inches(1.4), Inches(5.7), Inches(5.4), "The Lunar Gateway as an Interplanetary Hub", C_GOLD)
    tb19b = s19.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
    tf19b = tb19b.text_frame
    tf19b.word_wrap = True
    tf19b.margin_left = tf19b.margin_top = 0
    bullets_gateway = [
        "HALO & PPE Modules: Host high-capacity DTN routing nodes with terabyte solid-state storage.",
        "Near-Rectilinear Halo Orbit (NRHO): Provides continuous line-of-sight to Earth and regular coverage of the lunar South Pole.",
        "Surface-to-Orbit Aggregation: Collects low-power rover data via Ka-band proximity links, bundles it, and blasts it back to Earth via high-gain optical downlinks.",
        "Stepping Stone to Mars: Serves as the operational proving ground for the future Martian Interplanetary Internet."
    ]
    for b in bullets_gateway:
        p = tf19b.add_paragraph()
        p.text = "- " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s19, 19)

    # =========================================================================
    # SLIDE 20: SYNTHESIS MATRIX OF EVALUATED SCIENTIFIC LITERATURE
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    set_slide_background(s20, C_BG_LIGHT)
    add_header(s20, "Comparative Synthesis of Evaluated Scientific Literature", "6. VALIDATION & SYNTHESIS")

    table_shape20 = s20.shapes.add_table(8, 4, Inches(0.8), Inches(1.4), Inches(11.733), Inches(5.3))
    t20 = table_shape20.table
    t20.columns[0].width = Inches(1.8)
    t20.columns[1].width = Inches(2.2)
    t20.columns[2].width = Inches(4.2)
    t20.columns[3].width = Inches(3.533)

    h20 = ["Author & Year", "Protocol / Domain", "Core Scientific Contribution", "Key Performance Milestone"]
    for c_idx, h in enumerate(h20):
        cell = t20.cell(0, c_idx)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_SPACE_NAVY
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

    lit_data = [
        ("Cerf et al. (2007)", "RFC 4838 (DTN)", "Store-Carry-and-Forward overlay architecture", "Foundational interplanetary standard"),
        ("Burleigh et al. (2016)", "CGR / ION", "Deterministic Dijkstra over celestial contact plans", "0% packet drops under scheduled links"),
        ("Blanchet et al. (2022)", "BPv7 (RFC 9171)", "CBOR binary encoding & compressed custody", "35% lower protocol header overhead"),
        ("Farrell et al. (2023)", "BIBE (RFC 9174)", "Recursive bundle encapsulation for subnets", "Cross-domain gateway tunnel traversal"),
        ("Wang & Li (2023)", "Adaptive FEC (LTP)", "Deep Q-Learning dynamic code rate adaptation", "42% reduction in ARQ retransmission volume"),
        ("Zhang & Liu (2024)", "GAT-MARL AI", "Graph Attention Multi-Agent RL for constellations", "28% higher throughput under link jamming"),
        ("NASA / ESA (2023)", "LunaNet Framework", "BPv7 & BPSec for Artemis & Lunar Gateway", "Global standard for future lunar missions")
    ]
    for r_idx, row in enumerate(lit_data):
        for c_idx, val in enumerate(row):
            cell = t20.cell(r_idx + 1, c_idx)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_WHITE if r_idx % 2 == 0 else RGBColor(240, 245, 252)
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9.5)
            p.font.color.rgb = C_TEXT_DARK

    add_footer(s20, 20)

    # =========================================================================
    # SLIDE 21: CRITICAL OPEN RESEARCH CHALLENGES
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    set_slide_background(s21, C_BG_LIGHT)
    add_header(s21, "Critical Open Research Challenges & Future Roadmap", "6. VALIDATION & SYNTHESIS")

    challenges = [
        ("1. Contact Plan Scalability", "Mega-constellations (hundreds of SmallSats) make centralized contact plan distribution intractable. Research needed in decentralized contact discovery."),
        ("2. Quantum Space DTN", "Integrating Quantum Key Distribution (QKD) and quantum entanglement repeaters with asynchronous DTN bundle storage."),
        ("3. Deep-Space AI Security", "Onboard autonomous RL agents are vulnerable to adversarial telemetry poisoning and malicious state manipulation."),
        ("4. Energy-Constrained CubeSats", "Ultra-low power sleep states require synchronized wake-up timers that survive multi-month drift without GPS.")
    ]

    for idx, (head, desc) in enumerate(challenges):
        col = idx % 2
        row = idx // 2
        left = Inches(0.8 + col * 5.9)
        top = Inches(1.5 + row * 2.6)

        c = add_card(s21, left, top, Inches(5.7), Inches(2.3), head, C_RED_ACCENT if idx == 0 else C_AERO_BLUE)
        tb = s21.shapes.add_textbox(left + Inches(0.2), top + Inches(0.65), Inches(5.3), Inches(1.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = 0
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_TEXT_DARK

    add_footer(s21, 21)

    # =========================================================================
    # SLIDE 22: CONCLUSION & SUMMARY OF CONTRIBUTIONS
    # =========================================================================
    s22 = prs.slides.add_slide(blank_layout)
    set_slide_background(s22, C_BG_LIGHT)
    add_header(s22, "Conclusion & Key Seminar Takeaways", "6. VALIDATION & SYNTHESIS")

    add_card(s22, Inches(0.8), Inches(1.4), Inches(11.733), Inches(5.4), "Core Conclusions of the Seminar", C_SPACE_NAVY)
    tb22 = s22.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(11.1), Inches(4.5))
    tf22 = tb22.text_frame
    tf22.word_wrap = True
    tf22.margin_left = tf22.margin_top = 0
    takeaways = [
        "Paradigm Validation: Delay/Disruption Tolerant Networking is the only mathematically and physically viable architecture capable of overcoming astronomical latencies and orbital disruptions.",
        "Maturity of Standards: The transition from experimental BPv6 to IETF-standardized BPv7 (RFC 9171) with CBOR binary encoding and Compressed Custody Signals has resolved legacy scalability flaws.",
        "Deterministic Optimization: Contact Graph Routing (CGR) and emerging Graph Attention MARL AI capitalize on the deterministic predictability of celestial mechanics, achieving optimal data flow with zero redundant packet flooding.",
        "Operational Deployment: DTN has advanced from theoretical simulations (DINET 2008) to mission-critical infrastructure deployed on the ISS, Orion Artemis I, and the LunaNet Lunar Gateway architecture.",
        "Final Vision: Space DTN serves as the foundational protocol stack enabling humanity's permanent autonomous interplanetary internet across the Moon, Mars, and beyond."
    ]
    for idx, t in enumerate(takeaways):
        p = tf22.paragraphs[0] if idx == 0 else tf22.add_paragraph()
        p.text = f"{idx+1}. {t}"
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(8)

    add_footer(s22, 22)

    # =========================================================================
    # SLIDE 23: MAJOR REFERENCES & ACKNOWLEDGEMENTS
    # =========================================================================
    s23 = prs.slides.add_slide(blank_layout)
    set_slide_background(s23, C_BG_LIGHT)
    add_header(s23, "Key Scientific References & Department Acknowledgement", "REFERENCES")

    add_card(s23, Inches(0.8), Inches(1.4), Inches(7.5), Inches(5.4), "Primary Literature Citations", C_SPACE_NAVY)
    tb23a = s23.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(7.1), Inches(4.6))
    tf23a = tb23a.text_frame
    tf23a.word_wrap = True
    tf23a.margin_left = tf23a.margin_top = 0
    refs = [
        "[1] V. Cerf et al., 'Delay-Tolerant Networking Architecture', RFC 4838, IETF, 2007.",
        "[2] K. Fall, 'A delay-tolerant network architecture for challenged internets', ACM SIGCOMM, 2003.",
        "[3] S. Burleigh et al., 'Contact Graph Routing: An Overview', IEEE Comm. Mag., 2016.",
        "[4] M. Blanchet et al., 'Bundle Protocol Version 7', RFC 9171, IETF Standard, 2022.",
        "[5] M. Ramadas et al., 'Licklider Transmission Protocol - Specification', RFC 5326, 2008.",
        "[6] E. Birrane et al., 'Bundle Security Protocol Specification (BPSec)', RFC 9172, 2022.",
        "[7] NASA, 'LunaNet Interoperability Specification', NASA/TM-2023-0001, 2023.",
        "[8] L. Wood et al., 'A critique of custody transfer in DTN', IEEE Aerospace Conf., 2009."
    ]
    for idx, r in enumerate(refs):
        p = tf23a.paragraphs[0] if idx == 0 else tf23a.add_paragraph()
        p.text = r
        p.font.size = Pt(9.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(4)

    add_card(s23, Inches(8.6), Inches(1.4), Inches(3.933), Inches(5.4), "Acknowledgements", C_GOLD)
    tb23b = s23.shapes.add_textbox(Inches(8.8), Inches(2.0), Inches(3.5), Inches(4.6))
    tf23b = tb23b.text_frame
    tf23b.word_wrap = True
    tf23b.margin_left = tf23b.margin_top = 0
    p = tf23b.paragraphs[0]
    p.text = "Academic Gratitude:"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_SPACE_NAVY

    acks = [
        "Supervisor: Dr. Sanjeev Kumar, Assistant Professor, Department of ECE, JNGEC Sundernagar.",
        "Head of Department: Dr. Ashwani Kumar, Department of ECE.",
        "Director: Prof. (Dr.) Rajeshwar Singh, JNGEC Sundernagar.",
        "Faculty Members & Technical Staff of ECE Department for providing continuous academic encouragement and research resources."
    ]
    for a in acks:
        p = tf23b.add_paragraph()
        p.text = "- " + a
        p.font.size = Pt(10)
        p.font.color.rgb = C_TEXT_DARK
        p.space_after = Pt(4)

    add_footer(s23, 23)

    # =========================================================================
    # SLIDE 24: QUESTIONS & INTERACTIVE DISCUSSION (Closing Slide)
    # =========================================================================
    s24 = prs.slides.add_slide(blank_layout)
    set_slide_background(s24, C_SPACE_NAVY)

    # Decorative banner
    strip24 = s24.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.15))
    strip24.fill.solid()
    strip24.fill.fore_color.rgb = C_CYAN
    strip24.line.color.rgb = C_CYAN

    if os.path.exists(logo_path):
        s24.shapes.add_picture(logo_path, Inches(5.8), Inches(1.2), width=Inches(1.7))

    t_box24 = s24.shapes.add_textbox(Inches(1.0), Inches(3.0), Inches(11.333), Inches(2.2))
    tf24 = t_box24.text_frame
    tf24.word_wrap = True
    p = tf24.paragraphs[0]
    p.text = "THANK YOU!"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = C_GOLD

    p = tf24.add_paragraph()
    p.text = "Questions & Discussion"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    p = tf24.add_paragraph()
    p.text = "Delay Tolerant Networks in Space Communications\nDepartment of Electronics & Communication Engineering\nJNGEC Sundernagar (H.P.)"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(13)
    p.font.color.rgb = C_CYAN

    # Contact card
    cc = s24.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.8), Inches(5.4), Inches(5.7), Inches(1.2))
    cc.fill.solid()
    cc.fill.fore_color.rgb = C_NAVY_MID
    cc.line.color.rgb = C_CYAN
    cc.line.width = Pt(1.2)
    tf_cc = cc.text_frame
    tf_cc.margin_top = Inches(0.18)
    p = tf_cc.paragraphs[0]
    p.text = "Vishal Chandel | University Roll No.: 23010104072\nEmail: vishal.ece@jngec.ac.in | Department of ECE"
    p.alignment = PP_ALIGN.CENTER
    p.font.size = Pt(11)
    p.font.color.rgb = RGBColor(220, 235, 255)

    add_footer(s24, 24)

    # Save presentation
    out_pptx = os.path.join("seminar_vishal", "seminar_presentation.pptx")
    prs.save(out_pptx)
    print(f"Successfully generated PowerPoint presentation: {out_pptx} ({len(prs.slides)} slides)")

if __name__ == "__main__":
    create_presentation()
