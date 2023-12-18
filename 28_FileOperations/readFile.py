# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")

# print(f.read())
'''
Dave
Jane
Eddie
Jimmie
'''

# print(f.read(4))
'''
Dave
'''

# print(f.readline())
# print(f.readline())
'''
Dave

Jane

'''

for line in f:
    print(line)

f.close()
'''
Dave

Jane

Eddie

Jimmie
'''

try:
    f = open('names_list.txt')
    print(f.read())
except:
    print("The files you want to read doesn't exist")
finally:
    f.close()

'''
The files you want to read doesn't exist
'''

try:
    f = open('names.txt')
    print(f.read())
except:
    print("The files you want to read doesn't exist")
finally:
    f.close()
'''
Dave
Jane
Eddie
Jimmie
'''
