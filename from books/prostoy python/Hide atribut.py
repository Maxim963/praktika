class Duck:
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('Inside the getter')
        return self.__name
    @name.setter
    def name(self, input):
        print('Inside setter')
        self.__name = input


fowl = Duck('Maxim')
fowl.name = 'Luna'
print(fowl._Duck__name)

# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#     @property
#     def diametr(self):
#         return 2 * self.radius
#
# c = Circle(5)
# c.radius = 21
# print(c.diametr)
