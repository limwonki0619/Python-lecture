# Unit 25. 딕셔너리 응용하기

# 25.1 딕셔너리 조작하기 ----------------------------------------------------

# 25.1.1  딕셔너리에 키-값 쌍 추가하기
# * setdefault : 키-값 쌍 추가
# * update : 키의 값 수정, 키가 없으면 키-값 쌍 추가

# 25.1.2 딕셔너리에 키와 기본값 저장하기 : setdefault
x = dict(zip(['a', 'b', 'c', 'd'], [10, 20, 30, 40]))
x.setdefault('e')  # 키 'e'를 추가, 값은 default인 None가 들어감
print(x)
x.setdefault('f', 100)  # 키와 값을 추가
print(x)

# 25.1.3  딕셔너리에서 키의 값 수정하기 : update
x.update(a = 90, b = 30)  # 키가 문자열일 때문 사용할 수 있다.
y = {1:'one', 2:'two'}    # 키가 숫자일 경우는 ?

# update(딕셔너리)로 수정이 가능하다.
y.update({1:'One', 3:'THREE'})
print(y)

# 또한 리스트와 튜플로도 수정이 가능하다.
y.update([[2, 'TWO'], [4, 'FOUR']])  # 리스트
print(y)

y.update(((2, 'TWO'), (4, 'FOUR')))  # 튜플
print(y)

# 참고 : setdefault와 update의 차이

# setdefault는 키-값 추가만 할 수 있고, 수정은 불가
# update는 키-값 추가와 수정 모두 가능


# 25.1.4  딕셔너리에서 키-값 쌍 삭제하기 : pop

x = dict(zip(['a', 'b', 'c', 'd'], [10, 20, 30, 40]))
x.pop('a')    # pop(키)는 딕셔너리에서 특정 키-값 쌍을 삭제한뒤 삭제한 값을 반환
x.pop('b', 0) # pop(키, 기본값) 처럼 기본값을 지정하면 딕셔너리에 키가 있을때는 해당 값 반환
              # 키가 없을때는 기본값만 반환

# 25.1.5  딕셔너리에서 임의의 키-값 쌍 삭제하기 : popitem()

# popiten()은 딕셔너리에서 임의의 키-값 쌍을 삭제한 뒤 삭제한 키-값 쌍을 튜플로 반환
# Python 3.7 이상에서는 리스트의 마지막 요소를 삭제하고 반환

x = dict(zip(['a', 'b', 'c', 'd'], [10, 20, 30, 40]))
x.popitem()

# 25.1.6  딕셔너리의 모든 키-값 쌍을 삭제하기 : clear()
x = dict(zip(['a', 'b', 'c', 'd'], [10, 20, 30, 40]))
x.clear()  # 딕셔너리의 모든 키-값 쌍을 삭제


# 25.1.7  딕셔너리에서 키의 값을 가져오기 : get()
x = dict(zip(['a', 'b', 'c', 'd'], [10, 20, 30, 40]))
x.get('a')  # 딕셔너리에서 키'a' 값 반환

# 25.1.8  딕셔너리에서 키-값 쌍을 모두 가져오기 : items, keys, values

# 1. items  : 키-값 쌍을 모두 가져옴
# 2. keys   : 키를 모두 가져옴
# 3. values : 값을 모두 가져옴

x = dict(zip(['a', 'b', 'c', 'd'], [10, 20, 30, 40]))
x.items()
x.keys()
x.values()


# 25.1.9  리스트와 튜플로 딕셔너리 만들기

y = dict.fromkeys(['a', 'b', 'c', 'd'], 4)
print(y)

# 25.2 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기 -----------------------
for key, value in y.items():
    print(key, value)

# 25.2.1  딕셔너리의 키만 출력하기
for key in y.keys():
    print(key)

# 25.2.2 딕셔너리의 값만 출력하기
for value in y.values():
    print(value)



# 25.3 딕셔너리 표현식 사용하기 ---------------------------------------------

# {키: 값 for 키, 값 in 딕셔너리}
# dict({키: 값 for 키, 값 in 딕셔너리})
keys = ['a', 'b', 'c', 'd']

print({key: value for key, value in dict.fromkeys(keys).items()})


# 25.3.1  딕셔너리 표현식에서 if 조건문 사용하기  --------------------------

x = dict(zip(['a', 'b', 'c', 'd'], [10, 20, 30, 40]))

for key, value in x.items():  # 오류
    if value == 20:
        del x[key]

# 딕셔너리는 for 반복문으로 반복하면서 키-값 쌍을 삭제하면 안 됩니다.
# 이때는 딕셔너리 표현식에서 if 조건문을 사용하여 삭제할 값을 제외하면 됩니다.

print({key: value for key, value in x.items() if value != 20})


# 일반 딕셔너리는 copy 모듈의 copy 메서드로 객체 분리
# 중첩 딕셔너리는 copy 모듈의 deepcopu 메서드로 갹체 분리



# 25.7 연습문제: 평균 점수 구하기 -----------------------------------------

maria = dict(zip(['korean', 'english', 'mathematics', 'science'], [94, 91, 89, 83]))
print(maria)

average = 0
for value in maria.values():
    average += value/len(maria)
print(average)

# 모범답안
average = sum(maria.values())/len(maria)
print(average)



# 25.8 심사문제 : 딕셔너리에서 특정 값 삭제하기

# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고,
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다.
# 다음 코드를 완성하여 딕셔너리에서
# 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.

keys = input().split()
value = list(map(int, input().split()))
x = dict(zip(keys, value))

x = {key: value for key, value in x.items() if key != 'delta' and value != 30}
print(x)