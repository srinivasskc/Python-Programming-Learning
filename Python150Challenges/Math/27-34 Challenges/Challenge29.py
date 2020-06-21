# 029 Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places.

import math

num = int(input("Enter a number over 500: "))
answer = math.sqrt(num)
print(round(answer, 2))
