import random

# Get random number between 0 and 1
num = random.random()
print(num)

num = num * 100
print(num)

# Get random number between 0 and 9
num = random.randint(0,9)
print(num)

# Get random integer and division.
num1 = random.randint(0,1000)
print(num1)
num2 = random.randint(0,1000)
print(num2)
newrandfloat = num1/num2
print(newrandfloat)

# Get random number between 0 and 100
# (inclusive in steps of 5 - 0,10,15,20 etc)
num = random.randrange(0,100,5)
print(num)

# Get random value from choices
color = random.choice(["red","yellow","green"])
print(color)