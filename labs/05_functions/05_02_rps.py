'''
Code a game of rock paper scissors.

'''
import random


# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    # for example if the variable hand is 0, it should return the string "scissor"
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    elif hand == 2:
        return "paper"
    else:
        return "Wrong input!"


# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    if computer == player:
        return "You tied"
    elif (computer == "scissor" and player == "paper") or \
            (computer == "rock" and player == "scissor") or \
            (computer == "paper" and player == "rock"):
        return "You lost :("
    else:
        return "You won!"


'''
Start here
'''
wrong_input = True
player_hand = 0 # default value for player hand
# take in a number 0-2 from the user that represents their hand
while wrong_input:
    player_hand = int(input("Please enter an integer to show your hand (0, 1, 2): "))
    if player_hand in (0, 1, 2):
        wrong_input = False
    else:
        print("Your number is out of range!")
# generate a random number 0-2 to use for the computer's hand
pc_hand = random.randint(0, 2)
# call the function get_hand to get the string representation of the user's hand
player = get_hand(player_hand)
# call the function get_hand to get the string representation of the computer's hand
computer = get_hand(pc_hand)
# call the function determine_winner to figure out the winner
result = determine_winner(computer, player)
# print out the player hand and computer hand
print(f"The player's hand is {player} and the computer's hand is {computer}.")
# print out the winner
print(result)
