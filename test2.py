class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    def weighted_grade(self):
        return 'CBA'.index(self.grade) / self.age
pcrucard =[Student('Max', 'A', 34),
           Student('Andrew', 'C', 33),
           Student('Sergey', 'B', 45)]
print(sorted(pcrucard, key=lambda ent: ent.age))

