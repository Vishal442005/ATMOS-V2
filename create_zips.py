import zipfile, os, shutil

# Copy final PDFs to project root for easy user access
shutil.copy2('dev_report_build/main.pdf', 'dev_report.pdf')
shutil.copy2('vishal_report_build/main.pdf', 'vishal_report.pdf')
print("Copied final PDFs to dev_report.pdf and vishal_report.pdf")

# Create dev_report.zip
dev_zip_path = 'dev_report.zip'
if os.path.exists(dev_zip_path):
    os.remove(dev_zip_path)

with zipfile.ZipFile(dev_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add main.tex
    zipf.write('dev_report_build/main.tex', 'main.tex')
    # Add main.pdf
    zipf.write('dev_report_build/main.pdf', 'main.pdf')
    # Add certificate and evaluation
    if os.path.exists('dev_report_build/certificate.pdf'):
        zipf.write('dev_report_build/certificate.pdf', 'certificate.pdf')
    if os.path.exists('dev_report_build/evaluation.pdf'):
        zipf.write('dev_report_build/evaluation.pdf', 'evaluation.pdf')
    if os.path.exists('dev_report_build/logo.png'):
        zipf.write('dev_report_build/logo.png', 'logo.png')
    # Add figures folder
    for root, dirs, files in os.walk('dev_report_build/figures'):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, 'dev_report_build')
            zipf.write(full_path, rel_path)

print(f"dev_report.zip created! Size: {os.path.getsize(dev_zip_path):,} bytes")

# Create vishal_report.zip
vishal_zip_path = 'vishal_report.zip'
if os.path.exists(vishal_zip_path):
    os.remove(vishal_zip_path)

with zipfile.ZipFile(vishal_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add main.tex
    zipf.write('vishal_report_build/main.tex', 'main.tex')
    # Add main.pdf
    zipf.write('vishal_report_build/main.pdf', 'main.pdf')
    # Add certificate and evaluation
    if os.path.exists('vishal_report_build/certificate.pdf'):
        zipf.write('vishal_report_build/certificate.pdf', 'certificate.pdf')
    if os.path.exists('vishal_report_build/evaluation.pdf'):
        zipf.write('vishal_report_build/evaluation.pdf', 'evaluation.pdf')
    if os.path.exists('vishal_report_build/logo.png'):
        zipf.write('vishal_report_build/logo.png', 'logo.png')
    # Add figures folder
    for root, dirs, files in os.walk('vishal_report_build/figures'):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, 'vishal_report_build')
            zipf.write(full_path, rel_path)

print(f"vishal_report.zip created! Size: {os.path.getsize(vishal_zip_path):,} bytes")
