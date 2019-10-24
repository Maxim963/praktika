
english = 'monday', 'tuesday', 'wednesday'
russian = 'Понедельник', 'Вторник', 'Среда'
engrus= zip(english, russian)
print(dict(engrus),'\n')

num_list = [chet for chet in range(1,10000) if chet % 81 == 0]
print (num_list[80])

