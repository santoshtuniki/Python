x = 7

try:
    if not type(x) is str:
        raise TypeError('Only strings are allowed')
except NameError:
    print("Variable x is not defined")
except Exception as error:
    print(error)
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

'''
Only strings are allowed
The 'try except' is finished
'''
