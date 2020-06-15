# Create Calculator in Python

num1 = float(input("Enter a Number: "))
operator = input("Enter a Operator: ")
num2 = float(input("Enter a Number: "))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '%':
    print(num1 % num2)
else:
    print("Invalid Operator")
