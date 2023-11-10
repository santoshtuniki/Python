# Default values for parameters
def sum4(num1, num2 = 3):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum4(10)
print(total)                            #   13


# Default values for parameters
def sum5(num1 = 0, num2 = 0):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum5()
print(total)                            #   0

total = sum5(10)
print(total)                            #   10


# Return a value instead of "None"
def sum6(num1 = 0, num2 = 0):
    if(type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2

total = sum6("5")
print(total)                            #   0
