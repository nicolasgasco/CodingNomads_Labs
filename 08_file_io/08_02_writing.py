'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

with open ("words.txt", "r") as fin:
    new_list = []
    for word in reversed(fin.readlines()):
        new_list.append(word)

with open("words_reverse.txt", "w") as fout:
    for word in new_list:
        fout.write(word)
