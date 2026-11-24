import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect seminar.pdf metadata and streams
reader = pypdf.PdfReader('seminar_vishal/seminar.pdf')
print("Metadata:", reader.metadata)
print(f"Num pages: {len(reader.pages)}")

# Print text of first 3 pages and any differences
for i in range(len(reader.pages)):
    t = reader.pages[i].extract_text() or ""
    # Check if there are any comments, annotations, or structural changes
    annots = reader.pages[i].get('/Annots')
    if annots:
        print(f"Page {i+1} has {len(annots)} annotations!")
