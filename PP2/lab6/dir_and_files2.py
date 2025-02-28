import os

path = 'dir_and_files1.py'

print(f"Exists: {os.access(path, os.F_OK)}") # check for existence
print(f"Readability: {os.access(path, os.R_OK)}") # check for readability
print(f"Writability: {os.access(path, os.W_OK)}") # check for writability
print(f"Executability: {os.access(path, os.X_OK)}") # check for executability