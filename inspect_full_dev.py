with open('build_full_reports.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'dev_main_tex = r"""'
idx = text.find(target)
if idx != -1:
    idx_end = text.find('"""', idx + len(target))
    content = text[idx + len(target):idx_end]
    import re
    print("dev_main_tex length:", len(content))
    print("Chapters:", re.findall(r'\\chapter\{(.*?)\}', content))
    print("Sections:", len(re.findall(r'\\section\{(.*?)\}', content)))
    for s in re.findall(r'\\section\{(.*?)\}', content):
        print("  *", s)
