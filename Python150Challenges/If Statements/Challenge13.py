# 013 Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”.

num = int(input("Enter the number less than 20: "))

if num >= 20:
    print("Too High")
else:
    print("Thank you")