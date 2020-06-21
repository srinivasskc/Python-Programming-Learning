# 015 Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”.

color = input("Enter your favorite color: ")
if color == "red" or color == "RED" or color == "Red":
    print("I like red too")
else:
    print("I don't like " + color + " , I prefer red")
