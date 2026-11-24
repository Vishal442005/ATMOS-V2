import urllib.request
import urllib.parse
import json

# Search OpenAlex for peer-reviewed journal papers on low-cost sensor calibration with BAM-1020 / reference monitors and solar IoT
search_url = "https://api.openalex.org/works?search=low-cost+sensor+calibration+BAM-1020+machine+learning&filter=publication_year:2022-2026&sort=cited_by_count:desc&per_page=10"

req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    results = data.get('results', [])
    print(f"OpenAlex found {len(results)} highly-cited recent journal papers:")
    journal_papers = []
    for r in results:
        title = r.get('title')
        year = r.get('publication_year')
        venue = r.get('primary_location', {}).get('source', {}).get('display_name') if r.get('primary_location') and r.get('primary_location').get('source') else 'Unknown'
        citations = r.get('cited_by_count')
        doi = r.get('doi')
        pdf_url = r.get('open_access', {}).get('oa_url')
        print(f"- {title} ({year}) | {venue} | Citations: {citations} | DOI: {doi}")
        journal_papers.append({
            'title': title,
            'year': year,
            'venue': venue,
            'citations': citations,
            'doi': doi,
            'pdf_url': pdf_url
        })
    with open("openalex_journal_papers.json", "w") as f:
        json.dump(journal_papers, f, indent=2)
except Exception as e:
    print(f"Error querying OpenAlex: {e}")
