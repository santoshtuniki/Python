## STRING

# LITERAL ASSIGNMENT
first = 'Santosh'
last = 'Tuniki'

print(type(first))              # <class 'str'>
print(type(first) == str)       # True
print(isinstance(first, str))   # True
print('')

# CONSTRUCTOR FUNCTION
pizza = str('Pepperoni')

print(type(pizza))              # <class 'str'>
print(type(pizza) == str)       # True
print(isinstance(pizza, str))   # True
print('')

# CONCATANATION
fullname = first + " " + last
print(fullname)
print('')

fullname += '!'
print(fullname)
print('')

# CASTING NUMBER TO STRING
decade = str(2001)
print(decade)
print(type(decade))

# MULTI LINES	(''' 	''')	spaces are also counted
multiline = '''
Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability,
	with the use of significant indentation. 
'''
print(multiline)

# ESCAPING SPECIAL CHARACTERS
sentence = 'I\'am back at work!\tHow are you?\n\nI missed you \\bro.'
print(sentence, '\n')
