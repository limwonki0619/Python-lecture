# 2.2 5이상 9이하의 홀수를 입력받아 다이아몬드 형태의 별을 출력하는 프로그램을 작성하시오.
def diamond():
    N = int(input('5 이상 9 이하의 홀수를 입력해 주세요.'))

    if 5 <= N <= 9 and N % 2 == 1:
        print('올바른 입력입니다.')
        for top in range((N//2)+1):  # 다이아몬드 중앙포함 위쪽 만들기
            for top_blank in range(top, 4):
                print(' ', end='')
            for top_star in range((top*2)+1):
                print('*', end='')
            print()
        for bot in reversed(range(N//2)):  # 아래쪽 만들기
            for bot_blank in range(bot, 4):
                print(' ', end='')
            for bot_star in range((bot*2)+1):
                print('*', end='')
            print()
    else:
        print('올바르지 않은 입력입니다. 다시 입력해 주세요.')

diamond()

#  i  빈칸수   *수
#  0  4(0:4)    1 (i*2)+1
#  1  3(1:4)    3 (i*2)+1
#  2  2         5
#  3  1         7

#  2  2(2:4)    5
#  1  3(1:4)    3
#  0  4(0:4)    1




# 모범답안 ----------------------------------------------------------------------------------------

# 5이상 9이하의 홀수를 입력받아 다이아몬드 형태의 별을 출력하는 프로그램
n = int(input('5이상 9이하의 홀수> '))
height = (n + 1) // 2

for i in range(1, height+1):
    for k in range(height-i):
        print(' ', end='')
    for k in range(i*2-1):
        print('*', end='')
    print()

for i in reversed(range(1, height)):
    for k in range(i, height):
        print(' ', end='')
    for k in range(i*2-1):
        print('*', end='')
    print()