'''
Write a script that demonstrates a try/except/else.

'''
from random import randint
import math

print("Test your luck of the day!")
word = input("Input word of your choice for draw (maybe not too short):")
try:
    result = math.floor(math.sqrt(len(word) - randint(1, 5)))
    list_ = ["You will be very happy today!", "It's your lucky day!", "It's not your day! Sorry",
             "It's just another gloomy day!", "Get ready to be amused.", "Surprise!"]

    result_today = list_[result]

except ValueError as ve:
    print("Sorry... Something went wrong. Try another word please", )
else:
    print(result_today)
