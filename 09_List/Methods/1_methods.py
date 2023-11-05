users = ['Sai', 'Kumar', 'John']

data = ['John', 28, True]

# Get a range of elements

print(users[0:2])               #   ['Sai', 'Kumar']

print(users[1:])                #   ['Kumar', 'John']

print(users[:2])                #   ['Kumar', 'John']

print(users[-3:-1])             #   ['Sai', 'Kumar']

# Length of a list

print(len(data))                #   3


# Add elements to the list

users.append('Dave')

print(users)                    #   ['Sai', 'Kumar', 'John', 'Dave']

# Combine lists

users += ['Jason']              #   Make sure the added item is also a "list" & not a "string"

print(users)                    #   ['Sai', 'Kumar', 'John', 'Dave', 'Jason']


users.extend(['Robert', 'Stuart'])

print(users)                    #   ['Sai', 'Kumar', 'John', 'Dave', 'Jason', 'Robert', 'Stuart']


# users.extend(data)

# print(users)                    #   ['Sai', 'Kumar', 'John', 'Dave', 'Jason', 'Robert', 'Stuart', 'John', 28, True]


users.insert(0, 'Bob')

print(users)                    #   ['Bob', 'Sai', 'Kumar', 'John', 'Dave', 'Jason', 'Robert', 'Stuart']


users[2:2] = ['Eddie', 'Alex']

print(users)                    #   ['Bob', 'Sai', 'Eddie', 'Alex', 'Kumar', 'John', 'Dave', 'Jason', 'Robert', 'Stuart']