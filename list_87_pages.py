import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r = pypdf.PdfReader('dev_report_build/main.pdf')
print("Total pages:", len(r.pages))
for i, p in enumerate(r.pages):
    txt = p.extract_text() or ""
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    f = lines[0] if lines else "EMPTY"
    l = lines[-1] if lines else "EMPTY"
    figs = [line for line in lines if "Figure" in line or "Table" in line]
    f_str = f" | {figs[0][:35]}" if figs else ""
    print(f"P{i+1:2d} ({len(txt):4d}c): {f[:35]:<35} | {l[:25]:<25}{f_str}")
