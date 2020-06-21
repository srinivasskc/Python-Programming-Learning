# 011  Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.

larger_number = int(input("Enter a number greater than 100: "))
smaller_number = int(input("Enter a number less than 10: "))
number = str(larger_number // smaller_number)
print(number + " times smaller number goes into larger number")
