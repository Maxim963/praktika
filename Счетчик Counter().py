from collections import Counter
zavtrak = ['sup', 'sup', 'egg', 'sup', 'egg', 'borsh']
food_count = Counter(zavtrak)

obed = ['egg', 'borsh', 'meat', 'egg']
obed_counter = Counter(obed)

sortirovka = food_count.most_common(1) #most_common() выводит все элементы по убыванию
print(food_count)
print(obed_counter)
print(food_count + food_count)
print(food_count | obed_counter)