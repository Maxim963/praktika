word = 'бутылки'
for num_beer in range(99, 0, -1):
    print(num_beer, word, 'пива на стене')
    print(num_beer, word, 'пива')
    print('Возьми еще одну')
    print('Раздавай дальше')
    if num_beer == 1:
        print('Иди в магазин за пивом')
    else:
        new_num = num_beer - 1
        if new_num == 1:
            word = 'бутылка'
        print(new_num, word, 'пива на стене.')
    print()