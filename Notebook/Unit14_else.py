# Unit 14. else를 사용하여 두 방향으로 분기하기

# if 광고 전화인가?:
#    전화를 끊고, 차단 목록에 등록한다.
# else:
#   계속 통화한다.

# 14.1 else 사용하기 -----------------------------------------------------------------
# else는 if 조건문 뒤에 오며 단독으로 사용할 수 없습니다.
# 그리고 if와 마찬가지로 else도 :(콜론)을 붙이며 다음 줄에 실행할 코드가 옵니다.

# if 조건식:
#      코드1
# else:
#      코드2

x = 5

if x == 10:  # if와 else는 같은 위치에 있다.
    print('10입니다.')
else:
    print('10이 아닙니다.')

# 참고 : 변수에 값 할당을 if, else로 축약하기
# print('10입니다.') if x == 10: else print('10이 아닙니다.') print는 축약 불가

x = 5

if x == 10:
    y = x
else:
    y = 0
    print(y)

# 위 코드를 축약 하면 아래와 같다.
# 이런 문법을 조건부 표현식(conditional expression)이라고 한다.
y = x if x == 10 else 0


# 14.2 else와 들여쓰기 ------------------------------------------------------

x = 5

if x == 10:
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')  # 인덴테이션 중요 ***


# 14.3 if 조건문의 동작 방식 알아보기 ----------------------------------------
if True:
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')  # None은 거짓

# 실제 코드를 작성할 때 변수에 들어있는 값이나 함수의 결과가 None인 경우가 많으므로
# 이 부분은 꼭 기억해야 한다.

# 14.3.1 if 조건문에 숫자 지정하기
# 숫자는 정수(2진수, 10진수, 16진수), 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참입니다.
if 0:
    print('참')
else:
    print('거짓')

if 1:
    print('참')
else:
    print('거짓')

# 14.3.2 if 조건문에 문자열 지정하기
# 문자열은 내용이 있을 때 참, 빈 문자열은 거짓입니다.
if 'hello':
    print('참')
else:
    print('거짓')

if '':
    print('참')
else:
    print('거짓')

# 참고 : 0, None, 빈 문자열 ''을 not으로 뒤집으면 참(True)이 되므로 if를 동작시킬 수 있습니다.

# 참고 : True, False로 취급하는 것들 정리
# None
#
# False
#
# 0인 숫자들: 0, 0.0, 0j
#
# 비어 있는 문자열, 리스트, 튜플, 딕셔너리, 세트: '', "", [], (), {}, set()
# 클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때
# 앞에서 나열한 것들을 제외한 모든 요소들은 True로 취급합니다. 세트는 뒤에서 자세히 설명하겠습니다.


# 14.4 조건식을 여러 개 지정하기 -----------------------------------------------------------------
# 14.4.1 중첩 if 조건문과 논리 연산자

x = 10
y = 20

if x == 10 and y == 20:
    print('참')
else:
    print('거짓')

if 0 < x < 20:
    print('20보다 작은 양수 입니다.')


# 14.6 연습문제 : 합격여부 판단하기 -----------------------------------

written_test = 75
coding_test = True

if written_test >= 80 and coding_test == True:
    print('합격')
else:
    print('불합격')


# 14.7 심사문제 : 합격 여부 판단하기 -----------------------------------

kor, eng, mat, sci = map(int, input().split())

if 0 <= kor <= 100 and 0 <= eng <= 100 and 0 <= mat <= 100 and 0 <= sci <= 100:
    if (kor+eng+mat+sci)/4 >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

