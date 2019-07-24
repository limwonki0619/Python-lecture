# Unit 36. 클래스 상속 사용하기

# 이번에는 클래스 상속(inheritance)을 사용해보겠습니다.

# 상속은 무언가를 물려받는다는 뜻입니다.
# 그래서 클래스 상속은 물려받은 기능을 유지한채로
# 다른 기능을 추가할 때 사용하는 기능입니다.
# 클래스 상속은 기반 클래스의 능력을 그대로 활용하면서 새로운 클래스를 만들 때 사용합니다.


# 여기서 기능을 물려주는 클래스를 기반 클래스(base class),
# 상속을 받아 새롭게 만드는 클래스를 파생 클래스(derived class)라고 합니다.

# 보통 기반 클래스는 부모 클래스(parent class), 슈퍼 클래스(superclass)라고 부르고,
# 파생 클래스는 자식 클래스(child class), 서브 클래스(subclass)라고도 부릅니다.


# 그런데 그냥 새로운 클래스를 만들면 되지 왜 이런 상속 개념을 만들었을까요?
# 만약 새로운 기능이 필요할 때마다 계속 클래스를 만든다면 중복되는 부분을 반복해서 만들어야 합니다.
# 이럴 때 상속을 사용하면 중복되는 기능을 만들지 않아도 됩니다.
#
# 따라서 상속은 기존 기능을 재사용할 수 있어서 효율적입니다.


# 36.1 사람 클래스로 학생 클래스 만들기 -------------------------------------------------

# 클래스 상속은 다음과 같이 클래스를 만들 때 ( )(괄호)를 붙이고 안에 기반 클래스 이름을 넣습니다.

# class 기반클래스이름:
#     코드
#
# class 파생클래스이름(기반클래스이름):
#     코드

class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):  # Person 클래스를 상속받겠다. (자식이 부모를 선택!)
    def study(self):
        print('공부하기')

james = Student()
james.greeting()  # 안녕하세요. : 부모 클래스 Person의 메서드를 호출
james.study()     # 공부하기 :    자식 클래스 Student에 추가한 study 메서드

# Student 클래스를 만들 때 class Student(Person):과 같이 ( )(괄호) 안에
# 기반 클래스인 Person 클래스를 넣었습니다.
# 이렇게 하면 Person 클래스의 기능을 물려받은 Student 클래스가 됩니다.

# Student 클래스에는 greeting 메서드가 없지만
# Person 클래스를 상속받았으므로 greeting 메서드를 호출할 수 있습니다.
# 그리고 Student 클래스에 추가한 새로운 메서드인 study를 호출했습니다.

# 이처럼 클래스 상속은 기반 클래스의 기능을 유지하면서
# 새로운 기능을 추가할 수 있습니다.
#
# 특히 클래스 상속은 연관되면서 동등한 기능일 때 사용합니다.
# 즉, 학생은 사람이므로 연관된 개념이고, 학생은 사람에서 역할만 확장되었을 뿐 동등한 개념입니다.


# 참고 : 상속 관계 확인하기

# 클래스의 상속 관계를 확인하고 싶을 때는 issubclass 함수를 사용합니다.
# 즉, 클래스가 기반 클래스의 파생 클래스인지 확인합니다.
# 기반 클래스의 파생 클래스가 맞으면 True, 아니면 False를 반환합니다

# * issubclass(파생클래스, 기반클래스)
class Person:
    pass

class Student(Person):
    pass

issubclass(Student, Person)  # Student가 Person의 자식 클래스인가?



# 36.2 상속 관계와 포함 관계 알아보기 --------------------------------------------------


# 36.2.1  상속 관계 (is - a 관계)

# 앞에서 만든 Student 클래스는 Person 클래스를 상속받아서 만들었습니다.

class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def study(self):
        print('공부하기')

# 여기서 학생 Student는 사람 Person이므로 같은 종류입니다.
# 이처럼 상속은 명확하게 같은 종류이며 동등한 관계일 때 사용합니다.
# 즉, "학생은 사람이다."라고 했을 때 말이 되면 동등한 관계입니다.
# 그래서 상속 관계를 영어로 is-a 관계라고 부릅니다(Student is a Person).



# 36.2.2  포함 관계 (has - a 관계)

# 하지만 학생 클래스가 아니라 사람 목록을 관리하는 클래스를 만든다면 어떻게 해야 할까요?
# 다음과 같이 리스트 속성에 Person 인스턴스를 넣어서 관리하면 됩니다.

class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):  # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

# 여기서는 상속을 사용하지 않고 속성에 인스턴스를 넣어서 관리하므로
# PersonList가 Person을 포함하고 있습니다.
# 이러면 사람 목록 PersonList와 사람 Person은 동등한 관계가 아니라 포함 관계입니다.
#
# 즉, "사람 목록은 사람을 가지고 있다."라고 말할 수 있습니다.
# 그래서 포함 관계를 영어로 has-a 관계라고 부릅니다(PersonList has a Person).

# 정리하자면 같은 종류에 동등한 관계일 때는 상속을 사용하고,
# 그 이외에는 속성에 인스턴스를 넣는 포함 방식을 사용하면 됩니다.



# 36.3 기반 클래스의 속성 사용하기 -----------------------------------------------------

# 이번에는 기반 클래스에 들어있는 인스턴스 속성을 사용해보겠습니다.
# 다음과 같이 Person 클래스에 hello 속성이 있고, Person 클래스를 상속받아 Student 클래스를 만듭니다.
# 그다음에 Student로 인스턴스를 만들고 hello 속성에 접근해봅니다.

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'


james = Student()
print(james.school)
print(james.hello)  # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함


#  왜냐하면 기반 클래스 Person의 __init__ 메서드가 호출되지 않았기 때문입니다.
#  실행 결과를 잘 보면 'Student __init__'만 출력되었습니다.
# 즉, Person의 __init__ 메서드가 호출되지 않으면,
# self.hello = '안녕하세요.'도 실행되지 않아서 속성이 만들어지지 않습니다.


# 36.3.1  super()로 기반 클래스 초기화하기

# 이때는 super()를 사용해서 기반 클래스의 __init__ 메서드를 호출해줍니다.
# 다음과 같이 super() 뒤에 .(점)을 붙여서 메서드를 호출하는 방식입니다.

# * super().메서드()

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)


# 상속을 받았다면
# def __init__(self):
#    super().__init__() 를 사용해 부모 크래스의 __init__ 메서드를 호출해라



# 36.3.2  기반 클래스를 초기화하지 않아도 되는 경우

# 만약 파생 클래스에서 __init__ 메서드를 생략한다면
# 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 됩니다.

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요'

class Student(Person):
    pass

james = Student()
print(james.hello)

# 이처럼 파생 클래스에 __init__ 메서드가 없다면
# 기반 클래스의 __init__이 자동으로 호출되므로 기반 클래스의 속성을 사용할 수 있습니다.


# 참고 : 좀 더 명확하게 super 사용하기

# super는 다음과 같이 파생 클래스와 self를 넣어서
# 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법도 있습니다.
# 물론 super()와 기능은 같습니다.

# * super(파생클래스, self).메서드

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()     # super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩 도장'






# 36.4 메서드 오버라이딩 사용하기 -----------------------------------------------------

# 이번에는 파생 클래스에서 기반 클래스의 메서드를 새로 정의하는 메서드 오버라이딩에 대해 알아보겠습니다.
# 다음과 같이 Person의 greeting 메서드가 있는 상태에서 Student에도 greeting 메서드를 만듭니다.

class Person:
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')  # 메서드 재정의

james = Student()
james.greeting()

# 오버라이딩(overriding)은 무시하다, 우선하다라는 뜻을 가지고 있는데
# 말 그대로 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다는 뜻입니다.
# 여기서는 Person 클래스의 greeting 메서드를 무시하고
# Student 클래스에서 새로운 greeting 메서드를 만들었습니다.

# 그럼 메서드 오버라이딩은 왜 사용할까요?
# 보통 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 메서드 오버라이딩을 활용합니다.
# 만약 Student 클래스에서 인사하는 메서드를 greeting2로 만들어야 한다면
# 모든 소스 코드에서 메서드 호출 부분을 greeting2로 수정해야겠죠?

# 다시 Person 클래스의 greeting 메서드와 Student 클래스의 greeting 메서드를 보면
# '안녕하세요.'라는 문구가 중복됩니다.

# 이럴 때는 기반 클래스의 메서드를 재활용하면 중복을 줄일 수 있습니다.
# 다음과 같이 오버라이딩된 메서드에서 super()로 기반 클래스의 메서드를 호출해봅니다.

class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        super().greeting()  # 부모 클래스의 메서드를 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')

james = Student()
james.greeting()

# Student의 greeting에서 super().greeting()으로 Person의 greeting을 호출했습니다.
# 즉, 중복되는 기능은 파생 클래스에서 다시 만들지 않고, 기반 클래스의 기능을 사용하면 됩니다.
# 이처럼 메서드 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용합니다.




# 36.5 다중 상속 사용하기 -------------------------------------------------------------

# 다중 상속은 여러 기반 클래스로부터 상속을 받아서 파생 클래스를 만드는 방법입니다.
# 다음과 같이 클래스를 만들 때 ( )(괄호) 안에 클래스 이름을 ,(콤마)로 구분해서 넣습니다.

# class 기반클래스이름1:
#     코드
#
# class 기반클래스이름2:
#     코드
#
# class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
#     코드

# 그럼 사람 클래스와 대학교 클래스를 만든 뒤 다중 상속으로 대학생 클래스를 만들어보겠습니다.







# 36.6 추상 클래스 사용하기

# 파이썬은 추상 클래스(abstract class)라는 기능을 제공합니다.
# 추상 클래스는 메서드의 목록만 가진 클래스이며
# 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용합니다.

# from abc import *

# class 추상클래스이름(metaclass=ABCMeta):
#     @abstractmethod
#     def 메서드이름(self):
#         코드


# 먼저 추상 클래스를 만들려면 import로 abc 모듈을 가져와야 합니다
# ( abc는 abstract base class의 약자입니다).
# 그리고 클래스의 ( )(괄호) 안에 metaclass=ABCMeta를 지정하고,
# 메서드를 만들 때 위에 @abstractmethod를 붙여서 추상 메서드로 지정합니다.

