while True:
    value=input("Введите пожалуйста число [q - выход]: ")
    if value == 'q':  #выход
        break
    number=int(value)
    if number % 2==0:   #это четные
        continue
        print(number, "в квадрате равно:", number*number)
    else:
        print("Это что такое?")

        
        
        
