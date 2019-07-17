# Unit 19. 계단식으로 별 출력하기

for i in range(1, 6):   # 바깥쪽 루프 : 세로
    for k in range(i):  # 안쪽 루프   : 가로
        print('*', end='')
    print()

# 19.1 중첩 루프 사용하기

for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
    for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
        print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
    print('i:', i, '\\n', sep='')    # i값 출력, 개행 문자 모양도 출력
                                     # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
                                     # (print는 기본적으로 출력 후 다음 줄로 넘어감)

# 19.2 사각형으로 별 출력하기
for i in range(5):
    for k in range(5):
        print("*", end='')
    print()


# 19.3 계단식으로 별 출력하기
for i in range(6):            # *
    for k in range(i):        # **
        print(i, end='')      # ***
    print()                   # ****
                              # *****

for i in range(6):
    for m in range(i, 6):
        print(' ', end='')
    for k in range(i):
        print(i, end='')
    print()


# 19.5 연습문제 -------------------------------------------------------------

# 연습 1 : 대각선으로 별 출력하기
for i in range(6):
    for k in range(i):
        print(" ", end='')
    print("*")

# 연습 2 : 반대 대각선으로 별 출력하기
for i in range(6):            # 내 프로그램
    for k in range(i, 6):
        print(" ", end='')
    print("*")

for i in reversed(range(6)):  # 교수님 프로그램
    for k in range(i):
        print(' ', end='')
    print('*')

# 연습 3 : bubble sort

aList = [5, 4, 21, 3, 15, 2 ,95 ,11, 43, 76]
aList = list(map(int, input().split()))

for i in range(0, len(aList)-1):  # 오름차순 정렬
    for k in range(i+1, len(aList)):
        if aList[i] > aList[k]:
            aList[i], aList[k] = aList[k], aList[i]
print(aList)

for i in range(0, len(aList)-1):  # 내림차순 정렬
    for k in range(i+1, len(aList)):
        if aList[i] < aList[k]:
            aList[i], aList[k] = aList[k], aList[i]
print(aList)

# 연습문제 4 : 역삼각형 모양으로 별 출력하기
for i in range(5):  # 내 방법
    for k in range(i):
        print(' ', end='')
    for m in range(i, 5):
        print('*', end='')
    print()

for i in range(5):  # 교과서
    for k in range(5):
        if k < i:
            print(' ', end='')
        else:
            print('*', end='')
    print()


# 심사문제 : 산 출력하기

# 표준 입력으로 삼각형의 높이가 입력됩니다.
# 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 이때 출력 결과는 예제와 정확히 일치해야 합니다.
# 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.

step = int(input())

for i in range(step):  # 내가 작성한 코드.. 심사는 통과하지 못함.. 왜 ??????????
    for k in range(i, step):
        print(' ', end='')
    for m in range((i*2)+1):
        print('*', end='')
    print()

# 교과서 코드
height = int(input())

for i in range(height):
    for j in reversed(range(height)):
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(height):
        if j < i:
            print('*', end='')
    print()
