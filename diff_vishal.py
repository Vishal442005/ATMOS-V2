import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r1 = pypdf.PdfReader('vishal_report_build/main.pdf')
r2 = pypdf.PdfReader('vishal_report.pdf')

print(f"vishal_report_build/main.pdf: {len(r1.pages)} pages")
print(f"vishal_report.pdf: {len(r2.pages)} pages")

diffs = []
for i in range(min(len(r1.pages), len(r2.pages))):
    t1 = r1.pages[i].extract_text() or ""
    t2 = r2.pages[i].extract_text() or ""
    if t1 != t2:
        diffs.append((i+1, len(t1), len(t2)))

print(f"Total page diffs in first {min(len(r1.pages), len(r2.pages))} pages: {len(diffs)}")
for d in diffs[:10]:
    print(f"  Page {d[0]}: build_len={d[1]}, root_len={d[2]}")
