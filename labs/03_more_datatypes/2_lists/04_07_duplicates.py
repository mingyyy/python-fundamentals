'''

Write a script that removes all duplicates from a list.

'''
inputs = input("Enter a list (separated by comma): ").split(",")

n = len(inputs)
inputs_new = [inputs[0]]
k = 1
for i in range(1, n):
    inputs_part = inputs[i:]
    k = len(inputs_new)
    n = 0
    for j in range(0, k):
        if inputs_part[0] != inputs_new[j]:
            n += 1
        if n == k:
            inputs_new.append(inputs_part[0])

print("After removing all duplicates, the result is:")
print(inputs_new)

# after reading "set", I saw a easier solution
input_set = set(inputs)
print(input_set)




