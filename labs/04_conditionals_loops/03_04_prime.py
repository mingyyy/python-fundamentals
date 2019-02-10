'''
Print out every prime number between 1 and 100.

'''
for i in range(1, 101):
    n = 0
    for j in range(2, i):
        if i % j == 0:
            n += 1
    if n == 0:
        print(f"{i} is a prime number")
