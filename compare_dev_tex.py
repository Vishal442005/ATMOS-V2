with open('dev_report_build/main.tex', 'r', encoding='utf-8') as f:
    current_tex = f.read()

with open('build_full_reports.py', 'r', encoding='utf-8') as f:
    script_txt = f.read()

# Let's check if current_tex matches dev_main_tex in build_full_reports.py
pattern = r'dev_main_tex = r"""(.*?)"""'
import re
m = re.search(pattern, script_txt, re.DOTALL)
if m:
    orig_tex = m.group(1)
    print("Match with build_full_reports.py?", current_tex == orig_tex)
    if current_tex != orig_tex:
        print("Length current:", len(current_tex), "Length script:", len(orig_tex))
else:
    print("Could not find dev_main_tex in build_full_reports.py")
