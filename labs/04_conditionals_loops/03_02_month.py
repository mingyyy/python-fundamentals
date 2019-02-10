'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
num = int(input("Enter a number:"))
dic_month = dict([(1, "January"), (2, "February"), (3, "March"), (4, "April"), (5, "May"), (6, "June"), (7, "July"), (8, "August"), (9, "September"), (10, "October"), (11, "November"), (12, "December")])

n = 0
for k, v in dic_month.items():
    if num == k:
        n = 1
        if n == 1:
            print(v)
if n == 0:
    print("Others")





