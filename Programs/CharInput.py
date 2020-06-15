ch = input("Enter a character")
print(ch)

ch1 = input("Enter a character")
print(ch1)
#  Oh, if user enters skc, it will return skc.

ch2 = input("Enter a character")
print(ch2[0])
#  Yay, this prints only 1 character.
#  Hey wait.. ch2 contains skc

ch3 = input("Enter a character")[0]
print(ch3)
# User can enter a string, but only 1st character will be assigned to ch3
