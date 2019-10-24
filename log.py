class Max():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def names(self):
        print('ilove you')
        return self.__name
    @names.setter
    def names(self, input_name):
        print('Fuck you')
        self.__name=input_name
        pass
zxc = Max('Kop')
zxc.names = 'Seas'
print(zxc.names)