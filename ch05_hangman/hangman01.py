import random
# word_list 내부의 element중 하나를 임의로 선택하기 위해 random 모듈 도입
# numbers = [ 1, 2, 3, 4, 5 ]
# chosen_number = random.choice(numbers)
# print(chosen_number)

word_list = ['apple', 'banana', 'camel']
#todo -1 : world_list 에서 단어 하나를 임의적으로 선택하도록 random 모듈을 사용하고, 해당 단어를 chosen_word 변수에 담으시오.
chosen_word = random.choice(word_list)
print(chosen_word)

#todo -2 : 사용자에게 알파벳을 하나 추측해서 입력하라고 요청하고, 이를 guess 변수에 담으시오. 그리고 대문자로 시작하는 경우를 방지하기 위해 input() 함수 뒤에 .lower()를 적용하시오
guess = input('알파벳을 하나 입력하세요 >>> ').lower()

#todo -3 : guess에서 입력한 문자 하나가 chosen_word의 string 문자열 중에 하나의 문자와 일치하는지를 반복문을 통해 확인할 수 있도록 프로그램을 작성하시오. 맞으면 정답, 틀리면 오답이라고 출력될 수 있도록 할 것.
for alp in chosen_word:
    if guess == alp:
        print('정답')
    else:
        print('오답')



















