import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    count = 0
    for pattern, repl in replacements:
        new_text, n = re.subn(pattern, repl, text)
        if n > 0:
            text = new_text
            count += n
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"{filename}: replaced {count} occurrences")

# 1. make_sec1_intro.py
update_file('make_sec1_intro.py', [
    (r'width=0\.92\\textwidth', r'width=0.74\\textwidth'),
    (r'width=0\.88\\textwidth', r'width=0.72\\textwidth')
])

# 2. make_sec3_em_theory.py
update_file('make_sec3_em_theory.py', [
    (r'width=0\.92\\textwidth', r'width=0.72\\textwidth'),
    (r'width=0\.88\\textwidth', r'width=0.72\\textwidth'),
    (r'width=0\.72\\textwidth', r'width=0.68\\textwidth')
])

# 3. make_sec4_hfss_design.py
update_file('make_sec4_hfss_design.py', [
    (r'width=0\.92\\textwidth', r'width=0.72\\textwidth'),
    (r'width=0\.88\\textwidth', r'width=0.72\\textwidth')
])

# 4. make_sec5_results.py
update_file('make_sec5_results.py', [
    (r'width=0\.92\\textwidth', r'width=0.72\\textwidth'),
    (r'width=0\.88\\textwidth', r'width=0.70\\textwidth'),
    (r'width=0\.75\\textwidth', r'width=0.66\\textwidth'),
    (r'width=0\.72\\textwidth', r'width=0.66\\textwidth')
])

# 5. make_sec7_isac_6g.py
update_file('make_sec7_isac_6g.py', [
    (r'width=0\.92\\textwidth', r'width=0.72\\textwidth')
])
