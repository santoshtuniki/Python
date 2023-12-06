# VSCode reformatted lambda function into single line function

def squared(num): return num * num
# squared = lambda num: num * num


print(squared(2))  # 4


def addTwo(num): return num + 2
# addTwo = lambda num: num + 2


print(addTwo(5))  # 7


def sum(a, b): return a + b
# sum = lambda a, b: a + b


print(sum(2, 3))  # 5


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)

addTwenty = funcBuilder(20)

print(addTen(23))  # 33

print(addTwenty(23))  # 43
