with open('dev_report_build/main.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect chapters and sections
import re
chapters = re.findall(r'\\chapter\{(.*?)\}', text)
sections = re.findall(r'\\section\{(.*?)\}', text)
print("Chapters:", chapters)
print("Sections count:", len(sections))
print("Sample sections:", sections[:10])
