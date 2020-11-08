"""
Write a function named avoids that takes a word and a string of forbidden letters, and that returns True
if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and then prints the number of words
that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
"""

# takes a word and a string of forbidden letters
def avoids(word, letters_string):
    for letter in word:
        if letter in letters_string:
            return False
        return True

# user enter a string of forbidden
def num_word_exclude(file):
    forbidden_letters = input("Please enter a string of forbidden letters: ")
    with open(file, "r") as fin:
        with_letters = []
        all_words = []
        for word in fin.readlines():
            word = word.strip()
            all_words.append(word)
            for letter in forbidden_letters:
                if letter in word:
                    with_letters.append(word)
        no_letters = [x for x in all_words if x not in with_letters]
        return len(no_letters)

num_word_exclude("words.txt")