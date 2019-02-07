'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
import math

r = 3.14
h = 5
v = r ** 2 * math.pi * h
s = 2 * math.pi * r * (h +r)

print(f"The volume of the cylinder is {v} and the surface area is {s} ")
