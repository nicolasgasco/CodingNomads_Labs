'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

# Three values from the user
invest_amount = float(input("Please enter the investment amount: "))
int_rate_percent = float(input("Please enter the interest rate in percentage: "))
num_years = float(input("Please enter the number of years to invest: "))

# Value is calculate as such: FV = Invest x (1 + (Rate x Time)

fut_val = invest_amount * (1 + ((int_rate_percent/100) * num_years))
print("The future value is:", round(fut_val, 2))