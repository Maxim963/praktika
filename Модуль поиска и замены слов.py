import re
hello = 'Привет Анзор. Это твоя машина Анзор'
iskat = 'Анзор' #Искомое слово
obmen = re.sub(iskat, 'Max', hello) #меняет искомое слово на новое в указанном тексте
print(obmen)
zamena = re.search(iskat, hello) #Ищет искомое слово в тексте
if zamena:
    print(zamena.group()) #Выводит искомое слово в случае его нахождения
    print(zamena.span())  #Выводит начальный и конечный индекс искомого слова в тексте
    print(zamena.start())  #Выводит начальный индекс искомого слова в тексте
    print(zamena.end())    #Выводит конечный индекс искомого слова в тексте