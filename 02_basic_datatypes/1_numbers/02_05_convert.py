'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

# Convert an int to a float
integer = 10
print("The integer", integer, "has been converted to float:", float(integer))

# Convert a float to an int
floatn = 6.7
print("The float", floatn, "has been converted to integer:", int(floatn), "\n")

# Floor division with float and int
print("This is a normal division:", integer/floatn)
print("This is a floor division:", integer // floatn, "\n")


# Two inputted values to multiply
value1 = float(input("Please insert a first value: "))
value2 = float(input("Please insert another value: "))

print("The two values multiplied together are:", value1 * value2)





