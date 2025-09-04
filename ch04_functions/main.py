# # 함수 정의
# def display_name(name):
#     print(f'당신의 이름은 {name}입니다.')
#
# # 함수 호출
# display_name('김일')
#
# def display_name_age(name, age):
#     print(f'당신의 이름은 {name}이고, 나이는 {age}살입니다.')
#
# display_name_age('김이', 30)
# display_name_age(age=23, name='김삼') # keyword argument

'''

'''
# eng_name = input('당신의 이름을 영어로 입력하세요 >>> ')
# print(eng_name)
# print(eng_name.upper())


# 매개변수 x / 리턴 x
# def call1():
#     print('[ x | x ]')
#
# # 매개변수 o / 리턴 x
# def call2(unknown_parameter):
#     print('[ o | x ]')
#     print(f'{unknown_parameter}')
# # 매개변수 x / 리턴 o
# def call3():
#     print('[ x | o ]')
#     return 1
# # 매개변수 o / 리턴 o
# def call4(unknown1, unknown2):
#     print('[ o | o ]')
#     return unknown1 + unknown2
#
# # 함수 호출
# call1()
# call2('오늘의 날씨는 시원')
# call2(123456)
# call3()
# print(call3())
# print(call4('안녕','하세요'))
# print(call4(unknown2=1234,unknown1=5678))

'''
700 원 짜리 음료수를 뽑을 수 잇는 자판ㄱ ㅣ 프로그램 구현
돈 넣으며 ㄴ 몇 잔 음료수 뽑을수잇는지 
잔돈 얼마인지 모드 ㄴ경우의 수 출력

vending_machine()
정수 money

vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
....
음료수 = 4개, 잔돈 = 200원
'''


# def vending_machine(money):
#     drink = 0
#     DRINK_PRICE = 700
#     # while drink*DRINK_PRICE <= money:
#     #     price = DRINK_PRICE * drink
#     #     print(f'음료수 = {drink}개, 잔돈 = {money - price}')
#     #     drink += 1
#
#     for drink in range(0,money//DRINK_PRICE+1):
#         price = DRINK_PRICE * drink
#         print(f'음료수 = {drink}개, 잔돈 = {money - price}')
#
# vending_machine(3000)


'''
예제 : 구구단ㅁ 출력하기
함수정의 :
함수 이름 : multiply
매개변수 : 정수 n
리턴값 : 없음

함수호출:
multiplay(dan)
실행 예
몇 단을 출력하시겠습니까 ? >>> 3
3 x 1 = 3
...
3 x 9 = 27
'''
# def multiplay(n):
#     for i in range(1,10):
#         print(f'{n} x {i} = {n * i}')
#
#     # i = 1
#     # while i < 10:
#     #     print(f'{n} x {i} = {n * i}')
#     #     i += 1
#
# dan = int(input('몇 단을 출력하시겠습니까 ? >>> '))
# multiplay(dan)



def multiply():
    dan = int(input('몇 단을 출력하시겠습니까 ? >>> '))
    for i in range(1,10):
        print(f'{dan} x {i} = {dan * i}')

    # i = 1
    # while i < 10:
    #     print(f'{n} x {i} = {n * i}')
    #     i += 1

multiply()








