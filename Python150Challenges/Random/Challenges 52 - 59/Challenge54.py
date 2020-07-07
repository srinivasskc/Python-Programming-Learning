# 054 Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell the user if the computer selected heads or tails.

import random

toss = random.choice(["t","h"])

user_choice = input("Heads or Tails? h/t: ")
if user_choice == toss:
    print("You win")
else:
    print("Bad Luck")

print("Computer Choice:",toss)