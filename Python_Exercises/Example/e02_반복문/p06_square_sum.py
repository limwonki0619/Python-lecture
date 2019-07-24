# 1부터 N까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이

def Square_sum(n):

    square_sum = 0
    sum = 0

    for i in range(1, n+1):
        sum += i             # 합
        square_sum += i ** 2 # 제곱의 함

    sum_square = sum ** 2    # 합의 제곱
    dif = sum_square - square_sum

    print('합의 제곱 = {0}\n'
          '제곱의 합 = {1}\n'
          '합의 제곱 - 제곱의 합 = {2}'.format(sum_square, square_sum, dif))

Square_sum(5)

