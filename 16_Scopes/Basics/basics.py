name = 'Sai'  # Global Scope


def greeting():
    color = 'blue'  # Local Scope
    print(color)
    print(name)


greeting()
'''
blue
Sai
'''
# print(color)                    #   "color" is not defined


#   Local scopes are prioritized within the block of code/function
def greeting2(name):
    color = 'blue'  # Local Scope
    print(color)
    print(name)


greeting2('Santosh')
'''
blue
Santosh
'''


count = 1


def another():
    color = 'blue'
    count = 2
    print(count)

    def greeting(name):
        print(color)
        print(name)

    greeting('Daniel')


another()
'''
2
blue
Daniel
'''
