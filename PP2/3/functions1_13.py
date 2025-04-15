from random import randint
name = input("Hello! What is your name? ")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
def guess():
    attemps = 1
    guessed_int = randint(1, 20)
    while True:
        int_num = int(input("Take a guess."))
        if int_num == guessed_int:
            print(f"Good job, {name}! You guessed my number in {attemps} guesses!")
            break
        elif int_num > guessed_int:
            attemps += 1
            print("Your guess is too high.")
        else:
            attemps += 1
            print("Your guess is too low.")

guess()