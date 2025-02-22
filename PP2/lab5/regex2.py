import re

pattern = r".*ab{2,3}"

test = ["ab", "abbbb", "abbb", "aba", "abb", "ac", "b", "abc", "aabb", "labb"]

for i in test:
    if re.fullmatch(pattern, i):
        print(i)