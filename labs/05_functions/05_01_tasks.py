'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results

user_input = int(input("Please enter a number from 1 to 1,000,000,000: "))


def div_4n7(num):
    # function that checks if a number is divisible by both 4 AND 7.
    if num % 4 == 0 and num % 7 == 0:
        return "Yes, it's divisible by both 4 and 7."
    else:
        return "Sorry, it's not divisible by both 4 and 7"


def div_4o7(num):
    # function that checks if a number is divisible by 4 or 7.
    if num % 4 == 0 or num % 7 == 0:
        return "Yes, it's divisible by 4 or 7."
    else:
        return "Sorry, it's not divisible by 4 or 7"


def div_4_7(num):
    # function that shows if a number is divisible by either 4 or 7, or by both.
    if num % 4 == 0:
        if num % 7 == 0:
            return "It's divisible by 4 and 7."
        else:
            return "It's only divisible by 4, not by 7."

    else:
        if num % 7 == 0:
            return "It's only divisible by 7, not by 4."
        else:
            return "Sorry, it's not divisible by 4 nor 7."


print(div_4n7(user_input))
print(div_4o7(user_input))
print(div_4_7(user_input))
