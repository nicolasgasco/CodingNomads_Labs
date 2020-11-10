'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
import random
randomList = [random.randint(1000, 99999) for n in range(10000)]

generator2 = (x for x in randomList if x % 1111 == 0)

for x in generator2:
    print(x % 1111)