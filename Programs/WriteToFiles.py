# How to read files in python

employee_file = open("employee.txt", "r")
# modes: r-read, r+ - read and write, w - write, a - append

print(employee_file.readable())
# readable function prints bool value

print(employee_file.read())
# Prints all lines from file.

# Appending Data to File
employee_file = open("employee.txt", "a")
employee_file.write("\nAnu - Sr. HR")

# Writing to File
employee_file = open("employee.txt", "w")
employee_file.write("\nAnu - Sr. HR")
# W Mode will overwrite the existing file.

employee_file = open("employee1.txt", "w")
employee_file.write("Anu - Sr. HR")
# W Mode will overwrite the existing file.


employee_file.close()
