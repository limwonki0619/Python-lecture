# Unit 29. 함수 사용하기

# 29.1 Hello, world! 출력 함수 만들기 ----------------------------------------

# 함수는 def에 함수 이름을 지정하고 ( )(괄호)와 :(콜론)을 붙인 뒤
# 다음 줄에 원하는 코드를 작성합니다(함수의 이름을 짓는 방법은 변수와 같습니다).
# 이때 코드는 반드시 들여쓰기를 해야 합니다
# (들여쓰기 규칙은 if, for, while과 같습니다).

# def 함수이름():
#      코드


# 29.1.1  함수 만들기

def hello():
    print('Hello, world!')

# 29.1.2  함수 호출하기

hello()

# 29.1.3  소스 파일에서 함수를 만들고 호출하기

# 29.1.5  함수 작성과 함수 호출 순서

# 함수를 만들고 호출할 때 주의할 점이 있는데,
# 바로 함수를 만들기 전에 함수를 먼저 호출하면 안 된다는 점입니다.
# 즉, 다음과 같이 함수를 먼저 호출한 뒤 함수를 만들 수는 없습니다.

hello()  # hello 함수를 만들기 전에 함수를 먼저 호출


def hello():  # hello 함수를 만듦
    print('Hello, world!')

# 참고 : 빈 함수 만들기

def hello():
    pass

hello()



# 29.2 덧셈 함수 만들기 ------------------------------------------------------

# def 함수이름(매개변수1, 매개변수2):
#     코드

def add(a, b):
    print(a + b)

add(10, 20)


# 참고 : 함수 독스트링 사용하기

# def 함수이름(매개변수):
#     """독스트링"""
#     코드


# def 함수이름(매개변수):
#     """
#     여러 줄로 된
#     독스트링
#     """
#     코드


def add(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    return a + b


x = add(10, 20)  # 함수를 호출해도 독스트링은 출력되지 않음
print(x)

print(add.__doc__)  # 함수의 __doc__로 독스트링 출력



# 29.3 함수의 결과를 반환하기 ------------------------------------------------

def add(a, b):
    return a + b

add(2, 3)


# return으로 함수 중간에서 빠져나오기

def not_ten(a):
    if a == 10:
        return
    print(a, '입니다.', sep='')

not_ten(10)  # 함수 중간에 바로 빠져나오는 기능

#  return은 함수 중간에서 빠져나올 때 자주 사용합니다.
#  보통은 if와 조합해서 특정 조건일 때 함수 중간에서 빠져나옵니다.

def mySum(n):
    sum = 0  # 함수 안에서 사용하는 변수는 지역변수다
    for i in range(n+1):
        sum += i
    return sum

mySum(20)

# ex) 성적을 입력받아 학점을 리턴하는 함수 만들어보기

def grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    else:
        return 'F'

grade(60)


# 29.4 함수에서 값을 여러 개 반환하기 ------------------------------------------------------------------

def one_two():
    return [1, 2]

x, y = one_two()
print(x, y)


