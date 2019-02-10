'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input:
Result: 4

'''
# take string
str = input("Input a string please:")

# take letter
l = input("Input a letter please:")

i = 0 # counter
for x in str:
    i += 1
    if x == l:
        print(i)
        break
else:
    print("The letter is not in the string.")



