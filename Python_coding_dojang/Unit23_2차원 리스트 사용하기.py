# Unit 23. 2차원 리스트 사용하기

# 23.1 2차원 리스트를 만들고 요소에 접근하기 -------------------------------
a = [[10, 20], [30, 40], [50, 60]]
print(a)

a = [[10, 20],
     [30, 40],
     [50, 60]]
print(a)


# 23.1.1 2차원 리스트의 요소에 접근하기
# * 리스트[세로인덱스][세로인덱스]
# * 리스트[세로인덱스][세로인덱스] = 값

a = [[10, 20], [30, 40], [50, 60]]
print(a[0][1])


# 참고 | 톱니형 리스트
# 2차원 리스트 [[10, 20], [30, 40], [50, 60]]은 가로 크기가 일정한 사각형 리스트입니다.
# 특히 파이썬에서는 가로 크기가 불규칙한 톱니형 리스트(jagged list)도 만들 수 있습니다.

a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]

# 톱니형 리스트는 다음과 같이 append 메서드 등을 사용하여 동적으로 생성할 수도 있습니다.

a = []
a.append([])
a[0].append(10)
a[0].append(20)
a.append([])
a[1].append(500)
a[1].append(600)
a[1].append(700)

print(a)

# 사람이 보기 편하기 나타내기
from pprint import pprint
pprint(a, indent=4, width=20)


# 23.2 반복문으로 2차원 리스트의 요소를 모두 출력하기 ------------------------------

# 23.2.1 for 반복문을 한 번만 사용하기
a = [[10,20], [30,40], [50,60]]
for x, y in a:  # 리스트의 가로 한 줄(안쪽 리스트)에서 요소 두 개를 꺼냄
    print(x, y)

# 23.2.2 for 반복문을 두 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]

for i in a:        # a에서 안쪽 리스트를 꺼냄
    for k in i:    # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(k, end=' ')
    print()

# 23.2.3 for와 range 사용하기

a = [[10, 20], [30, 40], [50, 60]]

for i in range(len((a))):
    for k in range(len(a[i])):
        print(a[i][k], end=' ')
    print()




# 23.3 반복문으로 리스트 만들기

# 23.3.1 for반복문으로 1차원 리스트 만들기
a = []  # 빈리스트 생성
for i in range(10):
    a.append(1)  # append로 요소 값을 추가
print(a)


# 23.3.2 for 반복문으로 2차원 리스트 만들기
a = []

for i in range(3):
    line = []            # 안쪽 리스트로 사용할 빈 리스트 생성
    for k in range(2):
        line.append(0)   # 안쪽 리스트에 0추가
    a.append(line)       # 전체 리스트에 안쪽 리스트를 추가

print(a)


# 23.3.3 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)

a = [[0]*2 for i in range(3)]
print(a)

# 톱니형 리스트 만들기
a = [3, 1, 3, 2, 5]  # 가로 크기를 저장한 리스트
b = []

for i in a:              # 가로 크기를 저장한 리스트로 반복
    line = []            # 안쪽 리스트로 사용할 빈 리스트 생성
    for k in range(i):   # 리스트 a에 저장된 가로 크기만큼 반복
        line.append(0)
    b.append(line)       # 리스트 b에 안쪽 리스트를 추가

print(b)

a = [[0]*i for i in [3, 1, 3, 2, 5]]
print(a)


# 참고 : sorted로 2차원 리스트 정렬하기
# sorted(반복가능한 객체, key=정렬함수, reverse=True or False)
students = [
    ['john', 'C', 10],
    ['maria', 'A', 25],
    ['andrew', "B", 7]
]

print(sorted(students, key=lambda student: students[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students, key=lambda student: students[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬


# 23.4 2차원 리스트의 할당과 복사 알아보기
a = [[10, 20], [30, 40]]
b = a  # 같은 객체이므로 복사가 됨
b[0][0] = 500
print(a, b)

print(a[0][0] is b[0][0])
# copy 메서드를 사용해도 똑같음

# 2차원 이상의 다차원 리스트를 완전히 복사하려면 copy메서드 대신
# copy 모듈의 deepcopy 함수를 사용해야 한다.

import copy as cp

a = [[10, 20], [30, 40]]
b = cp.deepcopy(a)
b[0][0] = 500
print(a)
print(b)  # a와 b는 다른 객체

print(a[0][0] is b[0][0])

