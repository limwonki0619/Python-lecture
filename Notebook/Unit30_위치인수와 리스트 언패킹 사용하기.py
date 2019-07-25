# Unit 30. 함수에서 위치 인수와 키워드 인수 사용하기

# 이번에는 함수에서 위치 인수, 키워드 인수를 사용하는 방법과 리스트,
# 딕셔너리 언패킹(unpacking)을 활용하는 방법을 알아보겠습니다.


# 30.1 위치 인수와 리스트 언패킹 사용하기 -------------------------------

# 다음과 같이 함수에 인수를 순서대로 넣는 방식을
# 위치 인수(positional argument)라고 합니다.
# 즉, 인수의 위치가 정해져 있습니다.

print(10, 20, 30)

# 30.1.1  위치 인수를 사용하는 함수를 만들고 호출하기

def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


# 30.1.2 언패킹 사용하기

# 인수를 순서대로 넣을 때는 리스트나 튜플을 사용할 수도 있습니다.
# 다음과 같이 리스트 또는 튜플 앞에 *(애스터리스크)를 붙여서 함수에 넣어주면 됩니다.

# * 함수(*리스트)
# * 함수(*튜플)

x = [10, 20, 30]
print_numbers(*x)

# 즉, 리스트(튜플) 앞에 *를 붙이면 언패킹(unpacking)이 되어서
# print_numbers(10, 20, 30)과 똑같은 동작이 됩니다.
# 말 그대로 리스트의 포장을 푼다는 뜻입니다.

# 리스트 변수 대신 리스트 앞에 바로 *를 붙여도 동작은 같습니다.
print_numbers(*[10, 20, 30])

# 단, 이때 함수의 매개변수 개수와 리스트의 요소 개수는 같아야 합니다. 만약 개수가 다르면 함수를 호출할 수 없습니다.


# 30.1.3 가변 인수 함수 만들기

# 위치 인수와 리스트 언패킹은 어디에 사용할까요?
# 이 기능들은 인수의 개수가 정해지지 않은
# 가변 인수(variable argument)에 사용합니다.
# 즉, 같은 함수에 인수 한 개를 넣을 수도 있고,
# 열 개를 넣을 수도 있습니다. 또는, 인수를 넣지 않을 수도 있습니다.

# 가변 인수 함수는 매개변수 앞에 *를 붙여서 만든다.
# def 함수이름(*매개변수):
#     코드

# 이제 숫자 여러 개를 받고, 숫자를 각 줄에 출력하는 함수를 만들어보겠습니다.
# 다음과 같이 함수를 만들 때 괄호 안에 *args와 같이 매개변수 앞에 *를 붙입니다.
# 그리고 함수 안에서는 for로 args를 반복하면서 print로 값을 출력합니다.

def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(10, 20, 30, 40)

# 매개변수 이름은 원하는 대로 지어도 되지만,
# 관례적으로 arguments를 줄여서 args로 사용합니다. 특히 이 args는 튜플이라서 for로 반복할 수 있습니다.

y = [10, 20, 30, 40]
print_numbers(*y)

# 이처럼 함수를 만들 때 def print_numbers(*args):와 같이
# 매개변수에 *를 붙여주면 가변 인수 함수를 만들 수 있습니다.
# 그리고 이런 함수를 호출할 때는 인수를 각각 넣거나,
# 리스트(튜플) 언패킹을 사용하면 됩니다.


# 참고 : 고정 인수와 가변 인수를 함께 사용하기

# 고정 인수와 가변 인수를 함께 사용할 때는 다음과 같이 고정 매개변수를 먼저 지정하고,
# 그 다음 매개변수에 *를 붙여주면 됩니다.

def print_numbers(a, *args):
    print(a)
    print(args)

print_numbers(1)
print_numbers(1, 20, 30)
print_numbers(*[10, 20, 30])

# 단, 이때 def print_numbers(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면 안 됩니다.
# 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 합니다.





# 30.2 키워드 인수 사용하기 --------------------------------------------------

#  인수의 순서와 용도를 매번 기억하지 않도록 키워드 인수(keyword argument)라는 기능을 제공합니다.
#  키워드 인수는 말 그대로 인수에 이름(키워드)을 붙이는 기능인데 키워드=값 형식으로 사용합니다.

# * 함수(키워드 = 값)

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info(name='홍길동', age=10, address='서울시 용산구')

# 키워드 인수를 사용하니 함수를 호출할 때 인수의 용도가 명확하게 보입니다.
# 특히 키워드 인수를 사용하면 인수의 순서를 맞추지 않아도 키워드에 해당하는 값이 들어갑니다.

personal_info(age=10, name='홍길동', address='대전시 대덕구')  # 순서가 달라져도 입력가능

# personal_info 함수는 이름, 나이, 주소 순으로 인수를 넣어야 하지만,
# 키워드 인수를 사용해서 순서를 지키지 않고 값을 넣었습니다.



# 30.3 키워드 인수와 딕셔너리 언패킹 사용하기 ---------------------------------------------------

# 딕셔너리를 사용해서 키워드 인수로 값을 넣는 딕셔너리 언패킹을 사용해보겠습니다.
# 다음과 같이 딕셔너리 앞에 **(애스터리스크 두 개)를 붙여서 함수에 넣어줍니다.

# * 함수(**딕셔너리)

def personal_info(name, age, address):
    print('이름:', name)
    print('나이:', age)
    print('주소:', address)

# 이제 딕셔너리에 '키워드': 값 형식으로 인수를 저장하고, 앞에 **를 붙여서 함수에 넣어줍니다.
# 이때 딕셔너리의 키워드(키)는 반드시 문자열 형태라야 합니다.

x = dict(zip(['name', 'age', 'address'], ['홍길동', 30, '대전시 대덕구']))

personal_info(**x)

# **x처럼 딕셔너리를 언패킹하면 딕셔너리의 값들이 함수의 인수로 들어갑니다.
# 즉, personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
# 또는 personal_info('홍길동', 30, '서울시 용산구 이촌동')과 똑같은 동작이 됩니다.

# 딕셔너리 변수 대신 딕셔너리 앞에 바로 **를 붙여도 동작은 같습니다.

# 딕셔너리 언패킹을 사용할 때는 함수의 매개변수 이름과 딕셔너리의 키 이름이 같아야 합니다.
# 또한, 매개변수 개수와 딕셔너리 키의 개수도 같아야 합니다.


# 30.3.1  **를 두 번 사용하는 이유

# 딕셔너리는 **처럼 *를 두 번 사용할까요?
# 왜냐하면 딕셔너리는 키-값 쌍 형태로 값이 저장되어 있기 때문입니다.
# 먼저 *를 한 번만 사용해서 함수를 호출해봅니다.

personal_info(*x)  # 키가 출력됨
personal_info(**x) # 값이 출력됨


# 30.3.2  키워드 인수를 사용하는 가변 인수 함수 만들기

# 키워드 인수를 사용하는 가변 인수 함수를 만들어보겠습니다.
# 다음과 같이 키워드 인수를 사용하는 가변 인수 함수는 매개변수 앞에 **를 붙여서 만듭니다.

# def 함수이름(**매개변수):
#     코드


# 이제 값 여러 개를 받아서 매개변수 이름과 값을 각 줄에 출력하는 함수를 만들어보겠습니다.
# 함수를 만들 때 괄호 안에 **kwargs와 같이 매개변수 앞에 **를 붙입니다.
# 함수 안에서는 for로 kwargs.items()를 반복하면서 print로 값을 출력합니다.

# 매개변수 이름은 원하는 대로 지어도 되지만
# 관례적으로 keyword arguments를 줄여서 kwargs로 사용합니다.
# 특히 이 kwargs는 딕셔너리라서 for로 반복할 수 있습니다.

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

personal_info(name='홍길동')
personal_info(name='홍길동', age=10, adrress='대전시 대덕구')

y = {'name':'홍길동', 'age': 10, 'address': '대전시 대덕구'}
personal_info(**y)

# 이처럼 함수를 만들 때 def personal_info(**kwargs):와 같이 매개변수에 **를 붙여주면
# 키워드 인수를 사용하는 가변 인수 함수를 만들 수 있습니다.
# 그리고 이런 함수를 호출할 때는 키워드와 인수를 각각 넣거나 딕셔너리 언패킹을 사용하면 됩니다.


# 보통 **kwargs를 사용한 가변 인수 함수는 다음과 같이 함수 안에서 특정 키가 있는지 확인한 뒤 해당 기능을 만듭니다.

def personal_info(**kwargs):
    if 'name' in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

z = dict(zip(['name', 'address'], [10, '대전시 대덕구']))
personal_info(**z)


# 위치 인수와 키워드 인수를 함께 사용하기

# 함수에서 위치 인수를 받는 *args와
# 키워드 인수를 받는 **kwargs를 함께 사용할 수도 있습니다.
# 대표적인 함수가 print인데 print는 출력할 값을 위치 인수로 넣고
# sep, end 등을 키워드 인수로 넣습니다.
#
# 다음과 같이 함수의 매개변수를 *args, **kwargs로 지정하면
# 위치 인수와 키워드 인수를 함께 사용합니다.

def custom_print(*args, **kwargs):
    print(*args, **kwargs)

custom_print(1, 2, 3, sep=':', end='')

# 단, 이때 def custom_print(**kwargs, *args):처럼
# **kwargs가 *args보다 앞쪽에 오면 안 됩니다.
# 매개변수 순서에서 **kwargs는 반드시 가장 뒤쪽에 와야 합니다.




# 30.4 매개변수에 초깃값 지정하기

# 지금까지 함수를 호출할 때 항상 인수를 넣어서 값을 전달했습니다.
# 그러면 인수를 생략할 수는 없을까요?
# 이때는 함수의 매개변수에 초깃값을 지정하면 됩니다.
# 초깃값은 다음과 같이 함수를 만들 때 매개변수=값 형식으로 지정합니다.

# def 함수이름(매개변수=값):
#     코드

# address는 초깃값이 있으므로 personal_info는
# 다음과 같이 address 부분을 비워 두고 호출할 수 있습니다.


def personal_info(name, age, address = '비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info('홍길동', 30)

# 매개변수에 초깃값이 지정되어 있더라도 값을 넣으면 해당 값이 전달됩니다.

personal_info('홍길동', 30, '서울시 용산구 이촌동')



# 30.4.1  초깃값이 지정된 매개변수의 위치

# 매개변수의 초깃값을 지정할 때 한 가지 주의할 점이 있습니다.
# 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없습니다

# def personal_info(name, address='비공개', age):
# 이런식으로 초기값이 있을 경우 맨 뒤로 보내줘야 한다.



# 30.6 연습문제 : 가장 높은 점수를 구하는 함수 만들기

korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)


max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)



# 30.7 심사문제 : 가장 낮은 점수, 높은 점수와 평균점수를 구하는 함수 만들기

# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가 출력되게 만드세요.
# 평균 점수는 실수로 출력되어야 합니다.

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):  # 가변 인수 함수는 매개변수 앞에 *를 붙여서 만든다.
    return min(args), max(args)

def get_average(**kwargs):  # 키워드 인수를 사용하는 가변 인수 함수는 매개변수 앞에 **를 붙여서 만든다.
    return sum(kwargs.values()) / len(kwargs)


min_score, max_score = get_min_max_score(korean, english, mathematics, science)

average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))





a = [10, 20 ,30, 40]
d = dict(zip(['가',' 나',' 다'], [1, 2, 3]))
print(*d.values())







