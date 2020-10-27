'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
num = range(0, 1000000001)
user_input = int(input("Please insert a number between 0 and 1,000,000,000: "))

n = 0
while n in num:
    n += 1
    if n == user_input:
        print(n)

