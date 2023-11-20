name = 'Kumar'
count = 1


def another():
    color = 'blue'
    # count += 1                  #   UnboundLocalError: local variable 'count' referenced before assignment
    print(count)

    def greeting(name):
        print(color)
        print(name)

    greeting('Daniel')


another()
'''
1
blue
Daniel
'''


def another2():
    color = 'blue'
    global count  # referenced to global variable
    count += 1
    print(count)

    def greeting(name):
        print(color)
        print(name)

    greeting('Daniel')


another2()
'''
2
blue
Daniel
'''


def another3():
    color = 'blue'
    global count  # referenced to global variable
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = 'green'
        print(color)
        print(name)

    greeting('Daniel')


another3()
''''
3
green
Daniel
'''
