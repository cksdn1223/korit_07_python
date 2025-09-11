# from prettytable import PrettyTable
# table = PrettyTable()
# table.field_names = ["예외 클래스", "의미"]
# table.add_row(["BaseException", "최상위 예외 클래스"])
# table.add_row(["Exception","대부분 예외 클래스의 슈퍼 클래스"])
# table.add_row(["ArithmeticError","산술 연산에 문제가 있을 때"])
# table.add_row(["AttributeError","잘못된 속성을 참조할 때"])
# table.add_row(["EOFError","파일에서 더 이상 읽어 들일 데이터가 없을 때"])
# table.add_row(["ModuleNotFoundError","import할 모듈이 없을 때"])
# table.add_row(["FileNotFoundError","존재 하지 않는 파일일 때"])
# table.add_row(["IndexError","잘못된 인덱스를 사용할 때"])
# table.add_row(["NameError","잘못된 이름(변수)을 사용할 때"])
# table.add_row(["SyntaxError","문법이 틀렸을 때"])
# table.add_row(["TypeError","계산하려는 데이터 유형이 잘못되었을 때"])
# table.add_row(["ValueError","계산하려는 데이터 값이 잘못되었을 때"])
# table.add_autoindex("순번")
# print(table)

# try:
#     a = int(input('나누는 수(제수)를 입력하세요 >>> '))
#     b = int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
#     print(f'b / a = {b / a}')
# except ValueError:
#     print('예외 발생')

# try:
#     height = input('키 입력 >>> ')
#     height = round(height)
#     print(f'입력한 키 {height}cm')
# except:
#     print('예외')

# try:
#     a = int(input('나누는 수 입력 >> '))
#     b = int(input('나누어지는 수 입력 >> '))
#     print(f'b / a = {b / a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except TypeError:
#     print('자료형이 일치하지 않습니다.')
# except ValueError:
#     print('정수만 입력')

# z = [ 10, 20, 30, 40, 50 ]
# try:
#     print(z[10])
# except IndexError as e:
#     print(e)

# try:
#     a = int(input('나누는 수 정수 입력 >> '))
#     b = int(input('나누어지는수 정수입력 >> '))
#     result = b / a  # 여기서 오류 발생
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print(f'b / a = {result}')
# finally:
#     print('프로그램 종료')

# age = int(input('나이를 입력하세요 >>> '))
# print(f'당신의 나이는 {age}살 입니다.')

# try:
#     age = int(input('나이를 입력하세요 >>> '))
#     raise Exception('강제로 발생시킨 예외')
# except Exception as e:
#     print('발생한 예외 메시지는 다음과 같다.')
#     print(e)

# class NegatioveAgeError(Exception):     # Exception 클래스 상속 받았다는 의미
#     """사용자 정의 예외 클래스 : 나이가 음수일때 발생"""
#     pass
# class TooManyAgeError(Exception): pass
# try:
#     age = int(input('나이를 입력 >> '))
#     if age < 0:
#         raise NegatioveAgeError('나이는 음수일 수 없습니다.')
#     elif age > 200:
#         raise TooManyAgeError('200살 초과된 나이는 입력할 수 없습니다.')
# except NegatioveAgeError as e:
#     print('발생한 예외 메시지는 다음과 같다')
#     print(e)
# except TooManyAgeError as e:
#     print('발생한 예외 메시지는 다음과 같다')
#     print(e)
# else:
#     print(f'당신의 나이는 {age} 살이다.')
# finally:
#     print('프로그램 종료')
'''
나이가 200살 초과일 때 TooManyAgeError 예외를 발생시켜서 '200살 초과된 나이는 입력할 수 없습니다.' 라는 메시지 출력
'''
'''
사용자의 점수를 0이상 100이하로 입력받아서 80점 이상이면 합격, 아니면 불합격 출력
0이상 100이하의 유효한 값이 아니라면 예외발생
'점수는 0이상 100이하입니다' 라는ㅇ ㅖ외메시지 출력 -> 사용자저으이예외클래스
ScoreOutOfRangeError 클래스 정의
입력받는데 백점이라고 입력하면 '점수는 숫자로 입력해야합니다' 라는 메시지 출력
실수로 입력하면 '정수로 입력해야 합니다' 라는 메시지 출력
예상할 수 없는 예외가 발생시 Esception을 적용하여 디폴트 에러 미시지 출력
프로그램 종료 마지막 출력
'''
# class ScoreOutOfRangeError(Exception): pass
# try:
#     score = input('점수를 입력하세요 >>> ')
#     score = int(score)
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError('점수는 0이상 100이하입니다')
# except ScoreOutOfRangeError as e:
#     print(e)
# except ValueError:
#     if '.' in score:
#         print('정수로 입력해야 합니다')
#     else: print('점수는 숫자로 입력해야합니다')
# except TypeError as e:
#     print(e)
# except Exception as e:
#     print(e)
#
# else:
#     print(f'{'합격' if score >= 80 else '불합격'}')
# finally:
#     print('프로그램 종료')

'''
숫자 입력받아 해당숫자로 100을 나누는 값을 출력
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 적절한 예외 메시지를 출력
지시사항
1. 숫자 입력받기
2. 입력받은숫자로 100을 나눠 결과출력
3. 0일경우 예외처리 '0으로 나눌 수 없습니다' 출력
4. 숫자 아니면 '숫자만 입력할 수 있습니다' 출력
5. 예외 발생 안하면 '정상적으로 처리되었습니다.' 출력 겨로가 출력
6. 프로그램 종료 메시지 출력
'''
# try:
#     num = int(input('숫자 입력하세요 >> '))
#     result = 100/num
#     print(result)
# except ValueError:
#     print('정수만 입력할 수 있습니다.')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다')
# except Exception as e:
#     print(e)
# else:
#     print('정상적으로 처리되었습니다.')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
리스트의 인덱스를 입력받아  해당 인덱스의 값을 출력하는 프로그램
잘못된 인덱스 입력하면 ㅖ외메시지 출력
지시사항
1. 미리 정의된 리스트
2. 리스트 인덱스 입력
3. 입력받은 인덱스 사용해 리스트 값 출력
4. 인덱스가 리스트의 범위를 벗어나면 적절한 메시지 출력
5. 사람을 의심하고 예상되는 예외를 적용한다.
6. 예외가 발생하지 않으면 '정상적으로 처리되었습니다' 라는 메시지와 함께 해3당 인덱스의 값을 출력한다.
7. 프로그램 종료 메시지 출력
8. 마이너스인덱스는 적용 X -> 사용자 정의 예외 클래스 
-> NegativeNumIndexError라고 이름
'''
# class NegativeNumIndexError(Exception): pass
# my_list = [10, 20, 30, 40, 50]
# 
# index = input('리스트의 인덱스를 입력 > ')
# try:
#     index = int(index)
#     if index < 0:
#         raise NegativeNumIndexError('마이너스 인덱스는 적용되지 않습니다.')
#     print(my_list[index])
# except NegativeNumIndexError as e:
#     print(e)
# except ValueError as e:
#     if '.' in index:
#         print('실수는 인덱스가 될 수 없습니다.')
#     else:
#         print('문자열은 인덱스가 될 수 없습니다.')
# except IndexError:
#     print('인덱스 범위를 벗어났습니다.')
# except Exception as e:
#     print(e)
# else:
#     print('정상적으로 처리되었습니다.')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
사용자로부터 
지시 사항
1. 미리 정의된 클래스 객체
2. 사용자로부터 속성명 입력받기
3. 입력받은 속성명 사용해 객체의 속성값 출력
4. 잘못된 속성명 입력하면 존재하지 않는 속성입니다 메시지 출력
5. 예외 발생안하면 정상적으로 처리되었습니다 , 속성값 출력
6. 프로그램 종료 메시지 출력
'''
class Person:
    school = '코리아아이티대학교'
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person(name='김일', age=21)
#
# try:
#     print(getattr(person1, input('속성명을 입력하세요 >> ')))
# except AttributeError:
#     print('존재하지 않는 속성입니다.')
# except Exception as e:
#     print(e)
# else:
#     print('정상적으로 처리되었습니다.')
# finally:
#     print('프로그램 종료되었습니다.')

person1_dict = vars(person1)
print(person1_dict)
attr_key = input('출력 속성명 ')
print(person1_dict[attr_key])











