fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#########
for x in "banana": # b, a, n, a, n, a
  print(x)
########
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
##########
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue # skiping banana
  print(x)
###########
for x in range(6): # 0, 1, 2, 3, 4, 5
  print(x)
else:
  print("Finally finished!")
##########
for x in range(2, 6): # 2, 3, 4, 5
  print(x)
########
for x in range(2, 30, 3): # 2, 5, 8, 11...
  print(x)