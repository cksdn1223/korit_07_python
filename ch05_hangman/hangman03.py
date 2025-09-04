import random
'''
''.join(반복가능객체) method : '.' 앞에있는 문자열을 기준으로 반복 가능 객체의 element들을 합쳐서 str로 합쳐주는 emthod
'''
# temp = ['배', '고', '프', '다']
# feeling = ''.join(temp)
# print(feeling)
#
# feeling2 = '/'.join(temp)
# print(feeling2)

word_list = [ 'apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

#todo -1 : 비어있는 list 인 display를 선언하시오.
display = []

#todo -2 : chosen_word의 문자 개수만큼 '_'를 display에 추가하시오.
for _ in range(len(chosen_word)):
    display.append('_')

#todo -3 : 사용자가 추측을 반복할 수 있도록 while 반복문을 작성하시오. 사용자가 chosen_word의 모든 문자열들을 맞추었을 때, 즉 display에 더 이상 '_'가 없을때 반복문이 멈추도록 작성할겁니다. 반복문 종료 후 print('정답입니다!!') 출력

# def check_():
#     if '_' in display:
#         return True
#     return False

while '_' in display:
    print(' '.join(display))
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for index in range(len(chosen_word)):
        alp = chosen_word[index]
        if guess == alp:
            display[index] = alp

    # if guess in chosen_word:
    #     print('정답!')
    # else:
    #     print('오답')
    #     chance -= 1

#todo - 4 : 정답을 보여줄 때 apple 이라면 a p p l e 로 출력될 수 있도록 .join() 메서드를 활용
print('\n정답입니다 !!')
print(' '.join(display))









