users = ['Sai', 'Kumar', 'John', 'Dave', 'Jason', 'Bob']

users.sort()

print(users)                            #   ['Bob', 'Dave', 'Jason', 'John', 'Kumar', 'Sai']


users = ['Sai', 'Kumar', 'john', 'dave', 'Jason', 'Bob']

users.sort()

print(users)                            #   ['Bob', 'Jason', 'Kumar', 'Sai', 'dave', 'john']

users.sort(key=str.lower)

print(users)                            #   ['Bob', 'dave', 'Jason', 'john', 'Kumar', 'Sai']


num = [100, 10, 2, 66, 1, 73, 60]

num.sort()

print(num)                              #   [1, 2, 10, 60, 66, 73, 100]     ASCENDING ORDER

num = [100, 10, 2, 66, 1, 73, 60]

num.sort(reverse=True)

print(num)                              #   [100, 73, 66, 60, 10, 2, 1]     DESCENDING ORDER


num = [100, 10, 2, 66, 1, 73, 60]

num.reverse()

print(num)                              #   [60, 73, 1, 66, 2, 10, 100]     REVERSE


# SORT WITHOUR MUTATING ORIGINAL LIST

num = [100, 10, 2, 66, 1, 73, 60]

print(sorted(num))                      #   [1, 2, 10, 60, 66, 73, 100]

print(sorted(num, reverse=True))        #   [100, 73, 66, 60, 10, 2, 1]

print(num)                              #   [100, 10, 2, 66, 1, 73, 60]


# Copy the list

numCopy = num.copy()

numbers = list(num)

myCopy = num[:]

print(numCopy)                          #   [100, 10, 2, 66, 1, 73, 60]

print(numbers)                          #   [100, 10, 2, 66, 1, 73, 60]

print(myCopy)                           #   [100, 10, 2, 66, 1, 73, 60]