'''
1. if 문
2. if - else 문
3. if - elif - else
    얘는 else if 가 아닌 elif 이다
'''
# age = 21
# if age > 20:
#     print('성인입니다.')
# elif 20 >= age > 13:
#     print('청소년입니다.')
# else:
#     print('미성년자입니다')
'''
if 조건식1:
    실행문1
elif 조건식2:
    실행문2
elif 조건식3:
    실행문3
else:
    실행문4
'''

# age1 = input('나이를 입력하세요 >>> ') # 21 일때
# print(age1 + '10')  # 2110
# print(type(age1))   # class 'str'
# age2 = int(age1)    # 21을 인트로 바꿈
# print(age2 + 10)    # 31

'''
input() 함수의 return 자료형은 str
형변환 함수 int() / float() 사용해 수학적 연산 가능
'''

# age = int(input('나이 입력 >>> '))
# input()의 결과 str 를 다시 int 변환
# print(f'당신의 나이는 {age}살이고, 내년에는 {age+1}살이 됩니다.')

# if age > 19:
#     print('성인입니다')
# elif 19 >= age > 14:
#     print('청소년입니다')
# elif 14 >= age > 5:
#     print('어린이입니다')
# else:
#     print('유아입니다')
'''
중첩 if문
'''
age = 18
has_ticket = False # boolean 자료형일때 True False / 대문자로 시작
print(type(has_ticket)) # type bool
if age >= 19:
    # 중첩 if문
    if has_ticket:
        print('영화관 입장이 가능합니다.')
    else:
        print('티켓을 구매하세요')
else:
    print('미성년자 출입 금지')

age = float(age)
print(age)
'''
논리 연산자
&& => and
|| => or
!  => not
파이썬에서는 영어로 사용한다
'''