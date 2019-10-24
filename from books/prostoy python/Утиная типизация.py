class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '. '

class QuestionQuote(Quote):
    def says(self):
        return self.words + '??? '

class ExamplQuote(Quote):
    def says(self):
        return self.words + '!!! '

class BabblingBrook(): # не к чему не привязанный класс
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

hunter = Quote('Elmer Fudd', 'I am hunting wabbits')
# print(hunter.who(), 'says:', hunter.says(), end='\n'*2)

hunter1 = QuestionQuote('Bugs banny', 'Whats up')
# print(hunter1.who(), 'says', hunter1.says(), end='\n'*2)

hunter2 = ExamplQuote('Max', 'Hello')
# print(hunter2.who(), 'say', hunter2.says()*2, end='\n \n')

def who_says(obj):
    print(obj.who(), 'says:', obj.says())
who_says(brook) # утинная типизация (переменная относящаяся к не зависимуму классу
# выполняется как будто она зависит от классов с привязкой