try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")

'''
Variable x is not defined
'''

print('\n')


x = 5

try:
    print(x)
except:
    print("An exception occurred")
else:
    print("Nothing went wrong")

'''
5
Nothing went wrong
'''

print('\n')


x = 8

try:
    print(x)
except:
    print("An exception occurred")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

'''
8
Nothing went wrong
The 'try except' is finished
'''
