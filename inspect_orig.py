with open('dev_report_build/main_orig.tex', 'r', encoding='utf-8', errors='ignore') as f:
    orig = f.read()

print("Original length:", len(orig))
import re
print("Original chapters:", re.findall(r'\\chapter\{(.*?)\}', orig))
print("Original sections:", re.findall(r'\\section\{(.*?)\}', orig)[:15])
