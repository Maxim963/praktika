def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greather = [i for i in array[1:] if i >= pivot]
        return quicksort(less)+[pivot]+quicksort(greather)
while True:
    try:
        test = [int(i) for i in input('Digits:').split()]
    except:
        test = str()
        print('ПИСАТЬ ЦИФРЫ ЧЕРЕЗ ПРОБЕЛ!!!')
    print(quicksort(test))



