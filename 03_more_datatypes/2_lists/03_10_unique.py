'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

# list of all unique values
list1 = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(list2)


