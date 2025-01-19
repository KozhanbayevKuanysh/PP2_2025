tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple1)

print(len(tuple1))

thistuple2 = ("apple",)
print(type(thistuple2))

#NOT a tuple
thistuple3 = ("apple")
print(type(thistuple3))

thistuple4 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple4)