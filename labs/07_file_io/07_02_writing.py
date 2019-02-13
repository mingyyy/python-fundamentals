'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

with open("words.txt", "r") as f:
    store = []
    for line in f.readlines():
        store.append(line)

store_ = store[::-1]

with open("words_reverse.txt", "w+") as file:
    for word in store_:
        file.write(word)

