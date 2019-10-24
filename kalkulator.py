while True:
    print("Options:")
    print("Введите '+' для сложения")
    print("Введите '-' для вычитания")
    print("Введите '*' для умножения")
    print("Введите '/' для деления")
    user_input=input(": ")

    if user_input=="yyy":
        break
    elif user_input=="+":
        num1=float(input("Введите первое число: "))
        num2=float(input("Введите второе число: "))
        result=str(num1 + num2)
        print("Ваш ответ: " + result)
    elif user_input=="-":
        num1=float(input("Введите первое число: "))
        num2=float(input("Введите второе число: "))
        result=str(num1 - num2)
        print("Ваш ответ: " + result)
    elif user_input=="*":
        num1=float(input("Введите первое число: "))
        num2=float(input("Введите второе число: "))
        result=str(num1 * num2)
        print("Ваш ответ: " + result)
    elif user_input=="/":
        num1=float(input("Введите первое число: "))
        num2=float(input("Введите второе число: "))
        result=str(num1 / num2)
        print("Ваш ответ: " + result)
    else:
        print("Неправильный ввод, повторите снова")
