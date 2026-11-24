import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time

queries = [
    'all:"air quality" AND all:"sensor" AND all:"calibration" AND all:"machine learning"',
    'all:"PM2.5" AND all:"low-cost" AND (all:"LSTM" OR all:"forecasting")',
    'all:"air quality" AND (all:"solar" OR all:"energy harvesting") AND all:"IoT"'
]

results = []
seen = set()

for q in queries:
    url = f'http://export.arxiv.org/api/query?search_query={urllib.parse.quote(q)}&start=0&max_results=8&sortBy=submittedDate&sortOrder=descending'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        for entry in root.findall('atom:entry', ns):
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            if title in seen:
                continue
            seen.add(title)
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            published = entry.find('atom:published', ns).text.strip()
            pdf_url = ''
            for link in entry.findall('atom:link', ns):
                if link.attrib.get('title') == 'pdf':
                    pdf_url = link.attrib.get('href')
            results.append({'title': title, 'published': published, 'pdf_url': pdf_url, 'summary': summary})
        time.sleep(3) # respectful delay
    except Exception as e:
        print(f"Error querying {q}: {e}")

with open("downloaded_arxiv_papers.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"Retrieved {len(results)} distinct papers from arXiv.")
for i, r in enumerate(results[:10]):
    print(f"{i+1}. {r['title']} ({r['published'][:10]})")
    print(f"   URL: {r['pdf_url']}")
