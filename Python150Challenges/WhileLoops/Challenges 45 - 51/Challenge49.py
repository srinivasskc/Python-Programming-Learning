# 049 Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask them to have another guess. If they enter the same value as compnum, display the message “Well done, you took [count] attempts”. 050

compnum = 50
guess = int(input("Can you guess a number? "))
count = 1

while guess != compnum:
    if guess < compnum:
        print("your guess number is too low")
    else:
        print("your guess number is too high")
    count = count + 1
    guess = int(input("Can you guess another number? "))
print("Well done, you took ", count, "attempts")