'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
amount = int(input("Please tell us your intended investment amount, in US dollar: "))
i = int(input("Please key in the yearly interest rate, in percentage: "))
yr = int(input("How many years you want to invest : "))

fv = amount * (1 + i / 100) ** yr
print(f"If we assume a constant interest rate and based on yearly compounding, your investment after {yr} years would be {fv} US dollars.")

