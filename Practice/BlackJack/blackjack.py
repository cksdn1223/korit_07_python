import random
import time
from createDeck import createDeck


# 덱 클래스
class Deck:
    def __init__(self):
        self.cards = createDeck()

    def draw(self):
        choose = random.choice(list(self.cards.keys()))
        self.cards.pop(choose)  # 뽑은 카드는 덱에서 제거
        return choose


# 공통 플레이어 클래스
class BasePlayer:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.stand = False

    def hit(self, deck: Deck):
        card = deck.draw()
        self.hand.append(card)
        print(f"{self.name} 뽑은 카드: {card}")
        print(f"{self.name} 현재 점수: {self.calc_score()}")

    def calc_score(self):
        score = 0
        for card in self.hand:
            score += createDeck().get(card)  # 카드 점수 가져오기
        return score

    def show_hand(self):
        print(f"{self.name} 카드 -> {self.calc_score()}점")
        for card in self.hand:
            print(card, end=" ")
        print("\n======================\n")


# 사용자(Player)
class Player(BasePlayer):
    def action(self, deck: Deck):
        if not self.stand:
            print("1. Hit  2. Stand")
            choice = int(input("고르세요 >> "))
            if choice == 1:
                self.hit(deck)
            elif choice == 2:
                print(f"{self.name} Stand 선택")
                self.stand = True


# 딜러(Dealer)
class Dealer(BasePlayer):
    def action(self, deck: Deck):
        if not self.stand:
            if self.calc_score() <= 16:
                print("딜러 Hit")
                self.hit(deck)
            else:
                print("딜러 Stand 선택")
                self.stand = True


# 결과 판정
def result(player: Player, dealer: Dealer):
    player_score = player.calc_score()
    dealer_score = dealer.calc_score()

    if player_score > 21:
        winner = "딜러"
    elif dealer_score > 21:
        winner = "플레이어"
    else:
        if player_score > dealer_score:
            winner = "플레이어"
        elif dealer_score > player_score:
            winner = "딜러"
        else:
            winner = "무승부"

    print(f"=== 최종 결과 ===")
    player.show_hand()
    dealer.show_hand()
    print(f"우승: {winner} 🏆")
    return True


# 게임 실행
def start_game():
    deck = Deck()
    player = Player("플레이어")
    dealer = Dealer("딜러")

    # 카드 한 장씩 나눠주기
    player.hit(deck)
    dealer.hit(deck)

    while True:
        player.action(deck)
        dealer.action(deck)
        time.sleep(1)

        if (player.stand and dealer.stand) or player.calc_score() > 21 or dealer.calc_score() > 21:
            result(player, dealer)
            break


if __name__ == "__main__":
    start_game()