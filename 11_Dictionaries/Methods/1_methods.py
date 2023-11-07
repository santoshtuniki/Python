band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

# Access items

print(band['vocals'])                               #   Plant

print(band.get('guitar'))                           #   Page


# List all keys

print(band.keys())                                  #   dict_keys(['vocals', 'guitar'])


# List all values

print(band.values())                                #   dict_values(['Plant', 'Page'])


# List all key/value pairs as tuples

print(band.items())                                 #   dict_items([('vocals', 'Plant'), ('guitar', 'Page')])


# Verify if a key exists

print("guitar" in band)                             #   True

print("flute" in band)                              #   False
