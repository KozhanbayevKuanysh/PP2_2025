def square_nums_gen(n):
    for i in range(n + 1):
        yield i**2

print(*square_nums_gen(7))