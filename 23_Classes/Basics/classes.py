class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f'{self.make} ({self.model}).'

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'am a {self.make} {self.model}.")


car = Vehicle('Tesla', 'Model 3')

print(car.make)
print(car.model)
'''
Tesla
Model 3
'''

car.moves()
car.get_make_model()
'''
Moves along...
I'am a Tesla Model 3.
'''

car2 = Vehicle('Cadillac', 'Escalade')

print(car2)
'''
Cadillac (Escalade).
'''

car2.moves()
car2.get_make_model()
'''
Moves along...
I'am a Cadillac Escalade.
'''

del car2.make

# print(car2)
'''
AttributeError: 'Vehicle' object has no attribute 'make'
'''

del car2

# print(car2)
'''
NameError: name 'car2' is not defined.
'''