class Car:
    """Represents a car with model, year, and speed"""
    def __init__(self, model, year, speed=0):
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        """Add 5 to the speed"""
        self.speed += 5
        return self.speed

    def brake(self):
        """Subtract 5 to the speed"""
        if None:
            self.speed = 0
            return self.speed
        if self.speed != 0:
            self.speed -= 5
            if self.speed < 0:
                self.speed = 0
                return self.speed
            else:
                return self.speed
        else:
            self.speed = 0

    def honk_horn(self):
        """Print a beep beep sentence with model"""
        print(f"{self.model} goes 'beep beep'")

    def __str__(self):
        return f"{self.model}, {self.year}, {self.speed}"

    def __repr__(self):
        return f"Car({self.model}, {self.year}, {self.speed})"

i = Car("Ferrari", 2001, 250)
print(i)
'''
class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = 5
        self.y = 10

g = 1
f = 7
y = Point(g, f)
print(y.x + y.y)
'''