#Import the random module. This makes various funtions under the random package accessible in our code
import random
#Define my function with parameter x where x is the top interval and 1 is the bottom interval of our range
def GuessNumber(x):
    random_number = random.randint(1, x)                                                                                             
    guess = 0
#The while loop is used here so that the user can keep guessing numbers until they are able to guess the
#right number. The if statement is there to let the user know how close they are to the right answer

    while guess != random_number:
        guess = int(input("Guess a number my gee: "))
        if guess > random_number:
            print("Nope. Guess lower")
        elif guess < random_number:
            print ("Nope. Guess Higher")
    print(f"Spot on! You guessed {random_number} and that was right!")
#Pass an argument to the function to play this game
GuessNumber(10)