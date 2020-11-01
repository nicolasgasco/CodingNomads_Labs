'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:
    """Used to represent planets"""
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    # def __str__(self):
    #   return f"This class represents a planet with its {self.name}, {self.color}, and {self.size}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.color}, {self.size})"

    def __str__(self):
        return f"{self.name} is a {self.color} planet, its size is {self.size}"

planet1 = Planet("Pluto", "grey", 10000)
print(planet1)