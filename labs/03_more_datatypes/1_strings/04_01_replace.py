'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
# take string
str = input("Input a string please:")

# take symbol
sym = input("Input a symbol please:")
# first letter of the string
fl = str[:1]
print(str.replace(fl, sym))




