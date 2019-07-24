# Unit 31. 함수에서 재귀호출 사용하기

# 함수 안에서 함수 자기자신을 호출하는 방식을 재귀호출(recursive call)이라고 합니다.
# 재귀호출은 일반적인 상황에서는 잘 사용하지 않지만 알고리즘을 구현할 때 매우 유용합니다.


# 31.1 재귀호출 사용하기

def hello():
    print('Hello, world')
    hello()

hello()

# 소스 코드를 실행해보면 'Hello, world!' 문자열이 계속 출력되다가 에러가 발생합니다.
# 왜냐하면 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000으로 정해져 있어서 그렇습니다.
# 즉, hello 함수가 자기자신을 계속 호출하다가 최대 재귀 깊이를 초과하면 RecursionError가 발생합니다.


# 31.1.1  재귀호출에 종료 조건 만들기

# 재귀호출을 사용하려면 반드시 다음과 같이 종료 조건을 만들어주어야 합니다.

def hello(count):
    if count == 0:
        return     # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄

    print('hello, world', count)

    count -= 1     # count를 1 감소시킨 뒤
    hello(count)   # # 다시 hello에 넣음

hello(10)  #  # hello 함수 호출



# 31.2 재귀호출로 팩토리얼 구하기 ------------------------------------------

def factorial(n):
    if n == 1:     # n이 1일 때
        return 1   # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)   # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함

print(factorial(5))



# 31.2.1 재귀호출로 등차수열 구하기
def ari_seq(n, d):
    if n == 1:
        return 1
    return ari_seq(n-1, d) + d

ari_seq(5, 3)


# + 재귀호출로 등비수열 구하기

def geo_seq(n, g):
    if n == 1:
        return 1
    return geo_seq(n-1, g) * g

geo_seq(6, 2)

# 1 2 4 8 16 32

# an = ar^(n-1)

