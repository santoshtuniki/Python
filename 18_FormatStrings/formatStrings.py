# concatenation
person = 'Sai'
coins = 3

print('\n' + person + " has " + str(coins) + " coins left.")
# Sai has 3 coins left.


# %s
message = '\n%s has %s coins left.' % (person, coins)

print(message)  # Sai has 3 coins left.


# format
message = '\n{} has {} coins left.'.format(person, coins)

print(message)  # Sai has 3 coins left.


message2 = '\n{1} has {0} coins left.'.format(coins, person)

print(message2)  # Sai has 3 coins left.


message3 = '\n{person} has {coins} coins left.'.format(
    person=person, coins=coins
)

print(message3)  # Sai has 3 coins left.


player = {
    'person': 'Sai',
    'coins': 3
}

message4 = '\n{person} has {coins} coins left.'.format(**player)

print(message4)  # Sai has 3 coins left.
