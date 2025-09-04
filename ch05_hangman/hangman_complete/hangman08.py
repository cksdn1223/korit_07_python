def play_hangman():
    from hangman_arts import logo, stages
    from hangman_word_list import word_list
    import random

    print(logo)
    print('=' * 130)
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