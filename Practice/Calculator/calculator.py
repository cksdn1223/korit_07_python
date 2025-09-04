
numbers = []

str = ''
number = input('입력하고 엔터 (+-*/) > ')

for num in number:
    if num.isdigit():
        str += num
    else:
        numbers.append(str)
        numbers.append(num)
        str = ''
numbers.append(str)

num = int(numbers[0])
for index,i in enumerate(numbers):
    if i not in '0123456789':
        if numbers[index + 1] not in '0123456789':
            print(numbers[index-1])
            print('올바르지 않은 입력값 입니다.')
            break
        elif i == '+':
            num += int(numbers[index+1])
        elif i == '-':
            num -= int(numbers[index+1])
        elif i == '*':
            num *= int(numbers[index+1])
        elif i == '/':
            num /= int(numbers[index+1])

print(num)