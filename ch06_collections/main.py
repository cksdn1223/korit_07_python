#
# list_example = [30, 40, '김이', [100, '김삼']]
# tuple_example = (10, 20, 30, '김사')
# set_example = {100, 200, 300, 400, '김오'}
# dictionary_example = { '이름':'김일', '나이':20, '학교':'코리아아이티'}
#
# print(list_example)
# print(tuple_example)
# print(set_example)
# print(dictionary_example)

# list 선언 및 초기화
# li1 = [ 1, 2, 3, '김사']
#
# li2 = [ 100, 3.14, 'hello'] # list 선언 및 초기화 방법 # 1
# li3 = list( [ 4, 5, 6, 7, 8, 9, 0 ])    # list 선언 및 초기화 방법 # 2
# print(li3[0:4:2])   # 0번지부터 4번지앞까지 2씩증가시키면서.
#
# scores = [30, 40, 50]
# print(scores)
# scores.append(100)
# print(scores)
# scores.insert(0,90)
# print(scores)
#
# print(scores.pop()) # 마지막 삭제 후 리턴
# print(scores.pop(0))    # 결과값 : 90



'''
li4 리스트를 선언하고 1부터 10까지 집어넣어라
print(li4) 결과값은 [1,2,3,4,5,6,7,8,9,10]
'''
# li4 = []
# for i in range(10):
#     li4.append((i+1))
'''
각 list 내의 element들을 뽑아내서 * 2 씩 해라
'''
# for i in range(len(li4)):
#     li4[i] *= 2
# print(li4)
#
# for element in li4:
#     index = len(li4)-li4.index(element)-1
#     li4[index] *= 2
# print(li4)

# tu1 = (1,2,3)   # 튜플 생성 방법 # 1
# tu2 = tuple((4,5,6))    # 튜플 생성 방법 # 2
# tu3 = 7,8,9             # 튜플 생성 방법 # 3
#
# a, b, c = 7, 8, 9       # 복수의 변수 선언 및 초기화 방법 -> 즉 변수 개수와 데이터 개수가 같으면
# print(tu1, tu2, tu3)
# print(a, b, c)
#
# tu4 = 0
# print(type(tu4))
# # tu4라고해도 그냥 int다
#
# tu5 = 1,2,3,4,5,6,7,8,9,10
# print(type(tu5))
'''
element 추출 및 slicing은 동일
'''
# tu6 = 'hello. ', 'good morning ', 'my name is ', 'kim-il', 'i am ', '20 ', 'years old.'
# for word in tu6:
#     print(word.title(), end='')
#     # Hello. Good Morning My Name Is Kim-IlI Am 20 Years Old.

# set1 = {1,2,3}      # 세트 생성 방법 # 1
# set2 = set({4,5,6}) # 세트 생성 방법 # 2
#
# print(set1)
# print(set2)
#
# # 비어있는 list / tuple / set 생성 방법
# li = []
# tu = ()
# se = {()}
# print(type(li))
# print(type(tu))
# print(type(se))
#
# se2 = set({})
# print(type(se2))    # 결과값 : set

# se3 = {10, 20, 30}
# se3.add(50)
# print(se3)
# se3.remove(30)  # 순서가 없어서 '값' 을 정확하게 입력해야만한다.
# print(se3)
#
# # remove() vs. discard()
# # se3.remove(70)  # 오류 발생 - '값을 정확하게 입력' 해야함
# se3.discard(70)     # 오류발생X 정확한 값이 없으면 그냥 종료
# print(se3)



# dict1 = {
#     '이름': '김일',
#     '나이': 20,
#     '주소': ['서울특별시', '마포구', '목동'],
# }
# #list의 element추출 반복문
# li01 = [10,20,30,40]
# for num in li01:
#     print(num)
# # dictionary에서 같은방식의 반복문을 활용
# for key in dict1:
#     print(key, dict1[key])
#
# # key들만 추출하는 메서드
# print(dict1.keys())         # dict_keys(['이름', '나이', '주소'])
# print(type(dict1.keys()))   # <class 'dict_keys'>
#
# # value들만 추출하는 메서드
# print(dict1.values())       # dict_values(['김일', 20, ['서울특별시', '마포구', '목동']])
# print(type(dict1.values())) # <class 'dict_values'>
#
# # key들만 뽑아서 list를 만든다던지 / value 들만 뽑아서 list를 만들고 싶다면 형변환 함수를 사용해야함.
#
# keys = list(dict1.keys())
# values = list(dict1.values())
# print(keys)
# print(values)


# dict1['직업'] = '웹 퍼블리셔'  # 기존에 없는 key를 입력하고 = value 지정하면 됩니다.
# print(dict1)
# dict1['직업'] = '웹 개발자'   # key 하나당 value는 고정이기 때문에 재대입이 이루어집니다.
# print(dict1)
# # 삭제 방법
# print(dict1.pop('직업'))            # key 를 알아야지 삭제 가능   / .pop() 의 return 특성
# print(dict1)

'''
list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소로부터 7번째 요소만 추출한 결과 ,그리고 그 list에서 2 번째 요소를 출력하는 프로그램을 작성하시오.

실행 예
3번재 요소로부터 7 번째 요소 = [30, 40, 50, 60, 70]
3 번째 요소로부터 7번째 요소 중 2 번째 요소 = 40
'''
# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# li001 = list[2:7]
# print(f'3 번재 요소로부터 7 번째 요소 = {li001}')
# print(f'3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = {li001[1]}')


'''
1~ 12 사이의 월 입력 받고 월이 몇일까지 있는지 출력
윤년 고려  x
실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일까지입니다.
'''
# month = int(input('1 ~ 12 사이의 월 입력하세요 >>> '))
# #1
# dict_month = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31,
# }
# print(f'{month}월은 {dict_month[month]}일까지입니다.')
#
# #2
# list_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(f'{month}월은 {list_month[month - 1]}일까지입니다.')
#
# #3
# list_month2 = [28, 30, 31]
# if month in (1,3,5,7,8,10,12):
#     index = 2
# elif month == 2:
#     index = 0
# else:
#     index = 1
# print(f'{month}월은 {list_month2[index]}일까지입니다.')
#
# #4
# def check_month(month):
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         index = 31
#     elif month == 2:
#         index = 28
#     else:
#         index = 30
#     return index
# print(f'{month}월은 {check_month(month)}일까지입니다.')

'''
응용 예제

희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'} 입니다.
조사된 수학여행지는 ['제주', '민속촌'] 입니다.
'''
# set_travel = set()
#
# for i in range(3):
#     set_travel.add(input('희망하는 수학여행지를 입력하세요 >>> '))
#
# print(f"\n조사된 수학여행지는 {set_travel} 입니다.")
# print(f"조사된 수학여행지는 {list(set_travel)} 입니다.")

'''
임의의 양의 정수 입력 받고 그 정수만큼 숫자 받아 list 저장
저장된 숫자중 짝수만 새로운 list에 저장 출력

몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>>
...
입력받은숫자는 [....] 입니다.
입력받은 숫자들 중 짝수는 [...] 입니다.
'''
# list = []
# list2 = []
# for index in range(int(input('몇 개의 숫자를 입력할까요? >>> '))):
#     num = int(input(f'{index+1}번째 숫자를 입력하세요 >>> '))
#     list.append(num)
#     if num%2 == 0:
#         list2.append(num)
# print(f'입력 받은 숫자는 {list} 입니다.')
# print(f'입력 받은 숫자들 중 짝수는 {list2} 입니다.')

'''
딕셔너리 기반의 연락처 관리

3명의 이름과 전화번호를 입력받아 딕셔너리에 저장, 정보를 추출하는 프로그램

실행 예
1 번째 사람의 이름을 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>>
...

입력 받은 연락처는 {'김일':'010.....} 입니다.
'''
# contact = {}
# for i in range(3):
#     name = input(f'{i+1} 번째 사람의 이름을 입력하세요 >>> ')
#     number = input(f'{i+1} 번째 사람의 연락처를 입력하세요 >>> ')
#     contact[name] = number
#
#
# print(f'입력 받은 연락처는 {contact} 입니다.')

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 numbers1 을 선언하고 , 그 안에 입력받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()
매개 변수 : 정수 n

함수 호출
add_numbers1(last_num)
print(add_numbers2(last_num))

실행 예
숫자 몇 까지 입력하시겠습니까? >>> 
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,9,10]
'''
# numbers1 = []
# numbers2 = []
# def add_numbers1(n):
#     for i in range(n):
#         numbers1.append(i+1)
#     print(numbers1)
#
# def add_numbers2(n):
#     for i in range(n):
#         numbers2.append(i+1)
#     return numbers2
#
# def add_numbers3(n, li):
#     for i in range(n):
#         li.insert(i,i+1)
#     print(li)
#
# last_num = int(input('숫자 몇 까지 입력하시겠습니까? >>> '))
# add_numbers1(last_num)
# print(add_numbers2(last_num))
#
# hello = ['안','녕','하','세','요']
# add_numbers3(last_num, hello)


'''
짝수와 홀수 개수 세기
list를 입력받아 개수를 세시오

함수 정의
함수 이름 : count_even_odd
매개변수 : list numbers( 요소는 모두 정수일 것)

함수 호출
count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
'''
def count_even_odd(list):
    even = 0
    for num in list:
        if num % 2 == 0:
            even += 1
    print(f'짝수의 개수 : {even}개')
    print(f'홀수의 개수 : {len(list)-even}개')

count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])






















