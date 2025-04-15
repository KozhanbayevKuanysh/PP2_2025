import re

test = ["slaDblaEglaW", "LalalLAllastIsx", "AloBranEaspoRts", "WernerBroters"]

for i in test:
    print(re.split(r"[A-Z]", i))