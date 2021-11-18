import random

#This function allows the computer to guess a number you have picked

def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        #guess = random.randint(low, high)
        feedback = input(f"Is {guess} higher (H), lower (L), or correct (C)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"I guessed your number, {guess}, correctly peasant, therefore I am superior!")
    

computer_guess(10)