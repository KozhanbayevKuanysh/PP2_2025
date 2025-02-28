text = "Hello, World!"
upper = 0
lower = 0

for i in range(len(text)):
    if text[i].isupper():
        upper += 1
    elif text[i].islower():
        lower += 1
    else:
        continue

print(f"UpperCase letters: {upper} \nLowerCase letters: {lower}")