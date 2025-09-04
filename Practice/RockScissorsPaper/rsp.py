import random

rsp = ['가위', '바위', '보']
user = 0
computer = 0
nothing = 0
TIMES = 1000000
## 누가 승자인지 리턴하는 함수
def check(users, computers):
    if users == computers:
        return '무승부'
    if (users == '가위' and computers == '보' or
        users == '바위' and computers == '가위' or
        users == '보' and computers == '가위'):
        return 'users'
    return 'computers'

for i in range(TIMES):
    result = check(random.choice(rsp), random.choice(rsp))
    if result == 'users':
        user += 1
    elif result == 'computers':
        computer += 1
    else:
        nothing += 1

print(f'유저 승리 : {user}')
print(f'컴퓨터 승리 : {computer}')
print(f'무승부 : {nothing}')
print(f'승리 확률 : {(user / TIMES)*100:.1f}%')
# while True:
#     users = input('가위바위보 >>> ')
#     computers = random.choice(rsp)
#     check(users, computers)