import random

word_list = [ 'apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 1 : 비어있는 list인 display를 만드시오.
display = []
#todo - 2 : 이상의 코드 라인을 참조하여 chosen_word 의 각 문자 개수마다 '_' 를 추가하시오. 예를 들어 chosen_word == 'apple' 이라면 display = [ '_','_','_','_','_' ] 이 되어야 합니다. chosen_word의 문자 개수만큼 '_' 필요
for _ in range(len(chosen_word)):
    display.append('_')             # 반복실행문에서 변수 i 가 쓰이지 않아서 i와같은 특정변수를쓰기보다는 _ 를 써도 좋습니다.

#todo - 3 : chosen_word의 각 문자들을 반복시키시오. 만약 그 위치의 문자가 guess와 일치하면 해당 위치의 display에서 문자를 공개하시오. 예를 들어, 사용자가 'p' 를 입력했고, chosen_word가 apple 이라면 display = [ '_', 'p', 'p', '_', '_'] 로 바꿔야 합니다.
guess = input('알파벳을 하나 입력하세요 >>> ').lower()
# index = 0
# for alp in chosen_word:
#     if guess == alp:
#         display[index] = alp
#     index += 1

for index in range(len(chosen_word)):
    alp = chosen_word[index]
    if guess == alp:
        display[index] = alp

print(display)