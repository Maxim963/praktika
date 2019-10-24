while True:
    print('Выберите валюту приема для последующего обмена', '\n', '1 - $', '\n', '2 - Euro', '\n', '3 - Rub', '\n', '4 - KZtg')
    print('(Введите 0 для выхода)')
    try:
        pr = int(input("Анзор выбирает: "))
        if pr > 4:
            raise ValueError
        elif pr == str(pr):
            raise ValueError
    except (TypeError, ValueError, NameError):
        print ('Анзор такой валюты не существует!')
    if pr == 1:
        try:
            kurs = float(input("Введите курс выдаваемой валюты: "))
            razmer = float(input("В каком количестве получено:"))
        except (TypeError, ValueError):
            kurs = 0
            razmer = 0
            print ('Анзор пиши цифры!')
        print('Выдай клиенту:','\n',(kurs * razmer), 'тенге','\n')
    elif pr == 4:
        try:
            kurs = float(input("Введите курс выдаваемой валюты: "))
            razmer = float(input("Введите размер принятой валюты:"))
            if kurs == 0:
                print('делить на ноль нельзя!')
                raise ZeroDivisionError
        except (ZeroDivisionError, TypeError, ValueError):
            kurs = 1
            razmer = 0
            print ('Анзор пиши цифры!')
        print('Выдай клиенту:','\n', (razmer / kurs), '\n','\n')
    elif pr == 2:
        try:
            kurs = float(input("Введите курс выдаваемой валюты: "))
            razmer = float(input("Введите размер принятой валюты:"))
        except (TypeError, ValueError):
            kurs = 0
            razmer = 0
            print ('Анзор пиши цифры!')
        print('Выдай клиенту:','\n',(kurs * razmer), 'тенге', '\n','\n')
    elif pr == 3:
        try:
            kurs = float(input("Введите курс выдаваемой валюты: "))
            razmer = float(input("Введите размер принятой валюты:"))
        except (TypeError, ValueError):
            kurs = 0
            razmer = 0
            print ('Анзор пиши цифры!')
        print('Выдайте клиенту:','\n',(kurs * razmer), 'тенге', '\n','\n')
    elif pr == 0:
        break
    else:
        print('Ошибка выбора валюты','\n')
    print('Анзор ты молодец','\n')
    
    
