#This is guess the number game.

import random

print("What is your Name?")
name = input()

print("Hey, " + name + " ,I am thinking of a number between 1 and 20")

secretNumber = random.randint(1,20)
#To give us random integer including 1 and 20 and between 1-20

#print("DEBUG: Secret Number is " + str(secretNumber))


for guessesTaken in range(1,7):
#Include 1-6, not 7
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break
        #this condition is for true guess.


if guess ==  secretNumber:
    print("Good Job, " + name + " ,You guessed my Number in " + str(guessesTaken) + " guesses")
else:
    print("You did not guess the number: " + str(secretNumber))
    

print("you took "+ str(guessesTaken) + " guesses")
