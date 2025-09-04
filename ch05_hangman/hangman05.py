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

logo = '''
88        88         db         888b      88    ,ad8888ba,      88b           d88         db         888b      88  
88        88        d88b        8888b     88   d8"'    `"8b     888b         d888        d88b        8888b     88  
88        88       d8'`8b       88 `8b    88  d8'               88`8b       d8'88       d8'`8b       88 `8b    88  
88aaaaaaaa88      d8'  `8b      88  `8b   88  88                88 `8b     d8' 88      d8'  `8b      88  `8b   88  
88""""""""88     d8YaaaaY8b     88   `8b  88  88      88888     88  `8b   d8'  88     d8YaaaaY8b     88   `8b  88  
88        88    d8""""""""8b    88    `8b 88  Y8,        88     88   `8b d8'   88    d8""""""""8b    88    `8b 88  
88        88   d8'        `8b   88     `8888   Y8a.    .a88     88    `888'    88   d8'        `8b   88     `8888  
88        88  d8'          `8b  88      `888    `"Y88888P"      88     `8'     88  d8'          `8b  88      `888  
'''
print(logo)
print('='*130)
word_list = [
    'apple', 'banana', 'camel', 'dog', 'elephant',
    'flower', 'grape', 'house', 'island', 'jungle',
    'kangaroo', 'lemon', 'monkey', 'notebook', 'orange',
    'pencil', 'queen', 'rabbit', 'sunflower', 'tiger'
]
chosen_word = random.choice(word_list)

display = []
for _ in range(len(chosen_word)):
    display.append('_')
lives = 6
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
    print(f'실패하셨습니다.\n정답은 {chosen_word}')



