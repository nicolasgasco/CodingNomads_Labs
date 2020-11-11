'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''
list1 = ["first", "second", "third", "fourth", "fifth"]

def my_enumerate(list, num=0):
    new_list = [(i+num, list[i]) for i in range(len(list))]
    return new_list

print(my_enumerate(list1, 100))
