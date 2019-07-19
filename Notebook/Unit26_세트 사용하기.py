# Unit 26. 세트 사용하기

# 집합을 영어로 하면 세트인데 수학에서 배우는 그 집합이 맞습니다.
# 따라서 세트는 합집합, 교집합, 차집합 등의 연산이 가능합니다.

# 26.1 세트 만들기 ------------------------------------------------------

# 세트는 { }(중괄호) 안에 값을 저장하며 각 값은 ,(콤마)로 구분해줍니다.
# * 세트 = {값1, 값2, 값3}

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)

# 세트는 요소의 순서가 정해져 있지 않다. (Unordered)
fruits = {'strawberry', 'strawberry', 'grape'}
print(fruits)  # 종복되는 값은 넣을 수 없다. 실제로는 하나만 입력된다.

# 특히 세트는 리스트, 튜플, 딕셔너리와는 달리 []로 특정 요소를 출력할 수 없다.


# 26.1.1  세트에 특정 값이 있는지 확인하기 : in 연산자
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print('orange' in fruits)      # 특정 값이 있는지 확인
print('orange' not in fruits)  # 특정 값이 없는지 확인

# 26.1.2  set를 사용하여 세트 만들기

# * set(반복가능한 객체)  :: iterable

a = set('alpple')  # 유일한 문자만 세트로 만듦
print(a)

b = set(range(5))  # 세트에 숫자 넣기
print(b)

c = set()  # 빈 세트 만들기
print(c, type(c))

d = set('안녕하세요')
print(d)

frozen = frozenset('안녕하세요')
print(frozen, type(frozen))  # 내용을 변경할 수 없는 세트

# rozenset는 뒤에서 설명할 집합 연산과 메서드에서 요소를
# 추가하거나 삭제하는 연산, 메서드는 사용할 수 없습니다.
# 즉, 다음과 같이 frozenset의 요소를 변경하려고 하면 에러가 발생합니다.

# frozenset는 set안에 set를 넣고자 할 때 사용한다.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

set.union(a, b)  # 합집합
print(a | b)

set.intersection(a, b)  # 교집합
print(a & b)

set.difference(a, b)  # a - b 차집합
print(a - b)

set.symmetric_difference(a, b) # 대칭차집합 (XOR 연산)
print(a ^ b)

# XOR 연산
# True xor Ture = False
# True xor False = True
# false xor true = True
# false xor false = False


# 26.2.1  집합 연산 후 할당 연산자 사용하기

# |= &= -= ^=  모두 사용가능


# 26.2.2  부분 집합과 상위집합 확인하기

# 세트는 부분집합, 진부분집합, 상위집합, 진상위집합과 같이 속하는 관계를 표현할 수도 있습니다.
# 현재 세트가 다른 세트의 (진)부분집합 또는 (진)상위집합인지 확인할 때는
# 세트 자료형에 부등호와 등호 사용합니다.

a = {1, 2, 3, 4}
# * 현재세트 <= 다른세트
# * 현재세트.issubset(다른세트)

# 현재세트 <= 다른세트(부분집합) : 현재 세트가 다른 세트의 부분집합이냐?
a.issubset({1, 2, 3, 4, 5})  # True
print(a <= {1, 2, 3, 4})     # True

# 현재세트 <  다른세트(진 부분집합) : 현재 세트가 다른 세트의 진 부분집합이냐?
print(a <= {1, 2, 3, 4, 5})  # True


# * 현재세트 >= 다른세트
# * 현재세트.issuperset(다른세트)

# 현재세트 >= 다른세트 : 현재 세트가 다른 세트의 상위집합이냐?
print(a >= {1, 2, 3, 4})
a.issuperset({1, 2, 3, 4, 5})

# 현재세트 >  다른세트 : 현재 세트가 다른 세트의 진 상위집합이냐?
print(a > {1, 2, 3})


# 26.2.3  세트가 같은지 다른지 확인하기
print(a == {1, 2, 3, 4})  # 세트가 같냐?
print(a != {1, 2, 3})  # 세트가 다르냐?


# 26.2.4  세트가 겹치지 않는지 확인하기

# 현재세트.isdisjoint(다른세트)
set.intersection(a, b)  # 교집합을 set 타입으로 반환
a.isdisjoint(b)         # 현재세트가 다른세트와 겹치지 않냐? 교집함이 있으면 False, 없으면 True로 반환



# 26.3 세트 조작하기 ---------------------------------------------------------------

# 26.3.1  세트에 요소 추가하기 : 세트.add(요소)
a = {1, 2, 3, 4}
a.add(5)
print(a)

# 26.3.2  세트에서 특정 요소를 삭제하기 : 세트.remove(요소), 세트.discard(요소)

# remove(요소)는 세트에서 특정 요소를 삭제하고 요소가 없으면 에러를 발생시킵니다.
a.remove(3)
print(a)

a.remove(3)  # 없는 값을 삭제하라고 하면 에러 발생


# discard(요소)는 세트에서 특정 요소를 삭제하고 요소가 없으면 그냥 넘어갑니다.
# 다음은 세트 a에 2가 있으므로 2를 삭제하고, 3은 없으므로 그냥 넘어갑니다.
a.discard(2)
print(a)

a.discard(2)  # 제거할 요소가 없더라도 에러가 발생하지 않음
print(a)


# 26.3.3  세트에서 임의의 요소 삭제하기 : 세트.pop(요소)

# pop()은 세트에서 임의의 요소를 삭제하고 해당 요소를 반환합니다.
# 만약 요소가 없으면 에러를 발생시킵니다.

a = {1, 2, 3, 4}
a.pop()
print(a)

# 26.3.4  세트의 모든 요소를 삭제하기
a.clear()
print(a)

# 26.3.5  세트의 요소 개수 구하기
a = {1, 2, 3, 4}
len(a)


# 26.4 세트의 할당과 복사 ----------------------------------------------------------
# 세트도 객체를 분리할때는 copy 메서드를 사용해야 한다.



# 26.5 반복문으로 세트의 요소를 모두 출력하기 ---------------------------------------
a = {1, 2, 3, 4}

for i in a:
    print(i)

# 26.6 세트 표현식 사용하기 --------------------------------------------------------

# 세트는 for 반복문과 if 조건문을 사용하여 세트를 생성할 수 있습니다.
# 다음과 같이 세트 안에 식과 for 반복문을 지정하면 됩니다.

# {식 for 변수 in 반복가능한객체}
# set(식 for 변수 in 반복가능한객체)

a = {i for i in 'apple'}
print(a)

# 26.6.1  세트 표현식에 if 조건문 사용하기

# {식 for 변수 in 세트 if 조건식}
# set(식 for 변수 in 세트 if 조건식)

a = {i for i in 'pineapple' if i not in 'apl'}
print(a)


# 26.8 연습문제 : 공배수 구하기 ----------------------------------------------------

a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}
print(a & b)


# 26.9 심사문제 : 공약수 구하기

# 표준 입력으로 양의 정수 두 개가 입력됩니다.
# 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요.
# 단, 최종 결과는 공약수의 합으로 판단합니다.

one, two = map(int, input().split())

a = {i for i in range(1, one+1) if one % i == 0}
b = {i for i in range(1, two+1) if two % i == 0}

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)

