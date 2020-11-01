'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

with open ("words.txt", "r") as fin:
    new_list = []
    for word in fin.readlines():
        if len(word) >= 20:
            word = word.rstrip()
            new_list.append(word)
    print(new_list)

