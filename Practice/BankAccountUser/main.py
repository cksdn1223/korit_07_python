class Bank:
    def __init__(self):
        self.accounts = {}  # {username: Account}

    def create_account(self, user, initial_balance):
        account = Account(initial_balance)
        self.accounts[user.name] = account
        user.accounts.append(account)
        print(f'{user.name}님 계좌 생성 완료')

    def delete_account(self, user_name):
        if user_name in self.accounts:
            del self.accounts[user_name]
            print(f'{user_name} 계좌 삭제 완료')

    def show_bank_report(self):
        for user_name, account in self.accounts.items():
            print(f'소유주: {user_name} / 잔액: {account.balance}')

class User:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, bank, initial_balance):
        bank.create_account(self, initial_balance)

    def get_accounts(self):
        return self.accounts

    def show_user_info(self):
        print(f'사용자 이름: {self.name}')
        for i, account in enumerate(self.accounts, 1):
            print(f'계좌{i} 잔액: {account.balance}')

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'입금 완료. 현재 잔액: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('잔액이 부족합니다.')
        else:
            self.balance -= amount
            print(f'출금 성공. 현재 잔액: {self.balance}')

    def close_account(self, bank, user):
        bank.delete_account(user.name)
        user.accounts.remove(self)
        print('계좌 폐쇄 완료')

# 은행 생성
my_bank = Bank()

# 사용자 생성
alice = User("Alice")
bob = User("Bob")

# 계좌 생성
alice.open_account(my_bank, 1000)  # Alice 계좌 1000원
bob.open_account(my_bank, 500)     # Bob 계좌 500원

# 은행 전체 계좌 현황
print("\n[은행 전체 보고서]")
my_bank.show_bank_report()

# 사용자 정보 확인
print("\n[Alice 정보]")
alice.show_user_info()

# 입금 / 출금
print("\n[Alice 입금 200]")
alice.accounts[0].deposit(200)

print("\n[Bob 출금 600]")
bob.accounts[0].withdraw(600)  # 잔액 부족

print("\n[Bob 출금 300]")
bob.accounts[0].withdraw(300)  # 성공

# 은행 전체 보고서 확인
print("\n[은행 전체 보고서]")
my_bank.show_bank_report()

# 계좌 폐쇄
print("\n[Alice 계좌 폐쇄]")
alice.accounts[0].close_account(my_bank, alice)

# 은행 보고서 최종 확인
print("\n[최종 은행 보고서]")
my_bank.show_bank_report()