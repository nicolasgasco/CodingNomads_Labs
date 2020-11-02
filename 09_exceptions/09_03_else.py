'''
Write a script that demonstrates a try/except/else.

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