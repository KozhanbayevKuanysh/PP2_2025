import re

pattern = r"a.*b$"

test = ["aKT4kfdmb", "ab", "aOb", "bAba", "Adb", "adadb", "asb", "aaaabbbb", "aLW", "Hgb"]

for i in test:
    if re.fullmatch(pattern, i):
        print(i)