'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

# String from user
user_input = str(input("Please write something: "))
# Create a list of all the words in string and print word with most ocurrences
new_text = list(user_input.split(" "))
print(max(new_text, key = len))
