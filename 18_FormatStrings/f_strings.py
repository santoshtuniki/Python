person = 'Sai'
coins = 3

message = f'\n{person} has {coins} coins left.'

print(message)  # Sai has 3 coins left.


message2 = f'\n{person} has {2 * 3} coins left.'

print(message2)  # Sai has 6 coins left.


message3 = f'\n{person.lower()} has {2 * 3} coins left.'

print(message3)  # sai has 6 coins left.


player = {
    'person': 'Sai',
    'coins': 3
}

message4 = f'\n{player["person"]} has {player["coins"]} coins left.'

print(message4)  # Sai has 3 coins left.


num = 10
print(f'\n2.25 times {num} is {2.25 * num:.2f}.')
#   2.25 times 10 is 22.50.


for num in range(1, 11):
    print(f'\n2.25 times {num} is {2.25 * num:.2f}.')

for num in range(1, 11):
    print(f'\n{num} divided by 4.52 is {num / 4.25:.2%}.')
