import urllib.request
import urllib.parse
import json

search_url = "https://api.openalex.org/works?search=low-cost+air+quality+sensor+calibration+machine+learning+LSTM&filter=publication_year:2023-2026&sort=relevance_score:desc&per_page=10"

req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    results = data.get('results', [])
    print(f"OpenAlex relevant recent papers: {len(results)}")
    more_papers = []
    for r in results:
        title = r.get('title')
        year = r.get('publication_year')
        venue = r.get('primary_location', {}).get('source', {}).get('display_name') if r.get('primary_location') and r.get('primary_location').get('source') else 'Unknown'
        citations = r.get('cited_by_count')
        doi = r.get('doi')
        pdf_url = r.get('open_access', {}).get('oa_url')
        print(f"- {title} ({year}) | {venue} | Citations: {citations} | OA: {pdf_url}")
        more_papers.append({
            'title': title,
            'year': year,
            'venue': venue,
            'citations': citations,
            'doi': doi,
            'pdf_url': pdf_url
        })
    with open("openalex_ml_lstm_papers.json", "w") as f:
        json.dump(more_papers, f, indent=2)
except Exception as e:
    print(f"Error querying OpenAlex: {e}")
