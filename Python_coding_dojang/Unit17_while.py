# Unit 17. while 반복문으로 Hello, world! 100번 출력하기

i = 0
while i < 100:
    print('hello, world', i)
    i += 1
# 17.1 while 반복문 사용하기 ---------------------------------------------------------

# 17.1.1 초깃값을 1부터 시작하기

i = 1
while i <= 100:
    print(i)
    i += 1

# 17.1.2 초깃값을 감소시키기
i = 100
while i > 0:
    print(i)
    i -= 1

# 17.1.3 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while i < count:
    print(i)
    i += 1

count = int(input('반복할 횟수를 입력하세요: '))

while count > 0:
    print(count)
    count -= 1


# 17.2 반복 횟수가 정해지지 않은 경우 ---------------------------------------

import random as rd  # random 모듈을 가져와 rd라는 이름으로 사용

rd.random()
rd.randint(1, 6)  # 1 ~ 6사이의 정수를 출력합니다.

i = 0
while i != 3:  # 3이 아닐 때 계속 반복한다.
    i = rd.randint(1, 6)  # randint를 사용하요 1과 6사이의 난수 생성 (정수)
    print(i)


# 참고 : random.choice 함수를 사용하면 시퀀스 객체에서 요소를 무작위로 선택할 수 있다.
dice = [1, 2, 3, 4 ,5 ,6]
rd.choice(dice)  # random.choice 함수는 시퀀스 객체를 받으므로 리스트뿐만 아니라 튜플, range, 문자열 등을 넣어도 된다.



# 17.3 while 반복문으로 무한 루프 만들기 -------------------------------------

while True:  # while에 True를 지정하면 무한루프, True 대신 True로 취급하는 값을 사용해도 동작한다.
    print('hello world')


# 17.5 연습문제 -------------------------------------------------------------

i = 2
j = 5

while i <= 32 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1

# 17.6 심사문제 ------------------------------------------------------------

# 표준 입력으로 금액(정수)이 입력됩니다.
# 1회당 요금은 1,350원이고, 교통카드를 사용했을 때마다의 잔액을 각 줄에
# 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 최초 금액은 출력하지 않아야 합니다. 그리고 잔액은 음수가 될 수 없으며
# 잔액이 부족하면 출력을 끝냅니다.

money = int(input())

# while money > 0:
#     money -= 1350
#     if money <= 0:
#         break
#     print(money)

while money >= 1350:
    money -= 1350
    print(money)
