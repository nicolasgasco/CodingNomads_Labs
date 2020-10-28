'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

def pos_neg(num):
    if num > 0:
        return -num
    elif num < 0:
        return -num
    else:
        return num

def divide_3(num):
    return num / 3

def multiply_ten(num):
    return num * 10

print(multiply_ten(divide_3(pos_neg(-5))))