'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

with open ("words.txt", "r") as fin:
    new_list = []
    for word in fin.readlines():
        word = word.rstrip()
        new_list.append(word)

# shortest word
shortest_word = min(new_list, key= len)
print(f"The shorted word in the list is: '{shortest_word}'.")


# longest word
longest_word = max(new_list, key=len)
print(f"The longest word in the list is '{longest_word}'.")

# total number of words
print(f"The total number of words in the file is {len(new_list)}.")
