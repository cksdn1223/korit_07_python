MENU = {
    '에스프레소': {'재료': {'물': 50, '커피': 18}, '가격': 1.5},
    '라떼': {'재료': {'물': 200, '우유': 150, '커피': 24}, '가격': 2.5},
    '카푸치노': {'재료': {'물': 250, '우유': 100, '커피': 24}, '가격': 3.0},
}
profit = 0
resources = {'물': 300, '우유': 200, '커피': 100}

def is_resources_enough(order_ingredient):
    check = True
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f'{item}', end=' ')
            check = False
    if not check: print('부족')
    return check

def process_coins():
    sum = 0
    sum += float(input('쿼터 몇개 ? ')) * 0.25
    sum += float(input('다임 몇개 ? ')) * 0.10
    sum += float(input('니켈 몇개 ? ')) * 0.05
    sum += float(input('페니 몇개 ? ')) * 0.01
    return sum

def is_transaction_successful(money_received, drink_cost):
    change = money_received - drink_cost
    if change >= 0:
        global profit   # 전역 변수인 profit을 함수 내부에서 사용하기 위한 키워드
        profit += drink_cost
        print(f'잔돈 ${change:.2f}을(를) 반환합니다.')
        return True
    else:
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다.')
        return False

def make_coffe(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f'{drink_name}이(가) 나왔습니다. 맛있게 드세요 !!')

is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ')
    if choice == "off":
        print('종료되었습니다.')
        is_on = False
    elif choice == "report":
        for resource in resources:
            print(f'{resource} : {resources[resource]}'
                  f'{'g' if resource == '커피' else 'ml' if resource != '돈' else ''}')
        print(f'돈 : ${profit:.2f}')
    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received=money_received, drink_cost=drink['가격']):
                make_coffe(drink_name=choice, order_ingredient=drink['재료'])
        else:
            print(f'{choice} 구매 불가')
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요.')




