# 048 Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party.

invite = 0

invitation = "y"

while invitation == "y":
    name = input("What is your name? ")
    print(name, "has been invited")
    invite = invite + 1
    invitation = input("Do you want to invite anyone?: y/n ")
print(invite, "people are invited to the party")

