from collections import namedtuple

Utka = namedtuple('Utka', 'cvet razmer ') # именованный кортеж с двумя переменными
# заменяет класс с именем Utka

duck = Utka('wide orange', razmer='long')

my = Utka('red', 340)
print(my.cvet, str(my.razmer))