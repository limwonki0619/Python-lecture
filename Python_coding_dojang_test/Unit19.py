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