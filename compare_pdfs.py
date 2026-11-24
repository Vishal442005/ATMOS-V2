import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== VISHAL_REPORT.PDF ===")
r_vr = pypdf.PdfReader('vishal_report.pdf')
print(f"Total pages: {len(r_vr.pages)}")
for i in range(min(15, len(r_vr.pages))):
    txt = r_vr.pages[i].extract_text() or ""
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    first_line = lines[0] if lines else "EMPTY"
    print(f"  P{i+1}: len={len(txt)} | {first_line[:70]}")

print("\n=== SEMINAR_VISHAL/SEMINAR.PDF ===")
r_sem = pypdf.PdfReader('seminar_vishal/seminar.pdf')
print(f"Total pages: {len(r_sem.pages)}")
for i in range(min(15, len(r_sem.pages))):
    txt = r_sem.pages[i].extract_text() or ""
    lines = [l.strip() for l in txt.splitlines() if l.strip()]
    first_line = lines[0] if lines else "EMPTY"
    print(f"  P{i+1}: len={len(txt)} | {first_line[:70]}")
