users = ['Sai', 'Kumar', 'John']

data = ['John', 28, True]

emptyList = []

print(type(users))              #   <class 'list'>

# Constructor

myList = list(("apple", "banana", "cherry"))

print(myList)                   #   ['apple', 'banana', 'cherry']

print(type(myList))             #   <class 'list'>


# Check if the value is in list

print("Sai" in users)           #   True

print("Sai" in data)            #   False


# Get value based on index

print(users[0])                 #   Sai

print(users[-1])                #   John


# Find index based on value

print(users.index('Kumar'))     #   1
