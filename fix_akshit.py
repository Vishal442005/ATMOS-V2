with open('build_seminar_akshit.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(r'\usepackage{microtype}', r'\usepackage{microtype}' + '\n' + r'\usepackage{float}')
text = text.replace('Köhler', r'K\"ohler')
text = text.replace('Hänel', r'H\"anel')

with open('build_seminar_akshit.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated build_seminar_akshit.py!')
