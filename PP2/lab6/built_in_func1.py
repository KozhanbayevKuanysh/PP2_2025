from functools import reduce
numbers = [1, 3, 4, 30, 12, 2]

result = reduce(lambda x, y: x * y, numbers)

print(result)