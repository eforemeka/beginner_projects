import random

def guess_number(x):
    random_number = random.randint(1,x)
    count = 0

    while guess != random_number:
        guess = int(input("Guess a number: "))
        count = count + 1
        print("Wrong, try again")

    print (f"You guessed correctly! It only took you {count} times to do so!")

guess_number(20)