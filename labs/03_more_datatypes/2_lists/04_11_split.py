'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
inputs = input("Enter a sentence here:").split(" ")
str_list = []
for w in inputs:
    str_list.append(w)

maxn = 1
maxw = str_list[0]
for w in str_list:
    pmn = str_list.count(w)
    pmw = w
    if pmn > maxn: # if more than one word have the most occurrence, only the first one will be the winner.
        maxn = pmn
        maxw = w

wc = len(str_list)

if wc == 1:
    print("There is only one word in the sentence.")
else:
    print(f"There are {wc} words in the sentence.")


print(f' "{maxw}" has the most occurrences, in total {maxn} times.')
