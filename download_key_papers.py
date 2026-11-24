import urllib.request
import os
import pypdf

os.makedirs("downloaded_papers", exist_ok=True)

paper_urls = [
    {
        "name": "paper_temporal_dl_calibration_2026.pdf",
        "url": "https://arxiv.org/pdf/2604.21527v1",
        "title": "A temporal deep learning framework for calibration of low-cost air quality sensors"
    },
    {
        "name": "paper_sensors_iot_calibration_2025.pdf",
        "url": "https://www.mdpi.com/1424-8220/25/10/3183/pdf?version=1747625370",
        "title": "Machine Learning-Based Calibration and Performance Evaluation of Low-Cost IoT Air Quality Sensors"
    },
    {
        "name": "paper_atmosphere_field_calibration_2023.pdf",
        "url": "https://www.mdpi.com/2073-4433/14/2/368/pdf?version=1676293060",
        "title": "Field Calibration of a Low-Cost Air Quality Monitoring Device in an Urban Background Site Using ML"
    },
    {
        "name": "paper_omnist_spatiotemporal_2026.pdf",
        "url": "https://arxiv.org/pdf/2611.04256v1",
        "title": "OmniST: Topology-Invariant Spatiotemporal Forecasting with Guaranteed-Coverage Uncertainty"
    },
    {
        "name": "paper_lightweight_calibration_2026.pdf",
        "url": "https://arxiv.org/pdf/2610.11236v1",
        "title": "Low-Cost Sensor Calibration: Dataset, Evaluation Scenarios, and a Lightweight Model"
    }
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

downloaded = []
for p in paper_urls:
    dest = os.path.join("downloaded_papers", p["name"])
    if not os.path.exists(dest):
        print(f"Downloading {p['title']}...")
        try:
            req = urllib.request.Request(p["url"], headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as out_f:
                out_f.write(resp.read())
            print(f"Saved to {dest} ({os.path.getsize(dest):,} bytes)")
            downloaded.append(dest)
        except Exception as e:
            print(f"Failed to download {p['title']}: {e}")
    else:
        print(f"Already exists: {dest} ({os.path.getsize(dest):,} bytes)")
        downloaded.append(dest)

print(f"\nSuccessfully downloaded/verified {len(downloaded)} papers.")
