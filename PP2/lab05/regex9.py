import re

test = ["slaDblaEglaW", "LalalLAllastIsx", "AloBranEaspoRts", "WernerBroters"]

for i in test:
    print(re.sub(r"(?<!^)([A-Z])", r" \1", i))