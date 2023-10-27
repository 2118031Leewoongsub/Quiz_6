numbers = input('주민등록번호를 입력하세요: ')

if len(numbers) != 13 or not numbers.isdigit():
    print('주민등록번호는 13자리 숫자 입니다.')
else:
    number = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

    sum = sum(int(numbers[i]) * number[i] for i in range(12))
    x = (11 - (sum % 11)) % 10
    y = int(numbers[12])

    if x == y:
        print('유효합니다')
    else:
        print('유효하지 않습니다')

