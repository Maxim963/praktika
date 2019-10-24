print ("Это калькулятор для Анзора")
start = input("выбери действие: (-, +, *, /)")
a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))
if start == "+":
    c = a + b
    print('Результат: ' + str(с))
elif start == "-":
    c = a - b
    print('Результат: ' + str(с))
elif start == "*":
    c = a * b
    print('Результат: ' + str(с))
elif start == "/":
    c=a/b
    print('Результат: ' + str(с))
else:
    print("НЕ ПРАВИЛЬНОЕ ДЕЙСТВИЕ!")

