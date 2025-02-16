def even_nums_gen(n):
    for i in range(n + 1):
        if i % 2 == 0: 
            yield i

n = int(input())
print(*even_nums_gen(n), sep=', ')