import json

with open('seminar_vishal/papers_metadata.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)

print(f"Total papers in JSON: {len(papers)}")

space_keywords = ['space', 'satellite', 'lunar', 'mars', 'orbit', 'leo', 'interplanetary', 'deep space', 'cgr', 'contact graph', 'bundle protocol', 'ltp', 'licklider']

space_papers = []
for p in papers:
    text = (p['title'] + " " + p['summary']).lower()
    score = sum(1 for kw in space_keywords if kw in text)
    p['relevance_score'] = score
    space_papers.append(p)

space_papers.sort(key=lambda x: x['relevance_score'], reverse=True)

print("\n--- TOP SPACE DTN PAPERS ---")
for i, p in enumerate(space_papers, 1):
    print(f"{i}. [Score {p['relevance_score']}] [{p['arxiv_id']}] ({p['year']})")
    print(f"   Title: {p['title']}")
    print(f"   Authors: {', '.join(p['authors'][:3])}")
    print()
