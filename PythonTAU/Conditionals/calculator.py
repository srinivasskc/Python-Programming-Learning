def add():
    print("Addition")
    a1 = float(input("Enter a number: "))
    a2 = float(input("Enter another number: "))
    print(a1+a2)

def subtraction():
    print("Subtraction")
    s1 = float(input("Enter a number: "))
    s2 = float(input("Enter another number: "))
    print(s1-s2)

def mul():
    print("Multiplication")
    m1 = float(input("Enter a number: "))
    m2 = float(input("Enter another number: "))
    print(m1*m2)

def div():
    print("Division")
    d1 = float(input("Enter a number: "))
    d2 = float(input("Enter another number: "))
    print(d1/d2)

def mod():
    print("Modulus")
    md1 = float(input("Enter a number: "))
    md2 = float(input("Enter another number: "))
    print(md1%md2)
"""
add()
subtraction()
mul()
div()
mod()
"""

# Asking the User to Input for Operator

operator = input("Which operator do you want to use? +, - , *, / , %   ")

if operator == '+':
    add()
elif operator == '-':
    subtraction()
elif operator == '*':
    mul()
elif operator == '/':
    div()
else:
    mod()




