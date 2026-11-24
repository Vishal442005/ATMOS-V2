import urllib.request
import os

solar_papers = [
    ("paper_solar_iot_air_quality.pdf", "https://arxiv.org/pdf/2306.13404v1"), # IoT air monitoring solar
    ("paper_pm25_forecasting_transformer_2024.pdf", "https://arxiv.org/pdf/2403.04878v1")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for fname, url in solar_papers:
    dest = os.path.join("downloaded_papers", fname)
    if not os.path.exists(dest):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
                f.write(resp.read())
            print(f"Downloaded {fname}: {os.path.getsize(dest):,} bytes")
        except Exception as e:
            print(f"Error {fname}: {e}")
