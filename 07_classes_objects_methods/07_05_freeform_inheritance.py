'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

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
        return f"A {self.__class__.__name__} of the make {self.make} and model {self.model}, " \
               f"of the year {self.year} and with a weight of {self.weight}"

class Utility(Car):
    """Class used to represent utility vehicles"""
    def __init__(self, make, model, year, load_cap):
        super().__init__(make, model,year)
        self.load_cap = load_cap

    def __str__(self):
        return f"A {self.__class__.__name__} of the make {self.make} and model {self.model}, " \
               f"of the year {self.year} and with a load capacity of {self.load_cap}"

u1 = Utility("Isuzu", "Loader", 1995, 1500)
print(u1)