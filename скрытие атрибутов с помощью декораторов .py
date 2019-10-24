class Max():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def names(self):
        print('ilove you')
        return self.hidden_name
    @names.setter
    def names(self, input_name):
        print('Fuck you')
        self.hidden_name=input_name
        pass
zxc = Max('Kop')
zxc.names = 'Seas'
print(zxc.names)