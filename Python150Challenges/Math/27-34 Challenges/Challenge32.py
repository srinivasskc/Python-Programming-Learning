# 032  Ask for the radius and the depth of a cylinder and work out the total volume (circle area*depth) rounded to three decimal places.
import math

radius = int(input("Enter the radius of cylinder : "))
depth = int(input("Enter the depth of cylinder: "))

area = math.pi * (radius**2)
volume = area * depth

print(round(volume,3))
