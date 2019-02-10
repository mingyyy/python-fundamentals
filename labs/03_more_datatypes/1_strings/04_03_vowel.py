'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''
# vowels in English : a e i o u (y)
v = ["A", "E", "I", "O", "U"]
str = input("Please enter a string:")

n = 0 # counter

for i in str.upper():
    if i in v:
        n += 1
if n == 1:
    print(f"If excluding Y from vowels, there is one vowel used in the string. ")
else:
    print(f"If excluding Y from vowels, there are {n} times of vowels used in the string. ")

# According to Merriam-Webster:
# Y is a vowel if the word has no other vowel: gym, my.
# Y is a vowel if the letter is at the end of a word or syllable: candy, deny, bicycle, acrylic.
# Y is a vowel if the letter is in the middle of a syllable: system, borborygmus.
# Because it is too complicated to check if a string is a English word, or to count syllables.
# So I will only consider Y as a vowel if there is no other vowels.

# An online solution seems to solve the English word puzzle.
# https://stackoverflow.com/questions/44233588/how-to-check-to-see-if-a-string-is-contained-in-any-english-word

# Counting syllables solution online.
# https://stackoverflow.com/questions/34209176/counting-syllables-within-a-word

if n == 0:
    for i in str.upper():
        if i == "Y":
            n += 1
    if n == 1:
        print(f"If counting Y as a vowel, there is one vowel used in the string.")
    else:
        print(f"If counting Y as a vowel, there are {n} times of vowels used in the string.")




