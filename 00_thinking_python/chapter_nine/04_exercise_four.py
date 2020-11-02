"""
Write a function named uses_only that takes a word and a string of letters,
and that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa”?

"""

# takes a word and a string of letters
# return True if the words contains only letter in the list
def uses_only(choose_word, letters_string):
    word = choose_word
    string = letters_string
    x = 0
    for letter in set(letters_string):
        if letter in word:
            x += 1
        else:
            x -= 1
    if x == len(set(word)):
        return True
    else:
        return False

# print(uses_only("aaaaaaaaaaaaaaaaaaaaaaa", "acefhlo"))

def isolate_words(file, string):
    with open (file, "r") as fin:
        words = []
        x = 0
        for word in fin.readlines():
            word = word.strip()
            for letter in set(string):
                if letter in set(word):
                    x += 1
                else:
                    x += 3
            if x == len(set(word)):
                words.append(word)
        return words


#uses_only Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?
print(isolate_words("words.txt", ""))


