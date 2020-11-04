'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

# open war and peace, read the file content and store in variable
with open("books/war_and_peace.txt", "r") as fin:
        war_peace = []
        for word in fin.readlines():
            war_peace.append(word)

# Open crime_and_punishment.txt and overwrite the whole content with an empty string
with open("books/crime_and_punishment.txt", "w") as fout:
        fout.write("")

# 3) Loop over all three files and print out only the first character each. Your program
#     should NEVER terminate with a Traceback.
#
#     a) Which Exception can you expect to encounter? Why?
#
#     b) How do you catch it to avoid the program from terminating with a Traceback?

def print_first_char(file):
    try:
        with open(file, "r") as fin:
            list = []
            for letter in fin.readline():
                list.append(letter)
    except FileNotFoundError:
        print("Please insert a valid file name")
    except Exception:
        print("Something went wrong")
    else:
        print(list[0])


print_first_char("books/war_and_peace.txt")
#print_first_char("books/pride_and_prejudice.txt")