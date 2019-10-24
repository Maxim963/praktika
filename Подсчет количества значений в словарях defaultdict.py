from collections import defaultdict

food_counter = defaultdict(int) #присваивает ключам словаря food_counter значения по умолчанию - 0
for food in ['sup', 'sup', 'egg', 'sup', 'egg', 'borsh']: #Создает из переменной food ключи словаря
    food_counter[food] += 1  #Запускает счетчик количества ключей и исходя из количества создает значения(items) для ключей
for food, how_mutch in food_counter.items(): # Создает переменную how_mutch которая извлекает из словаря ключи и их значения
    print(food, how_mutch)
print(food_counter.keys())