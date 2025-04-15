import os

path = r'C:\\Users\\kkozh\\OneDrive\\Documents\\PrinProg2\\PP2_2025\\PP2\\lab6\\dir_and_files2.py'

if os.path.exists(path):
    print(f"File Name: {os.path.basename(path)}")
    print(f"Directory Portion: {os.path.dirname(path)}")
else:
    print("Does not exist")