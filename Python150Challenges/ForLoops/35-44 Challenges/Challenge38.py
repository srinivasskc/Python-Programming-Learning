# 038 Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and repeat this for the number of times they entered. 039

name = input("Enter the name: ")
num = int(input("Enter a number: "))

for i in range(num):
    for i in name:
        print(i)
