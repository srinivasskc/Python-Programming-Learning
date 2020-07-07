# 055 Randomly choose a number between 1 and 5.
# Ask the user to pick a number.
# If they guess correctly, display the message “Well done”,
# otherwise tell them if they are too high or too low and
# ask them to pick a second number.
# If they guess correctly on their second guess,
# display “Correct”, otherwise display “You lose”.

import random

num = random.randint(1, 5)

user_choice = int(input("Pick a number : "))

if user_choice == num:
    print("Well done")
elif user_choice > num:
    print("Too High")
    user_choice = int(input("Pick another number : "))
    if user_choice == num:
        print("Correct")
    else:
        print("You Lose")
elif user_choice < num:
    print("Too Low")
    user_choice = int(input("Pick another number : "))
    if user_choice == num:
        print("Correct")
    else:
        print("You Lose")
