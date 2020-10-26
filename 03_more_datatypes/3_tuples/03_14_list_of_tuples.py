'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

# take string from user
user_input = (input("Please write something: "))


new_list = []
for element in user_input.split(" "):
    new_list.append(tuple(element))

print(new_list)