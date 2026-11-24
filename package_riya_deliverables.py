import os
import shutil
import subprocess
import zipfile
import pypdf

# 1. Sync figures
src_figs = os.path.join('riya_report_build', 'figures')
dst_figs = os.path.join('Riya', 'figures')
os.makedirs(dst_figs, exist_ok=True)

for item in os.listdir(src_figs):
    s = os.path.join(src_figs, item)
    d = os.path.join(dst_figs, item)
    if os.path.isfile(s):
        shutil.copy2(s, d)
print(f"Copied {len(os.listdir(dst_figs))} figures to Riya/figures/")

# 2. Copy main.tex and main.pdf
src_tex = os.path.join('riya_report_build', 'main.tex')
dst_tex = os.path.join('Riya', 'main.tex')
shutil.copy2(src_tex, dst_tex)

src_pdf = os.path.join('riya_report_build', 'main.pdf')
dst_pdf1 = os.path.join('Riya', 'main.pdf')
dst_pdf2 = os.path.join('Riya', 'riya_report.pdf')
shutil.copy2(src_pdf, dst_pdf1)
shutil.copy2(src_pdf, dst_pdf2)
print("Copied main.tex, main.pdf, riya_report.pdf to Riya/")

# 3. Test compilation standalone inside Riya/
print("Testing standalone compilation in Riya/...")
cmd = r"Set-Location Riya; ..\tools\tectonic\tectonic.exe main.tex; Set-Location .."
proc = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
if proc.returncode != 0:
    print("Standalone compilation failed:")
    print(proc.stderr[:1000])
else:
    reader = pypdf.PdfReader(os.path.join('Riya', 'main.pdf'))
    print(f"Standalone compilation SUCCESS! Pages: {len(reader.pages)}")

# 4. Package riya_report.zip
zip_name = 'riya_report.zip'
print(f"Creating {zip_name}...")
with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(dst_tex, arcname='main.tex')
    z.write(dst_pdf1, arcname='main.pdf')
    z.write(dst_pdf2, arcname='riya_report.pdf')
    
    for root, dirs, files in os.walk(dst_figs):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, 'Riya')
            z.write(full_path, arcname=rel_path)

print(f"Created {zip_name} successfully!")
with zipfile.ZipFile(zip_name, 'r') as z:
    items = z.namelist()
    print(f"Items in {zip_name}: {len(items)}")
    print(f"Archive Size: {os.path.getsize(zip_name) / (1024*1024):.2f} MB")
