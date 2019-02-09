'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
UserI = input("Enter a sentence here: ").split()
result_list = []

for w in UserI:
    word_list = []
    print(w)
    for i in w:
        word_list.append(i)

    tuple_list = tuple(word_list)
    result_list.append(tuple_list)

print(result_list)



