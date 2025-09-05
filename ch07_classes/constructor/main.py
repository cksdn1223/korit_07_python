'''
일종의 setter 를 활용하여 속성에 속성값을 넣어줬습니다.
그럼 Java 에서 수업한 것처럼 속성값이 대입되지 않은 객체를 생성한 다음에 속성값을 집어넣어주는 과정을 거쳐야합니다.

근데 매개변수 생성자를 정의해버리면 객체 생성시에 속성값을 넣을 수 있겠네요.
'''
# 클래스 정의
# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def show_info(self):
#         print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')
#
# # 객체 생성 (빈객체 -> 속성값 대입 -> 속성값 출력)
# satang = Candy()
# satang.set_info('구형', '갈색')
# satang.show_info()

'''
비효율적으로 느껴짐 -> 생성자 도입

Java / Js 에선 생성자 명은 클래스명과 동일하거나 constructor인데 python에선 다릅니다.
'''
# class Candy2:
#     # 생성자 정의
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def show_info(self):
#         print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')
#
# satang2 = Candy2('정육면체', '흰색')
# satang2.show_info()
#
# class Sample:
#     def __init__(self):
#         print('인스턴스가 생성되었습니다.')
#
#     # 소멸자 정의
#     def __del__(self):
#         print('인스턴스가 소멸되었습니다.')
#
# # 객체 생성
# sample = Sample()
# print()
# # 객체 소멸자 호출 방법
# del sample      # del 객체명
# print('객체 지운 후의 코드라인입니다.')
'''
생성자를 이용해 용량을 가진 usb 인스턴스를 만드세요
1. 클래스 USB
2. 생성자 정의 매개변수 capacity
3. get_info() 메서드

main
usb = USB(64)
usb.get_info()

USB 객체가 생성되었습니다.
64GB USB
'''
# class USB:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         print('USB 객체가 생성되었습니다.')
#
#     def get_info(self):
#         print(f'{self.capacity}GB USB')
#
# usb = USB(64)
# usb.get_info()

'''
이름을 저장하는 Pers9on 클래스
man 과 woman 인스턴스 생성
man = Person('james')
woman = Person('emily')

man과 woman 인스턴스 생성되면 다음고 같은 메세지 출력
james is born
emily is born.

man 인스턴스 삭제
del man

james is dead.
'''
# class  Person:
#     def __init__(self, name):
#         self.name = name
#         print(f'{self.name} is born.')
#
#     def __del__(self):
#         if self.name == 'james':
#             print(f'{self.name} is dead.')
#
# man = Person('james')
# woman = Person('emily')
#
# del man

'''
python판 getter / setter

setter -> 매개변수 o / 리턴 x
getter -> 매개변수 x / 리턴 o
'''
# class Student:
#     # setter 예시
#     def set_name(self, name):
#         self.name = name
#     # getter 예시
#     def get_name(self):
#         return self.name

'''
지시 사항
age / address / score 속성을 setter를 통해서 추가
속성에 맞는 getter 도 추가

student1 객체 생성
김일, 20, 4.5 를 각각 이름/나이/점수 에 대입하시오.

getter만을 활용하여,
김일 학생의 나이는 20 살로 파이썬 과목의 점수는 4.5점 입니다. 출력
'''
class Student:
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_address(self, address):
        self.address = address
    def set_score(self, score):
        self.score = score

    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    def get_address(self):
        return self.address
    def get_age(self):
        return self.age

student1 = Student()
student1.set_age(20)
student1.set_name('김일')
student1.set_score(4.5)
print(f'{student1.get_name()} 학생의 나이는 {student1.get_age()} 살로 파이썬 과목의 점수는 {student1.get_score()}점 입니다.')







