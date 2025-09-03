'''
for 반복문
'''

# for i in range(10):
#     print(i+1)
'''
i가 0부터 시작
range() : for 문과 함께 연계되서 쓰이는편
range( (시작값), 종료값, (증감값) )

시작값 : 생략 가능, 생략하면 0부터 시작
종료값 : 명시하지 않으면 끝까지 진행
증감값 : 생략 가능, 생략할 경우에 1씩 증가

for (아무거나) in range(시작값, 종료값, 증감값):
    반복실행문
'''
for i in range(1, 10, 2):    # 종료값 미만 10 이면 9까지
    print(i)
'''
range(1, 10, 1)
-> for(int i = 1 ; i < 10 ; i++)
'''
str_example = '안녕하세요'
for i in str_example:
    print(i)
'''
java 향상된 for문
일반 for문처럼 쓰려면 range()
형식:
for 변수명 in iterable(반복가능객체):
    반복실행문
'''
num_list = [ 1, 2, 3, 4, 5 ]
for i in num_list:
    print(i, end= ' / ')
# print() 함수는 자동 개행이기때문에 end 키워드를 쓸 수 있습니다.