"""
Write a function named uses_all that takes a word and a string of required letters, and that returns True if the word
 uses all the required letters at least once. How many words are there that use all the vowels aeiou? How about aeiouy?

"""
# takes a word and a string of letters
def uses_all(choose_word, letters_string):
    x = 0
    for letter in set(letters_string):
        no_rep = set(choose_word)
        if letter in no_rep:
            x += 1
        else:
            x += 0
        if x == len(set(choose_word)):
            return True
        else:
            return False



print(uses_all("ciao", "ccciiaao"))