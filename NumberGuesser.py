#what am I even trying to do??

#I want the user to guess a number the computer has randomly selected and calculate how many times
#it takes the user to guess the correct number.
import random

def guess_number(x):
    random_number = random.randint(1,x)
    count = 0

    while guess != random_number:
        guess = int(input("Guess a number: "))
        count = count + 1
        print("Wrong, try again")
        break

    print (f"You guessed correctly! It only took you {count} times to do so!")

guess_number(20)