import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r1 = pypdf.PdfReader('dev_report_build/main.pdf')
r2 = pypdf.PdfReader('dev_report.pdf')

print("main.pdf pages:", len(r1.pages))
print("dev_report.pdf pages:", len(r2.pages))

# Check what the extra 3 pages in dev_report.pdf are, or where they diverge
for i in range(min(len(r1.pages), len(r2.pages))):
    t1 = r1.pages[i].extract_text() or ""
    t2 = r2.pages[i].extract_text() or ""
    if t1.strip() != t2.strip():
        print(f"Diverges at page {i+1}")
        print("--- main.pdf ---")
        print(t1[:200])
        print("--- dev_report.pdf ---")
        print(t2[:200])
        break
