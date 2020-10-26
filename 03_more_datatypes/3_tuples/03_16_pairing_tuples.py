'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

# Takes in a list of numbers
num_list = list(input("Please insert a list of numbers: "))
num_list.sort()

new_list = []
for n, y in zip(*[iter(num_list)] * 2): # this part off the Internet, of course
    new_tuple = n, y
    new_list.append(new_tuple)
print(new_list)
