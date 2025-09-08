MENU = {
    '에스프레소': {'재료': {'물': 50, '커피': 18}, '가격': 1.5},
    '라떼': {'재료': {'물': 200, '우유': 150, '커피': 24}, '가격': 2.5},
    '카푸치노': {'재료': {'물': 250, '우유': 100, '커피': 24}, '가격': 3.0},
}

COIN_VALUES = {'quarters': 0.25, 'dimes': 0.10, 'nickels': 0.05, 'pennies': 0.01}


class CoinMachine:
    def __init__(self):
        self.inserted_money = 0

    def import_coin(self, price):
        self.inserted_money = 0
        while True:
            print(f'가격: ${price}')
            print('quarters, dimes, nickels, pennies / 입력 후 엔터 / 빈 입력 시 계산')
            user_input = input('동전을 넣으세요 >> ')
            if user_input.strip() == '':
                break
            parts = user_input.split()
            if len(parts) == 2 and parts[0] in COIN_VALUES:
                try:
                    count = int(parts[1])
                    self.inserted_money += COIN_VALUES[parts[0]] * count
                    print(f'현재 넣은 돈: ${self.inserted_money:.2f}')
                except ValueError:
                    print('잘못된 입력입니다.')
            else:
                print('잘못된 입력입니다.')

        if self.inserted_money < price:
            print(f'돈이 부족합니다. ${self.inserted_money:.2f} 반환합니다.')
            return False, 0
        change = round(self.inserted_money - price, 2)
        return True, change

class CoffeeMachine:
    def __init__(self, menu, resources):
        self.menu = menu
        self.resources = resources
        self.coin_machine = CoinMachine()

    def start_machine(self):
        while True:
            order = input('무엇을 드시겠습니까? (에스프레소/라떼/카푸치노) ')
            if order == 'off':
                print('종료되었습니다.')
                break
            elif order == 'report':
                self.report_resources()
                continue
            elif order not in self.menu:
                print('올바르지 않은 입력입니다.')
                continue

            if self.can_make_drink(order):
                success, change = self.coin_machine.import_coin(self.menu[order]['가격'])
                if success:
                    self.deduct_resources(order)
                    self.resources['돈'] += self.menu[order]['가격']
                    if change > 0:
                        print(f'여기 ${change:.2f}의 잔돈이 있습니다.')
                    print(f'여기 {order}가 나왔습니다. 맛있게 드세요!')
                else:
                    print(f'{order} 구매 실패')
            else:
                print(f'{order} 구매 불가')

    def can_make_drink(self, order):
        missing = []
        for ingredient, amount in self.menu[order]['재료'].items():
            if self.resources.get(ingredient, 0) < amount:
                missing.append(ingredient)
        if missing:
            print(f'{", ".join(missing)} 부족')
            return False
        return True

    def deduct_resources(self, order):
        for ingredient, amount in self.menu[order]['재료'].items():
            self.resources[ingredient] -= amount

    def report_resources(self):
        for res, val in self.resources.items():
            unit = 'ml' if res in ['물', '우유'] else 'g' if res == '커피' else '$'
            print(f'{res}: {val}{unit}')


if __name__ == '__main__':
    resources = {'물': 300, '우유': 200, '커피': 100, '돈': 0}
    machine = CoffeeMachine(MENU, resources)
    machine.start_machine()
