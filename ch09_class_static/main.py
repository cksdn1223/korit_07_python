# 클래스 변수 예시
# class Korean:
#     country = '한국'
#     # 클래스 변수
#     # 인스턴스 변수의 경우는 생성자 내부에 있었습니다(__init__내부).
#     # 클래스 변수는 이상처럼 클래스 내부에 선언하고 초기화하면 됩니다.
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#         # 인스턴스 변수들
#
# # 객체 생성
# man1 = Korean('김일', 21, '서울특별시 종로구')
# print(man1.name)        # 인스턴스 변수 참조
# print(man1.age)
# print(man1.address)
#
# print(man1.country)     # 결과값 : 한국
# print(Korean.country)   # 결과값 : 한국
'''
객체명.클래스변수 를 통해서 클래스변수에 접근이 가능하긴 하지만, 클래스 내부의 코드를 들여다보기 전까지는 country라는 변수가 인스턴스 변수인지 클래스 변수인지 알 방법이 없다는 문제가 있습니다.

이상을 이유로 클래스 변수를 확인하고자 할때는 객체명.클래스명 보다는 클래스명.클래스변수명 을 통해서 참조하는 것이 권장됩니다.
'''

# class Korean2:
#     country = '대한민국' # 클래스 변수 선언 및 초기화
#     # 클래스 메서드 정의 방법
#     @classmethod                        # @classmethod 데코레이터를 달면 클래스 메서드로 인지함.
#     def trip(cls, travelling_site):     # 그 결과 첫 번째 매개변수가 self가 아니라 cls
#         if cls.country == travelling_site:
#             print('국내여행')
#         else:
#             print('해외여행')
#
# Korean2.trip('대한민국')
# Korean2.trip('미국')
# man2 = Korean2()
# man2.trip('일본')
# 클래스 변수와 마찬가지로 객체명.클래스메서드명() 으로 호출이 가능하기는 하지만 마찬가지로 이게 인스턴스 메서드인지 알기 어렵기 때문에 클래스 메서드를 호출할 때는 클래스명.클래스메서드명() 으로 하는것이 권장됩니다.
# class Korean3:
#     country = '한국'
#
#     @staticmethod
#     def slogan():
#         print('Imagine Your Korea!')
#
#     @staticmethod
#     def slogan2(str_example):
#         """매개변수가 있는 녀석"""
#         print('Imagine Your Korea!' + str_example)
#
# Korean3.slogan()
# Korean3.slogan2(' 근데 너무 덥다')
'''
기본 예제
가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 정의할겁니다.
'''
# 클래스 정의
# class Bag:
#     # 클래스 변수의 선언 및 초기화
#     count = 0
#
#     def __init__(self): # 생성자 호출 및 인스턴스 변수들 정의할용도, 생성자도 인스턴스 변수네 self 잇으니가
#         Bag.count += 1  # 생성자가 호출될 때마다 클래스변수인 count가 1씩 증가 cls.count 가 아니라 클래스며이.count라는 것에 주목
#         print('가방 객체 생성')
#
#     # 클래스 메서드 정의
#     @classmethod
#     def sell(cls):
#         print('가방이 팔렸습니다.')
#         cls.count -= 1
#         # 얘는 클래스 메서드가 클래스 변수에 접근한 것이기 때문에 Bag.count가 아니라 cls.count로 작성되었습니다.
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
# print(f'현재 가방 재고 : {Bag.count}')
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
#
# # 객체 생성
# bag1 = Bag()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
# bag2 = Bag()
# bag3 = Bag()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
# bag1.sell()     # 실제로 bag1 객체가 사라진건 아니다. 단순 count만 -1 했기 때문에
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
# Bag.sell()
# print(f'현재 가방 재고 : {Bag.remain_bag()}')

'''
응용 예제
1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스르 작성하시오.
지시 사항
1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오.
man = Person('김일')
woman = Person('김이')
2. man 과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
김일이(가) 태어났습니다.
김이이(가) 태어났습니다.
3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f'전체 인구수 : {Person.get_population()}')
4. 다음과 같은 명령어로 man 인스턴스를 삭제하시오.
del man
5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 김일
'''
# class Person:
#     population = 0
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#         print(f'{self.name}이(가) 태어났습니다.')
#
#     def __del__(self):
#         Person.population -= 1
#         if self.name == '김일':
#             print(f'RIP {self.name}')
#
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
# man = Person('김일')
# woman = Person('김이')
#
# print(f'전체 인구수 : {Person.get_population()}')
# del man
# print(f'전체 인구수 : {Person.get_population()}')
'''
다음 지시 사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 작성하시오.
지시 사항
1. Shop 클래스는 다음과 같은 변수를 가지고 있다.
total : 가게 전체 매출액
menu_list : {메뉴명:가격} 으로 이루어진 딕셔너리 요소를 가진 list
menu_list = [{'떡볶이':3000},{'순대':4000},{'튀김':500},{'김밥':2000}]
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
Shop.sales('떡볶이', 1)    # 떡볶이을(를) 1 개 판매
Shop.sales('김밥', 2)     # 김밥을(를) 2 개 판매
Shop.sales('튀김', 5)    # 튀김을(를) 5 개 판매
3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인
print(f'매출 : {Shop.get_total()}원')
'''
class Shop:
    total = 0
    menu_list = [{'떡볶이':3000},{'순대':4000},{'튀김':500},{'김밥':2000}]
    menu_dict = {'떡볶이': 3000, '순대':4000, '튀김':500,'김밥':2000,}
    @classmethod
    def sales(cls,menu_name, amount):
        # for menu in cls.menu_list:
        #     if menu_name in menu:
        #         cls.total += menu[menu_name] * amount
        #         print(f'{menu_name}을(를) {amount} 개 판매')
        if menu_name in cls.menu_dict:
            cls.total += cls.menu_dict[menu_name] * amount
            print(f'{menu_name}을(를) {amount} 개 판매')
    @classmethod
    def get_total(cls):
        return cls.total

Shop.sales('떡볶이', 1)
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)

print(f'매출 : {Shop.get_total()}')





















