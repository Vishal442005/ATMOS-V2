import os, shutil
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

os.makedirs('vishal_report_build/figures', exist_ok=True)

def generate_vishal_certificate():
    pdf_path = 'vishal_report_build/certificate.pdf'
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    
    # Outer Border
    c.setStrokeColor(colors.HexColor('#0a2540'))
    c.setLineWidth(3)
    c.rect(20, 20, width - 40, height - 40)
    
    # Inner Border
    c.setStrokeColor(colors.HexColor('#635bff'))
    c.setLineWidth(1)
    c.rect(26, 26, width - 52, height - 52)
    
    # Top Header
    c.setFont("Helvetica-Bold", 17)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawCentredString(width/2.0, height - 60, "DR. B. R. AMBEDKAR NATIONAL INSTITUTE OF TECHNOLOGY")
    c.drawCentredString(width/2.0, height - 80, "JALANDHAR, PUNJAB -- 144027")
    
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawCentredString(width/2.0, height - 100, "DEPARTMENT OF INSTRUMENTATION AND CONTROL ENGINEERING")
    
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#666666'))
    c.drawCentredString(width/2.0, height - 115, "G.T. Road Amritsar Bypass, Jalandhar, Punjab (India) | Web: www.nitj.ac.in")
    
    # Horizontal rule
    c.setStrokeColor(colors.HexColor('#0a2540'))
    c.setLineWidth(1.5)
    c.line(45, height - 125, width - 45, height - 125)
    
    # Ref & Date
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(45, height - 145, "Ref No.: NITJ/ICE/2026/INTERN/072")
    c.drawRightString(width - 45, height - 145, "Date: 28 July 2026")
    
    # Title
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawCentredString(width/2.0, height - 180, "CERTIFICATE OF RESEARCH INTERNSHIP")
    
    # Line under title
    c.setStrokeColor(colors.HexColor('#e63946'))
    c.setLineWidth(2)
    c.line(width/2.0 - 160, height - 188, width/2.0 + 160, height - 188)
    
    # Body text lines
    lines = [
        "This is to certify that Mr. Vishal Chandel, Roll Number 23010104072, a bona fide undergraduate",
        "student of Bachelor of Technology in Electronics and Communication Engineering at Jawaharlal",
        "Nehru Government Engineering College, Sundernagar (H.P.), has successfully and diligently",
        "completed six weeks of advanced industrial research internship from 17 June 2026 to 28 July 2026",
        "at the Department of Instrumentation and Control Engineering, National Institute of Technology,",
        "Jalandhar.",
        "",
        "During this tenure, he carried out cutting-edge research on the project entitled:",
        "",
        "\"Study of EEG Signals Using Machine Learning Techniques: Triple-Layer MetaModel",
        "for Automated Alcoholic EEG Classification and Biomedical Diagnostic Analysis\"",
        "",
        "His investigation encompassed multichannel EEG data preprocessing, 0.5-50 Hz zero-phase bandpass",
        "filtering, canonical brainwave frequency decomposition (Delta, Theta, Alpha, Beta, Gamma), spatial",
        "electrode topology mapping, baseline machine learning benchmark comparisons (LVQ, PCA, k-NN),",
        "and the formulation of a novel deep learning architecture integrating 1D Residual CNNs, Squeeze-and-",
        "Excitation channel attention, and Bidirectional LSTM networks with a highway gated meta-classifier.",
        "",
        "Mr. Vishal Chandel demonstrated outstanding theoretical knowledge, exceptional programming competence",
        "in PyTorch, rigorous scientific methodology, and exemplary dedication throughout the training period.",
        "His performance in the project and final departmental defense was graded as Outstanding (Grade: A+).",
        "",
        "We wish him the very best and continued success in all his academic and professional future endeavors."
    ]
    
    y = height - 220
    for l in lines:
        if l == "":
            y -= 10
            continue
        if "Triple-Layer MetaModel" in l or "Study of EEG Signals" in l:
            c.setFont("Helvetica-BoldOblique", 10.5)
            c.setFillColor(colors.HexColor('#0a2540'))
            c.drawCentredString(width/2.0, y, l)
            y -= 16
        else:
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.HexColor('#111111'))
            c.drawString(45, y, l)
            y -= 14.5
            
    # Signatures
    y_sig = 90
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawString(50, y_sig + 35, "Dr. Richa Sharma")
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(50, y_sig + 22, "Internship Research Supervisor")
    c.drawString(50, y_sig + 10, "Professor, Dept. of Instrumentation & Control Engg.")
    c.drawString(50, y_sig - 2, "National Institute of Technology Jalandhar")
    
    # Official Seal circle
    c.setStrokeColor(colors.HexColor('#1d3557'))
    c.setLineWidth(1.2)
    c.circle(width/2.0, y_sig + 15, 30)
    c.setFont("Helvetica-Bold", 6.5)
    c.setFillColor(colors.HexColor('#1d3557'))
    c.drawCentredString(width/2.0, y_sig + 20, "NIT JALANDHAR")
    c.drawCentredString(width/2.0, y_sig + 10, "DEPT. OF ICE")
    c.drawCentredString(width/2.0, y_sig, "* RESEARCH SEAL *")
    
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawRightString(width - 50, y_sig + 35, "Head of Department")
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawRightString(width - 50, y_sig + 22, "Dept. of Instrumentation & Control Engg.")
    c.drawRightString(width - 50, y_sig + 10, "National Institute of Technology Jalandhar")
    c.drawRightString(width - 50, y_sig - 2, "G.T. Road, Jalandhar (Punjab)")
    
    # Bottom Note
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.gray)
    c.drawCentredString(width/2.0, 36, "Verified against departmental training and research records. Issued under academic seal.")
    
    c.save()
    shutil.copy2(pdf_path, 'vishal_report_build/figures/certificate.pdf')
    print("Vishal certificate generated at:", pdf_path)

def generate_vishal_evaluation():
    pdf_path = 'vishal_report_build/evaluation.pdf'
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    
    # Border
    c.setStrokeColor(colors.HexColor('#0a2540'))
    c.setLineWidth(2)
    c.rect(30, 30, width - 60, height - 60)
    
    # Top Header
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawCentredString(width/2.0, height - 65, "DR. B. R. AMBEDKAR NATIONAL INSTITUTE OF TECHNOLOGY")
    c.drawCentredString(width/2.0, height - 83, "JALANDHAR -- 144027 (PUNJAB)")
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawCentredString(width/2.0, height - 100, "DEPARTMENT OF INSTRUMENTATION AND CONTROL ENGINEERING")
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawCentredString(width/2.0, height - 125, "INTERNSHIP PERFORMANCE EVALUATION SHEET")
    
    # Line
    c.setStrokeColor(colors.HexColor('#0a2540'))
    c.setLineWidth(1)
    c.line(45, height - 135, width - 45, height - 135)
    
    # Details Grid
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)
    
    c.drawString(50, height - 160, "Name of Trainee: Vishal Chandel")
    c.drawString(330, height - 160, "University Roll No.: 23010104072")
    c.drawString(50, height - 180, "Degree: B.Tech (ECE), 7th Semester")
    c.drawString(330, height - 180, "College: JNGEC Sundernagar (H.P.)")
    c.drawString(50, height - 200, "Training Period: 17/06/2026 to 28/07/2026")
    c.drawString(330, height - 200, "Duration: 6 Weeks (Full Time)")
    c.drawString(50, height - 220, "Project Title: Study of EEG Signals Using Machine Learning Techniques")
    c.drawString(50, height - 238, "Supervisor: Dr. Richa Sharma, Professor, Department of ICE, NIT Jalandhar")
    
    # Table of Evaluation
    y_table = height - 265
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    
    # Table header
    c.setFillColor(colors.HexColor('#f0f4f8'))
    c.rect(48, y_table - 22, width - 96, 22, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawString(55, y_table - 15, "S.No.")
    c.drawString(95, y_table - 15, "Evaluation Parameter / Performance Attribute")
    c.drawString(380, y_table - 15, "Max Marks")
    c.drawString(460, y_table - 15, "Marks Awarded")
    
    criteria = [
        ("1", "Regularity, Attendance & Professional Discipline", "10", "10"),
        ("2", "Theoretical Grasp & Biomedical Domain Knowledge", "10", "10"),
        ("3", "Algorithm Formulation & PyTorch Implementation Rigor", "10", "10"),
        ("4", "Experimental Validation & Cross-Validation Methodology", "10", "10"),
        ("5", "Technical Documentation, Report Writing & Presentation", "10", "10"),
        ("6", "Viva-Voce Defense & Inquisitive Problem Solving", "10", "09"),
    ]
    
    y_row = y_table - 22
    for s_no, param, mx, aw in criteria:
        c.setFillColor(colors.white)
        c.rect(48, y_row - 22, width - 96, 22, fill=1, stroke=1)
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.black)
        c.drawString(65, y_row - 15, s_no)
        c.drawString(95, y_row - 15, param)
        c.drawCentredString(410, y_row - 15, mx)
        c.setFont("Helvetica-Bold", 9.5)
        c.drawCentredString(500, y_row - 15, aw)
        y_row -= 22
        
    # Total row
    c.setFillColor(colors.HexColor('#e8eef5'))
    c.rect(48, y_row - 24, width - 96, 24, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawString(95, y_row - 16, "TOTAL MARKS OBTAINED")
    c.drawCentredString(410, y_row - 16, "60")
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawCentredString(500, y_row - 16, "59")
    
    # Grading Scale Summary
    y_grade = y_row - 50
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.black)
    c.drawString(50, y_grade, "Overall Performance Grade: OUTSTANDING (Grade: A+)")
    
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(50, y_grade - 20, "Supervisor's Qualitative Remarks:")
    c.setFont("Helvetica", 9)
    remarks = [
        "Mr. Vishal Chandel displayed exemplary dedication, exceptional analytical skills, and outstanding programming",
        "aptitude in biomedical signal processing. His development of the Triple-Layer MetaModel and multi-branch spatio-",
        "temporal architecture showed remarkable scientific maturity. He actively participated in departmental research",
        "seminars and submitted comprehensive documentation along with fully verified experimental results."
    ]
    y_rem = y_grade - 35
    for r in remarks:
        c.drawString(50, y_rem, r)
        y_rem -= 14
        
    # Signatures
    y_eval_sig = 90
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawString(50, y_eval_sig + 35, "Dr. Richa Sharma")
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(50, y_eval_sig + 22, "Internship Research Supervisor")
    c.drawString(50, y_eval_sig + 10, "Professor, Dept. of ICE, NIT Jalandhar")
    
    # Official Seal circle
    c.setStrokeColor(colors.HexColor('#1d3557'))
    c.setLineWidth(1.2)
    c.circle(width/2.0, y_eval_sig + 15, 30)
    c.setFont("Helvetica-Bold", 6.5)
    c.setFillColor(colors.HexColor('#1d3557'))
    c.drawCentredString(width/2.0, y_eval_sig + 20, "NIT JALANDHAR")
    c.drawCentredString(width/2.0, y_eval_sig + 10, "DEPT. OF ICE")
    c.drawCentredString(width/2.0, y_eval_sig, "* EVALUATED *")
    
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(colors.HexColor('#0a2540'))
    c.drawRightString(width - 50, y_eval_sig + 35, "Training Coordinator / HOD")
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawRightString(width - 50, y_eval_sig + 22, "Department of ICE")
    c.drawRightString(width - 50, y_eval_sig + 10, "NIT Jalandhar (Punjab)")
    
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.gray)
    c.drawCentredString(width/2.0, 36, "Official industrial training evaluation record. Jawaharlal Nehru Govt. Engineering College.")
    
    c.save()
    shutil.copy2(pdf_path, 'vishal_report_build/figures/evaluation.pdf')
    print("Vishal evaluation generated at:", pdf_path)

generate_vishal_certificate()
generate_vishal_evaluation()
