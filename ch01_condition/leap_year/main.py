'''

    1. 4로 나누어 떨어지는 해는 윤년입니다.
    2. 그러나, 100으로 나누어 떨어지는 해는 윤년이 아닙니다.
    3. 그런데, 400으로 나누어 떨어지는 해는 윤년입니다.


윤년인지 확인하고 싶은 연도를 입력하세요 >>> 2200년
2200년은 윤년이 아닙니다.

윤년인지 확인하고 싶은 연도를 입력하세요 >>> 2000년
2000년은 윤년입니다.
'''

year = int(input('윤년인지 확인하고 싶은 연도를 입력하세요 >>> '))
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    print(f'{year}년은 윤년입니다.')
else:
    print(f'{year}년은 윤년이 아닙니다.')


if year % 400 == 0:
    print('윤년입니다.')
elif year % 100 == 0:
    print('윤년이아닙니다')
elif year% 4 == 0:
    print('윤년입니다')
else:
    print('윤년이 아닙니다.')

if year % 4 == 0:
    if year % 400 == 0:
        print('윤년')
    elif year % 100 == 0:
        print('윤년X')
    else:
        print('윤년')
else:
    print('윤년x')