'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
# input three strings
i1 = input("Enter first string, please:")
i2 = input("Enter second string, please:")
i3 = input("Enter third string, please:")

# counting the characters, if space is counted as a character.
c1 = len(i1)
c2 = len(i2)
c3 = len(i3)

# compare the number of characters

if c1 == c2:
    if c1 == c3: # c1 = c2 = c3
        print("They have the same number of character.")
        print(i1, i2, i3)
    elif c3 > c1: # c3 > 1 = c2
        print(i3)
    else: # c3 < c1 = c2
        print(i1, i2)
elif c1 < c2:
    if c2 == c3: # c1 < c2 = c3
        print(i2, i3)
    elif c2 < c3: # c1 < c2 < c3
        print(i3)
    else: # c1 < c2 > c3
        print(i2)
else: # c1 > c2
    if c1 == c3: # c1 = c3 > c2
        print(i1, i3)
    elif c1 < c3: # c2 < c1 < c3
        print(i3)
    else: # c2 < c1 >c3
        print(i1)






