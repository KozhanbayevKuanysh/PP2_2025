def nums_div_gen(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

print(*nums_div_gen(52))