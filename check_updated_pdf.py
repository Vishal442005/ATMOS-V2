import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')
r = pypdf.PdfReader('seminar_vishal/seminar.pdf')
for i in range(5):
    print(f"=== PAGE {i+1} ===")
    print(r.pages[i].extract_text())
