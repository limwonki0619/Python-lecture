# 심사문제 지뢰찾기

# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다.
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다.
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤
# append로 각 줄을 추가하면 됩니다(list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).

row, col = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for r in range(row): # row : 0 1 2
    for c in range(col): # col : 0 1 2

        if matrix[r][c] != '*':
            matrix[r][c] = 0  # *가 아닌자리를 숫자 0으로 변경

            # matrix[-1][-1] | matrix[-1][0] matrix[-1][1] matrix[-1][2] | matrix[-1][3]
            # ---------------|-------------------------------------------|---------------
            # matrix[0][-1]  | matrix[0][0]  matrix[0][1]  matrix[0][2]  | matrix[-1][3]
            # matrix[1][-1]  | matrix[1][0]  matrix[1][1]  matrix[1][2]  | matrix[-1][3]
            # matrix[2][-1]  | matrix[2][0]  matrix[2][1]  matrix[2][2]  | matrix[-1][3]
            # ---------------|-------------------------------------------|---------------
            # matrix[3][-1]  | matrix[3][0]  matrix[3][1]  matrix[3][2]  | matrix[3][3]

            # 검사할 영역

            for i in range(r-1, r+2):      # -1 0 1, 3칸씩 검사
                for k in range(c-1, c+2):  # -1 0 1, 3칸씩 검사

                    if i < 0 or k < 0 or i >= row or k >= col:  # 바깥쪽 영역 무시
                        continue
                    elif matrix[r][c] == '*':  # 영역 내 별표 무시
                        continue
                    elif matrix[i][k] == '*':  # 주위에 *가 있을 경우
                        matrix[r][c] += 1      # 해당 자리에 + 1을 해준 후 다시 할당

for mat in matrix: # 전체 리스트에서 안쪽 리스트 하나씩 할당 [1, 2, 3]
    for clean in mat:  # 안쪽 리스트에서 값을 하나씩 받아 출력  1 -> 2 -> 3
        print(clean, end='')
    print()

