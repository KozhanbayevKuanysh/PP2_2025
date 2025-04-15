from math import tan, pi

sides = int(input("Number of sides: "))
length = int(input("The length of a side: "))

print(f"The area of the polygon is: {round((sides * length**2) / (4 * tan(pi / sides)), 6)}")