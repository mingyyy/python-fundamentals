'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math


class Rectangle():
    '''
    class Rectangle has two attributes the length and width of the rectangle
    length: float
    width: float
    '''

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # calculate the area of a rectangle, presented in four decimal points
        return round(self.length * self.width, 4)

    def perimeter(self):
        # calculate the perimeter of a rectangle, presented in four decimal points
        return round(2 * (self.length + self.width), 4)


class Circle():
    '''
    class Circle takes in one attribute:
    radius: float
    '''

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # calculate the area of a circle, presented in four decimal points
        return round(math.pi * float(self.radius) ** 2, 4)

    def circumference(self):
        # calculate the circumference of a circle, presented in four decimal points
        return round(2 * math.pi * float(self.radius), 4)


# calculate area and circumference of a circle with radius = 3.45
c = Circle(3.45)
print(c.area())
print(c.circumference())

# calculate area and perimeter of a rectangle with length = 3.4 and width = 1.67
r = Rectangle(3.4, 1.67)
print(r.area())
print(r.perimeter())


