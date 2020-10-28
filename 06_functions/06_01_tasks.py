'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def isdivisible_single(num):
    if num % 7 == 0 or num % 4 == 0:
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def isdivisible_both(num):
    if num % 7 == 0 and num % 4 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000
x = int(input("Please write a number between 1 and 1000000000: "))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
y = isdivisible_single(x)
z = isdivisible_both(x)
# print your new variables to display the results
print(y, z)
