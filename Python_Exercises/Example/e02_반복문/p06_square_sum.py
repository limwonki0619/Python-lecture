


















# 모범답안 -------------------------------------------------
# 1부터 N까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이
n = int(input('자연수 입력> '))

sumOfSquare = 0
sum = 0
for i in range(1, n+1):
    sum += i
    sumOfSquare += i ** 2
squareOfSum = sum ** 2
print('합의 제곱 =', squareOfSum)
print('제곱의 합 =', sumOfSquare)
print('차이 =', squareOfSum - sumOfSquare)