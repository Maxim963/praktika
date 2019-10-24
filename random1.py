from random import *
while True:
    x = randint(1, 1000000)
    y = 0
    count = 1
    while y != x:
        y = int(input('угадайте число до 1000000:  '))
        if y < x:
            count += 1
            print(' Больше...')
        elif y > x:
            count += 1
            print('Меньше...')
        else:
            print('\n', 'Угадано это',  x, '\n',  'за', + count,  'попыток', '\n', '\n')
            break


