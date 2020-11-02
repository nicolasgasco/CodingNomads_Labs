import random
# create two classes for hero and opponent

class Hero:
    "Class for the hero of the game"
    def __init__(self, name, level, gender):
        self.name = name
        self.level = level
        self.gender = gender

    def attack(self, opponent):
        print(f"{self.name} attacks {opponent.name}!\n")

        hero_roll = random.randint(1, 12) * self.level
        opp_roll = random.randint(1, 12) * opponent.level

        print(f"Your roll is {hero_roll}.")
        print(f"{opponent.name}'s roll is {opp_roll}.\n")

        if hero_roll >= opp_roll:
            print(f"{self.name} won over {opponent.name}!\n\n")
            return True
        else:
            print(f"DEFEAT! {opponent.name} has defeated {self.name}!\n\n")
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.level}, {self.gender})"


class Opponent():
    "Class for the opponent of the game"
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.level})"

h1 = Hero("Luke Skywalker", 15, "male")
op1 = Opponent("Bounty hunter", 8)
