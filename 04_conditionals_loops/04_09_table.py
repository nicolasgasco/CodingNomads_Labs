'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
new_list = []
for n in range(0, 50):
    new_list.append(n)
i = 1
str(new_list)
print(str(f"{new_list[0:10]}\n{new_list[10:20]}\n{new_list[20:30]}\n{new_list[30:40]}\n{new_list[40:50]}"))
