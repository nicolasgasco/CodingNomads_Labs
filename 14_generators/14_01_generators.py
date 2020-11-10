'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

generator = (x**3 for x in range(50))

print(generator)

for n in generator:
    print(n)