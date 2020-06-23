#036 Alter program 035 so that it will ask the user to enter their name and a number and then display their name that number of times.

name = input("Enter the name: ")
num  = int(input("Enter the number: "))

for i in range(num):
    print(name)

