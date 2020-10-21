'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
# Cylinder has a radius and a height
radius = 3.14
height = 5

# Calculate area of a cylinder ("2πr**2+2πrh"). Pi is needed for the calculation
import math
area = (2 * math.pi * radius**2) + (2 * math.pi * radius * height)
print("The surface area of the cylinder is:", area)

# Calculate volume of a cylinder ("πr**2h")
volume = math.pi * radius**2 * height
print("The volume of the cylinder is:", volume)