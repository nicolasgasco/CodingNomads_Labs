'''
Print out every prime number between 1 and 100.

'''
numbers = range(1, 101)
prime_numbers = []
num = 87
for n in range(2, num):
    if num % n == 0:
        prime_numbers.append(n)
        continue
    else:
        prime_numbers.append(n)

print(prime_numbers)