import random

dice = (1,2,3,4,5,6)
computer = 0
user = 0
draw = 0
RUN_TIME = 100000

for i in range(RUN_TIME):
    user_dice = random.choice(dice)
    computer_dice = random.choice(dice)

    if user_dice == computer_dice:
        print('무승부!')
        draw += 1
    elif user_dice >= computer_dice:
        print('승리!')
        user += 1
    else:
        print('패배..')
        computer += 1
    # print(f'내 주사위 : {user_dice}\n컴퓨터 주사위 : {computer_dice}')

print(f'{user} and {computer} and {draw}')
print(f'승리확률 : {(user*100 / RUN_TIME):.1f}%')
print(f'패배확률 : {(computer*100 / RUN_TIME):.1f}%')
print(f'무승부확률 : {(draw*100 / RUN_TIME):.1f}%')


import matplotlib.pyplot as plt
plt.bar(["User Win", "Computer Win", "Draw"], [user, computer, draw])
plt.show()