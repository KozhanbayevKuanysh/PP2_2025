numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
prime = list(filter(is_prime, numbers))

print("Prime numbers: ",prime)