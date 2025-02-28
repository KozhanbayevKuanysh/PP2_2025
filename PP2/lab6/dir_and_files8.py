import os

path = 'a.txt'

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
    else:
        print("Permission denied")
else:
    print("File not found")