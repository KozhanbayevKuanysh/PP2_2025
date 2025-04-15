import os

for i in range(26):
    file_name = f"{chr(i + 65)}.txt"
    with open(f'sample\\{file_name}', "w") as file:
        pass