import json, os

with open('seminar_vishal/extracted_figures_meta.json', 'r', encoding='utf-8') as f:
    figs = json.load(f)

with open('seminar_vishal/selected_16_papers.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)

papers_dict = {i+1: p for i, p in enumerate(papers)}

print(f"Total figures: {len(figs)}")
for fig in figs:
    p = papers_dict.get(fig['paper_num'], {})
    p_title = p.get('title', 'Unknown')[:35]
    print(f"P{fig['paper_num']} [{fig['file']}]: {fig.get('width', 'N/A')}x{fig.get('height', 'N/A')} - Paper: {p_title}")
