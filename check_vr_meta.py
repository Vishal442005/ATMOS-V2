import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

r_vr = pypdf.PdfReader('vishal_report.pdf')
print("vishal_report.pdf metadata:", r_vr.metadata)
print("vishal_report.pdf num pages:", len(r_vr.pages))
