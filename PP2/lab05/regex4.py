import re

pattern = r"[A-Z][a-z]*"

test = ["LLLLLLW", "Lbb", "sb", "pPba", "QQbb", "Pc", "O", "IOISAS"]

for i in test:
    if re.fullmatch(pattern, i):
        print(i)