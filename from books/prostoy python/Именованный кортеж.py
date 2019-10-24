from collections import namedtuple

Utka = namedtuple('Utka', 'cvet razmer ') # именованный кортеж с двумя переменными
# заменяет класс с именем Utka

duck = Utka('wide orange', razmer='long')

my = Utka('red', 340)
print(my.cvet, duck.cvet)
print(*my)

dom = {'cvet': 'beton', 'razmer': 23}
dom2 = Utka(**dom) # делает именованный кортеж из словаря
print(dom2)

dom3 = dom2._replace(cvet='blue', razmer='big') #создаем измененный кортеж на основе прежнего
print(dom3)