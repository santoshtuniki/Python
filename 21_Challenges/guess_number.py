import sys
import random as rnd


def guess_number(name='player1'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        playerChoice = input(
            f"\n{name}, Guess which number I'm thinking of ... 1, 2, or 3.\n\n"
        )

        if playerChoice not in ["1", "2", "3"]:
            print(f'\n{name}, please enter 1, 2, or 3 only.')
            return play_guess_number()

        computerChoice = rnd.choice("123")

        print(f'\n{name}, you chose {playerChoice}.')

        print(f'\nI was thinking of the number {computerChoice}.\n')

        player = int(playerChoice)

        computer = int(computerChoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f'{name}, you win!'
            else:
                return f'Sorry, {name}. Better luck next time.'

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        while True:
            playAgain = input("\nY for Yes\nN for No\n")
            if playAgain.lower() not in ["y", "n"]:
                continue
            else:
                break

        if playAgain.lower() == "y":
            return play_guess_number()
        else:
            print("\nThank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                return

    return play_guess_number


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

    guess_my_number = guess_number(args.name)
    guess_my_number()
