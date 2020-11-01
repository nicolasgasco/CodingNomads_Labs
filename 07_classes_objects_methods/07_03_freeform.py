'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Create at least two objects of each class using the __init__ method.
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''

# Three classes for everyday objects with __init__ at least three attributes
class Car:
    """Class used to represent cars"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"A {self.__class__.__name__} of the make {self.make} and model {self.model} of the year {self.year}"

class SportsCar(Car):
    """Class used to represent sports car"""
    def __init__(self, make, model, year, hp):
        super().__init__(make, model, year)
        self.hp = hp

    def __str__(self):
        return f"A {self.__class__.__name__} of the make {self.make} and model {self.model}, of the year {self.year} and with {self.hp} hp"

class SUV(Car):
    """Class used to represent SUV"""
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year)
        self.weight = weight

    def __str__(self):
        return f"A {self.__class__.__name__} of the make {self.make} and model {self.model}, of the year {self.year} and with a weight of {self.weight}"


# at least two objects of each using __init__ method
c1 = Car("Toyota", "Corolla", 2020)
s1 = SportsCar("Ferrari", "Testarossa", 1992, 400)
su1 = SUV("Opel", "Grandland", 2020, 1500)

print(s1)
print(c1)
print(su1)