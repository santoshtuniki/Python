fruits = ["apple", "banana", "cherry"]

fruits.remove('banana')

print(fruits)                   #   ['apple', 'cherry']

fruits.pop()

print(fruits)                   #   ['apple']


fruits = ["apple", "banana", "cherry"]

del fruits[2]

print(fruits)                   #   ['apple', 'banana']

# del fruits

# print(fruits)                   #   NameError: name 'fruits' is not defined

fruits.clear()

print(fruits)                   #   []