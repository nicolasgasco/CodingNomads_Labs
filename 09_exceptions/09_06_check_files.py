'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'

def read_num_char(file, multiplier):
    try:
        with open(file, "r") as fin:
            first_character = int(fin.read(1))
            result = first_character * multiplier
    except IOError:
        print("Please provide a valid input")
        pass
    except TypeError:
        print("Please provide a valid number")
        pass
    except Exception:
        print("Something went wrong")
        pass
    else:
        return result


print(read_num_char("integers.txt", 5))