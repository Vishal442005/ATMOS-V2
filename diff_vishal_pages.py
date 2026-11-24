import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r_build = pypdf.PdfReader('vishal_report_build/main.pdf')
r_root = pypdf.PdfReader('vishal_report.pdf')

for p in [0, 1, 6, 7, 8, 9, 10, 11]:
    print(f"=== PAGE {p+1} ===")
    print("--- BUILD ---")
    print(r_build.pages[p].extract_text()[:300])
    print("--- ROOT ---")
    print(r_root.pages[p].extract_text()[:300])
