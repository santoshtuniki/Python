# Passing multiple arguments
def multiple_args(*args):
    print(args)
    print(type(args))

multiple_args(5, 6, "Hi")

"""
(5, 6, 'Hi')
<class 'tuple'>
"""

# To use multiple arguments
def sum(*args):
    print(args[0] + args[1])

sum(5, 6, "Hi")                                 #   11

def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_named_items(first = "Santosh", last = "Tuniki")

"""
{'first': 'Santosh', 'last': 'Tuniki'}
<class 'dict'>
"""