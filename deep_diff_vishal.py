import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r1 = pypdf.PdfReader('vishal_report_build/main.pdf')
r2 = pypdf.PdfReader('vishal_report.pdf')

print("Page count 1:", len(r1.pages))
print("Page count 2:", len(r2.pages))

diffs = []
for i in range(len(r1.pages)):
    t1 = r1.pages[i].extract_text() or ""
    t2 = r2.pages[i].extract_text() or ""
    if t1.strip() != t2.strip():
        diffs.append(i+1)

print(f"Diff pages count: {len(diffs)}, pages: {diffs}")
for p in diffs:
    print(f"\n================ PAGE {p} ================")
    t1 = r1.pages[p-1].extract_text() or ""
    t2 = r2.pages[p-1].extract_text() or ""
    print(f"--- BUILD (len={len(t1)}) ---")
    print(t1[:300])
    print(f"--- ROOT (len={len(t2)}) ---")
    print(t2[:300])
