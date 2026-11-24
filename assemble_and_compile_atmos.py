# assemble_and_compile_atmos.py

import os
import subprocess
import pypdf

from atmos_make_sec0_frontmatter import get_frontmatter
from atmos_make_sec1_intro import get_chapter1
from atmos_make_sec2_litreview import get_chapter2
from atmos_make_sec3_hardware import get_chapter3
from atmos_make_sec4_software_iot import get_chapter4
from atmos_make_sec5_ml_methodology import get_chapter5
from atmos_make_sec6_results import get_chapter6
from atmos_make_sec7_advantages import get_chapter7
from atmos_make_sec8_conclusion import get_chapter8
from atmos_make_sec9_appendices_refs import get_appendices_and_refs

build_dir = 'atmos_report_build'
os.makedirs(build_dir, exist_ok=True)
tex_path = os.path.join(build_dir, 'main.tex')

print("Assembling atmos_report_build/main.tex...")
full_tex = "".join([
    get_frontmatter(),
    get_chapter1(),
    get_chapter2(),
    get_chapter3(),
    get_chapter4(),
    get_chapter5(),
    get_chapter6(),
    get_chapter7(),
    get_chapter8(),
    get_appendices_and_refs()
])

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(full_tex)

print(f"Wrote main.tex ({len(full_tex)} chars, {len(full_tex.splitlines())} lines).")

print("Compiling with Tectonic...")
cmd = r"Set-Location atmos_report_build; ..\tools\tectonic\tectonic.exe main.tex; Set-Location .."
proc = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)

print("Tectonic stdout:", proc.stdout[-500:] if proc.stdout else "None")
if proc.stderr:
    print("Tectonic stderr:", proc.stderr[-500:])

pdf_path = os.path.join(build_dir, 'main.pdf')
if os.path.exists(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    page_count = len(reader.pages)
    file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"\n==========================================")
    print(f"SUCCESS: Compiled atmos_report_build/main.pdf")
    print(f"Total Page Count: {page_count} pages")
    print(f"File Size: {file_size_mb:.2f} MB")
    print(f"==========================================")
else:
    print("ERROR: main.pdf was not generated. Inspect logs.")
