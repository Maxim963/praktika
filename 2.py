a=11
b=24
unit=int(input('Сколько сейчас часов?'))
if unit<=a:
    print('AM')
elif unit <=b:
    print('PM')
else:
    print('Not correct!')
