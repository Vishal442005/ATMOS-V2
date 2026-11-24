import os, glob
import pypdfium2 as pdfium
from PIL import Image

pdf_files = sorted(glob.glob('seminar_vishal/papers/*.pdf'))
print(f"Found {len(pdf_files)} PDFs in seminar_vishal/papers/")

os.makedirs('seminar_vishal/figures/extracted', exist_ok=True)

# For each PDF, let's render select pages or inspect if there are images
# Rendering pages with high resolution allows us to crop or use architectural figures directly,
# or we can extract embedded images.
for i, pdf_path in enumerate(pdf_files[:5], 1):
    doc = pdfium.PdfDocument(pdf_path)
    print(f"Paper {i}: {os.path.basename(pdf_path)} - {len(doc)} pages")
    # render page 1 and page 2 or find pages with diagrams
    for p_num in range(min(5, len(doc))):
        page = doc[p_num]
        # check page text for keywords like 'Figure', 'Fig.', 'architecture', 'routing', 'topology'
        textpage = page.get_textpage()
        text = textpage.get_text_range().lower()
        if 'figure' in text or 'fig.' in text or 'architecture' in text or 'topology' in text:
            img = page.render(scale=2.0).to_pil()
            out_name = f"paper{i}_page{p_num+1}.png"
            img.save(os.path.join('seminar_vishal/figures/extracted', out_name), quality=85)
            print(f"  Extracted page {p_num+1} -> {out_name}")
            break
