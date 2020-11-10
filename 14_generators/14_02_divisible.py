'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
import random
randomList = [random.randint(1000, 99999) for n in range(10000)]

generator2 = (x for x in randomList if x % 1111 == 0)

for x in generator2:
    print(x)
