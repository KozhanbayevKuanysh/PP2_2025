import re

test = ["camelCase", "cameLcaSE", "reTry", "playAgain", "goOut"]

for i in test:
    print(re.sub(r"(?<!^)([A-Z])", r"_\1", i).lower())