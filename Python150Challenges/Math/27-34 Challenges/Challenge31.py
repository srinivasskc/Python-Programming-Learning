# 031 Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work out the area of the circle (π*radius2).

import math

radius = float(input("Enter the radius of a circle: "))
pi_value = math.pi
area_of_circle = pi_value * (radius**2)
print(area_of_circle)