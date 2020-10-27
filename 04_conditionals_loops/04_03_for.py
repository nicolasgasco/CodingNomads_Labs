'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
odd_numbers = []
for n in range(1,101):
    if n % 2 != 0:
        odd_numbers.append(n)

print(odd_numbers)