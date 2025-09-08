# class Student:
#     def __init__(self, name, student_id):
#         self._name = name
#         self._student_id = student_id
#         # 성적을 저장하기 윈한 빈 딕셔너리 과목명 key, 점수 value
#         self._grades = {}
#
#
#     # python 버전의 getter에 해당함
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value




# student1 = Student('김일', 2025001)
# # getter의 호출 예시 객체명.속성명 -> 객체명.메서드명() 이 아니라는것
# print(f'학생 이름 : {student1.name}')
#
# student1.name = '김영'
# print(f'변경된 학생 이름 : {student1.name}')
'''
_name 이라는 속성이 있는데 객체명.name 을 통해서 '김일' / '김영' 이라는 속성값이 출력됨
객체명._name = '김영'이 아니라 객체명.name = '김영' 으로 객체의 속성값을 직접 바꾼 것처럼 보임
_name / name은 서로 다른 개념인데 '_' 가 붙으면 파이썬 언어 내부적으로 동일한 속성으로 처리해줍니다.

객체명.속성명 뒤에 ()가 없음에도 불구하고 그냥 파이썬은 이걸 메서드처럼 처리해준다는 겁니다. 그래서 '객체명.속성명'이면 getter 로 처리해주고, '객체명.속성명 = 데이터' 면 setter 로 처리해준다고 보시면 됩니다.

이상의 코드라인이 성립하기 위해서 필수적인 부분이
'@property' 와 '@속성명.setter' 라는 '데코레이터(decorator)' 때문입니다.
'''


class Student:
    def __init__(self, name, age, score):
        self._name = name
        self._age = age
        self._score = score

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    def set_age(self, age):
        if 200 >= age >= 0:
            self._age = age
        else:
            print('불가능한 나이 입력')
    def set_score(self, score):
        if 4.5 >= score >= 0:
            self._score = score
        else:
            print('불가능한 점수 입력')

    @property
    def age(self):
        return self._age
    @property
    def score(self):
        return self._score

student1 = Student('김일', 25,3.0)

student1.set_age(50)
student1.set_score(4.0)

print(student1.name)
print(student1.age)
print(student1.score)
























