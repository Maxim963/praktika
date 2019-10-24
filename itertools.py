import itertools as zz
for item in zz.chain([1, 2], ['a', 'b']): #выводит каждый аргумент с новой строки
    print(item)
#for it in zz.cycle([1, 2, 3]): # бесконечный итератор проходит по кругу по всем аргументам
    #print(it)
#for kalk in zz.accumulate([1,3,5,7,9]): #Выводит поочередно каждый аргумент прибавляя к нему следующий
    #print(kalk)
def ned(a, b):
    return a + b
for pods in zz.accumulate([8,8,8,8,8], ned): #Выводит поочередно каждый аргумент присваимая ему функцию def
    print(pods)