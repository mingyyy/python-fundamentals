'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

try:
    numerator = int(input("Please enter the numerator (number to be divided): "))
    denominator = int(input("Please enter the denominator (the divisor): "))
    result = numerator / denominator
    print(f"The result of {numerator} divided by {denominator} is {result}")
except ZeroDivisionError as zde:
    print("There was an error with the message: ", zde)

except ValueError as ve:
    print("Wrong data type. You need to enter a number! ")





