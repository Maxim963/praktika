def add_arg(arg1, arg2):
    print(arg1 + arg2)

def run_any_with_arg(funkc, arg1, arg2): #Эта функция вызывает функцию add_arg и ее аргументы (arg1 arg2)
    funkc(arg1, arg2)
run_any_with_arg(add_arg, 14, 16)
