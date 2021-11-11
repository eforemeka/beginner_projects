#This is the welcome section of my code i guess
print("Welcome to my game!")

playing = input("Would you like to begin? ")

if playing.lower() != "yes":
    print ("Dammit! Goodbye!")
    quit()

print ("Okay! Let's get our freaky on baybayy!")
score = 0
points = 0

#Here, the questions begin

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct! You smart!")
    score += 1
    points += 50
else:
    print("Really? Wrong!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct! You smart!")
    score += 1
    points += 50
else:
    print("Really? Wrong!")

print("You got " + str(score) + " questions right and scored a total of " + str(points) + " points")