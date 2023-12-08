x = 6

try:
    print(x/0)
except NameError:
    print("Variable x is not defined")
except Exception as error:
    print(error)
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

'''
division by zero
The 'try except' is finished
'''
