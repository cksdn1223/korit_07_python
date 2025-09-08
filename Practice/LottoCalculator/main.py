import random
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='Malgun Gothic')

def generate_lotto():
    return sorted(random.sample(range(1,46), 6))

def simulate_lotto(trials=100000):
    win_counts = {1:0, 2:0, 3:0, 4:0, 5:0}  # 0:꽝

    for _ in range(trials):
        lotto = generate_lotto()
        user = generate_lotto()  # 랜덤 유저 번호
        matched = len(set(lotto) & set(user))

        # 등수 판정
        if matched == 6:
            win_counts[1] += 1
        elif matched == 5:
            win_counts[2] += 1  # 보너스 번호 제외 간단화
        elif matched == 4:
            win_counts[3] += 1
        elif matched == 3:
            win_counts[4] += 1
        elif matched == 2:
            win_counts[5] += 1

    plt.title('로또 시뮬레이션')
    plt.ylabel('당첨 횟수')
    plt.bar([f"1등\n{win_counts[1]}", f"2등\n{win_counts[2]}", f"3등\n{win_counts[3]}"], [win_counts[1], win_counts[2], win_counts[3]])
    plt.ylim(0, 2000)
    plt.show()

simulate_lotto(1000000)