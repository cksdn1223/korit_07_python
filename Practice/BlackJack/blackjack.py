import random
import time

from createDeck import *

deck = createDeck()
dealer_deck = []
player_deck = []
dealer_stand = False
player_stand = False
def choose_card():
    choose = random.choice(list(deck.keys()))   # 고르기
    deck.pop(choose)  # 덱에서 고른거 빼기
    return choose


def cal_score(who_deck):
    score = 0
    for card in who_deck:
        score += (createDeck().get(card))
    return score

def hit(who_deck):
    card = choose_card()
    who_deck.append(card)
    print(f'뽑으신 카드 : {card}')
    print(f'현재 점수 : {cal_score(who_deck)}')


def start_game():
    dealer_deck.append(choose_card())
    player_deck.append(choose_card())

    print('카드를 한장씩 받으셨습니다.')
    show_info()

def show_info():
    print('======================')
    print(f'플레이어 카드 -> {cal_score(player_deck)}점')
    for card in player_deck: print(card, end=' ')
    print()
    print(f'딜러 카드 -> {cal_score(dealer_deck)}점')
    for card in dealer_deck: print(card, end=' ')
    print('\n======================')

def result():
    if (dealer_stand and player_stand) or (cal_score(dealer_deck) > 21 or cal_score(player_deck) > 21):
        dealer_score = cal_score(dealer_deck)
        player_score = cal_score(player_deck)
        # 21 초과(Bust) 처리
        if player_score > 21:
            winner = '딜러'
        elif dealer_score > 21:
            winner = '플레이어'
        else:
            winner = '딜러' if dealer_score > player_score else '무승부' if dealer_score == player_score else '플레이어'
        print(f'{winner} 우승 !!!')
        return True
    else:
        return False
start_game()
while True:
    if not player_stand:
        print('1. hit 2. stand')
        choose = int(input('고르세요 >> '))
        print('======================')
        if choose == 1:
            print('hit을 선택하셨습니다. 플레이어 카드 뽑습니다.')
            hit(player_deck)
        elif choose == 2:
            print('플레이어 stand 선택.')
            player_stand = True

    if not dealer_stand:
        if cal_score(dealer_deck) <= 16:
            print('hit을 선택하셨습니다. 딜러 카드 뽑습니다.')
            hit(dealer_deck)
        else:
            print('딜러 stand 선택.')
            dealer_stand = True
    time.sleep(3)

    if result():
        break

    show_info()



