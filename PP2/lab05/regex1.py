import re

pattern = r".*ab*"

test = ["alo", "abbbb", "a", "ab", "abb", "ac", "b", "abc", "aabb", "lab"]

for i in test:
    if re.fullmatch(pattern, i):
        print(i)