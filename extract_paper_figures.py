import fitz # PyMuPDF
import glob, os, json

os.makedirs('seminar_vishal/figures', exist_ok=True)

# Load selected papers metadata
with open('seminar_vishal/selected_16_papers.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)

print(f"Processing figures for {len(papers)} selected papers...")

extracted_figs = []

for i, p in enumerate(papers, 1):
    pdf_path = p.get('local_pdf')
    if not pdf_path or not os.path.exists(pdf_path):
        continue
    
    doc = fitz.open(pdf_path)
    safe_title = p['title'].encode('ascii', errors='replace').decode()[:40]
    print(f"\n--- Paper {i}: [{p['arxiv_id']}] {safe_title} ---")
    
    # 1. Search for embedded raster images
    found_embedded = 0
    for page_idx, page in enumerate(doc):
        image_list = page.get_images(full=True)
        for img_idx, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            width = base_image["width"]
            height = base_image["height"]
            
            # Filter out tiny icons, logos, or 1x1 spacer pixels
            if width > 200 and height > 150:
                fig_filename = f"paper{i}_fig_p{page_idx+1}_{img_idx+1}.{image_ext}"
                fig_path = os.path.join('seminar_vishal/figures', fig_filename)
                with open(fig_path, "wb") as f_img:
                    f_img.write(image_bytes)
                print(f"  Extracted image: {fig_filename} ({width}x{height})")
                extracted_figs.append({
                    'paper_num': i,
                    'arxiv_id': p['arxiv_id'],
                    'page': page_idx + 1,
                    'file': fig_filename,
                    'width': width,
                    'height': height,
                    'type': 'embedded'
                })
                found_embedded += 1
                if found_embedded >= 3: # limit per paper so we don't extract 50 plots from a single paper
                    break
        if found_embedded >= 3:
            break
            
    # 2. If no embedded raster images (many IEEE/ACM papers use vector PDF drawings for architectures and flowcharts),
    # let's render the pages that contain "Fig." or "Figure" with rect or page render!
    if found_embedded == 0:
        print("  No raster images found; searching for vector diagrams...")
        for page_idx, page in enumerate(doc):
            text = page.get_text().lower()
            if "fig." in text or "figure" in text or "architecture" in text or "topology" in text:
                pix = page.get_pixmap(dpi=200)
                fig_filename = f"paper{i}_diagram_p{page_idx+1}.png"
                fig_path = os.path.join('seminar_vishal/figures', fig_filename)
                pix.save(fig_path)
                print(f"  Rendered diagram page: {fig_filename}")
                extracted_figs.append({
                    'paper_num': i,
                    'arxiv_id': p['arxiv_id'],
                    'page': page_idx + 1,
                    'file': fig_filename,
                    'type': 'rendered_page'
                })
                break

print(f"\nTotal extracted figures: {len(extracted_figs)}")
with open('seminar_vishal/extracted_figures_meta.json', 'w', encoding='utf-8') as f:
    json.dump(extracted_figs, f, indent=2)
