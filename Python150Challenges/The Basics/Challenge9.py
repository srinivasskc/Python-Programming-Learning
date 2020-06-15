# 009 Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.

no_of_days = int(input("Enter no.of days: "))
hours = no_of_days * 24
minutes = hours * 60
seconds = minutes * 60

print("No. of hours: ", hours)
print("No. of Minutes: ", minutes)
print("No. of Seconds: ", seconds)
