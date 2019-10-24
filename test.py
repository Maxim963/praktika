def add_arg(arg1, arg2):
    print(arg1 + arg2)

#def pechat_args(posa1, posa2,*args):
  #  print ('Хочу это:', posa1)
   # print('Хочу это тоже:', posa2)
    #print('Всё остальное что я хочу:', args)

def run_any_with_arg(funkc, arg1, arg2): #Эта функция вызывает функцию add_arg и ее аргументы (arg1 arg2)
    funkc(arg1, arg2)
run_any_with_arg(add_arg, 14, 16)

def sum_args(*args):
    return sum(args)
def run_run_args(sasa, *args):
    return sasa(*args)
gg=run_run_args(sum_args, 1, 3, 5, 7, 9)
print(gg)
