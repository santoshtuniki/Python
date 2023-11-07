fruits = ("apple", "banana", "mango")

print(type(fruits))                                 #   <class 'tuple'>

myTuple = tuple(("apple", "banana", "mango"))

print(type(myTuple))                                #   <class 'tuple'>


# To make changes to tuple

newList = list(myTuple)

newList.append("oranges")

print(newList)                                      #   ['apple', 'banana', 'mango', 'oranges']

newTuple = tuple(newList)

print(newTuple)                                     #   ('apple', 'banana', 'mango', 'oranges')


# Unpacking
myFruits = ('apple', 'banana', 'mango', 'oranges')  #   packing

(one, two, *hey) = myFruits

print(one)                                          #   apple

print(two)                                          #   banana

print(hey)                                          #   ['mango', 'oranges']

(one, *two, hey) = myFruits

print(one)                                          #   apple

print(two)                                          #   ['banana', 'mango']

print(hey)                                          #   'oranges'


# Methods

num = (1, 2, 2, 4, 5, 5, 5, 6)

print(num)                                          #   (1, 2, 2, 4, 5, 5, 5, 6)

print(num.count(5))                                 #   3

print(num.index(2))                                 #   1

