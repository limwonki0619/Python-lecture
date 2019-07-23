# 29.4 심사문제 : 사칙 연산 함수 만들기

# 표준 입력으로 숫자 두 개가 입력됩니다.
# 다음 소스 코드를 완성하여 두 숫자의 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가
# 출력되게 만드세요. 이때 나눗셈의 결과는 실수라야 합니다.

x, y = map(int, input().split())

def calc(x, y):
    return x + y, x - y, x * y, float(x / y)

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))