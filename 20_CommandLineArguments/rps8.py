import sys

import random

from enum import Enum


def rps(name='player1'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        playerChoice = input(
            f"\n{name}, please enter ... \n1. For Rock,\n2. For Paper,\n3. For Scissor:\n\n"
        )

        if playerChoice not in ["1", "2", "3"]:
            print(f'\n{name}, please enter 1, 2, or 3 only.')
            return play_rps()

        computerChoice = random.choice("123")

        computer = int(computerChoice)

        player = int(playerChoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '')}.")

        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name

            if player == 1 and computer == 3:
                player_wins += 1
                return f'🎉 {name}, you win!'
            elif player == 2 and computer == 1:
                player_wins += 1
                return f'🎉 {name}, you win!'
            elif player == 3 and computer == 2:
                player_wins += 1
                return f'🎉 {name}, you win!'
            elif player == computer:
                return '😲 Tie Game!'
            else:
                python_wins += 1
                return f'🐍 Python wins!\nSorry, {name}... 😢'

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f'\nGame count: {game_count}')
        print(f"\n{name}'s wins: {player_wins}")
        print(f'\nPython wins: {python_wins}')

        print(f"\nPlay Again, {name}?")

        while True:
            playAgain = input("\nY for Yes\nN for No\n")
            if playAgain.lower() not in ["y", "n"]:
                continue
            else:
                break

        if playAgain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_rps


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized game experience.'
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True,
        help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    rock_paper_scissor = rps(args.name)
    rock_paper_scissor()
