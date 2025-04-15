def reversed_num_gen(n):
    while n >= 0:
        yield n
        n -= 1

print(*reversed_num_gen(6))