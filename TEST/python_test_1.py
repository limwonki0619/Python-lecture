
# 문제 3

# 두 개의 정수를 입력받아 작은 수에서부터 큰 수까지 홀수의 합을 구해서 출력하는 프로그램을 for문을 사용하여 작성하라.

start, end = map(int, input().split())

sum = 0
for i in range(start, end+1):
    if i % 2 == 1:
        sum += i
print(sum)


# 문제 4 : 연 복리 이자율을 입력받아 원금이 2배가 되는데 최소 몇년이 걸리는지 알아보는 프로그램을 while loop를 사용하여 작성하라.

# 복리를 구하는 식
# = PV *(1+R)^N
# 여기서 PV는 현재 값이고, R은 이율이며 N 은 투자 기간의 길이입니다.

r = int(input('연복리이자율 : '))
n = 0
pv = 10000000

while True > 0:
    n += 1
    if  pv * ((1 + r/100) ** n) >= pv * 2:
        print('원금 {0:,}을 연 복리 {1}%로 운용할 경우 원금의 두배가 되기까지 약 {2}년이 걸린다.'.format(pv, r, n))
        break

# 72의 법칙으로 확인
print(72 / 15)


# 문제 5 : bts 리스트가 주어졌을 때 아래와 같은 답이 나오도록 print문을 작성하시오

bts = ['RM', '진', '슈가', '제이홉', '지민', '뷔', '정국']

# 5.1)
print(bts[-2])

# 5.2)
print(bts[:1])

# 5.3)
print(bts[-2:])

# 5.4)
print(bts[2:5])

# 5.5)
print(bts[::2])


# 문제 6 : 다음과 같은 딕셔너리 vegetables가 주어졌을 때 아래 그림과 같이 가격이 높은 것부터 내림차순으로 출력하는 프로그램을
#          작성하되, 가격은 길이를 7로 만들고 1000단위 ,를 찍은 뒤 우측정렬 하시오.
import operator

vegetables = dict(zip(['가지', '오이' ,'수박', '호박', '깻잎'], [800, 600, 15000, 1000, 500]))
sort_veg = sorted(vegetables.items(), key=operator.itemgetter(1), reverse=True)

for veg, price in sort_veg:
    print(veg, '{0:>7,}'.format(price))


# 문제 7 : 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수라고 부른다.
#          두 자리수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 이다.
#          세 자리수 x, y(단 x <= y)를 곱해 만들 수 있는 가장 큰 대칭수는 얼마이고 그때 x,y값은 얼마인가?

maxNum = 0
for i in range(100, 1000):
    for k in range(i, 1000):
        value = i * k
        if str(value) == str(value)[::-1]:
            if i <= k and i*k > maxNum:
                maxNum = i*k
                maxA = i
                maxB = k

print('세 자리 수 Palindrome 중 (x <= y)이 만족하는 가장 큰 수는 : {0} x {1} = {2}'.format(maxA, maxB, maxNum))

# 문제 8 : 다음의 규칙대로 동작하는 프로그램을 만드시오.
#          - 타일판은 5 x 5
#          - 타일 종류는 1 ~ 4의 네가지로 랜덤값으로 정한 후 타일판 출력
#          - 가로나 세로로 3개 이상 같은 타일이 연속될 경우 타일을 '*'로 바꾸고 타일판 출력

import random

pan = []
for r in range(5):
    line = []
    for c in range(5):
        ranNum = random.randint(1, 5)
        line.append(ranNum)
    pan.append(line)

    # 오답
    # for i in range(r-2, r+3):
    #     for k in range(c-2, c+3):
    #
    #         if i < 0 or k < 0 or i >= 5 or k >= 5:
    #             continue
    #         elif pan[i][k] == pan[r][c]:
    #             pan[r][c] == '*'
    #         else:
    #             continue

# for r in range(row): # row : 0 1 2
#     for c in range(col): # col : 0 1 2
#
#         if matrix[r][c] != '*':
#             matrix[r][c] = 0  # *가 아닌자리를 숫자 0으로 변경
#
#             # matrix[-1][-1] | matrix[-1][0] matrix[-1][1] matrix[-1][2] | matrix[-1][3]
#             # ---------------|-------------------------------------------|---------------
#             # matrix[0][-1]  | matrix[0][0]  matrix[0][1]  matrix[0][2]  | matrix[-1][3]
#             # matrix[1][-1]  | matrix[1][0]  matrix[1][1]  matrix[1][2]  | matrix[-1][3]
#             # matrix[2][-1]  | matrix[2][0]  matrix[2][1]  matrix[2][2]  | matrix[-1][3]
#             # ---------------|-------------------------------------------|---------------
#             # matrix[3][-1]  | matrix[3][0]  matrix[3][1]  matrix[3][2]  | matrix[3][3]
#
#             # 검사할 영역
#
#             for i in range(r-1, r+2):      # -1 0 1, 3칸씩 검사
#                 for k in range(c-1, c+2):  # -1 0 1, 3칸씩 검사
#
#                     if i < 0 or k < 0 or i >= row or k >= col:  # 바깥쪽 영역 무시
#                         continue
#                     elif matrix[r][c] == '*':  # 영역 내 별표 무시
#                         continue
#                     elif matrix[i][k] == '*':  # 주위에 *가 있을 경우
#                         matrix[r][c] += 1      # 해당 자리에 + 1을 해준 후 다시 할당

# 문제 9 : 다음과 같은 리스트 a가 주어졌을 때 a의 각 원소를 제곱한 값을 원소로 갖는 리스트 b를 람다표현식을 사용하여 구하시오.

a = list(range(1, 10, 2))

b = list(map(lambda x: x**2, a))
print(b)
