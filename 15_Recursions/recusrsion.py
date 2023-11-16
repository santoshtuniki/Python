def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


add_one(0)
print('')

newTotal = add_one(0)
print(newTotal)
print('')

def add_two(num):

    if (num >= 9):
        return num + 2

    total = num + 2
    print(total)

    return add_two(total)


newTotal = add_two(0)
print(newTotal)
print('')


def add_three(num):

    if (num >= 9):
        return num + 3

    total = num + 3
    print(total)

    add_three(total)


newTotal = add_three(0)
print(newTotal)
print('')
