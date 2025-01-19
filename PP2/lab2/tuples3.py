tuple1 = ("apple", "banana", "cherry")
tuple2 = list(tuple1)
tuple2[1] = "kiwi"
tuple1 = tuple(tuple2)

print(tuple1)

tuple3 = ("apple", "banana", "cherry")
tuple4 = list(tuple3)
tuple4.append("orange")
tuple4.remove("apple")
tuple3 = tuple(tuple4)

print(tuple3)

tuple5 = ("apple", "banana", "cherry")
y = ("orange",)
tuple5 += y

print(tuple5)

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists