car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
y = car.keys()
print(y) #before the change
car["color"] = "white"
print(y) #after the change

z = car.values()
print(z) #before the change
car.update({"year": 2020})
print(z) #after the change

x = car.items()
print(x)