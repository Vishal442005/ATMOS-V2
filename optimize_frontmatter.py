# optimize_frontmatter.py
import re

with open('generate_dev_master.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Certificate: Change \vspace{1.5cm} to \vspace{0.4cm} and adjust spacing
text = text.replace(r'\vspace{1.5cm}' + '\n' + r'\noindent' + '\n' + r'\begin{minipage}{0.48\textwidth}',
                    r'\vspace{0.4cm}' + '\n' + r'\noindent' + '\n' + r'\begin{minipage}{0.48\textwidth}')

# 2. Evaluation Sheet: Adjust arraystretch and vertical space so it fits on 1 page
text = re.sub(r'\\renewcommand\{\\arraystretch\}\{1\.15\}\n(\\begin\{tabular\}\{\|c\|p\{0\.55\\textwidth\}\|c\|c\|\})',
              r'\\renewcommand{\\arraystretch}{1.0}\n\1', text)
text = text.replace(r'\vspace{1.0cm}' + '\n' + r'\noindent' + '\n' + r'\begin{minipage}{0.48\textwidth}' + '\n' + r'  \begin{flushleft}' + '\n' + r'    \textbf{Er. Rajesh Sharma}',
                    r'\vspace{0.3cm}' + '\n' + r'\noindent' + '\n' + r'\begin{minipage}{0.48\textwidth}' + '\n' + r'  \begin{flushleft}' + '\n' + r'    \textbf{Er. Rajesh Sharma}')

# 3. List of Abbreviations: Change arraystretch from 1.15 to 0.95 so it fits cleanly on 2 pages
text = text.replace(r'\renewcommand{\arraystretch}{1.15}' + '\n' + r'\begin{longtable}{|p{3.0cm}|p{11.5cm}|}',
                    r'\renewcommand{\arraystretch}{0.96}' + '\n' + r'\begin{longtable}{|p{3.0cm}|p{11.5cm}|}')

with open('generate_dev_master.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Optimized generate_dev_master.py frontmatter spacing!")
