'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
import math
def root_multiply(num1, num2):
    """Function to calculate the squared root of num1 and multiply it by num2"""
    try:
        rt = math.sqrt(num1)
    except Exception:
        print("Please don't use a negative value")
    else:
        result = rt * num2
        return result

print(root_multiply(-2,2))