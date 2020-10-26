'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

# take two dictionaries, joins the values

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict_3 = {}


for x, y in dict_1.items():
    for z, h in dict_2.items():
        if x == z:
            dict_3[x] = (y + h)
        elif x not in dict_2 and x not in dict_3:
            dict_3[x] = y
        elif z not in dict_1 and z not in dict_3:
            dict_3[z] = h
            
print(dict_3)


