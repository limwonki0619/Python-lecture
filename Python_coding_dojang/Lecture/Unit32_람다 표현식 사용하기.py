# Unit 32. 람다 표현식 사용하기

# 지금까지 def로 함수를 정의해서 사용했습니다.
# 이번에는 람다 표현식으로 익명 함수를 만드는 방법을 알아보겠습니다.

# 람다 표현식은 식 형태로 되어 있다고 해서 람다 표현식(lambda expression)이라고 부릅니다.
# 특히 람다 표현식은 함수를 간편하게 작성할 수 있어서 다른 함수의 인수로 넣을 때 주로 사용합니다.



# 32.1 람다 표현식으로 함수 만들기 ---------------------------------------------------------------------
def plus_ten(x):
    return x + 10

plus_ten(1)

# 이 plus_ten 함수를 람다 표현식으로 작성해보겠습니다.
# 람다 표현식은 다음과 같이 lambda에 매개변수를 지정하고 :(콜론) 뒤에 반환값으로 사용할 식을 지정합니다.

# * lambda 매개변수들: 식
plues_ten = lambda x: x+10


# 32.1.1  람다 표현식 자체를 호출하기
# * (lambda 매개변수들: 식)(인수들)

(lambda x: x+10)(1)


# 32.1.2  람다 표현식 안에서는 변수를 만들 수 없다

# 람다 표현식에서 주의할 점은 람다 표현식 안에서는 새 변수를 만들 수 없다는 점입니다.
# 따라서 반환값 부분은 변수 없이 식 한 줄로 표현할 수 있어야 합니다.
# 변수가 필요한 코드일 경우에는 def로 함수를 작성하는 것이 좋습니다.



# 32.1.3  람다 표현식을 인수로 사용하기

# 람다 표현식을 사용하는 이유는 함수의 인수 부분에서 간단하게 함수를 만들기 위해서 입니다.
# 이런 방식으로 사용하는 대표적인 예가 map입니다.

def plus_ten(x):
    return x + 10
list(map(plus_ten, [1, 2, 3]))


list(map(lambda x: x+10, [1, 2, 3]))

# 참고 : 람다 표현식으로 매개변수가 없는 함수 만들기
(lambda: 1)()

x = 10
(lambda: x)()

# 람다 표현식으로 매개변수가 없는 함수를 만들 때는
# lambda 뒤에 아무것도 지정하지 않고 :(콜론)을 붙입니다.
# 단, 콜론 뒤에는 반드시 반환할 값이 있어야 합니다.



# 32.2 람다 표현식과 map, filter, reduce 함수 활용하기 ---------------------------------------


# 32.2.1  람다 표현식에 조건부 표현식 사용하기

# * lambda 매개변수들: 식1 if 조건식 else 식2
a = list(range(1, 10))
list(map(lambda x: str(x) if x % 3 == 0 else x, a))

# map은 리스트의 요소를 각각 처리하므로 lambda의 반환값도 요소라야 합니다.
# 여기서는 요소가 3의 배수일 때는 str(x)로 요소를 문자열로 만들어서 반환했고,
# 3의 배수가 아닐 때는 x로 요소를 그대로 반환했습니다.

# 람다 표현식 안에서 조건부 표현식 if, else를 사용할 때는 :(콜론)을 붙이지 않습니다. 일반적인 if, else와 문법이 다르므로 주의해야 합니다. 조건부 표현식은 식1 if 조건식 else 식2 형식으로 사용하며 식1은 조건식이 참일 때, 식2는 조건식이 거짓일 때 사용할 식입니다.
#
# 특히 람다 표현식에서 if를 사용했다면 반드시 else를 사용해야 합니다.
# 다음과 같이 if만 사용하면 문법 에러가 발생하므로 주의해야 합니다.


# 그리고 람다 표현식 안에서는 elif를 사용할 수 없습니다.
# 따라서 조건부 표현식은 식1 if 조건식1 else 식2 if 조건식2 else 식3 형식처럼
# if를 연속으로 사용해야 합니다.
#
# 예를 들어 리스트에서 1은 문자열로 변환하고, 2는 실수로 변환,
# 3 이상은 10을 더하는 식은 다음과 같이 만듭니다.

a = list(range(1, 10))
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))

# 별로 복잡하지 않은 조건인데도 알아보기가 힘듭니다.
# 이런 경우에는 억지로 람다 표현식을 사용하기 보다는
# 그냥 def로 함수를 만들고 if, elif, else를 사용하는 것을 권장합니다.

def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10  # 코드는 길이가 조금 길어지더라도 알아보기 쉽게 작성하는 것이 좋다.


# 32.2.2 amp에 객체를 여러개 넣기

# map은 리스트 등의 반복 가능한 객체를 여러 개 넣을 수도 있습니다.
# 다음은 두 리스트의 요소를 곱해서 새 리스트를 만듭니다.

a = list(range(1, 6))
b = list(range(2, 12, 2))

list(map(lambda x, y: x*y, a, b))


# 32.2.3  filter 사용하기

#  filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데,
#  filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져옵니다.

# * filter(함수, 반복가능한 객체)

def f(x):
    return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))

# 스트 a에서 8, 7, 9를 가져왔습니다.
# 즉, filter는 x > 5 and x < 10의 결과가 참인 요소만 가져오고 거짓인 요소는 버립니다.

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(lambda x: x > 5 and x < 10, a))  # 함수 f를 람다 표현식으로 만들어서 filter에 넣어보겠습니다.



# 32.2.4  reduce 사용하기
# reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤
# 이전 결과와 누적해서 반환하는 함수입니다

from functools import reduce
# reduce(함수, 반복가능한객체)

def f(x, y):
    return x + y

a = list(range(1, 6))

reduce(f, a)

# 함수 f에서 x + y를 반환하도록 만들었으므로 reduce는
# 그림과 같이 요소 두 개를 계속 더하면서 결과를 누적합니다

