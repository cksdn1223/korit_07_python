from bmfunction import *

while True:
    print('='*85)
    print('1. 책 추가 2. 책 제거 3. 책 구매 4. 책 검색 5. 재고 추가 6. 모든 책 보기 7. 책 추천 8. 종료')
    print('='*85)
    choose = int(input('원하는 메뉴를 고르세요 >>> '))
    if choose == 1:
        title = input('책 제목을 입력하세요 >>> ')
        author = input('책 저자를 입력하세요 >>> ')
        price = input('책 가격을 입력하세요 >>> ')
        stock = input('책 재고를 입력하세요 >>> ')
        add_book(title, author, int(price), int(stock))
    elif choose == 2:
        title = input('책 제목을 입력하세요 >>> ')
        stock = input('제거할 갯수를 입력하세요 >>> ')
        remove_book(title, int(stock))
    elif choose == 3:
        title = input('책 제목을 입력하세요 >>> ')
        stock = input('구매할 갯수를 입력하세요 >>> ')
        buy_book(title, int(stock))
    elif choose == 4:
        title = input('책 제목을 입력하세요 >>> ')
        search_book(title)
    elif choose == 5:
        title = input('책 제목을 입력하세요 >>> ')
        stock = input('추가할 갯수를 입력하세요 >>> ')
        add_stock(title, int(stock))
    elif choose == 6:
        all_books()
    elif choose == 7:
        recommend_book()
    elif choose == 8:
        break

