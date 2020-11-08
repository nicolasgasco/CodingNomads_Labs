"""
Write a function named uses_only that takes a word and a string of letters,
and that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa”?

"""

# takes a word and a string of letters
# return True if the words contains only letter in the list
def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
        return True
# print(uses_only("aaaaaaaaaaaaaaaaaaaaaaa", "acefhlo"))

print(uses_only("ciao", "ciaof"))

def isolate_words(file, string):
    with open (file, "r") as fin:
        words = []
        for word in fin.readlines():
            word_strip = word.strip()
            if uses_only(word_strip, string) == True:
                words.append(word_strip)
                return words


print(isolate_words("words.txt", "acefhlo"))


#uses_only Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?


