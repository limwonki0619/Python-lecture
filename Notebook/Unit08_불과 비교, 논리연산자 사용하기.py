# Unit 8. 불과 비교, 논리 연산자 알아보기

# 이번에는 참(True), 거짓(False)을 나타내는 불(boolean)을 알아보겠습니다.
# 그리고 두 값의 관계를 판단하는 비교 연산자와 두 값의 논릿값을 판단하는 논리 연산자도 함께 알아보겠습니다.
# 여기서 비교, 논리 연산자는 프로그래밍에서 매우 광범위하게 쓰입니다.
# 특히 앞으로 배울 if, while 구문을 작성할 때 비교, 논리 연산자를 자주 사용합니다.


# 8.1 불과 비교 연산자 사용하기 -----------------------------------------------------------------------------
# 불은 True, False로 표현하며 1, 3.6, 'Python'처럼 값의 일종입니다.
print(True)
print(False)


# 8.1.1 비교 연산자의 판단 결과

# 파이썬에서는 비교 연산자와 논리 연산자의 판단 결과로
# True, False를 사용합니다.
# 즉, 비교 결과가 맞으면 True, 아니면 False입니다.


# 8.1.2 숫자가 같은지 다른지 비교하기

# 이제 두 숫자가 같은지 또는 다른지 비교해보겠습니다.
# 두 숫자가 같은지 비교할 때는 ==(equal), 다른지 비교할 때는 !=(not equal)을 사용합니다.

print(10 == 10)
print(10 != 5)


# 8.1.3 문자열이 같은지 다른지 비교하기

print('Python' == 'python')
print('Python' != 'python')
print('Python' == 'Python')

# 숫자뿐만 아니라 문자열도 ==와 != 연산자로 비교할 수 있습니다.
# 이때 문자열은 비교할 때 대소문자를 구분합니다. ***
# 다음과 같이 단어가 같아도 대소문자가 다르면 다른 문자열로 판단합니다.


# 8.1.4 부등호 사용하기

print(10 > 20)    # 10이 20보다 큰지 비교
print(10 < 20)    # 10이 20보다 작은지 비교
print(10 >= 1)    # 10이 10보다 크거나 같은지 비교
print(10 <= 1)    # 10이 10보다 작거나 같은지 비교

# 여기서 비교 기준은 첫 번째 값입니다.
# 따라서 첫 번째 값보다 큰지, 작은지처럼 읽습니다. 항상 이점을 기억해두세요.



# 8.1.5 객체가 같은지 다른지 비교하기 : is, not is

print(1 == 1.0)
print(1 is 1.0)
print(1 is not 1.0)

# 1과 1.0은 정수와 실수라는 차이점이 있지만 값은 같습니다.
# 따라서 ==로 비교해보면 True가 나옵니다.
# 하지만 1과 1.0을 is로 비교해보면 False가 나옵니다.
#
# 왜냐하면 1은 정수 객체, 1.0은 실수 객체이므로 두 객체는 서로 다르기 때문입니다.
# 물론 1과 1.0을 is not으로 비교하면 True가 나오겠죠?



# 참고 : 정수 객체와 실수 객체가 서로 다른 것은 어떻게 확인하나요?

# 정수 객체와 실수 객체가 서로 다른지 확인하려면 id 함수를 사용하면 됩니다.
# id는 객체의 고유한 값(메모리 주소)을 구합니다
# (이 값은 파이썬을 실행하는 동안에는 계속 유지되며
# 다시 실행하면 달라집니다).

print(id(1))
print(id(1.0))

# 두 객체의 고유한 값이 다르므로 서로 다른 객체입니다.
# 그래서 1과 1.0을 is로 비교하면 False가 나옵니다.
# is, is not은 클래스로 객체를 만든 뒤에 객체가 서로 같은지 비교할 때 주로 사용합니다.
# 여기에 나오는 객체의 고유한 값(메모리 주소)에 대해서는 신경 쓸 필요 없습니다.
# ==, !=와 is, is not의 동작 방식이 다르다는 정도만 알아 두면 됩니다.


# 참고 : 값 비교에 is를 쓰지 않기



# 8.2 논리 연산자 사용하기  -------------------------------------------------------------

# 이번에는 논리 연산자를 사용해보겠습니다.
# 논리 연산자는 and, or, not이 있는데 먼저 and입니다.

# * a and b

print(True and True)
print(True and False)
print(False and True)
print(False and True)

# and는 두 값이 모두 True라야 True입니다.
# 하나라도 False이면 False가 나옵니다.


# 이번에는 or입니다.
# * a or b

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# or는 두 값 중 하나라도 True이면 True입니다.
# 두 값이 모두 False라야 False가 되죠.


# 마지막으로 not입니다.
# * not x

print(not True)
print(not False)

# not은 논릿값을 뒤집습니다.
# 그래서 not True는 False가 되고, not False는 True가 됩니다.

print(not True and False or not False)
# print((not True) and False or (not False))
# 여기서 and, or, not 논리 연산자가 식 하나에 들어있으면 not, and, or 순으로 판단합니다.


# 8.2.1 논리 연산자와 비교 연산자를 함께 사용하기

#  조금 응용해서 논리 연산자와 비교 연산자를 함께 사용해보겠습니다.

print(10 == 10 and 10 != 5)
print(10 > 5 or 10 < 3)
print(not 10 > 5)
print(not 1 is 1.0)

# 비교 연산자로 비교한 결과를 논리 연산자로 다시 판단했습니다.
# 이때는 1. 비교 연산자(is, is not, ==, !=, <, >, <=, >=)를 먼저 판단하고
# 2. 논리 연산자(not, and, or)를 판단하게 됩니다



# *** 참고 : 정수, 실수, 문자열을 불로 만들기

# 정수, 실수, 문자열을 불로 만들 때는 bool을 사용하면 됩니다.
# 이때 정수 1은 True, 0은 False입니다.

# 만약 문자열의 내용이 'False'라도 불로 만들면 True입니다.
# 문자열의 내용 자체는 판단하지 않으며 값이 있으면 True입니다.

# 즉, 정수 0, 실수 0.0이외의 모든 숫자는 True입니다.
# 그리고 빈 문자열 '', ""를 제외한 모든 문자열은 True입니다.

bool(0.0)
print(bool(0) == False)
print(bool(0) is False)


# *** 참고 : 단락 평가

# 논리 연산에서 중요한 부분이 단락 평가(short-circuit evalution)입니다.
# 단락 평가는 첫 번째 값만으로 결과가 확실할 때
# 두 번째 값은 확인(평가)하지 않는 방법을 말합니다.



# 즉, and 연산자는 두 값이 모두 참이라야 참이므로 첫 번째 값이 거짓이면
# 두 번째 값은 확인하지 않고 바로 거짓으로 결정합니다.

# 첫 번째 값이 거짓이므로 두 번째 값은 확인하지 않고 거짓으로 결정
print(False and True)     # True
print(False and False)    # False

# or 연산자는 두 값 중 하나만 참이라도 참이므로 첫 번째 값이 참이면
# 두 번째 값은 확인하지 않고 바로 참으로 결정합니다.

# 첫 번째 값이 참이므로 두 번째 값은 확인하지 않고 참으로 결정
print(True or True)     # True
print(True or False)    # True


# 특히 파이썬에서 논리 연산자는 이 단락 평가에 따라 반환하는 값이 결정됩니다.
# True, False를 논리 연산자로 확인하면 True, False가 나왔는데,
# True and 'Python'의 결과는 무엇이 나올까요?

print(True and 'Python')
print(True and bool('Python'))

# 문자열 'Python'도 불로 따지면 True라서 True and True가 되어
# True가 나올 것 같지만 'Python'이 나왔습니다.
#
# 왜냐하면 파이썬에서 논리 연산자는
# 마지막으로 단락 평가를 실시한 값을 그대로 반환하기 때문입니다.
# 따라서 논리 연산자는 무조건 불을 반환하지 않습니다.


print('Python' and True)
print('Python' and False)

# 여기서는 문자열 'Python'을 True로 쳐서 and 연산자가 두 번째 값까지 확인하므로
# 두 번째 값이 반환됩니다.

# 만약 다음과 같이 and 연산자 앞에 False나 False로 치는 값이 와서
# 첫 번째 값 만으로 결과가 결정나는 경우에는 첫 번째 값이 반환됩니다.
print(False and 'Python')
print(0 and 'Python')

# or 연산자도 마찬가지로 마지막으로 단락 평가를 실시한 값이 반환됩니다.
# 다음은 or 연산자에서 첫 번째 값만으로 결과가 결정되므로 첫 번째 값이 반환됩니다.

print(True or 'Python')
print('Python' or True)

# 만약 두 번째 값까지 판단해야 한다면 두 번째 값이 반환됩니다.

print(False or 'Python')
print(0 or False)

