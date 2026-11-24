# sync_and_package.py
import os
import shutil
import zipfile

# 1. Copy main.pdf to dev_report.pdf
src_pdf = r"dev_report_build\main.pdf"
dst_pdf = "dev_report.pdf"
shutil.copyfile(src_pdf, dst_pdf)
print(f"Copied {src_pdf} to {dst_pdf} (size: {os.path.getsize(dst_pdf)} bytes)")

# 2. Package into dev_report.zip
zip_path = "dev_report.zip"
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    # Add main.tex
    zf.write(r"dev_report_build\main.tex", "main.tex")
    # Add dev_report.pdf
    zf.write(dst_pdf, "dev_report.pdf")
    # Add figures folder
    fig_dir = r"dev_report_build\figures"
    for root, dirs, files in os.walk(fig_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, "dev_report_build")
            zf.write(full_path, rel_path)

print(f"Created {zip_path} successfully! (size: {os.path.getsize(zip_path)} bytes)")
