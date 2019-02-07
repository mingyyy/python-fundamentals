'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# 1) int to float
i2f = float(2)
# 2) float to int
f2i = int(2.334)
# 3) floor division
fd = 3 // 1.56
# 4) multiplication
in1 = int(input("Please enter an integer from 1 to 10:"))
in2 = float(input("Please enter your height in cm (e.g. 160.2):"))
m = in1 * in2
print(f"Congrats! You win {m} !")




