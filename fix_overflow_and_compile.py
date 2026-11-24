import subprocess
import pypdf
import os

tex_path = r"c:\Users\Visha\Desktop\Project\manuscript_Atmos_V2\manuscript_Atmos_V2_IEEE_Sensors_8Pages.tex"

with open(tex_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Clean line 105-108
old_corrupted = "which evaluates to {\\mathrm{bat,avg}} \\approx 95.8\\,\\text{mA}$."
if old_corrupted in text:
    text = text.replace(old_corrupted, "yielding $I_{\\mathrm{bat,avg}} \\approx 95.8\\,\\text{mA}$.")

# Also check for \label{eq:avg_current}
pos_avg = text.find(r"\label{eq:avg_current}")
if pos_avg != -1:
    pos_begin = text.rfind(r"\begin{equation}", 0, pos_avg)
    pos_end = text.find(r"\end{equation}", pos_avg) + len(r"\end{equation}")
    clean_eq1 = r"""\begin{equation}
I_{\mathrm{bat,avg}} = \frac{15(265) + 5(280) + 3(125) + 37(0.015)}{60}
\label{eq:avg_current}
\end{equation}
yielding $I_{\mathrm{bat,avg}} \approx 95.8\,\text{mA}$."""
    # Find up to next sentence
    pos_next = text.find("Under adaptive", pos_end)
    text = text[:pos_begin] + clean_eq1 + "\n" + text[pos_next:]

# 2. Fix LSTM Gates (User Image 2)
new_lstm_clean = r"""\begin{align}
\mathbf{f}_\tau &= \sigma\left( \mathbf{W}_f \mathbf{x}_\tau + \mathbf{U}_f \mathbf{h}_{\tau-1} + \mathbf{b}_f \right), \label{eq:gate_f} \\
\mathbf{i}_\tau &= \sigma\left( \mathbf{W}_i \mathbf{x}_\tau + \mathbf{U}_i \mathbf{h}_{\tau-1} + \mathbf{b}_i \right), \label{eq:gate_i} \\
\tilde{\mathbf{C}}_\tau &= \tanh\left( \mathbf{W}_c \mathbf{x}_\tau + \mathbf{U}_c \mathbf{h}_{\tau-1} + \mathbf{b}_c \right), \label{eq:gate_c_cand} \\
\mathbf{C}_\tau &= \mathbf{f}_\tau \odot \mathbf{C}_{\tau-1} + \mathbf{i}_\tau \odot \tilde{\mathbf{C}}_\tau, \label{eq:gate_c} \\
\mathbf{o}_\tau &= \sigma\left( \mathbf{W}_o \mathbf{x}_\tau + \mathbf{U}_o \mathbf{h}_{\tau-1} + \mathbf{b}_o \right), \label{eq:gate_o} \\
\mathbf{h}_\tau &= \mathbf{o}_\tau \odot \tanh\left( \mathbf{C}_\tau \right) \label{eq:gate_h}
\end{align}"""

pos_lstm = text.find(r"\mathbf{f}_\tau")
if pos_lstm != -1:
    b_align = text.rfind(r"\begin{align}", 0, pos_lstm)
    e_align = text.find(r"\end{align}", pos_lstm) + len(r"\end{align}")
    text = text[:b_align] + new_lstm_clean + text[e_align:]

# 3. Clean Tables 1, 2, 3
# Replace any \begin{tabularx}{\columnwidth}{lccccc} with \begin{tabular}{lccccc}
text = text.replace(r"\begin{tabularx}{\columnwidth}{lccccc}", r"{\footnotesize \setlength{\tabcolsep}{3.2pt} \begin{tabular}{lccccc}")
text = text.replace(r"\begin{tabularx}{\columnwidth}{lccc}", r"{\footnotesize \setlength{\tabcolsep}{3.8pt} \begin{tabular}{lccc}")
text = text.replace(r"\begin{tabularx}{\columnwidth}{lcccc}", r"{\footnotesize \setlength{\tabcolsep}{3.8pt} \begin{tabular}{lcccc}")

# Clean their ends:
for tab_label in [r"\label{tab:calib_metrics}", r"\label{tab:humidity_breakdown}", r"\label{tab:forecast}"]:
    p = text.find(tab_label)
    if p != -1:
        p_end = text.find(r"\end{table}", p)
        # Search backwards from p_end for \end{tabularx} or \end{tabular*}
        seg = text[p:p_end]
        if r"\end{tabularx}" in seg:
            seg = seg.replace(r"\end{tabularx}", r"\end{tabular}}")
            text = text[:p] + seg + text[p_end:]
        elif r"\end{tabular*}" in seg:
            seg = seg.replace(r"\end{tabular*}", r"\end{tabular}}")
            text = text[:p] + seg + text[p_end:]

# 4. Clean Table 4 (User Image 1)
clean_table4 = r"""\begin{table*}[!t]
\caption{Comprehensive Benchmarking Comparison of ATMOS-V2 Against Representative Literature (2018--2026)}
\label{tab:sota_benchmark}
\centering
\footnotesize
\setlength{\tabcolsep}{3.2pt}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}lcccccc@{}}
\toprule
\textbf{System / Study} & \textbf{Year} & \textbf{Cost} & \textbf{Power Architecture} & \textbf{Reference Instrument} & \textbf{$R^2$ ($\text{PM}_{2.5}$)} & \textbf{Forecasting Capacity} \\
\midrule
Zheng et al.~\cite{zheng2018field} & 2018 & $\sim$\$120 & Grid / Mains Only & Met One BAM-1020 FEM & 0.68--0.72 & None (Static Sensing) \\
Magi et al.~\cite{magi2020evaluation} & 2020 & $\sim$\$250 & Grid / Mains Only & TEOM Federal Standard & 0.77 & None (Static Sensing) \\
Kumar et al.~\cite{kumar2023lowcost} & 2023 & $\sim$\$95 & Solar 5W + Lead-Acid & Portable Optical FEM & 0.81 & None (Static Sensing) \\
Ali et al.~\cite{ali2024iot} & 2024 & $\sim$\$80 & Solar 3W + 18650 & Co-located Reference & 0.84 & 1h--3h ARIMA Baseline \\
Sengupta et al.~\cite{sengupta2026temporal} & 2026 & $\sim$\$350 & Grid / Mains Only & UK AURN Reference & 0.89 & None (Calibration Focus) \\
Yun et al.~\cite{yun2026lowcost} & 2026 & $\sim$\$110 & USB 5V Mains & Indoor Standard & 0.86 & None (Transferability Focus) \\
\midrule
\textbf{ATMOS-V2 (This Work)} & \textbf{2026} & \textbf{$<$\$65} & \textbf{Solar 2W + 18650 Li-ion} & \textbf{Met One BAM-1020 FEM} & \textbf{0.924} & \textbf{Multi-Horizon 1h--24h LSTM} \\
\bottomrule
\end{tabular*}
\end{table*}"""

pos_t4 = text.find(r"\label{tab:sota_benchmark}")
if pos_t4 != -1:
    b_t4 = text.rfind(r"\begin{table*}", 0, pos_t4)
    e_t4 = text.find(r"\end{table*}", pos_t4) + len(r"\end{table*}")
    text = text[:b_t4] + clean_table4 + text[e_t4:]

with open(tex_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Applied fixes without regex replacement errors. Running Tectonic...")
tectonic_exe = r"c:\Users\Visha\Desktop\Project\tools\tectonic\tectonic.exe"
res = subprocess.run([tectonic_exe, "-X", "compile", tex_path], capture_output=True, text=True, cwd=os.path.dirname(tex_path))
print("Tectonic return code:", res.returncode)

overfull_lines = [l for l in res.stderr.splitlines() if "overfull" in l.lower()]
print(f"Total Overfull warnings: {len(overfull_lines)}")
for o in overfull_lines:
    print("  ", o)

if res.returncode == 0:
    pdf_path = r"c:\Users\Visha\Desktop\Project\manuscript_Atmos_V2\manuscript_Atmos_V2_IEEE_Sensors_8Pages.pdf"
    reader = pypdf.PdfReader(pdf_path)
    print("SUCCESSFUL COMPILATION!")
    print(f"Total pages: {len(reader.pages)}")
    for i, p in enumerate(reader.pages):
        print(f"Page {i+1}: text length = {len(p.extract_text())}")
else:
    for l in res.stderr.splitlines()[-30:]:
        print(l)
