from random import randint
def found_x(do=1000):
    x = randint(1, do)
    y = 0
    count = 1
    last = []
    start = ('угадайте число до %s: \n '%str(do))
    while y != x:
        y = int(input(start))
        if y < x:
            count += 1
            last.append(y)
            print(' Больше чем {}{}'.format(y, '\n'))
        elif y > x:
            count += 1
            last.append(y)
            print('Меньше чем {}{}'.format(y, '\n'))
        else:
            if count in range(5,21):
                rez = 'Угадано это {} за {} попыток{}'.format(int(x), int(count), '\n')
                print('{:<30}'.format(rez))
                print('Вводимые цифры {:-^50}{}'.format(str(last), '\n'))
                # print('Угадано это {} за {} попыток{}'.format(int(x), int(count), '\n, \n'))
            elif count in range(5):
                rez = 'Угадано это {} за {} попытки{}'.format(int(x), int(count), '\n')
                print(rez)
                print('Вводимые цифры {:-^50}{}'.format(str(last), '\n'))
                # print('Угадано это {} за {} попытки{}'.format(int(x), int(count), '\n, \n'))
            break

while True:
    found_x(int(input('До какого числа угадываем? ')))
