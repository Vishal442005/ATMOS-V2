import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r = pypdf.PdfReader('seminar_vishal/seminar.pdf')
print(f"Total pages: {len(r.pages)}")
for i, page in enumerate(r.pages):
    txt = page.extract_text() or ""
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    first_3 = " // ".join(lines[:3]) if lines else "EMPTY"
    print(f"Page {i+1:2d} ({len(txt):4d} chars): {first_3[:90]}")
