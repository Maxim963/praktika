class CountFromBy:
    def __init__(self, num: int=0, count: int=1) -> None:
        self.num = num
        self.count = count
    def increase(self) -> None:
        self.num += self.count
    def __repr__(self):
        return str(self.num)


a = CountFromBy()
a.increase()
a.increase()
#b = CountFromBy()
c = CountFromBy(100, 10)
c.increase()
c.increase()
j = CountFromBy(50, 5)
print(a)
print(c)
# print(type(j))
# print(id(j))
# print(hex(id(j)))
# for i in range(5):
#   print(f)
# print(f)
