# 20.1 1부터 100까지 숫자 출력하기

# FizzBuzz는 매우 간단한 프로그래밍 문제이며 규칙은 다음과 같습니다.
#
# 1에서 100까지 출력
# 3의 배수는 Fizz 출력
# 5의 배수는 Buzz 출력
# 3과 5의 공배수는 FizzBuzz 출력

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 코드 단축하기 ***
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리
    # 'Fizz' * True


# 20.7 연습문제 : 2와 11의 배수, 공배수 처리하기 -------------------------------------------

for i in range(1, 101):
    if i % 22 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)

# 코드 단순화
for i in range(1, 101):
    print('Fizz' * (i & 2 == 0) + 'Buzz' * (i % 11 == 0) or i)



# 심사문제

# 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 1~1000, 두 번째 입력 값의 범위는 10~1000이며
# 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다).
# 첫 번째 정수부터 두 번째 정수까지 숫자를 출력하면서
# 5의 배수일 때는 'Fizz', 7의 배수일 때는 'Buzz',
# 5와 7의 공배수일 때는 'FizzBuzz'를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).

start, stop = map(int, input().split())

for i in range(start, stop+1):
    if i % 35 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 ==0:
        print('Buzz')
    else:
        print(i)

# 코드 단순화

for i in range(start, stop+1):
    print('Fizz' * (i % 5 == 0) + 'Buzz' * (i % 7 == 0) or i)
