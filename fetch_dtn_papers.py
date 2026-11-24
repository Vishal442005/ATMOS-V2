import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import os, time, re, json

queries = [
    'all:"delay tolerant network" AND all:"space"',
    'all:"contact graph routing" AND all:"space"',
    'all:"bundle protocol" AND all:"interplanetary"',
    'all:"licklider transmission protocol" OR all:"LTP"',
    'all:"delay-tolerant" AND all:"satellite"'
]

papers = []
seen_ids = set()

for q in queries:
    url = f"http://export.arxiv.org/api/query?search_query={urllib.parse.quote(q)}&start=0&max_results=12"
    print(f"Querying arXiv: {q}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        root = ET.fromstring(data)
        
        # namespace for Atom
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        for entry in root.findall('atom:entry', ns):
            id_text = entry.find('atom:id', ns).text.strip()
            arxiv_id = id_text.split('/abs/')[-1]
            if arxiv_id in seen_ids:
                continue
            seen_ids.add(arxiv_id)
            
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            title = re.sub(r'\s+', ' ', title)
            
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            summary = re.sub(r'\s+', ' ', summary)
            
            published = entry.find('atom:published', ns).text.strip()[:4]
            
            authors = [a.find('atom:name', ns).text.strip() for a in entry.findall('atom:author', ns)]
            
            pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
            
            papers.append({
                'arxiv_id': arxiv_id,
                'title': title,
                'authors': authors,
                'year': published,
                'summary': summary,
                'pdf_url': pdf_url
            })
    except Exception as e:
        print(f"Error querying {q}: {e}")
    time.sleep(1.5)

print(f"\nTotal unique papers fetched: {len(papers)}")

with open('seminar_vishal/papers_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(papers, f, indent=2)

for i, p in enumerate(papers[:20], 1):
    print(f"{i}. [{p['arxiv_id']}] ({p['year']}) {p['title']} - {', '.join(p['authors'][:2])}")
