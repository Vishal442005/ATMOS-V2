import pypdf
import os
import re
import json

papers = [f for f in os.listdir("downloaded_papers") if f.endswith(".pdf")]
analysis = {}

for p in papers:
    path = os.path.join("downloaded_papers", p)
    try:
        reader = pypdf.PdfReader(path)
        num_pages = len(reader.pages)
        full_text = ""
        figures = []
        tables = []
        headings = []
        
        for idx, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            full_text += f"\n--- Page {idx+1} ---\n" + text
            
            # Find figure captions
            fig_matches = re.findall(r'(Fig(?:ure)?\.?\s*\d+[:\.\-]\s*[^.\n]+(?:\.[^.\n]+)?)', text, re.IGNORECASE)
            figures.extend(fig_matches)
            
            # Find table captions
            tbl_matches = re.findall(r'(Table\s*\d+[:\.\-]\s*[^.\n]+)', text, re.IGNORECASE)
            tables.extend(tbl_matches)
            
            # Find major headings
            head_matches = re.findall(r'(\n(?:\d+\.?\s+|[I|V|X]+\.\s+)[A-Z][A-Za-z\s]{3,40}\n)', text)
            headings.extend([h.strip() for h in head_matches])

        # Extract title and abstract from first 2 pages
        p1_2 = "".join([(reader.pages[i].extract_text() or "") for i in range(min(2, num_pages))])
        
        # Check metrics mentioned
        metrics_found = []
        for m in ['RMSE', 'MAE', 'R2', 'R^2', 'MAPE', 'MBE', 'Mean Bias', 'correlation', 'PDR', 'latency', 'power', 'mW', 'mAh', 'Bland-Altman', 'BAM-1020', 'TEOM']:
            if re.search(r'\b' + re.escape(m) + r'\b', full_text, re.IGNORECASE):
                metrics_found.append(m)

        analysis[p] = {
            "num_pages": num_pages,
            "headings_sample": list(set(headings))[:10],
            "figures_count": len(figures),
            "figures_sample": figures[:8],
            "tables_count": len(tables),
            "tables_sample": tables[:6],
            "metrics_found": metrics_found,
            "abstract_snippet": p1_2[:600].replace('\n', ' ')
        }
    except Exception as e:
        analysis[p] = {"error": str(e)}

with open("papers_deep_analysis.json", "w", encoding="utf-8") as out:
    json.dump(analysis, out, indent=2)

print("Analyzed", len(papers), "papers successfully.")
for p, data in analysis.items():
    print(f"\n==========================================")
    print(f"Paper: {p} ({data.get('num_pages')} pages)")
    print(f"Metrics: {data.get('metrics_found')}")
    print(f"Figures ({data.get('figures_count')} found): {data.get('figures_sample')[:3]}")
    print(f"Tables ({data.get('tables_count')} found): {data.get('tables_sample')[:2]}")
    print(f"Headings: {data.get('headings_sample')[:5]}")
