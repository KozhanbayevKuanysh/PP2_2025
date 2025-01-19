fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = []

for fruit in fruits:
  if "a" in fruit:
    newlist1.append(fruit)

print(newlist1)

newlist2 = [x for x in fruits if "a" in x]

print(newlist2)