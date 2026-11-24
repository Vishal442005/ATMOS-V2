import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r1 = pypdf.PdfReader('test_tectonic/seminar.pdf')
r2 = pypdf.PdfReader('seminar_vishal/seminar.pdf')

print(f"test_tectonic/seminar.pdf pages: {len(r1.pages)}")
print(f"seminar_vishal/seminar.pdf pages: {len(r2.pages)}")

diff_pages = []
for i in range(len(r1.pages)):
    t1 = r1.pages[i].extract_text() or ""
    t2 = r2.pages[i].extract_text() or ""
    if t1 != t2:
        diff_pages.append(i+1)

print(f"Pages with different text: {diff_pages}")
for p in diff_pages:
    print(f"\n--- Page {p} difference ---")
    t1 = r1.pages[p-1].extract_text() or ""
    t2 = r2.pages[p-1].extract_text() or ""
    print("COMPILED:")
    print(t1[:250])
    print("CURRENT IN SEMINAR_VISHAL:")
    print(t2[:250])
