odd = {key: key*key for key in range(1, 10)}
print(odd)

mn = {mno for mno in range(10) if mno % 2 ==0}
print(mn)
#got = list(range(10))

for i in ('got %s' % num for num in range(10)):
    print(i)

def good (x, y, z, c, v):
    return x, y, z, c, v
pr = list(good('Andrew', 'Stas', 'Max', 'Sergey', 'Misha'))

get_odd = [get for get in range(10) if get % 2 ==1]
print(get_odd[2])

dic = dict(zip(pr, mn ))
print(dic)


def test(func1):
    def new_func(*args, **kwargs):
        print('start')
        result = func1(*args, **kwargs)
        print('end')
        return result
    return new_func
@test
def greeting():
    print('Greetings')
greeting()