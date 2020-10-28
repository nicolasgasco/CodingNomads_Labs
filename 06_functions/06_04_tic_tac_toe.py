'''

Code a game of rock paper scissors.

Instructions
- take in a number 0-2 from the user that represents their hand
- generate a random number 0-2 to use for the computer's hand
- call the function get_hand to get the string representation of the user's hand
- call the function get_hand to get the string representation of the computer's hand
- call the function determine_winner to figure out who won
- print out the player hand and computer hand
- print out the winner
Some Tips
Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"
    pass

'''
import random
# take in a number 0-2 from the user that represents their hand
user_hand = int(input("Please insert 0 per scissors, 1 for rock, or 2 for paper: "))

# generate a random number 0-2 to use for the computer's hand
computer_hand = random.randint(0,2)

# call the function get_hand to get the string representation of the user's hand
def get_hand(hand):
    if hand == 0:
        return "Scissors"
    elif hand == 1:
        return "Rock"
    elif hand == 2:
        return "Paper"
    pass

# call the function get_hand to get the string representation of the computer's hand

# call the function determine_winner to figure out who won
def determine_winner(hand1, hand2):
    if hand1 == "Scissors" and hand2 == "Paper":
        return hand1
    elif hand1 == "Scissors" and hand2 == "Rock":
        return hand2
    elif hand1 == "Scissors" and hand2 == "Scissors":
        return str("Draw")
    elif hand1 == "Rock" and hand2 == "Paper":
        return hand2
    elif hand1 == "Rock" and hand2 == "Rock":
        return str("Draw")
    elif hand1 == "Rock" and hand2 == "Scissors":
        return hand1
    elif hand1 == "Paper" and hand2 == "Paper":
        return str("Draw")
    elif hand1 == "Paper" and hand2 == "Rock":
        return hand1
    elif hand1 == "Paper" and hand2 == "Scissors":
        return hand2


# print out the player hand and computer hand
print(f"The user hand is: {get_hand(user_hand)}")
print(f"The computer hand is: {get_hand(computer_hand)}")



# print out the winner
print(f"The winner is: {determine_winner(get_hand(user_hand), get_hand(computer_hand))}")