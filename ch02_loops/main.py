'''
1. while 반복문
형식:
while 조건식1:
    반복실행문
'''
from random import random

# n1 = 1
# while n1 < 11:
#     print(n1)
#     n1 += 1
'''
10부터 1까지 역순
'''
# n2 = 10
# while n2 > 0:
#     print(n2)
#     n2 -= 1
'''
중첩 while 문
중첩 while 및 f-string 활용
'''
dan = 2
while dan < 10:
    number = 1
    while number < 10:
        print(f'{dan} X {number} = {dan * number}')
        number += 1
    dan += 1

