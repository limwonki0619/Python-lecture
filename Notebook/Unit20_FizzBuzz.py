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