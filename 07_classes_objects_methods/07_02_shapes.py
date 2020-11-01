'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math

# class for rectangle with length and width
class Rectangle:
    """Used to describe a rectangle with lenght and width"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    def calc_perim(self):
        return (self.length + self.width)*2

    def __str__(self):
        return f"A rectangle with lenght {self.length} and width {self.width}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.length}, {self.width})"


# class for circle with radius

class Circle:
    """Used to describe a circle with radius"""

    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return math.pi * self.radius**2

    def calc_circum(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"A circle with radius {self.radius}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.radius})"



r1 = Rectangle(10, 15)
print(repr(r1))
print(str(r1))
print(f"The area of the rectangle is {r1.calc_area()}")
print(f"The perimeter of the rectangle is {r1.calc_perim()}\n")

c1 = Circle(6)
print(repr(c1))
print(str(c1))
print(f"The area of the circle is {round(c1.calc_area(), 2)}")
print(f"The circumference of the circle is {round(c1.calc_circum(), 2)}")