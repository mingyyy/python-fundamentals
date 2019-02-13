'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

# Shortest/Longest words in the file
with open("words.txt", "r") as f:
    cw = f.readline().rstrip()
    lw = cw
    shortests = [cw]
    longests = [lw]
    n = 0
    for word in f.readlines():
        w = str(word.rstrip())
        n += 1
        if len(w) < len(cw):
            shortests.clear()
            shortests.append(w)
            cw = w
        elif len(w) == len(cw) :
            shortests.append(w)
        elif len(w) == len(lw):
            longests.append(w)
        elif len(w) > len(lw):
            longests.clear()
            longests.append(w)
            lw = w
        else:
            pass


print(shortests)
print(f"There are {len(shortests)} words each has only {len(cw)} characters.\n")

print(longests)
print(f"There are {len(longests)} words each of which contains {len(lw)} characters.\n")

print(f"There are {n} words in total.")
