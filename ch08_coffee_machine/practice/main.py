MENU = {
    '에스프레소': {'재료': {'물': 50, '커피': 18}, '가격': 1.5},
    '라떼': {'재료': {'물': 200, '우유': 150, '커피': 24}, '가격': 2.5},
    '카푸치노': {'재료': {'물': 250, '우유': 100, '커피': 24}, '가격': 3.0},
}
resources = {'물': 300, '우유': 200, '커피': 100, '돈': 0}
coin = {'quarters': 0.25, 'dimes': 0.10, 'nickels': 0.05, 'pennies': 0.01}

#  재료와 돈 계산 함수
def can_buy_check(order):
    check = True
    for item in MENU[order]['재료']:
        # 현재 보유하고있는 자원이 오더의 재료나 돈보다 적다면 False
        if MENU[order]['재료'][item] > resources[item]:
            print(f'{item}', end=' ')
            check = False
    # 위 조건에 걸리지 않는다면 구매 가능 True 리턴
    if not check: print(' 부족')
    return check

def report_resources():
    for resource in resources:
        print(f'{resource} : '
              f'{'$' if resource == '돈' else ''}{resources[resource]}'
              f'{'g' if resource == '커피' else 'ml' if resource != '돈' else ''}')

def import_coin(order):
    money = 0
    while True:
        print(f'{order}가격 : {MENU[order]['가격']}')
        print('quarters = $0.25, dimes = $0.10, nickels = $0.05, pennies = $0.01 / 아무것도 입력 안할시 계산')
        import_c = input('동전을 삽입하세요 >> ')
        if " " in import_c:
            parts = import_c.split(" ")
            if len(parts) == 2:
                coin_name, coin_count = parts[0], int(parts[1])
                if coin_name in coin.keys():
                    money += coin[coin_name]*coin_count
                    print(f'현재 넣은 돈 : {money}')
            elif len(parts) == 1:
                coin_name = parts[0]
                if coin_name in coin.keys():
                    money += coin[coin_name]
                    print(f'현재 넣은 돈 : {money}')
            else:
                print('다시 입력하세요')
        elif import_c == '':
            if MENU[order]['가격'] == money:
                resources['돈'] += MENU[order]['가격']
            elif MENU[order]['가격'] < money:
                change = money - MENU[order]['가격']
                if change > resources['돈']:
                    print(f'자판기 내 돈 부족')
                    return False
                resources['돈'] += MENU[order]['가격']
                print(f'여기 ${change:.2f}의 잔돈이 있습니다.')
            else:
                print(f'돈이 부족합니다. 돈을반환합니다. {money}')
                return False
            return True
        else:
            print('다시 입력하세요')

def minus_material(order):
    for item in MENU[order]['재료']:
        resources[item] -= MENU[order]['재료'][item]


while True:
    order = input('무엇을 드시겠습니까? (에스프레소/라떼/카푸치노) ')
    # 관리자 명령어
    if order == 'admin':
        print('관리자 명령어 : off report')
        continue
    elif order == "off":
        print('종료되었습니다.')
        break
    elif order == "report":
        report_resources()
        continue
    #옳바르게  입력했는지 확인
    if order not in MENU:
        print('옳바르지 않은 입력입니다.')
        continue

    # 구매 가능한지 체크
    if can_buy_check(order):
        if import_coin(order):
            minus_material(order)
            print(f'여기 {order}가 나왔습니다. 맛있게 드세요!')
        else:
            print(f'{order} 구매 실패')
    else:
        print(f'{order} 구매 불가')

