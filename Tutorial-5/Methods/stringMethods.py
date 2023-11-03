first = 'Santosh'
last = 'Tuniki'

multiline = '''
Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability,
    with the use of significant philosophy indentation. 
'''

print(first)
print(first.lower())
print(first.upper())
print(first)

txt = "Welcome to my 2nd world"
print(txt.title(), '\n')

txt2 = "hello b2b2b2 and 3g3g3g"
print(txt2.title(), '\n')

print(multiline.title())
print(multiline.replace('philosophy', 'ideology'))
print(multiline.replace('philosophy', 'ideology', 1))
print(multiline)

print(len(multiline), '\n')			        # 172
multiline += "                     "
multiline = "                  " + multiline
print(len(multiline), '\n')			        # 211

print(len(multiline.strip()), '\n')		    # 169
print(len(multiline.lstrip()), '\n')		# 192
print(len(multiline.rstrip()), '\n')		# 188

title = 'menu'.upper()
print(title)
print(title.center(20, '='))                            # => Make  a string of len 20 with MENU as center and fill either sides with '='
print('Coffee'.ljust(16, '.') + '$1'.rjust(4))           # => Make  a string of len 16 with Cofee at beginning and '.' to it's left
print('Muffin'.ljust(16, '.') + '$2'.rjust(4))
print('Cheesecake'.ljust(16, '.') + '$4'.rjust(4))
'''
MENU
========MENU========
Cofee...........  $1
Muffin..........  $2
Cheesecake......  $4
'''

# STRING INDEX VALUES

print(first[1], '\n')           # a
print(first[-1], '\n')          # h
print(first[1:-1], '\n')        # antos
print(first[1:], '\n')          # antosh

# SOME STRING METHODS RETURNING BOOLEAN

print(first.startswith('T'), '\n')  # False
print(first.endswith('h'), '\n')    # True