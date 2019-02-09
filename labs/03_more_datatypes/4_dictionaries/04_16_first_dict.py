'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

result_d = {x: x**2 for x in range(1, 11, 1)}
print(result_d)
print(type(result_d))
