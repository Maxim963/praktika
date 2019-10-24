from __future__ import print_function
from pprint import pprint
from threading import Thread
g = 'рус'

cou = []

with open('russian.txt', encoding='windows-1251') as re:
    for i in re:
        if g in i[len(g)*(-1)-1:]:
            Thread(cou.append(g))
            Thread(print(i, end=': '))
pprint(len(cou))
