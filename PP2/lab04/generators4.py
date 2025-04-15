def squares(a, b):
    while a <= b:
        yield a**2
        a += 1

for i in squares(6, 10):
    print(i)