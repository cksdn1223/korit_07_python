import random

lotto = []

while len(lotto) < 6:
    random_choice = random.randint(1, 45)
    if random_choice not in lotto:
        lotto.append(random_choice)

lotto.sort()

guess_lotto = []
while len(guess_lotto) < 6:
    guess = input('로또 넘버를 입력하세요 >>> ')
    if guess.isdigit() and 0 < int(guess) < 46:
        if int(guess) not in guess_lotto:
            guess_lotto.append(int(guess))
        else:
            print('이미 입력하신 값 입니다.')
    else:
        print('올바르지 않은 입력입니다.')

guess_lotto.sort()


print(f'로또 번호 : {lotto}')
print(f'유저 번호 : {guess_lotto}')

count = 0

for i in guess_lotto:
    if i in lotto:
        count += 1

print(f'{count}개 맞추셨습니다.')
print(f'{7-count}등 입니다 !!')

