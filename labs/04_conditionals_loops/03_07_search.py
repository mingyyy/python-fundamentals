'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
user_input = int(input("Please enter a number between 0 and 1,000,000,000: "))
found = False
i = 0
while found is False:
    if i != user_input:
        i += 1
    else:
        print(f"The number is {i}")
        found = True

