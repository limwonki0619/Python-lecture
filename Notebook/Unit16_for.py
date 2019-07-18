# 16.1 for와 range 사용하기 ----------------------------------

for i in range(100):
    print('hello world')

# 16.1.1 반복문에서 변수의 변화 알아보기

for i in range(100):
    print('hello world', i)

# 16.2 for와 range 응용하기 -----------------------------------

# 16.2.1 시작하는 숫자와 끝나는 숫자 지정하기
for i in range(2, 5):
    print('hello world', i)

# 16.2.2 증가폭 사용하기
for i in range(0, 10, 2):
    print('hello world', i)


# 16.2.3 숫자를 감소시키기
for i in range(10, 0):  # range(10, 0)은 작동하지 않음
    print(i)            # 왜냐면 range는 숫자가 증가하는 기본 값이 양수 '1'이기 때문임

for i in range(10, 0, -2):
    print(i)

# for 변수 in reversed(range(횟수))
# for 변수 in reversed(range(시작, 끝))
# for 변수 in reversed(range(시작, 끝, 증가폭))
# reversed는 시퀀스 객체를 뒤집어 준다.

for i in reversed(range(0, 10)):
    print(i, end=' ')

# 16.2.4 입력한 횟수대로 반복하기

count = int(input('반복할 횟수를 입력하세요.'))

for i in range(count):
    print(i, end=' ')

# 16.3 시퀀스 객체로 반복하기 -----------------------------------------------

a = list(range(10, 60, 10))

for i in a:
    print(i, end=' ')

fruits = ('apple', 'orange', 'grape')

for fruit in fruits:
    print(fruit)

for letter in 'python':
    print(letter, end=' ')

for letter in reversed('Python'):
    print(letter, end=' ')

# 16.5 연습문제 : 리스트의 요소에 10을 곱해서 출력하기

x = [49, -17, 25, 102, 8, 62, 21]

for i in x:
    print(i * 10, end=' ')

# 16.6 심사문제 : 구구단 만들기

x = int(input())

for i in range(1, 10, 1):
    print(x, '*', i, '=', x*i)


lux = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))

for key in lux:
    print(key, '=', lux[key])


