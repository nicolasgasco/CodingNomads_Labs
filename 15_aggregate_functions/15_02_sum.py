'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

def sum(list):
    total = 0
    for n in list:
        total += n
    return total

list1 = [1, 34, 43, 1, 455, 234]
list2 = [2, 3, 5]

print(sum(list2))