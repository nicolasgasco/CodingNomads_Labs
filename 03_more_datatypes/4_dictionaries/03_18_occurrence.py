'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

# take string from user
user_input = input("Please insert a sentence here: ")

new_list = list(user_input)
# create dictionary of letter in strings with occurence

new_dict = {}
for l in new_list:
    if l == " ":
        continue
    new_dict[l] = user_input.count(l)

print(new_dict)
