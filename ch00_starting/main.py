print("Hello, Python ! ")

# 주석
'주'
'''주석'''

print(1)    # 숫자 1 + 2 = 3
print('1')  # 문자열 1 + 2 = 12

print(type('1'))    # str
print(type(1))      # int
print(type(1.1))      # float

'''
print() : 출력 하는 함수
type()  : argument가 어떤 자료형인지 알려주는 함수
    - js 에서는 typeof가 연산자였음
'''

print('python 수업 시작')
print('''
다중 작성 \'\'\' \'\'\' 작성
줄 넘어갈 때 마다 + 안써줘도 됨
''')

''' 
알 수 있는점 print() > 자동 개행이 된다
변수 : 데이터를 저장
'''

# 변수 선언 및 초기화
# 변수 명 = 데이터
name = '김일'
age = 20
print('안녕하세요. 제 이름은 ' + name + '입니다. 나이는 ' + str(age) + '살입니다.')

'''
python은 java나 js 할때처럼 맨 처음이 str이면 뒤의 int/float 을 알아서 바꾸는 것을 안합니다.

형변환 함수 사용해야합니다

str()   : 문자열 자료형으로 바꿈
int()   : 정수 자료형으로 바꿈
float() : 실수 자료형으로 바꿈

f-string 개념 f''
'''
print(f'안녕하세요 제 이름은 {name}이고, 나이는 {age}살입니다.')
'''
java 에서의 Scanner 같은 기능 을 하는 함수 : input()
'''
name2 = input('이름 입력 >>> ')
print(name2)