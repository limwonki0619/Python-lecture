# Unit 18. break, continue로 반복문 제어하기

# break : 제어흐름 중단
# continue : 제어흐름 유지, 코드 실행만 건너뜀

# 18.1 break로 반복문 끝내기 --------------------------------------------

# 18.1.1 while에서 break로 반복문 끝내기

i = 0
while True:  # 무한루프
    print(i)
    i += 1        # i를 1씩 증가시킴
    if i == 100:  # i가 100일 때
        break     # 반복문을 끝냄, while의 제어흐름을 벗어남

# 18.1.2 for에서 break로 반복문 끝내기

for i in range(10000):  # 0부터 9999까지 반복
    print(i)
    if i == 100:
        break

# 주사위 2개 던저셔 눈금의 합이 10이상이면 탈출하는 코드 작성해보기

import random as rd

one = 0
two = 0
i = 0

while True:
    one = rd.randint(1, 6)
    two = rd.randint(1, 6)
    i += 1
    print(one, two)
    if one+two >= 10:
        break
print('주사위를 던진 횟수 = ',i)  # 루프를 빠져나옴

# 18.2 continue로 코드 실행 건너뛰기 ------------------------------------

# 18.2.1 for에서 continue로 코드 실행 건너뛰기

for i in range(100):  # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:    # i를 2로 나누어 나머지가 0이면 짝수일 때
        continue      # 아래 코드를 실행하지 않고 건너뜀
    print(i)

# 18.2.2 while 반복문에서 continue로 코드 실행 건너뛰기

i = 0
while i < 100:      # i가 100보다 작을 때 반복
    i += 1          # i를 1씩 증가시킴
    if i % 2 == 0:  # i를 2로 나누었을 때 나머지가 0이면 짝수
        continue    # 아래 코드를 실행하지 않고 건너뜀
    print(i)

# 참고 : 반복문과 pass

for i in range(10):  # 10번 반복
    pass             # 아무 일도 하지 않음

while True:          # 무한루프
    pass             # 아무 일도 하지 않음


# 연습문제 TODO
# 심사문제 TODO