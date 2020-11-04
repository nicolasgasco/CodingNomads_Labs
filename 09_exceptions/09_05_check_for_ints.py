'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

# ask user to input integer

def ask_int():
    while True:
        try:
            integer = int(input("Please insert an integer: "))
        except Exception:
            print(f"Is not an integer")
        else:
            print(f"Is an integer")


ask_int()