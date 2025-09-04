import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [ 'apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
display = []
for _ in range(len(chosen_word)):
    display.append('_')

#todo -1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6 으로 초기화하세요.
lives = 6

#todo -2 : hangman03을 참조하여 while 반복문 바깥을 완성하시오.
#todo -3 : while문의 조건을 수정하여 6번의 기회가 소진되면 반복문이 종료될 수 있도록 작성하시오.
#todo -4 : lives의 변수와 stages 리스트의 관계를 파악하여  guess 를 입력할 때마다 올바른 stages의 element가 출력될수있도록 작성
while lives > 0:
    print(' '.join(display))
    print(f'남은 기회 : {lives}')
    guess = input('알파벳을 입력하세요 >>> ').lower()

    for index in range(len(chosen_word)):
        alp = chosen_word[index]
        if guess == alp:
            display[index] = alp

    if guess not in chosen_word:
        lives -= 1
    print(stages[lives])

    if '_' not in display:
        print(f'성공하셨습니다!\n정답은 {chosen_word}')
        break

if '_' in display:
    print(f'실패하셨습니다.\n 정답은 {chosen_word}')


