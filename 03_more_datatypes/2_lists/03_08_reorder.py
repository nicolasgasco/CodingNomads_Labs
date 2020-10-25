'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

# Ask 10 numbers from user
num_list = []

while len(num_list) < 10:
    user_input = input("Please insert a number: ")
    num_list.append(user_input)

print("These are ocurrences number 2, 4, 6, 8, 10: ", num_list[::2])

new_list2 = []
i += 2
for i in num_list:
    new_list2.append(i)

print(new_list2)