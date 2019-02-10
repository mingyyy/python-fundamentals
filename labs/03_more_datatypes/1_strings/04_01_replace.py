'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

import re

# take string
sentence = input("Input a string please: ")

# take symbol
sym = input("Input a symbol please: ")
# first letter of the string
fl = sentence[0]

fl_re = re.compile(fl, re.IGNORECASE) # turn off case-sensitive
sentence_re = fl_re.sub(sym, sentence)
print(sentence_re)



