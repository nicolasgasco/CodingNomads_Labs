'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

# Take user name
user_name = input("Please enter your user name: ")
# Move first letter to end
pig_name = user_name[1:] + user_name[0] + "ay"

# Print out name in pig latin
print("This is your name in pig Latin:", pig_name.capitalize())