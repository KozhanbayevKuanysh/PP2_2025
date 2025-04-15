import re

test = ["lsoa, OLodk", ". sas, w.s ", "WSWA", "sxx., ", "ho v ce.", " P ),(.D"]

for i in test:
    a = re.sub(r"[ ,.]", ":", i)
    print(a)