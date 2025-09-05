''''''
'''
형식 :
class 클래스명(파스칼케이스):
    본문

객체 생성 형식 :
객체이름 = 클래스명()
'''
# # 클래스 정의 형식 예시
# class WaffleMaChine:
#     pass
#
# # 객체 생성 예시
# waffle = WaffleMaChine()
# print(waffle)   # 결과값 : <__main__.WaffleMaChine object at 0x0000019EE787AE40>
#
# ''''''
# # 클래스 정의
# class Person:
#     # 메서드 정의(함수가 클래스 내에 있으니까)
#     def set_info(self, name, age, tel, address):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.address = address
#
#     def show_info(self):
#         print(f'이름 : {self.name}')
#         print(f'나이 : {self.age}')
#         print(f'연락처 : {self.tel}')
#         print(f'주소 : {self.address}')

# # 객체 생성
# person01 = Person()
# # Person 클래스의 메서드 호출
# person01.set_info('김일',20,'010-1234-5678', '서울특별시 마포구')
# person01.show_info()

'''
person02 객체를 생성하고, set_info() 를 활용하여 이름 나이 연락처 주소 입력하고
display_info2() 를 정의하여 다음 실행 예와 같이 출력
실행 예
제 이름은 ___ 이고, ___ 살입니다.
연락처는 ____ 인데, ___ 에 살고 있습니다.
'''
class Person:
    # 메서드 정의(함수가 클래스 내에 있으니까)
    def set_info(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):
        return f'제 이름은 {self.name} 이고, {self.age} 살입니다.\n연락처는 {self.tel} 인데, {self.address} 에 살고 있습니다.'

person02 = Person()
person02.set_info('김찬우', 25,'010-9334-0580','부산광역시 해운대구')
print(person02.show_info())























