'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


while True:
    try:
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
        res = num1 / num2
    except ValueError:
        print(f"Please insert a number, not a string")

    except ZeroDivisionError:
        print(f"You cannot divide by 0.")

    except Exception:
        print(f"An error occurred")

    else:
        print(res)