class JustNotCoolError(Exception):
    pass

x = 3

try:
    raise JustNotCoolError("This just isn't cool man!")
except NameError:
    print("Variable x is not defined")
except Exception as error:
    print(error)
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

'''
This just isn't cool man!
The 'try except' is finished
'''
