# assemble_expanded_dev.py
import generate_dev_master
import write_dev_master
import create_c4_c5_app
import build_full_expanded_content
import add_extra_depth_83

# Weave into Chapter 1
c1 = write_dev_master.c1_text
pos_c1_end = c1.find(r'\chapter{Weekly Progress Report}')
assert pos_c1_end != -1, "Chapter 2 heading not found in c1_text"
new_c1 = c1[:pos_c1_end] + "\n" + build_full_expanded_content.c1_extra + "\n" + c1[pos_c1_end:]

# Weave into Chapter 3: Add controllability/observability/bode AND add BLDC FOC math
c3 = write_dev_master.c3_text
pos_foc_insert = c3.find(r'\section{Digital PID Controller Theory and Real-Time Implementation}')
assert pos_foc_insert != -1, "Section Digital PID not found in c3_text"
c3_with_foc = c3[:pos_foc_insert] + "\n" + add_extra_depth_83.bldc_foc_math + "\n" + c3[pos_foc_insert:]

pos_c3_end = c3_with_foc.find(r'\section{Firmware Architecture and FreeRTOS Multitasking}')
assert pos_c3_end != -1, "Section FreeRTOS not found in c3_text"
new_c3 = c3_with_foc[:pos_c3_end] + "\n" + build_full_expanded_content.c3_extra_math + "\n" + c3_with_foc[pos_c3_end:]

# Weave into Chapter 4: Add FreeRTOS task table and empirical noise benchmark
c4 = create_c4_c5_app.c4_text
pos_c4_noise = c4.find(r'\section{Electrical Power Rail Budget and Battery Performance}')
assert pos_c4_noise != -1, "Section Electrical Power not found in c4_text"
c4_with_noise = c4[:pos_c4_noise] + "\n" + add_extra_depth_83.empirical_noise_benchmark + "\n" + c4[pos_c4_noise:]

new_c4 = c4_with_noise + "\n" + build_full_expanded_content.c4_extra

# Weave into Chapter 5
c5 = create_c4_c5_app.c5_text
pos_future = c5.find(r'\section{Future Roadmap and Scalability}')
assert pos_future != -1, "Future Roadmap not found in c5_text"
new_c5 = c5[:pos_future] + "\n" + build_full_expanded_content.c5_extra + "\n" + c5[pos_future:]

# Assemble full main.tex
full_tex = (
    generate_dev_master.tex_content + "\n" +
    new_c1 + "\n" +
    new_c3 + "\n" +
    new_c4 + "\n" +
    new_c5 + "\n" +
    create_c4_c5_app.app_text
)

out_file = r"dev_report_build\main.tex"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(full_tex)

print(f"Assembled 83-page targeted main.tex successfully! Total characters: {len(full_tex)}")
