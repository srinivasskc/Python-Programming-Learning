# 043 Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down, display the message “I don’t understand”.

direction = input("In which direction, do you want to count: (Up/Down)?")

if direction == "Up":
    top_number = int(input("Enter the Top Number: "))
    for i in range(1,top_number+1):
        print(i)
elif direction == "Down":
    down_number = int(input("Enter the Number below 20: "))
    for i in range(20,down_number-1,-1):
        print(i)
else:
    print("I don't Understand")