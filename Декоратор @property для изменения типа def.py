class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def diagonal(self):
        from math import sqrt

        return sqrt(self.width ** 2 + self.height ** 2)


rectangle = Rectangle(5.6, 7.3)

'''Использовать c декоратором
@property'''
print(rectangle.area)
print(rectangle.diagonal)

'''Использовать без декоратора 
@property'''
#print(rectangle.area())
#print(rectangle.diagonal())