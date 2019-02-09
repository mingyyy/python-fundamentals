'''
Take in 10 numbers from the user. Place the numbers in a list.
Calculate the product of all of the numbers in the list.
Also, find the largest number in the list.

Print the results.

'''
import sys

while True:

    numbers = input("Enter 10 numbers (separated by comma): ").split(",")
    if len(numbers) != 10:
        numbers = input("Not 10 numbers, please re-enter numbers after ENTER.")
        continue
    for n in numbers:
        try:
            val = int(n)
        except ValueError:
            print("Sorry... your input is a string not a number!")
            continue # not working as expected ...

    prod = 1
    for n in numbers:
         prod *= int(n)

    print(f"The product of the 10 numbers is: {prod}")
    sys.exit()



