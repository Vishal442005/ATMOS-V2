import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r = pypdf.PdfReader('dev_report.pdf')
print("Total pages in dev_report.pdf:", len(r.pages))
for i, p in enumerate(r.pages):
    txt = p.extract_text() or ""
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    f = lines[0] if lines else "EMPTY"
    l = lines[-1] if lines else "EMPTY"
    print(f"P{i+1:2d}: {len(txt):4d} chars | Starts: {f[:45]:<45} | Ends: {l[:35]:<35}")
