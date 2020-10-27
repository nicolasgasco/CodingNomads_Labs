'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

user_input = int(input("Please write a number between 1 and 12: "))

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Septmber', 'October', 'November', 'December']


if user_input == 0:
    print("Other")
elif user_input <= 12:
    print(months[user_input - 1])
else:
    print("Other")