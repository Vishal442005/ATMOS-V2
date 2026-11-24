# generate_full_riya_tex.py
# Writes the complete, rigorous, publication-grade main.tex for Riya Kumari's Internship Report.

import os

os.makedirs('riya_report_build', exist_ok=True)
tex_file = os.path.join('riya_report_build', 'main.tex')

print("Starting generation of main.tex...")
