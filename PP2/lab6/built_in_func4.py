import time

number = int(input())
time1 = int(input("(miliseconds: )"))

time.sleep(time1 / 1000)

print(f"Square root of {number} after {time1} miliseconds is {number**0.5}")