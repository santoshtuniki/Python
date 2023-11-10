# function definition
def hello():
    print("Hello World!")

# function call
hello()                                 #   Hello World!

# arguments & parameters
def sum1(num1, num2):
    print(num1 + num2)

sum1(1, 2)                              #   3
sum1(100, 8)                            #   108


# Return
def sum2(num1, num2):
    return num1 + num2

total = sum2(100, 2)
print(total)                            #   102


# Type checking arguments
def sum3(num1, num2):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum3(10, 2)
print(total)                            #   12

total = sum3("10", 2)
print(total)                            #   None

# total = sum()
# print(total)                            #   TypeError: sum() takes at least 1 positional argument (0 given)
