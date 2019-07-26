# 파이썬은 데코레이터(decorator)라는 기능을 제공합니다.
# 데코레이터는 장식하다, 꾸미다라는 뜻의 decorate에 er(or)을 붙인 말인데
# 장식하는 도구 정도로 설명할 수 있습니다.

# 지금까지 클래스에서 메서드를 만들 때 @staticmethod, @classmethod, @abstractmethod 등을 붙였는데, 이렇게 @로 시작하는 것들이 데코레이터입니다.
# 즉, 함수(메서드)를 장식한다고 해서 이런 이름이 붙었습니다.


# class Calc:
#     @staticmethod    # 데코레이터
#     def add(a, b):
#         print(a + b)




# 42.1 데코레이터 만들기 ------------------------------------------------------

# 데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용합니다.
# 예를 들어서 함수의 시작과 끝을 출력하고 싶다면 다음과 같이 함수 시작, 끝 부분에 print를 넣어주어야 합니다.

def trace(func):    # 호출할 함수를 매개변수로 받음
    def wrapper():  # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()                             # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                         # wrapper 함수 반환

def hello():
    print('hello')

def world():
    print('world')

trace_hello = trace(hello)
trace_hello()
trace_world = trace(world)
trace_world()


# 42.1.1  @로 데코레이터 사용하기

# 이제 @을 사용하여 좀 더 간편하게 데코레이터를 사용해보겠습니다.
# 다음과 같이 호출할 함수 위에 @데코레이터 형식으로 지정합니다.

@trace  # @데코레이터
def hello():
    print('hello')


@trace  # @데코레이터
def world():
    print('world')

hello()  # 함수를 그대로 호출
world()  # 함수를 그대로 호출

@trace
def hi():
    print('hi')

#  데코레이터는 함수를 감싸는 형태로 구성되어 있습니다.
#  따라서 데코레이터는 기존 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용합니다.


