# 007 Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age].

name = input("Enter the name of person: ")
age  = int(input("Enter the age of person: "))
age = str(age + 1)
print(name + " next birthday you will be " + age)
