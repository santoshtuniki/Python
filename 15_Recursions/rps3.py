import sys

import random

from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    playerChoice = input(
        "\nEnter ... \n1. For Rock,\n2. For Paper,\n3. For Scissor:\n\n")

    if playerChoice not in ["1", "2", "3"]:
        print('You must enter 1, 2, or 3 only.')
        return play_rps()

    player = int(playerChoice)

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")

    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

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

    print("\nPlay Again?")

    while True:
        playAgain = input("\nY for Yes\nN for No\n")
        if playAgain.lower() not in ["y", "n"]:
            continue
        else:
            break

    if playAgain.lower() == "y":
        return play_rps()
    else:
        print("\nThank you for playing!\n")
        sys.exit("Bye...")


play_rps()
