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