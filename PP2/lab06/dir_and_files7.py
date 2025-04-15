import os

path1 = r'exercises.txt'
path2 = r'test5.txt'

with open(path1, 'r') as file1:
    with open(path2, 'a') as file2:
        file2.write(f'\n{file1.read()}')