# Unit 34. 클래스 사용하기

# ​클래스는 객체를 표현하기 위한 문법입니다.
#  예를 들어 게임을 만든다고 하면 기사, 마법사, 궁수, 사제 등 직업별로 클래스를 만들어서 표현할 수 있습니다.

# class는 상속을 받는다.


# 34.1 클래스와 메서드 만들기

# class 클래스이름:
#     def 메서드(self):
#         코드

# 클래스는 class에 클래스 이름을 지정하고 :(콜론)을 붙인 뒤
# 다음 줄부터 def로 메서드를 작성하면 됩니다.
# 여기서 메서드는 클래스 안에 들어있는 함수를 뜻합니다.

# 클래스 이름을 짓는 방법은 변수와 같습니다.
# 보통 파이썬에서는 클래스의 이름은 대문자로 시작합니다.
# 그리고 메서드 작성 방법은 함수와 같으며 코드는 반드시 들여쓰기를 해야 합니다
# (들여쓰기 규칙은 if, for, while과 같습니다).
#
# 특히 메서드의 첫 번째 매개변수는 반드시 self를 지정해야 합니다. ***

class Person:            # ()가 없다.
    def greeting(self):  # super는 조상 self는 나 자신
        print('hello')

# 그럼 이 클래스를 사용해봐야겠죠?
# 다음과 같이 클래스에 ()(괄호)를 붙인 뒤 변수에 할당합니다.

# * 인스턴스 = 클래스()
james = Person()

# Person으로 변수 james를 만들었는데
# 이 james가 Person의 인스턴스(instance)입니다.
# 클래스는 특정 개념을 표현만 할뿐 사용을 하려면 인스턴스를 생성해야 합니다.


# 34.1.1  메서드 호출하기

# 이제 메서드를 호출해보겠습니다.
# 메서드는 클래스가 아니라 인스턴스를 통해 호출합니다.
# 다음과 같이 인스턴스 뒤에 .(점)을 붙이고 메서드를 호출하면 됩니다.

james.greeting()

type(james)


# 34.1.2  파이썬에서 흔히 볼 수 있는 클래스

# 지금까지 사용한 int, list, dict 등도 사실 클래스입니다.
# 우리는 이 클래스로 인스턴스를 만들고 메서드를 사용했습니다.

a = int(10)
b = list(range(10))
c = dict(x=10, y=20)

# int 클래스에 10을 넣어서 인스턴스 a를 만들었습니다.
# 마찬가지로 list 클래스에 range(10)을 넣어서 인스턴스 b를 만들고,
# dict 클래스에 x=10, y=20을 넣어서 인스턴스 c를 만들었습니다.
# 잘 보면 Person으로 인스턴스를 만드는 방법과 똑같습니다.


# 다음과 같이 리스트를 조작할 때 메서드를 사용했었죠?

d = list(range(10))
d.append(20)

# 인스턴스 d에서 메서드 append를 호출해서 값을 추가합니다.
# 이 부분도 지금까지 메서드를 만들고 사용한 것과 같은 방식입니다.

# 즉, 파이썬에서는 자료형도 클래스입니다.
# 다음과 같이 type을 사용하면 객체(인스턴스)가 어떤 클래스인지 확인할 수 있습니다.




# 34.1.3  인스턴스와 객체의 차이점?

# 클래스는 객체를 표현하는 문법이라고 했는데,
# 클래스로 인스턴스를 만든다고 하니 좀 헷갈리죠?
#
# 사실 인스턴스와 객체는 같은 것을 뜻합니다.
# 보통 객체만 지칭할 때는 그냥 객체(object)라고 부릅니다.
# 하지만 클래스와 연관지어서 말할 때는 인스턴스(instance)라고 부릅니다.
# 그래서 다음과 같이 리스트 변수 a, b가 있으면 a, b는 객체입니다.
# 그리고 a와 b는 list 클래스의 인스턴스입니다.

a = list(range(10))
b = list(range(20))

# a = 변수 = 객체 = list 클래스의 인스턴스

# 참고 1 : 빈 클래스 만들기
class Person:
    pass


# 참고 2 : 메서드 안에서 메서드 호출하기

# 메서드 안에서 메서드를 호출할 때는
# 다음과 같이 self.메서드() 형식으로 호출해야 합니다.
# self 없이 메서드 이름만 사용하면
# 클래스 바깥쪽에 있는 함수를 호출한다는 뜻이 되므로 주의해야 합니다.

class Person:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출

james = Person()
james.hello()  # Hello


# 참고 3 : 특정 클래스의 인스턴스인지 확인하기

# 현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는
# isinstance 함수를 사용합니다.
# 특정 클래스의 인스턴스가 맞으면 True, 아니면 False를 반환합니다.

isinstance(james, Person)


# isinstance는 주로 객체의 자료형을 판단할 때 사용합니다.
# 예를 들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야 하는데,
# 실수와 음의 정수는 계산할 수 없습니다.
# 이런 경우에 isinstance를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있습니다.

def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        print('올바른 입력값이 아닙니다.', end='')
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)

factorial(5)
factorial(2.3)



# 34.2 속성 사용하기

# 지금까지 클래스에서 메서드를 만들고 호출해보았습니다.
# 이번에는 클래스에서 속성을 만들고 사용해보겠습니다.
#
# 속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당합니다.

# class 클래스이름:
#     def __init__(self):
#         self.속성 = 값

class Person:
    def __init__(self):
        self.hello = '안녕하세요.'

    def greeting(self):
        print(self.hello)

james = Person()
james.greeting()

print(james.hello)  # public 속성 -> 외부에서 변경이 가능, 보안에 취약

james.hello = '안녕하세요? 여러분!'
james.greeting()


# __init__ 메서드는 james = Person()처럼 클래스에
# ( )(괄호)를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드입니다.
# 즉, __init__(initialize)이라는 이름 그대로 인스턴스(객체)를 초기화합니다.

# 특히 이렇게 앞 뒤로 __(밑줄 두 개)가 붙은 메서드는 파이썬이 자동으로 호출해주는 메서드인데
# 스페셜 메서드(special method) 또는 매직 메서드(magic method)라고 부릅니다.



# 이제 greeting 메서드를 살펴보겠습니다.
# greeting 메서드에서는 print로 self.hello를 출력하도록 만들었습니다.

# def greeting(self):
#     print(self.hello)

# 지금까지 __init__ 메서드에서 속성을 만들고 greeting 메서드에서 속성을 사용해봤습니다.
# 속성은 __init__ 메서드에서 만든다는 점과 self에 .(점)을 붙인 뒤 값을 할당한다는 점이 중요합니다.
# 클래스 안에서 속성을 사용할 때도 self.hello처럼 self에 점을 붙여서 사용하면 됩니다.



# 34.2.1  self의 의미

# self는 인스턴스 자기 자신을 의미합니다.
# 우리는 인스턴스가 생성될 때 self.hello = '안녕하세요.'처럼 자기 자신에 속성을 추가했습니다.
# 여기서 __init__의 매개변수 self에 들어가는 값은 Person()이라 할 수 있습니다.
# 그리고 self가 완성된 뒤 james에 할당됩니다.
# 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어옵니다.
# 그래서 greeting 메서드에서 print(self.hello)처럼 속성을 출력할 수 있었던 것입니다.


# 34.2.2  인스턴스를 만들 때 값 받기

# 이번에는 클래스로 인스턴스를 만들 때 값을 받는 방법을 알아보겠습니다. 다음과 같이 __init__ 메서드에서 self 다음에 값을 받을 매개변수를 지정합니다. 그리고 매개변수를 self.속성에 넣어줍니다.

# class 클래스이름:
#     def __init__(self, 매개변수1, 매개변수2):
#         self.속성1 = 매개변수1
#         self.속성2 = 매개변수2

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '대전시 대덕구')
maria.greeting()

print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

# __init__ 메서드를 보면 self 다음에 name, age, address를 지정했습니다.
# 그리고 메서드 안에서는 self.name = name처럼 매개변수를
# 그대로 self에 넣어서 속성으로 만들었습니다.

# greeting 메서드는 인사를 하고 이름을 출력하도록 수정했습니다.
# 물론 name 속성에 접근할 때는 self.name처럼 사용해야 합니다.

# 이제 Person의 ( )(괄호) 안에 이름, 나이, 주소를 콤마로 구분해서 넣은 뒤에 변수에 할당합니다.
# 이렇게 하면 이름은 '마리아',
# 나이는 20, 주소는
# '서울시 서초구 반포동'인 maria 인스턴스가 만들어집니다.


# maria 인스턴스의 greeting 메서드를 호출해보면 '안녕하세요. 저는 마리아입니다.'처럼 인삿말과 함께 이름도 출력됩니다.
maria.greeting()


# 클래스 안에서 속성에 접근할 때는 self.속성 형식이었죠?
# 클래스 바깥에서 속성에 접근할 때는 인스턴스.속성 형식으로 접근합니다.
# 다음과 같이 maria.name, maria.age, maria.address의 값을 출력해보면
# Person으로 인스턴스를 만들 때 넣었던 값이 출력됩니다.

print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동

# 이렇게 인스턴스를 통해 접근하는 속성을 인스턴스 속성이라 부릅니다.




# 참고 : 클래스의 위치 인수, 키워드 인수

# 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있습니다.
# 규칙은 함수와 같습니다. 위치 인수와 리스트 언패킹을 사용하려면
# 다음과 같이 *args를 사용하면 됩니다.
# 이때 매개변수에서 값을 가져오려면 args[0]처럼 사용해야 합니다.

class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '대전시 대덕구'])

# 키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 같이 **kwargs를 사용하면 됩니다.
# 이때 매개변수에서 값을 가져오려면 kwargs['name']처럼 사용해야 합니다.

class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})



# 참고 : 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기

# 지금까지 클래스의 인스턴스 속성은 __init__ 메서드에서 추가한 뒤 사용했습니다.
# 하지만 클래스로 인스턴스를 만든 뒤에도
# 인스턴스.속성 = 값 형식으로 속성을 계속 추가할 수 있습니다.
#
# 다음 Person 클래스는 빈 클래스이지만 인스턴스를 만든 뒤
# name 속성을 추가합니다.

class Person:
    pass

maria = Person()
maria.name = '마리아'  # maria 인스터느에 name 속성을 추가
maria.name

# 이렇게 추가한 속성은 해당 인스턴스에만 생성됩니다.
# 따라서 클래스로 다른 인스턴스를 만들었을 때는 추가한 속성이 생성되지 않습니다.

james = Person()    # james 인스턴스 생성
james.name          # maria 인스턴스에만 name 속성을 추가했으므로 james 인스턴스에는 name 속성이 없음

james.name = '제임스'
james.name

# 인스턴스는 자유롭게 속성을 추가할 수 있지만 특정 속성만 허용하고
# 다른 속성은 제한하고 싶을 수도 있습니다.
# 이때는 클래스에서 __slots__에 허용할 속성 이름을 리스트로 넣어주면 됩니다.
# 특히 속성 이름은 반드시 문자열로 지정해줍니다.

# __slots__ = ['속성이름1, '속성이름2']

class Person:
    __slots__ = ['name', 'age']    # name, age만 허용(다른 속성은 생성 제한)

maria = Person()
maria.name = '마리아'                     # 허용된 속성
maria.age = 20                            # 허용된 속성
maria.address = '서울시 서초구 반포동'    # 허용되지 않은 속성은 추가할 때 에러가 발생함




# 34.3 비공개 속성 사용하기 -------------------------------------------------------------------------------

# 앞에서 만든 Person 클래스에는 hello, name, age, address 속성이 있었습니다.

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

# 이 속성들은 메서드에서 self로 접근할 수 있고,
# 인스턴스.속성 형식으로 클래스 바깥에서도 접근할 수 있습니다.

# 이번에는 클래스 바깥에서는 접근할 수 없고
# 클래스 안에서만 사용할 수 있는 비공개 속성(private attribute)을 사용해보겠습니다.

# 비공개 속성은 __속성과 같이
# 이름이 __(밑줄 두 개)로 시작해야 합니다.
# 단, __속성__처럼 밑줄 두 개가 양 옆에 왔을 때는 비공개 속성이 아니므로 주의해야 합니다.

# class 클래스이름:
#     def __init__(self, 매개변수)
#         self.__속성 = 값

# 그럼 Person 클래스에 지갑 속성 __wallet을 넣어보겠습니다.
# 다음 내용을 IDLE의 소스 코드 편집 창에 입력한 뒤 실행해보세요.

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함

# 실행을 해보면 에러가 발생합니다.
# self.__wallet처럼 앞에 밑줄 두 개를 붙여서 비공개 속성으로 만들었으므로
# 클래스 바깥에서 maria.__wallet으로는 접근할 수 없습니다.
# 사람이 가지고 있는 지갑은 본인만 사용할 수 있는데 maria.__wallet -= 10000처럼
# 바깥에서 마음대로 돈을 뺄 수는 없겠죠?

# 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있습니다.
# 다음과 같이 돈을 내는 pay 메서드를 만들어봅니다.

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amount):
        self.__wallet -= amount

        print('이제 {0}원 남았네요'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)

# pay는 돈을 내면 해당 금액을 지갑에서 빼도록 만들었습니다.
# 이제 지갑에 있는 돈을 쓸 수 있게 되었습니다.
#
# 물론 지갑에 든 돈은 굳이 밝힐 필요가 없으므로 print로 출력하지 않아도 됩니다.
# 보통은 다음과 같이 지갑에 든 돈이 얼마인지 확인하고
# 돈이 모자라면 쓰지 못하는 식으로 만듭니다.


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amount):
        if amount > self.__wallet:

            print('돈이 모자라네..')
            return

        self.__wallet -= amount
        # print('이제 {0}원 남았네요'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)


# 이처럼 비공개 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용합니다.
# 즉, 중요한 값인데 바깥에서 함부로 바꾸면 안될 때 비공개 속성을 주로 사용합니다.
# 비공개 속성을 바꾸는 경우는 클래스의 메서드로 한정합니다.


# 지금까지 클래스 사용 방법에 대해 알아보았습니다.
# 클래스는 특정 개념을 표현(정의)만 할 뿐 사용을 하려면
# 인스턴스로 만들어야 한다는 점이 중요합니다. 그리고 속성, 메서드를 사용할 때는
# self와 인스턴스를 통해 사용해야 한다는 점도 기억해두세요.




# 참고 : 공개 속성과 비공개 속성
# 클래스 바깥에서 접근할 수 있는 속성을 공개 속성(public attribute)이라 부르고,
# 클래스 안에서만 접근할 수 있는 속성을 비공개 속성(private attribute)이라 부릅니다.


# 참고 : 비공개 메서드 사용하기
# 속성뿐만 아니라 메서드도 이름이 __(밑줄 두 개)로 시작하면
# 클래스 안에서만 호출할 수 있는 비공개 메서드가 됩니다.

class Person():
    def __greeting(self):
        print('hello')

    def hello(self):
        self.__greeting()  # 클래스 안에서는 비공개 메서드를 호출할 수 있음.

james = Person()
james.__greeting()  # 에러 : 클래스 바깥에서는 비공개 메서드를 호출할 수 없다.

# 비공개 메서드도 메서드를 클래스 바깥으로 드러내고 싶지 않을 때 사용합니다.
# 보통 내부에서만 호출되어야 하는 메서드를 비공개 메서드로 만듭니다.
#
# 예를 들어 게임 캐릭터가 마나를 소비해서 스킬을 쓴다고 치면
# 마나 소비량을 계산해서 차감하는 메서드는 비공개 메서드로 만들고,
# 스킬을 쓰는 메서드는 공개 메서드로 만듭니다.
#
# 만약 마나를 차감하는 메서드가 공개되어 있다면
# 마음대로 마나를 차감시킬 수 있으므로 잘못된 클래스 설계가 됩니다.


