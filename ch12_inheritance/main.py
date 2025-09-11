class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name}이(가) {food}를 먹습니다.')

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def study(self):
        print(f'{self.name}은(는) {self.school}에서 공부를 합니다.')

    def eat(self, food):
        print(f'{self.school}에서', end=' ')
        super().eat(food)


potter = Student("해리포터", '호그와트')
potter.eat("감자")
potter.study()
