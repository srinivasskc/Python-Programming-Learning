# Dictionaries in Python

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Dec"])

print(monthConversions.get("Jan"))

print(monthConversions.get("hello"))
print(monthConversions.get("hello", "Not a Valid Value"))
