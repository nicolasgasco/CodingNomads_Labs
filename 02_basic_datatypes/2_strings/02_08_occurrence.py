'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

# String of words from the user
string = input("Please write something here: ")

# Letter from the user
letter = input("Please write a letter: ")

# Find the index of first occurrence in string
print(string.find(letter))
