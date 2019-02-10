'''
Print out every prime number between 1 and 100.

'''
sum = 0
for i in range(1, 101):
    n = 0
    for j in range(2, i):
        if i % j == 0: # prime number can only be divided by 1 and itself.
            n += 1
    if n == 0:
        print(f"{i} is a prime number")
        sum += 1
print(f"In total, there are {sum} prime numbers between 1 and 100. ")
