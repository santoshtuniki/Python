class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'am a {self.make} {self.model}.")


car = Vehicle('Tesla', 'Model 3')

car.moves()
car.get_make_model()
'''
Moves along...
I'am a Tesla Model 3.
'''


class Aeroplane(Vehicle):
    def moves(self):
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')


class Bus(Vehicle):
    pass


cessna = Aeroplane('Cessna', 'Skyhawk')

mack = Truck('Mack', 'Pinnacle')

tsrtc = Bus('Yamaha', 'GC1000')

cessna.moves()
cessna.get_make_model()
'''
Flies along...
I'am a Cessna Skyhawk.
'''

mack.moves()
mack.get_make_model()
'''
Rumbles along...
I'am a Mack Pinnacle.
'''

tsrtc.moves()
tsrtc.get_make_model()
'''
Moves along...
I'am a Yamaha GC1000.
'''


class Ship(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Sails along...')

titanic = Ship('Titanic', 'Atlantia', 'N-5738')

titanic.get_make_model()
titanic.moves()
'''
I'am a Titanic Atlantia.
Sails along...
'''

print('\n')

for v in (car, cessna, mack, tsrtc, titanic):
    v.get_make_model()
    v.moves()
    print('\n')

'''
I'am a Tesla Model 3.
Moves along...


I'am a Cessna Skyhawk.
Flies along...


I'am a Mack Pinnacle.
Rumbles along...


I'am a Yamaha GC1000.
Moves along...


I'am a Titanic Atlantia.
Sails along...
'''