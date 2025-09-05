import random

book_inventory = {}

def add_book(title, author, price, stock):
    if title == "" or author == "" or price == "" or stock == "":
        print('비어있는 값이 있습니다.')
        return
    elif title in book_inventory.keys():
        if author == book_inventory.get(title)['author']:
            print(f'{title} 책은 이미 보유중인 도서입니다.')
            add_stock(title, stock)
            return

    book = {'title': title, 'author': author, 'price': int(price), 'stock': int(stock)}
    book_inventory[title] = book
    print(f'{title} 책 추가완료 !')

def remove_book(title, stock):
    if not check_book_exists(title):
        return
    elif stock <= book_inventory.get(title)['stock']:
        book_inventory.get(title)['stock'] -= stock
        print(f'{title} {stock}개 재고에서 삭제합니다.')
    else:
        print('올바르지 않은 입력입니다.')

def buy_book(title, stock):
    if not check_book_exists(title):
        return
    elif stock <= book_inventory.get(title)['stock']:
        book_inventory.get(title)['stock'] -= stock
        print(f'{title} {stock} 권 구매했습니다.')
        print(f'현재 {title} 보유량 : {book_inventory.get(title)["stock"]}')

def search_book(title):
    if title in book_inventory.keys():
        book = book_inventory.get(title)
        print(f'{title} 책의 정보')
        print(f'저자 : {book["author"]}')
        print(f'재고 : {book["stock"]}')
        print(f'가격 : {book["price"]}')
    else:
        print(f'현재 검색하신 {title} 책은 보유하고있지 않습니다.')

def add_stock(title, stock):
    if not check_book_exists(title):
        return
    elif stock <= 0:
        print(f'{stock}은 올바르지 않은 입력값 입니다.')
    else:
        print(f'{title} 책의 재고를 {stock}권 추가하였습니다.')
        book_inventory.get(title)['stock'] += stock
        print(f'현재 보유량 : {book_inventory.get(title)["stock"]}')

def check_book_exists(title):
    if title not in book_inventory:
        print(f'{title} 책을 보유중이지 않습니다.')
        return False
    return True

def all_books():
    if len(book_inventory) != 0:
        for title, book in book_inventory.items():
            print("-----")
            print(f'제목 : {title}')
            print(f'저자 : {book["author"]}')
            print(f'재고 : {book["stock"]}')
            print(f'가격 : {book["price"]}')
        print("-----")
    else:
        print('현재 보유중인 책이 없습니다.')

def recommend_book():
    if len(book_inventory) != 0:
        book = random.choice(list(book_inventory.keys()))
        print(f'추천드리는 책 {book}')
        search_book(book)
    else:
        print('현재 보유중인 책이 없습니다.')