from collections import namedtuple
class Thing():
    pass

example = Thing()

# print(example)
# print(Thing)

class Thing2():
    letters='abc'

print(Thing2.letters)

class Thing3():
    def __init__(self):
        self.letters = 'zxc'

some = Thing3()
print(some.letters)

class Element():
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number
    @property
    def name(self):
        return self._name
    @property
    def symbol(self):
        return self._symbol
    @property
    def number(self):
        return self._number
    # def __str__(self):
    #     return('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))

obclass = Element('Hydrogen', 'H', 1)

slovar = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# hydrogen = Element(slovar['name'], slovar['symbol'], slovar['number'])
hydrogen = Element(**slovar)
print(hydrogen.number)

class Bear:
    def eats(self):
        print('berries')

class Rabbit:
    def eats(self):
        print('clover')

class Octothorpe:
    def eats(self):
        print('campers')

b = Bear()
r = Rabbit()
o = Octothorpe()
r.eats()

class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smart = SmartPhone()
    def does(self):
        print('Мой лазер - {}, мой claw - {}, my smartphone - {}'.format(self.laser.does(), self.claw.does(), self.smart.does()))

rob = Robot()
rob.does()