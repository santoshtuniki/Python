# Change item values

fruits = ["apple", "banana", "cherry"]

fruits[2] = 'Berry'

print(fruits)                    #   ['apple', 'banana', 'Berry']

fruits[2:2] = ['Berry', 'Terry']

print(fruits)                    #   ['apple', 'banana', 'Berry', 'Terry]

# Change a Range of Item Values

fruits = ["apple", "banana", "cherry", "orange", "mango"]

fruits[1:3] = ["kiwi", "watermelon"]

print(fruits)                   #   ['apple', 'kiwi', 'watermelon', 'orange', 'mango']


fruits = ["apple", "banana", "cherry", "orange", "mango"]

fruits[1:2] = ["kiwi", "watermelon"]

print(fruits)                   #   ['apple', 'kiwi', 'watermelon', 'cherry', 'orange', 'mango']


fruits = ["apple", "banana", "cherry", "orange", "mango"]

fruits[1:3] = ["watermelon"]

print(fruits)                   #   ['apple', 'watermelon', 'orange', 'mango']