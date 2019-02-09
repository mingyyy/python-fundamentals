'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

flat_list = []
start_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for s in start_list:
    for i in s:
        flat_list.append(i)

print(flat_list)
