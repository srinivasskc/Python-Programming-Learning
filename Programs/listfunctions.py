# List Functions

numbers = [8, 3, 4, 5, 2, 5, 1]
employees = ['Varun', 'Ankita', 'Kiran', 'Kailash', 'Abhilash']

print(numbers)
print(employees)

# Extend Employees List with Numbers List
employees.extend(numbers)
print(employees)

# Append adds another value to the list. It can add only one value to the list
employees.append("Srini")
print(employees)

# Insert Elements at Index Position
employees.insert(2, "John")
print(employees)

# Delete Element from the list
employees.remove("John")
print(employees)

# Clear Elements from the list
employees.clear()
print(employees)

# Sort Elements in the List
# We cannot sort elements having strings and numbers

employees = ['Varun', 'Ankita', 'Kiran', 'Kailash', 'Abhilash']
employees.sort()
print(employees)
numbers.sort()
print(numbers)

# Copy One List to Another
employees2 = employees.copy()
print(employees2)
