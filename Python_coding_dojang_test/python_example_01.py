# 파이썬 연습문제


# 1. 조건문 ---------------------------------------------------------------------------------------------------

# 1.1 연도를 입력으로 받아 윤년인지 아닌지를 출력하는 프로그램을 작성하시오. ----------------------------------

# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때
# 또는 400의 배수일 때이다. 예를들어, 2012년은 4의 배수라서 윤년이지만,
# 1900년은 4의 배수이지만, 100의 배수이기 때문에 윤년이 아니다.
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.)

# 4의 배수이면서 100의 배수가 아니고, 400의 배수일 때 윤년이다.

# 윤년 : 4의 배수이지만 100의 배수는 아니며, 400의 배수인 해
# 평년 : not 윤년

years = list(range(1900, 2013, 1))

for year in years:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, '윤년')
    else:
        print(year, '평년')

# 1900년도 일때,
print(1900 % 4 == 0)    # T 4의 배수다.
print(1900 % 100 != 0)  # F 100의 배수다. -> 평년
print(1900 % 400 == 0)  # F 400의 배수가 아니다. -> 평년


# 1.2  상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, -----------------------------
# 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
# 상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
# 이런 상근이를 불쌍하게 보던, 창영이는 자신이 사용하는 방법을 추천해 주었다.
# 바로 "45분 일찍 알람 맞추기"이다. 이 방법은 단순하다.
# 원래 맞춰져 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다.
# 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다.
# 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
# 현재 상근이가 맞춰논 알람 시각을 입력으로 받아(시와 분) 창영이의 방법을 사용한다면,
# 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

def alarm():
    hour, minute = map(int, input().split())
    if minute > 45:
        minute -= 45
        print(hour,'시', minute,'분')
    else:
        hour -= 1
        minute -= 45
        print(hour,'시', abs(minute),'분')

alarm()


# 1.3 세 정수 a, b, c를 입력으로 받아 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. -----------------------------

def order():
    aList = list(map(int, input().split()))
    for i in range(0, len(aList)-1):
        for k in range(i+1, len(aList)):
            if aList[i] > aList[k]:
                aList[i], aList[k] = aList[k], aList[i]
    print(aList[1])

order()

# 정렬 알고리즘 http://ejklike.github.io/2017/03/04/sorting-algorithms-with-python.html


# 1.4 세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부른다.
# (여기서 a < b < c 이고 a + b > c)
# 예를 들면, 32 + 42 = 9 + 16 = 25 = 52 이므로 3, 4, 5는 피타고라스 수다.
# a + b + c = 1000 인 피타고라스 수를 구하시오. (답은 한가지 뿐이다.)

# a^2 + b^2 = c^2
# c = (1000 - a - b)

# 코드출처 : https://www.opentutorials.org/module/2980/17440
for a in range(1, 1000):    # a에 들어갈 수 있는 수를 모두 뽑는다.
    for b in range(1, a):   # 뽑은 a의 범위에서 조합가능한 모든 b를 뽑는다.
        if a**2 + b**2 == (1000 - a - b)**2:  # a^2 + b^2 == c^2이 되는 값을 구한다.
            print('a =',a , 'b =', b, 'c =', 1000 - a - b)  # 조건이 만족하는 a와 b와 c를 출력한다.
            print(a**2, '+', b**2, '=', (1000 - a - b)**2)
            break                                           # 조건이 만족되면 루프를 빠져나온다.


# 2. 반복문 ------------------------------------------------------------------------------------

# 2.1 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. ---------------------

# 입력: 첫째 줄에 테스트 케이스의 개수 T를 입력받는다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.
# (0 < A, B < 10)
#
# 출력: 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.
# x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.


# 2.2 5이상 9이하의 홀수를 입력받아 다이아몬드 형태의 별을 출력하는 프로그램을 작성하시오.

N = int(input())

if 5 <= N <= 9 and N % 2 == 1:
    for i in range(N-3):
        for top_b in range(i, 4):
            print(' ', end='')
        for top_s in range((i*2)+1):
            print('*', end='')
        print()

while True:
    for i in range(3):
        print(i)
    break
