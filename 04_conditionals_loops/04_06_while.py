'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

num = range(0, 1001)
new_list = []
for n in num:
    new_list.append(n)
b = new_list[0::5]
print(b[1:])