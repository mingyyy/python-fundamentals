'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
'''
ub = int(input("Please enter a number as upper bound:"))
lb = int(input("Please enter a number as lower bound:"))
s = 0
for i in range(lb, ub+1):
    s += i

print(f'The sum (inclusive of both ends) is: {s}')
