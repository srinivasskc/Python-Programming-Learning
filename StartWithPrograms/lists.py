userAge = [10, 21, 29, 35, 55]
print(userAge)

userAge1 = []
print(userAge1)

print(userAge[0])
print(userAge[1])
print(userAge[-1])
print(userAge[-2])

userAge1 = userAge
print(userAge1)

#Slice Notation [startIndex : index-1]
userAge3 = userAge[2:4]
print(userAge3)

#Slice Notation with Third Number - Steeper
# We will get sublist of every second number from index 1 to index 5-1 because stepper is 2.
userAge4 = userAge[1:5:2]
print(userAge4)

userAgeNew = [1, 3, 5 , 7, 9 , 13, 15, 22, 29, 36, 45, 56, 70, 99]
userAge5 = userAgeNew[1:10:2]
print(userAge5)
#It prints: 1, 45-1=36, 22, 13, 7

userAgeNoStartIndex = userAgeNew[ :4]
print(userAgeNoStartIndex)
#By default Start Index is Zero. It gives values from Zero Index to 4-1 index.

userAgeNoEndIndex = userAgeNew[1: ]
print(userAgeNoEndIndex)
#It prints from Index 2 till end of the index.

#Modifying the Value at index
userAgeNew[10] = 40
print(userAgeNew)

#Adding Items to the index.
userAgeNew.append(100)
print(userAgeNew)

#Deleting Item from Index
del userAgeNew[1]
print(userAgeNew)


