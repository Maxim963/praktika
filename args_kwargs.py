def apply(func: object, value: object):
    print(func(value))
# apply(print, (4 * 5))
# apply(id, 42)
# apply(type, 78)
# apply(len, 'Maxim')
# apply(type, apply)

def outer():
    def inter():
        print('Vnutri')
    print('Snaruji')
    return inter
i = outer()
apply(type, i)
i()

def my_f(**kwargs):
    for  s, v in kwargs.items():
        print(s, v, sep='-->', end='\n')
    if kwargs:
        print()
my_f(Max = 10, Maxim = 20, Ann = 30, Ser = 50, And = 90, Father = 70)


def my_f2(*args):
    for y in args:
        print(y, end=' | ')
    if args:
        print()

def my_f3 (*args, **kwargs):
    if args:
        for i in args:
            print(i, end=', ')
        print()
    if kwargs:
        for a, s in kwargs.items():
            print(a, s, sep='=', end=' ')
        print()

poi = ['Metallica', 'LP', 'LB', 'Prodigy', 'Nirvana', 'OffSpring']

my_f3(*poi)
my_f3('Koshka', 'Moshka', 'Vse', *poi, Max = 10, Maxim = 20, Ann = 30, Ser = 50, And = 90, Father = 70)

