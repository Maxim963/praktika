import datetime
from pycbrf.toolbox import ExchangeRates
from tkinter import *

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
#print(rates['USD'].value)
#print(rates['R01235'].name)
#print(rates['EUR'].name)
#print('Сейчас: ',(datetime.datetime.now()))

root = Tk()
e = Entry(root, width=200)
b = Button(root, text='Перевести')
l = Label(root, bg='white', fg='black', width=200)
def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)
 
b.bind('<Button-1>', strToSortlist)
 
e.pack()
b.pack()
l.pack()
root.mainloop()


