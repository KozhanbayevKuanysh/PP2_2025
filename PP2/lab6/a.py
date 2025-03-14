def infinite_fibonacci():
    num1 = 0
    num2 = 1
    nextnum = num1
    while True:
        yield nextnum
        num1, num2 = num2, nextnum
        nextnum = num1 + num2

fib_gen = infinite_fibonacci()
for i in range(10):
    print(next(fib_gen), end=" ")