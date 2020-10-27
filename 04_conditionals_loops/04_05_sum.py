'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

# two numbers from user, they rapresent range
start = int(input("Please enter a number: "))
end = int(input("Please enter another number: "))

num_list = range(start, end+1)
all_num = []
for n in num_list:
    all_num.append(n)
print(sum(all_num))
