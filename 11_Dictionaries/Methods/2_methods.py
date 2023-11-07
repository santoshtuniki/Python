band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band2 = dict(vocals = 'Plant', guitar = 'Page')

# Change value/Add value

band['vocals'] = 'Hello'

print(band)                                         #   {'vocals': 'Hello', 'guitar': 'Page'}

band.update({'guitar': 'Welcome'})

print(band)                                         #   {'vocals': 'Hello', 'guitar': 'Welcome'}


# Remove items

print(band.pop('vocals'))                           #   Hello

band['drum'] = 'Bonham'

print(band.popitem())                               #   ('drum', 'Bonham')

band['drum'] = 'Bonham'

print(band)                                         #   {'guitar': 'Welcome', 'drum': 'Bonham'}

del band['drum']

print(band)                                         #   {'guitar': 'Welcome'}

band2.clear()

print(band2)                                        #   {}

# del band2

# print(band2)                                        #   NameError: name 'band2' is not defined.