# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print(f'{self.name}이(가) {food}를 먹습니다.')
#
# class Student(Person):
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school
#     def study(self):
#         print(f'{self.name}은(는) {self.school}에서 공부를 합니다.')
#
#     def eat(self, food):
#         print(f'{self.school}에서', end=' ')
#         super().eat(food)
#
#
# potter = Student("해리포터", '호그와트')
# potter.eat("감자")
# potter.study()

# print(isinstance(potter, Person))   # 결과값 True
# print(isinstance(potter, Student))  # 결과값 True
""""""
'''
지시사항을 읽고 Hybrid 클래스 구현
1. 다음과 같은 슈퍼클래스 Car를 가지고 있는 Hybrid 클래수 구현
2.서브 클래스 Hybrid는 다음과 같은 특징을 지니고 있습니다.
    1) 최대 배터리 충전량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재합니다. 최대 충전량 초과 할수없고,
    0보다 작은 값으로 충전할 수 없다.
    3) 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드 있음
3. 다음과 같은 방식으로 전체 동작을 확인할 수 있음
car = Hybrid(oil=0, amount=0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

하이브리드 차량이 생산되었습니다.
기름을 50 주유 했습니다.
전기를 30 충전 했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30
'''
# class Car:
#     max_oil = 50
#     def __init__(self, oil):
#         self.oil = oil
#
#     def add_oil(self, oil):
#         if oil <= 0:
#             return
#         self.oil += oil
#         if self.oil > Car.max_oil:
#             self.oil = Car.max_oil
#         print(f'기름을 {self.oil} 주유 했습니다.')
#
#     def car_info(self):
#         print(f'현재 주유 상태 : {self.oil}')
#
# class Hybrid(Car):
#     max_amount = 30
#     def __init__(self, oil, amount):
#         super().__init__(oil)
#         self.amount = amount
#         print('하이브리드 차량이 생산되었습니다.')
#
#
#     def charge(self, amount):
#         if amount <= 0:
#             return
#         self.amount = Hybrid.max_amount if self.amount+amount > Hybrid.max_amount else self.amount+amount
#         print(f'전기를 {self.amount} 충전 했습니다.')
#
#     def hybrid_info(self):
#         super().car_info()
#         print(f'현재 충전 상태 : {self.amount}')
#
# car = Hybrid(oil=0, amount=0)
# car.add_oil(100)
# car.charge(50)
# car.hybrid_info()

'''
지시 사항
1. 슈퍼 클래스 Shape를 정의하시오.
    - 생성자에 name을 인스턴스 변수로 설정
    - draw() 메서드를 정의하여 self.name 을 출력 call1
2. Shape 클래스를 상속받는 서브클래스 Circle 정의
    - Circle은 radius(반지름) 속성을 추가로 가집니다.
    - 생성자 에서 radius도 추가할 것.
    - area() 메서드를 정의하여 원의 넓이를 계산하고 return call3
    ( 넓이 = 3.14 * radius * radius )
3. Shape 클래스를 상속 받는 서브 클래스 Rectangle을 정의
    - Rectangle은 width(너비) / height(높이) 속성을 추가로 가집니다. 
    - 생성자에서 width / height 를 초기화할 것
    - area() 메서드를 정의하여 사각형의 넓이를 계산하고 return call3
    (넓이 = width * height )
4. Circle과 Rectangle의 draw() 메서드를 오버라이딩하여 각각의 넓이를 출력

circle = Circle('원1',5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1',10,8)
rectangle.draw()
print(f'직사각형의 넓이 : {rectangle.area()}')

실행 예
반지름이 5인 원이 생성되었습니다.
이름이 원1인 원의 넓이는 ____ 입니다.
원의 넓이 : ____ 입니다.
너비가 10 높이가 8인 직사각형이 생성되었습니다.
이름이 직사각형1인 직사각형의 넓이는 ____ 입니다.
직사각형의 넓이 : ____ 입니다.
'''
# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def draw(self):
#         print(self.name)
#
# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius
#         print(f'반지름이 {self.radius}인 원이 생성되었습니다.')
#
#     def draw(self):
#         print(f'이름이 {self.name}인 원의 넓이는 {self.area()} 입니다.')
#     def area(self):
#         return 3.14 * (self.radius ** 2)
#
# class Rectangle(Shape):
#     def __init__(self, name, width, height):
#         super().__init__(name)
#         self.width = width
#         self.height = height
#         print(f'너비가 {self.width} 높이가 {self.height}인 직사각형이 생성되었습니다.')
#
#     def draw(self):
#         print(f'이름이 {self.name}인 직사각형의 넓이는 {self.area()} 입니다.')
#     def area(self):
#         return self.width * self.height
#
# circle = Circle('원1',5)
# circle.draw()
# print(f'원의 넓이 : {circle.area()}')
#
# rectangle = Rectangle('직사각형1',10,8)
# rectangle.draw()
# print(f'직사각형의 넓이 : {rectangle.area()}')























