import random
import matplotlib.pyplot as plt
from matplotlib import rc

# 한글 폰트 설정 (Windows 기준)
rc('font', family='Malgun Gothic')

TIME = 10000
car_change_visible = 0
car_keep_visible = 0
car_change_hidden = 0
car_keep_hidden = 0

for _ in range(TIME):
    deck = ['Car', 'Goat', 'Goat']
    random.shuffle(deck)
    choose = random.randint(0,2)

    # =========================
    # 1️⃣ 염소 공개 시뮬레이션
    li = ['_', '_', '_']
    # 사회자가 염소 공개
    if choose == 0:
        li[1 if deck[1] == 'Goat' else 2] = 'Goat'
    elif choose == 1:
        li[0 if deck[0] == 'Goat' else 2] = 'Goat'
    else:
        li[0 if deck[0] == 'Goat' else 1] = 'Goat'

    # 선택 유지
    if deck[choose] == 'Car':
        car_keep_visible += 1
    # 선택 변경
    new_choice = [i for i in range(3) if i != choose and li[i] == '_'][0]
    if deck[new_choice] == 'Car':
        car_change_visible += 1

    # =========================
    # 2️⃣ 염소 비공개 시뮬레이션
    # 선택 유지
    if deck[choose] == 'Car':
        car_keep_hidden += 1
    # 선택 변경 (무작위 다른 문)
    new_choice_hidden = [i for i in range(3) if i != choose][0]
    if deck[new_choice_hidden] == 'Car':
        car_change_hidden += 1

# 확률 계산
prob_visible = [car_keep_visible / TIME * 100, car_change_visible / TIME * 100]
prob_hidden = [car_keep_hidden / TIME * 100, car_change_hidden / TIME * 100]

# 막대 그래프 비교
labels = ['선택 유지', '선택 변경']
x = range(len(labels))
width = 0.35

plt.bar([i - width/2 for i in x], prob_visible, width=width, color='skyblue', label='염소 공개')
plt.bar([i + width/2 for i in x], prob_hidden, width=width, color='orange', label='염소 비공개')

plt.xticks(x, labels)
plt.ylabel('승률 (%)')
plt.title('몬티홀 문제 비교 시뮬레이션')
plt.ylim(0, 100)
plt.legend()

# 값 표시
for i in range(len(labels)):
    plt.text(i - width/2, prob_visible[i]+1, f"{prob_visible[i]:.1f}%", ha='center')
    plt.text(i + width/2, prob_hidden[i]+1, f"{prob_hidden[i]:.1f}%", ha='center')

plt.show()
