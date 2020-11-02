'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''

try:
    list_ = ["hello world!"]
    print(list_[1])
except Exception as e:
    print(f"An error ocurred (Description: {e})")
