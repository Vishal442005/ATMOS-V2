import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import os, time, re, json

queries = [
    'ti:"contact graph routing"',
    'abs:"contact graph routing"',
    'ti:"delay-tolerant" AND ti:"space"',
    'ti:"delay-tolerant" AND ti:"satellite"',
    'abs:"bundle protocol" AND abs:"space"',
    'abs:"licklider transmission protocol"',
    'all:"deep space" AND all:"delay-tolerant network"',
    'all:"interplanetary internet" AND all:"delay tolerant"',
    'all:"lunar" AND all:"delay tolerant network"',
    'ti:"DTN" AND all:"satellite"'
]

with open('seminar_vishal/papers_metadata.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

existing_ids = {p['arxiv_id']: p for p in existing}
print(f"Loaded {len(existing_ids)} existing papers.")

ns = {'atom': 'http://www.w3.org/2005/Atom'}

for q in queries:
    url = f"http://export.arxiv.org/api/query?search_query={urllib.parse.quote(q)}&start=0&max_results=10"
    print(f"Querying: {q}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        root = ET.fromstring(data)
        
        for entry in root.findall('atom:entry', ns):
            id_text = entry.find('atom:id', ns).text.strip()
            arxiv_id = id_text.split('/abs/')[-1]
            if arxiv_id in existing_ids:
                continue
            
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            title = re.sub(r'\s+', ' ', title)
            
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            summary = re.sub(r'\s+', ' ', summary)
            
            published = entry.find('atom:published', ns).text.strip()[:4]
            authors = [a.find('atom:name', ns).text.strip() for a in entry.findall('atom:author', ns)]
            pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            
            p_obj = {
                'arxiv_id': arxiv_id,
                'title': title,
                'authors': authors,
                'year': published,
                'summary': summary,
                'pdf_url': pdf_url
            }
            existing_ids[arxiv_id] = p_obj
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1.2)

all_papers = list(existing_ids.values())
print(f"Total papers now: {len(all_papers)}")

with open('seminar_vishal/papers_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(all_papers, f, indent=2)
