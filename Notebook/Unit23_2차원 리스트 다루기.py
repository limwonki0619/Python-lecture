# Unit 23. 2차원 리스트 다루기

a = [[10, 20],  # 2차원 리스트 생성하기
     [30, 40],
     [50, 60]]

a[0][0]        # a[세로][가로]
a[1][0]
a[2][1] == 60  # 해당 위치의 값 변경하기

print(a)

for x, y in a:
    print(x, y)


# for 반복문으로 1차원 리스트 만들기

a = []
for i in range(10):
    a.append(0)
print(a)

# for 반복문으로 2차원 리스트 만들기

a = []                  # 전체 리스트
for i in range(4):      # 안쪽 리스트 갯수
    line = []
    for k in range(2):  # 요소 갯수
        line.append(0)
    a.append(line)
print(a)

# 리스트 표현식으로 2차원 리스트 만들기

a = [[0 for j in range(2)] for i in range(3)]
# 리스트 표현식 안에서 리스트 표현식을 사용했습니다.
# 먼저 [0 for j in range(2)]로 0을 2번 반복하여 [0, 0]으로 만들고
# 다시 for i in range(3)으로 [0, 0]을 3번 반복하여 [[0, 0], [0, 0], [0, 0]]으로 만듭니다.

a = [[0] * 2 for i in range(3)]  # 안쪽 리스트 크기(3) 리스트 안의 리스트 크기 (2)
print(a)

a = [[0] * i for i in [3, 1, 3, 2, 5]]  # 안쪽 리스트 크기 [3, 1 ~] 리스트 안의 리스트 크기 (3, 1~)
print(a)

students = [
    ['john', 'C', 19],
    ['maria', 'A', 25],
    ['andrew', 'B', 7]
]

print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬


# 2차원 리스트의 할당과 복사

a = [[i] * 2 for i in range(10, 30, 10)]

import copy             # copy 모듈을 가져옴
b = copy.deepcopy(a)    # copy.deepcopy 함수를 사용하여 깊은 복사
b[0][0] = 500
print(a, b)

a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1


# 23.6 연습문제 : 3차원 리스트 만들기 -----------------------------------------------

# 높이 2, 세로 4, 가로 3

a = [[i] * 2 for i in range(10, 30, 10)]
b = [[[0] * 3 for i in range(4)] for k in range(2)]  # 높이 --> 세로 --> 가로



# 23.7 심사문제 : 지뢰찾기 ----------------------------------------------------------

# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다.
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다.
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
#
# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서
# input을 호출한 뒤 append로 각 줄을 추가하면 됩니다
# (list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).

import random

col, row = map(int, input().split())

field = [[random.choice(['.','.','.', '*'])] * col for i in  range(row)]
