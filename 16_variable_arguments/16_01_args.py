'''
Write a script with a function that demonstrates the use of *args.

'''

def token_color(*args):
    for color in args:
        print(f"Please pick a {color} token")

token_color("red", "blue", "yellow", "white", "black", "brown", "purple", "green")