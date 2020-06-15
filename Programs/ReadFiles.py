# How to read files in python

employee_file = open("employee.txt", "r")
# modes: r-read, r+ - read and write, w - write, a - append

print(employee_file.readable())
# readable function prints bool value

# print(employee_file.read())
# Prints all lines from file.

print(employee_file.readline())
print(employee_file.readline())
# prints each line from file

# print(employee_file.readlines())
# prints each line as a List, after readline().

print(employee_file.readlines()[1])
# prints each line as a List, after readline().


employee_file.close()
