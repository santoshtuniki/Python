def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


tommy = parent_function('Tommy')
jenny = parent_function('Jenny')

tommy()
tommy()

jenny()

tommy()
'''
Tommy has 2 coins left.

Tommy has 1 coin left.

Jenny has 2 coins left.

Tommy is out of coins.
'''