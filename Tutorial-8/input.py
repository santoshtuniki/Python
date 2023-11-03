import sys

import random

from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print("")

playerChoice = input("Enter ... \n1. For Rock,\n2. For Paper,\n3. For Scissor:\n\n")

player = int(playerChoice)

if player < 1 or player > 3:
    sys.exit('You must enter 1, 2, or 3 only.')

computerChoice = random.choice("123")

computer = int(computerChoice)

print("")

print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")

print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")

print("")

if player == 1 and computer == 3:
    print('You win!')
elif player == 2 and computer == 1:
    print('You win!')
elif player == 3 and computer == 2:
    print('You win!')
elif player == computer:
    print('Tie Game!')
else:
    print('Python wins!')

