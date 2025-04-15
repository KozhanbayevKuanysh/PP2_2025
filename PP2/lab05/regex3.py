import re

pattern = r"[a-z]+_[a-z]+"

test = ["ab_bas", "lLao_x", "hed", "t_aese", "n_u", "AIIS_ELO", "bA_b", "_rol", "rek_"]

for i in test:
    if re.fullmatch(pattern, i):
        print(i)