# 022  Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.

firstname = input("Enter your firstname in lowercase: ")
surname = input("Enter your surname in lowercase: ")

ftitle = firstname.title()
stitle = surname.title()
fulltitle = ftitle +" "+ stitle
print(fulltitle)