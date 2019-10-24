import datetime
from pycbrf.toolbox import ExchangeRates
from pprint import pprint
rates = ExchangeRates(datetime.date.today())
rates.date_requested  # выбранная Дата- 00:00:00
rates.date_received  # выбранная Дата- 00:00:00
# 26-е был выходной, а курс на выходные установлен 25-го
rates.dates_match  # False

# Список всех курсов валют на день доступ в rates.rates.

# Поддерживаются разные идентификаторы валют:
rates['USD'].name  # Доллар США
rates['R01235'].name  # Доллар США
rates['840'].name  # Доллар США
dol= float(rates['USD'].value)
evr= float(rates['EUR'].value)

while True:
    print('Сейчас: ',(datetime.datetime.today().strftime("%H:%M:%S")))
    print('\n','Стас выбери валютную пару:', '\n', '1 - ($-Rub)', '\n', '2 - (EUR-Rub)', '\n', '3 - (Rub-$)', '\n', '4 - (Rub-EUR)')
    print('0 - выход')
    print('5 - показать курсы всех существующих валют')
    try:
        pr = int(input("Стас выбирает: "))
        if pr > 5:
            raise ValueError
             
        elif pr == str(pr):
            raise ValueError
    except (TypeError, ValueError, NameError):
        pr = int(input('Последняя попытка ))):'))
        
    if pr == 1:
        try:
            print('Сколько долларов ты хочешь обменять:')
            kol = float(input())
            print('Стас ты получешь: ',(kol * dol), 'рублей по курсу ЦБ РФ', '\n')
        except (TypeError, ValueError):
            kol = 0
            
            print ('Стас пиши цифры!')
    elif pr == 2:
        try:
            print('Сколько евро ты хочешь обменять:')
            kol = float(input())
            print('Стас ты получешь: ',(kol * evr), 'рублей по курсу ЦБ РФ', '\n')
        except (TypeError, ValueError):
            kol = 0
            
            print ('Стас пиши цифры!')
    elif pr==3:
        try:
            print('Стас, сколько рублей ты меняешь:')
            kol = float(input())
            print('Стас ты получешь: ',(kol / dol), 'долларов по курсу ЦБ РФ', '\n')
        except (TypeError, ValueError):
            kol = 0
            
            print ('Стас пиши реальные цифры!')
    elif pr==4:
        try:
            print('Стас, сколько рублей ты меняешь:')
            kol = float(input())
            print('Стас ты получешь: ',(kol / evr), 'евро по курсу ЦБ РФ', '\n')
        except (TypeError, ValueError):
            kol = 0
            
            print ('Стас пиши реальные цифры!')
    elif pr==5:
        print(rates.rates)
    elif pr==0:
        break
    else:
        print('Ошибка выбора валюты','\n')
