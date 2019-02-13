'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of all of
all .jpg files (with the complete path of the files).

If you are feeling bold, create a list for each kind of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then sub out the
folder name with a bigger folder. This program should work for any specified folder on your computer.


'''


path = "/Users/Ming/documents/omneia"

from os import walk

f = []
d = []
JPGs = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)

for file in f:
    extension = file[-3:]
    d.append(extension)

#print(set(d))

lists = [[] for _ in range(len(set(d)))]
i = 0

for ex in set(d):
    n = 0
    for file in f:
        if file.endswith(ex) is True:
            lists[i].append(path + "/" + file)
            n += 1
    i += 1
    print(f"There are {n} .{ex} files.")

for i in range(len(set(d))):
    print(lists[i])





