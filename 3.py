class cats():
    def __init__(self, name, pol, age, poroda):
        self.name = name
        self.pol = pol
        self.age = age
        self.poroda = poroda
        self.ves = 6
    def sleep(self):
        print(self.name + ' сладко спит')
    def vesy(self, kg):
        if int(kg) > 7:
            self.ves = kg
            print(self.name + ' сильно поправился')
        elif int(kg) < 4:
            self.ves = kg
            print(self.name +' сильно похудел')
        elif float(kg) in range(4, 8):
            print('У ' + self.name + ' вес в норме')

my = cats('Dominik', 'kot', 2, 'scottishfold')
saf = cats('Simba', 'kot', 11, 'nevsk-maskarad')
print(saf.age)
my.sleep()
domka=my.vesy(3)
print(my.vesy(7))
print(saf.vesy(8))