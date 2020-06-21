print("1) Square ")
print("2) Triangle")
print()

num = int(input("Enter a Number: "))

if num == 1:
    length = int(input("Enter length of the Sides: "))
    print("Area of Square: ", length*length)
elif num == 2:
    base = int(input("Enter base of the triangle: "))
    height = int(input("Enter the height of triangle: "))
    print("Area of Triangle: ", (base*height)/2)
else:
    print("Invalid Entry")
