import os

path = r'exercises.txt'
num_of_lines = 0
with open(path, 'r') as file: 
    for line in file:
        num_of_lines += 1

print(f"Number of lines: {num_of_lines}")