#Lists
fruits = ["mango", "banana", "Oranges"]
years = [0, "1990", 6.25, "30"]

# Printing the Lists
print(fruits,years)

#appending single item to the list using Append Method
fruits.append("apple")
years.append("1992")
print(fruits,years)

#Extend the List with another list using Extend Method
fruits.extend(fruits)
#self extend
print(fruits)

fruits.extend(years)
#extend another list
print(fruits)

#removing the item from list using Remove Method and First Item Occurrence in the list.
movies = ['AAA', 'BALU', 'PANJA', 'KICK']
print(movies)
movies.remove('BALU')
print(movies)
#movies.remove('BALU')  #Not in the List
#print(movies)
print(fruits)
fruits.remove("banana")

# The pop() method removes the item at the given index from the list and returns the removed item.
print(fruits)
fruits.pop(0)
print(fruits)
fruits.pop(-1)
print(fruits)

# The sort() method sorts the elements of a given list in a specific order - Ascending or Descending.
#fruits.sort()  #String Values and Integer Values
#print(fruits)  #Should Throw an Error

#Sort Numbers
intNumbers = [10, 5, 2, 200, 6000]
intNumbers.sort()
print(intNumbers)

floatNumbers = [10.0, 1.25, 3.21, 0.25]
floatNumbers.sort()
print(floatNumbers)

# float and int numbers sort
numbers = [2000,12.24, 1, 500, 69]
numbers.sort()
print(numbers)

# Checking Membership in a List : Python has a function called in and this function allows us to check membership.
print(fruits)
print("apple" in fruits)

#Count Function
print(fruits.count("apple"))

# Check Membership using Index Function
print(fruits.index("Oranges"))
