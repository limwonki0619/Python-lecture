# Unit 21. 터틀 그래픽스로 그림 그리기

import turtle as t
t.shape('turtle')
t.forward(100)

# 거북이 움직이기 ..

# 연습문제 오각별 그리기
import turtle as t

n = 5
t.shape('turtle')

for i in range(n):
    t.forward(100)
    t.right((360 / n) * 2)
    t.forward(100)
    t.left(360 / n)


# 21. 2 심사문제 ----------------------------------------------------------

# 표준 입력으로 꼭지점 개수(정수)와 선의 길이(정수)가 입력됩니다
# (꼭지점 개수의 입력 범위는 5~10, 선의 길이 입력 범위는 50~150입니다).
# 다음 소스 코드를 완성하여 꼭지점 개수와 선의 길이에 맞는 별이 그려지게 만드세요.
# 별을 그릴 때는 현재 위치부터 오른쪽으로 이동해서 시작해야 하며
# 시계 방향으로 그려야 합니다.

import turtle as t

n, line = map(int, input().split())
t.shape('turtle')
for i in range(n):
    t.forward(line)
    t.right((360 / n) * 2)
    t.forward(line)
    t.left(360 / n)
