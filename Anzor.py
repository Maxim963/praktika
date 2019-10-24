while True:
    print('Это калькулятор для Анзора')
    user_input = input("Выбери действие (+ - * /) ")
    print("Напиши 'exit' для выхода")
    if user_input=="exit":
        break
    elif user_input=="+":
        num1=float(input("Введи первое число: "))
        num2=float(input("Введи второе число: "))
        result=str(num1 + num2)
        print("Анзор тебе: ",  result, "лет")
    elif user_input=="-":
        num1=float(input("Введи первое число: "))
        num2=float(input("Введи второе число: "))
        result=str(num1 - num2)
        print("Анзор тебе: ",  result, "лет")
    elif user_input=="*":
        num1=float(input("Введи первое число: "))
        num2=float(input("Введи второе число: "))
        result=str(num1 * num2)
        print("Анзор тебе: ",  result, "лет")
    elif user_input=="/":
        num1=float(input("Введи первое число: "))
        num2=float(input("Введи второе число: "))
        result=str(num1 / num2)
        print("Анзор тебе: ",  result, "лет")
    else:
        print("Анзор не тупи, повтори снова")
while False:
    print('Пошел на хуй!')
