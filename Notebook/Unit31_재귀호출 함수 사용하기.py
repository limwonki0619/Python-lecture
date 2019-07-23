# Unit 31. 함수에서 재귀호출 사용하기

# 함수 안에서 함수 자기자신을 호출하는 방식을 재귀호출(recursive call)이라고 합니다.
# 재귀호출은 일반적인 상황에서는 잘 사용하지 않지만 알고리즘을 구현할 때 매우 유용합니다

# 31.1 재귀호출 사용하기

def hello():
    print('Hello, world!')
    hello()

hello()

# 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000으로 정해져 있어서
# hello 함수가 자기자신을 계속 호출하다가 최대 재귀 깊이를 초과하면
# RecursionError가 발생합니다.


# 31.1.1  재귀호출에 종료 조건 만들기

# 재귀호출을 사용하려면 반드시 다음과 같이 종료 조건을 만들어주어야 합니다.

def hello(count):
    if count == 0:
        return
    print('hello world', count)

    count -= 1
    hello(count)

hello(5)


# 31.2 재귀호출로 팩토리얼 구하기

def factorial(n):
    if n == 1:     # n이 1일 때
        return  1  # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)

print(factorial(5))

# factorial 함수의 핵심은 반환값 부분입니다.
# 계산 결과가 즉시 구해지는 것이 아니라 재귀호출로 n - 1을 계속 전달하다가
# n이 1일 때 비로소 1을 반환하면서 n과 곱하고 다시 결괏값을 반환합니다.
# 그 뒤 n과 반환된 결괏값을 곱하여 다시 반환하는 과정을 반복합니다.

# factorial(5)를 호출해서 n이 1이 될 때까지 재귀호출하면 다음과 같은 모양이 됩니다.

# 이제 if n == 1:을 만나서 factorial 함수가 1을 반환합니다.
# 그 뒤 1과 2를 곱해서 2를 반환하고,
# 3과 2를 곱해서 6을 반환하고, 4와 6을 곱해서 24를 반환하고,
# 5와 24를 곱해서 120을 반환하게 됩니다.


# 31.4 연습문제 : 재귀호출로 회문 판별하기

def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print(is_palindrome('level'))


# 31.5 심사문제 : 재귀호출로 피보나치 수 구하기

# 표준 입력으로 정수 한 개가 입력됩니다(입력 값의 범위는 10~30).
# 다음 소스 코드를 완성하여 입력된 정수에 해당하는 피보나치 수가 출력되게 만드세요.
# 피보나치 수는 0과 1로 시작하며, 다음 번 피보나치 수는 바로 앞의 두 피보나치 수의 합입니다.

n = int(input())

def fib(n):
    if n < 3:
        return 1
    else:
       return fib(n-2) + fib(n-1)

print(fib(5))

# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)





