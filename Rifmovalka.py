from __future__ import print_function
from pprint import pprint
from threading import Thread
while True:
    g = input('Введите слово для поиска рифмы: ')

    cou = []

    with open('russian.txt', encoding='windows-1251') as re:
        for i in re:
            if g in i[len(g)*(-1)-1:] and str(g) != str(i):
                Thread(cou.append(g))
                Thread(print(i.title(), end= '- '))
    print('Найдено: %i рифм %s'%(len(cou), '\n'))
