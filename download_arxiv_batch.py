import urllib.request
import os
import time

os.makedirs("downloaded_papers", exist_ok=True)

arxiv_papers = [
    ("paper_omnist_2026.pdf", "https://arxiv.org/pdf/2611.04256v1"),
    ("paper_lightweight_calib_2026.pdf", "https://arxiv.org/pdf/2610.11236v1"),
    ("paper_gaudi_diffusion_2026.pdf", "https://arxiv.org/pdf/2609.30340v1"),
    ("paper_spatiotemporal_pm25_2024.pdf", "https://arxiv.org/pdf/2412.13935v1")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

for fname, url in arxiv_papers:
    dest = os.path.join("downloaded_papers", fname)
    if not os.path.exists(dest):
        print(f"Downloading {fname} from {url}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp, open(dest, 'wb') as f:
                f.write(resp.read())
            print(f"Downloaded {fname}: {os.path.getsize(dest):,} bytes")
            time.sleep(3)
        except Exception as e:
            print(f"Error downloading {fname}: {e}")
    else:
        print(f"Exists: {fname}")

print("All done.")
