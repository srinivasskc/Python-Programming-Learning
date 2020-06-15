# Handle Errors in Python using Try and Except blocks

# num = int(input("Enter a Number:"))
# print(num)
# ValueError

# value = 10/0
# ZeroDivisionError

try:
    # value = 10 / 0
    number = int(input("Enter a Number:"))
    print(number)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Division Error")
