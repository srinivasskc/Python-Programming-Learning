print("How many cars do you have?")
numCars = input()

try:
    if int(numCars) >= 3:
        print("You are rich")
    else:
        print("Oh You have only " + numCars + " Cars")
except ValueError:
    print("Please enter valid number")
    
