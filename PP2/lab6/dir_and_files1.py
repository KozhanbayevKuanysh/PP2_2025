import os

path = os.getcwd()
contents = os.listdir(path)

print("Files:")
for i in contents:
    if os.path.isfile(i) == True:
        print(i)
print("---------------")

print("Directories:")
for i in contents:
    if os.path.isdir(i) == True:
        print(i)
print("---------------")

print("All files and directories:")
for i in contents:
    print(i)