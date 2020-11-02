import random
import time
from CLIgame_characters import Hero, Opponent

def main():
    print_welcome()
    play_game()

def print_welcome():
    print("""
----------------------------------------------------------
---------- Welcome to Star Wars CLI adventures! ----------
----------------------------------------------------------
This is my very first game in Python and an optional exer-
cise for the CodingNomads Python course. Since I dont't
have much immagination and I'm a big Star Wars fan, I
chose to go with the Star Wars theme. Originality...

""")
    time.sleep(2)

def play_game():

    opponents = [
        Opponent("Fighting droid", 5),
        Opponent("Rookie trooper", 8),
        Opponent("General", 10),
        Opponent("Experienced trooper", 11),
        Opponent("Sith apprentice", 14),
        Opponent("Sith lord", 18),
        Opponent("Darth Vader", 20),
    ]

    hero = Hero("Luke Skywalker", 19, "male")

    while True:
        #select random opponent
        current_opponent = random.choice(opponents)
        print(f"Beware... {current_opponent.name} of level {current_opponent.level} has shown up"
              f" and is very angry at you!\n")

        cmd = input("Do you want to [a]ttack, [e]scape or [l]ook around?\nPlease insert input here: ")
        # check up for input validity
        while cmd not in ["a", "e", "l", "q"]:
            print("Please enter a valid input to play")
            print('To exit the game, type [q] for "quit".')
            cmd = input("Do you want to [a]ttack, [e]scape or [l]ook around?\nPlease insert input here: ")

        # Attack logic
        if cmd == "a":
            if hero.attack(current_opponent):
                opponents.remove(current_opponent)
            else:
                print(f"{hero.name} takes a short nap...")
                time.sleep(5) # 5 seconds pause
                print(f"{hero.name} come back refreshed!\n")
        # Escape logic
        if cmd == "e":
            print("You roll a dice to escape...")
            dice = random.randint(1, 12)
            time.sleep(3)
            if dice >= 6:
                print(f"{dice}! Pheeew! You escaped.")
            else:
                print(f"{dice}! Your escape wasn't successful")
                cmd = input("Do you want to [a]ttack or trying to [e]scape again\nPlease insert input here: ")
                # check up for input validity
                while cmd not in ["a", "e", "l", "q"]:
                    print("Please enter a valid input to play")
                    print('To exit the game, type [q] for "quit".')
                    cmd = input("Do you want to [a]ttack or trying to [e]scape again\nPlease insert input here: ")
                    if cmd == "a":
                        if hero.attack(current_opponent):
                            opponents.remove(current_opponent)
                        else:
                            print(f"{hero.name}, you died!")
                            break
                else:
                    if cmd == "a":
                        if hero.attack(current_opponent):
                            opponents.remove(current_opponent)
                        else:
                            print(f"{hero.name}, you died!")
                            break
    # Lookaround logic
    if cmd == "l":
        pass

main()

