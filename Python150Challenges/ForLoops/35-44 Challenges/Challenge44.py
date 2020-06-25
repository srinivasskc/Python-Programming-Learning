# 044 Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message “Too many people”.

party_count = int(input("How many people do you want to invite for party: "))

if party_count < 10:
    for i in range(1,party_count+1):
        names = input("Enter the name of persons: ")
        print(names + " has been invited")
else:
    print("Too many people")

