#Declaring list of elements with different data types
myList = [1, 2 , 3 , 4.5, "Hello 5"]

#print entire list
print(myList)

#print third element
print(myList[2])

#print last element
print(myList[-1])

#assign myList from index 1 to 4 to myList2 and print myList2
myList2 = myList[1:5]
print(myList2)

#modifying second element in mylist
myList[1] = 20
print(myList)


#append new item to myList
myList.append("How are you")
print(myList)

#remove fourth element from myList
del myList[4]
print(myList)


print()
#print elements from startindex till sizeofIndex-1
print(myList)
#[1, 20, 3, 4.5, 'How are you']
print("The length of list is: ", len(myList))

myListWithoutEnd = myList[2: ]
print(myListWithoutEnd)

print()
#print till end of index
print(myList)
myListWithoutStart = myList[ :5]
print(myListWithoutStart)
