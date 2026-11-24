import json, os, urllib.request, time

with open('seminar_vishal/papers_metadata.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Define criteria to select top 16 distinct papers that cover the evolutionary progression
selected_papers = []

# Keywords to classify into evolutionary themes
themes = {
    'lunar_ai': ['lunar', 'reinforcement learning', 'marl'],
    'cgr_optimization': ['cgr', 'contact graph', 'tsrcg', 'buffer constraints', 'capacity'],
    'ltp_transport': ['ltp', 'licklider', 'fec', 'transport'],
    'bundle_redmars': ['bundle-in-bundle', 'redmars', 'recursive', 'border gateway', 'endpoint identifier'],
    'satellite_traffic': ['heterogeneous', 'downlinks', 'harvest', 'satellite network'],
    'architectural_models': ['algebraic', 'mobility pattern', 'improving an approach', 'capacity limits']
}

# We can score each paper for space DTN relevance
for p in papers:
    text = (p['title'] + " " + p['summary']).lower()
    score = 0
    # Higher score for explicitly space, satellite, lunar, mars, interplanetary, CGR, LTP, bundle
    if 'space' in text: score += 3
    if 'satellite' in text: score += 3
    if 'lunar' in text or 'mars' in text or 'interplanetary' in text: score += 4
    if 'contact graph' in text or 'cgr' in text: score += 4
    if 'ltp' in text or 'licklider' in text: score += 4
    if 'bundle protocol' in text or 'bundle-in-bundle' in text: score += 4
    if 'delay-tolerant' in text or 'delay tolerant' in text: score += 2
    if 'routing' in text: score += 1
    p['space_score'] = score

papers.sort(key=lambda x: x['space_score'], reverse=True)

# Select top 16 distinct papers
final_selected = []
seen_titles = set()
for p in papers:
    # Avoid duplicates
    base_title = p['title'].lower()[:30]
    if base_title in seen_titles:
        continue
    # Filter out purely vehicular terrestrial unless explicitly relevant
    if 'vehicular' in p['title'].lower() and 'space' not in p['title'].lower():
        continue
    seen_titles.add(base_title)
    final_selected.append(p)
    if len(final_selected) == 16:
        break

print(f"Selected {len(final_selected)} top papers:")
for i, p in enumerate(final_selected, 1):
    safe_title = p['title'].encode('ascii', errors='replace').decode()
    print(f"{i}. [{p['arxiv_id']}] ({p['year']}) Score {p['space_score']}: {safe_title}")

with open('seminar_vishal/selected_16_papers.json', 'w', encoding='utf-8') as f:
    json.dump(final_selected, f, indent=2)

# Download PDFs
os.makedirs('seminar_vishal/papers', exist_ok=True)

for i, p in enumerate(final_selected, 1):
    safe_id = p['arxiv_id'].replace('/', '_')
    pdf_path = os.path.join('seminar_vishal/papers', f"paper_{i}_{safe_id}.pdf")
    p['local_pdf'] = pdf_path
    
    if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 10000:
        print(f"[{i}/16] Already downloaded: {pdf_path}")
        continue
        
    safe_t = p['title'][:50].encode('ascii', errors='replace').decode()
    print(f"[{i}/16] Downloading {safe_t}... from {p['pdf_url']}")
    try:
        req = urllib.request.Request(p['pdf_url'], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=30) as resp, open(pdf_path, 'wb') as out:
            out.write(resp.read())
        print(f"     Saved ({os.path.getsize(pdf_path)} bytes)")
    except Exception as e:
        print(f"     Failed: {e}")
    time.sleep(1.0)

with open('seminar_vishal/selected_16_papers.json', 'w', encoding='utf-8') as f:
    json.dump(final_selected, f, indent=2)

print("\nAll downloads completed!")
