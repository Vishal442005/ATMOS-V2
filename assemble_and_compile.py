# assemble_and_compile.py
import os
import subprocess
import generate_dev_master
import write_dev_master
import create_c4_c5_app

# Combine all parts
full_tex = (
    generate_dev_master.tex_content + "\n" +
    write_dev_master.c1_text + "\n" +
    write_dev_master.c3_text + "\n" +
    create_c4_c5_app.c4_text + "\n" +
    create_c4_c5_app.c5_text + "\n" +
    create_c4_c5_app.app_text
)

out_path = r"dev_report_build\main.tex"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_tex)

print(f"Wrote full main.tex successfully! Total characters: {len(full_tex)}")
