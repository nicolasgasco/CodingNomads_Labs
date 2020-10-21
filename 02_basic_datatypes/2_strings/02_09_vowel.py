'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

# Create user input

user_input = input("Please write something here: ")

# Need this to rule out uppercase letters
input_lower = user_input.lower()

# Cannot find a way to do all vowels together yet
a_count = input_lower.count("a")
e_count = input_lower.count("e")
i_count = input_lower.count("i")
o_count = input_lower.count("o")
u_count = input_lower.count("u")

total_count = a_count + e_count + i_count + o_count + u_count

print("The total number of vowels is:", total_count, end="\n")
print("The number of As is:", a_count)
print("The number of Es is:", e_count)
print("The number of Is is:", i_count)
print("The number of Os is:", o_count)
print("The number of Us is:", u_count)

#This doesn't word for foreign languages with accents

