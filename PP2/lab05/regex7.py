import re

test = ["mahal_saj", "foar_sawe_sik", "wi_load_pore", "lird_moran", "apw_pp_tyf_mms"]

for i in test:
    splitted = i.split("_")
    print(splitted[0] + "".join(word.capitalize() for word in splitted[1:]))