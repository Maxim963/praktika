class person:
    country = ' Russia'
    def __init__(self, prof, age, city, high): #перегружает конструктор класса
        self.prof=prof
        self.age=age                           #Сам конструктор
        self.city=city
        self.high=high


    def __repr__(self): #Что из конструктора выводить при сортировке
        return '({},{},{},{},{})'.format(self.prof, self.high, self.age, self.city, person.country)
        #return repr(self.prof) #Берется из конструктора

Maxim = person('Мальцев', 34, 'Химки', 184)
Stanislav = person('Байраковский', 33, 'Чертаново', 178)   #Присваеваем переменным данные из класса с конструктора
Sergey = person('Москаленко', 45, 'Одинцово', 178)
Andrew = person('Зарубин', 34, 'Электросталь', 185)

vse = [Maxim, Stanislav, Sergey, Andrew]

a_age = sorted(vse, key = lambda person: person.age) #Выбираем по какому параметру конструктора сортировать.
a_high = sorted(vse, key = lambda person: person.high) #Выбираем по какому параметру конструктора сортировать.
a_prof = sorted(vse, key = lambda person: person.prof) #Выбираем по какому параметру конструктора сортировать.
a_city = sorted(vse, key=lambda person: person.city) #Выбираем по какому параметру конструктора сортировать.

print('Это отсортировано по возрасту:', '\n', a_age, '\n')
print('Это отсортировано по росту:', '\n', a_high, '\n')
print('Это отсортировано по фамилии:', '\n', a_prof, '\n')
print('Это отсортировано по городу:', '\n', a_city, '\n')

#print(vse)


