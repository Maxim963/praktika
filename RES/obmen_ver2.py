from datetime import date
from pycbrf.toolbox import ExchangeRates
rates = ExchangeRates(date.today())
rates.date_requested  # выбранная Дата- 00:00:00
rates.date_received  # выбранная Дата- 00:00:00
# 26-е был выходной, а курс на выходные установлен 25-го
rates.dates_match  # False

# Список всех курсов валют на день доступ в rates.rates.

# Поддерживаются разные идентификаторы валют:
rates['USD'].name  # Доллар США
rates['R01235'].name  # Доллар США
rates['840'].name  # Доллар США
def rub_to_other (x, y):
    return x / y
def other_to_rub (x, y):
    return x * y
while True:
    print('Сейчас: ', (datetime.datetime.today().strftime("%H:%M:%S")), end='\n')
    print('Стас выбери валютную пару:', '1 - ($-Rub)', '2 - (EUR-Rub)', '3 - (Rub-$)', '4 - (Rub-EUR)', end='\n',)
    print('0 - выход')
    print('5 - показать курсы всех существующих валют', '\n')
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
            print('Ты получешь:',(other_to_rub(float(input('Сколько Долларов ты меняешь:')), (float(rates['USD'].value)))),'Рублей', '\n')
        except (TypeError, ValueError):
            print('Стас пиши цифры!')
    elif pr == 2:
        try:
            print('Ты получешь:',(other_to_rub(float(input('Сколько Евро ты меняешь:')), (float(rates['EUR'].value)))),'Рублей', '\n')
        except (TypeError, ValueError):
            print('Стас пиши цифры!')
    elif pr == 3:
        try:
            print('Ты получешь:',(rub_to_other(float(input('Сколько рублей ты меняешь:')), (float(rates['USD'].value)))), (rates['USD'].name), '\n')
        except (TypeError, ValueError):
            print('Стас пиши реальные цифры!')
    elif pr == 4:
        try:
            print('Ты получешь:',(rub_to_other(float(input('Сколько рублей ты меняешь:')), (float(rates['EUR'].value)))), (rates['EUR'].name), '\n')
        except (TypeError, ValueError):
            print('Стас пиши реальные цифры!')
    elif pr == 5:
        print(rates['USD'].value, rates['USD'].name,'\n')
        print(rates['EUR'].value, rates['EUR'].name,'\n')
        print(rates['AUD'].value, rates['AUD'].name,'\n')
        print(rates['AZN'].value, rates['AZN'].name,'\n')
        print(rates['GBP'].value, rates['GBP'].name,'\n')
        print(rates['AMD'].value, rates['AMD'].name, '\n')
        print(rates['BYN'].value, rates['BYN'].name, '\n')
        print(rates['BGN'].value, rates['BGN'].name, '\n')
        print(rates['BRL'].value, rates['BRL'].name, '\n')
        print(rates['HUF'].value, rates['HUF'].name, '\n')
        print(rates['HKD'].value, rates['HKD'].name, '\n')
        print(rates['DKK'].value, rates['DKK'].name, '\n')
        print(rates['INR'].value, rates['INR'].name, '\n')
        print(rates['KZT'].value, rates['KZT'].name, '\n')
        print(rates['CAD'].value, rates['CAD'].name, '\n')
        print(rates['KGS'].value, rates['KGS'].name, '\n')
        print(rates['CNY'].value, rates['CNY'].name, '\n')
        print(rates['MDL'].value, rates['MDL'].name, '\n')
        print(rates['NOK'].value, rates['NOK'].name, '\n')
        print(rates['PLN'].value, rates['PLN'].name, '\n')
        print(rates['RON'].value, rates['RON'].name, '\n')
        print(rates['XDR'].value, rates['XDR'].name, '\n')
        print(rates['SGD'].value, rates['SGD'].name, '\n')
        print(rates['TJS'].value, rates['TJS'].name, '\n')
        print(rates['TRY'].value, rates['TRY'].name, '\n')
        print(rates['TMT'].value, rates['TMT'].name, '\n')
        print(rates['UZS'].value, rates['UZS'].name, '\n')
        print(rates['UAH'].value, rates['UAH'].name, '\n')
        print(rates['CZK'].value, rates['CZK'].name, '\n')
        print(rates['SEK'].value, rates['SEK'].name, '\n')
        print(rates['CHF'].value, rates['CHF'].name, '\n')
        print(rates['ZAR'].value, rates['ZAR'].name, '\n')
        print(rates['KRW'].value, rates['KRW'].name, '\n')
        print(rates['JPY'].value, rates['JPY'].name, '\n')
    elif pr == 0:
        break
    else:
        print('Ошибка выбора валюты','\n')
