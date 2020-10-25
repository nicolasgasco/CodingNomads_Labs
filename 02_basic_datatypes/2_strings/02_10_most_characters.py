'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

# Three strings from user
inp_1 = input("Please write a first sentence: ")
inp_2 = input("Please write a second sentence: ")
inp_3 = input("Please write a third sentence: ")

# Prints them with their length
len_1 = len(inp_1)
len_2 = len(inp_2)
len_3 = len(inp_3)

'''

print(len_1, ",", inp_1)
print(len_2, ",", inp_2)
print(len_3, ",", inp_3)

'''

# print only the string
if len_1 > len_2 & len_1 > len_3:
    print(f"{len_1}, {inp_1}")
elif len_2 > len_1 & len_2 > len_3:
    print(f"{len_2}, {inp_2}")
elif len_3 > len_1 & len_3 > 2:
    print(f"{len_3}, {inp_3}")
else:   print("This is impossible")




