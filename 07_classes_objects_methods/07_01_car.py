'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

# Write a class for a car
class Car:
    "Class used to describe a car with model, year, and max speed"

    # model, year, max_speed in init
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"The car's model is {self.model}, the year of fabrication is {self.year}, and the max speed is {self.max_speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.model}, {self.year}, {self.max_speed})"

# method to increase max_speed by 5
    def speed_increase(self):
        self.max_speed -= 5

# method to print details of car
car1 = Car("Ferrari 575", 2002, 290)
car2 = Car("Lamborghini Gallardo", 200, 300)

car2.speed_increase()
car2.speed_increase()
car2.speed_increase()
print(car2)

#create two objects
