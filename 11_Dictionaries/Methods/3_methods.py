band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band2 = band                        #   Creates a reference to band

print(band2 is band)                #   True

# Create a copy

band2 = band.copy()                 

print(band2)                        #   {'vocals': 'Plant', 'guitar': 'Page'}

print(band2 is band)                #   False

band3 = dict(band)

print(band3)                        #   {'vocals': 'Plant', 'guitar': 'Page'}

print(band3 is band)                #   False


# Nested dictionary

member1 = {
    'name': 'Plant',
    'instrument': 'Vocals'
}

member2 = {
    'name': 'Page',
    'instrument': 'Guitar'
}

band = {
    'member1': member1,
    'member2': member2
}

print(band)

# {'member1': {'name': 'Plant', 'instrument': 'Vocals'}, 'member2': {'name': 'Page', 'instrument': 'Guitar'}}

print(band['member1']['name'])      #   Plant