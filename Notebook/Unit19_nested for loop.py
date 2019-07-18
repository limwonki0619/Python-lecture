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
        print(i, end='')    # ***
    print()                   # ****
                              # *****

for i in range(6):
    for m in range(i, 6):
        print(' ', end='')
    for k in range(i):
        print(i, end='')
    print()




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