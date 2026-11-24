# verify_compiled_pages.py
import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"dev_report_build\main.pdf"
reader = pypdf.PdfReader(pdf_path)
total_pages = len(reader.pages)
print(f"=== TOTAL PAGES: {total_pages} ===")

suspicious_pages = []

for idx, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    chars = len(text.strip())
    first_line = text.strip().splitlines()[0] if text.strip() else "[BLANK PAGE]"
    last_line = text.strip().splitlines()[-1] if text.strip() else "[BLANK PAGE]"
    
    # Check for empty or very short pages (< 250 chars)
    if chars < 250:
        suspicious_pages.append((idx + 1, chars, first_line))
        print(f"Page {idx+1:2d}: [WARNING: LOW CHAR COUNT {chars:3d}] -> {first_line[:60]}")
    else:
        print(f"Page {idx+1:2d}: {chars:4d} chars | Starts: {first_line[:35]} | Ends: {last_line[:35]}")

print("\n--- SUMMARY OF LOW-CHAR PAGES ---")
if not suspicious_pages:
    print("Zero empty or low-char pages found! Layout is tightly packed and perfectly fitting.")
else:
    for p, c, l in suspicious_pages:
        print(f"Page {p}: {c} chars -> {l}")
