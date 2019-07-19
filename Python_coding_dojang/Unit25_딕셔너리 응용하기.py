# Unit 25. 딕셔너리 응용하기


# 25.1 딕셔너리 조작하기 -----------------------------------

# 25.1.1 딕셔너리에 키-값 쌍 추가하기

# setdefault: 키-값 쌍 추가
# update: 키의 값 수정, 키가 없으면 키-값 쌍 추가

# 25.1.2  딕셔너리에 키와 기본값 저장하기
x = dict(zip(['a', 'b', 'c', 'd'], [10, 20, 30, 40]))
x.setdefault('f', 100)  # setdefault(키)는 딕셔너리에 키-값 쌍을 추가합니다

# 25.1.3  딕셔너리에서 키의 값 수정하기
x.update(e=90)
x.update(g=1000)
x.update(a=900, k=60)

# update(키=값)은 키가 문자열일 때만 사용할 수 있습니다.
# 만약 키가 숫자일 경우에는 update(딕셔너리)처럼 딕셔너리를 넣어서 값을 수정할 수 있습니다.

y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
print(y)

# 25.1.4  딕셔너리에서 키-값 쌍 삭제하기

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
x.pop('z', 0)  # 키가 없을 떄는 기본값(0)만 반환

# 25.1.5  딕셔너리에서 임의의 키-값 쌍 삭제하기

# popitem()은 딕셔너리에서 임의의 키-값 쌍을 삭제한 뒤
# 삭제한 키-값 쌍을 튜플로 반환합니다.

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
key, value = x.popitem()  # 파이썬 3.6 이상에서는 맨 뒤의 값이 삭제된다.
print(key, value)

# 25.1.6  딕셔너리의 모든 키-값 쌍을 삭제하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)

# 25.1.7  딕셔너리에서 키의 값을 가져오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('a')


# 25.1.8  딕셔너리에서 키-값 쌍을 모두 가져오기
# * items: 키-값 쌍을 모두 가져옴
# * keys: 키를 모두 가져옴
# * values: 값을 모두 가져옴

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.items()
x.keys()
x.values()

# 25.1.9  리스트와 튜플로 딕셔너리 만들기
keys = ['a', 'b', 'c', 'd']  # 튜플도 가능
x = dict.fromkeys(keys)
print(x)

import random
x = dict.fromkeys(keys, 0)
print(x)

# 참고
print(x['z'])  # 지금까지 사용한 딕셔너리(dict)는 없는 키에 접근했을 경우 에러가 발생합니다

# defaultdict는 없는 키에 접근하더라도 에러가 발생하지 않으며 기본값을 반환합니다.
# defaultdict는 collections 모듈에 들어있으며 기본값 생성 함수를 넣습니다.

from collections import defaultdict    # collections 모듈에서 defaultdict를 가져옴

y = defaultdict(int)
print(['z'])  # 셔너리 y에는 키 'z'가 없지만 y['z']와 같이 키의 값을 가져와보면 0이 나옵니다. 왜냐하면 기본값을 0으로 설정했기 때문입니다.


# 기본값을 'python'으로 출력하기
def return_python():
    return 'python'

y = defaultdict(return_python)
print(y['a'])
print(y[0])

z = defaultdict(lambda: 'python')
print(z['a'])
print(y[0])


# 25.2 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기 --------------------------------------------
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=' ')  # 키만 출력

# for 키, 값 in 딕셔너리.items():  키와 값 모두 출력하기
#      반복할 코드
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

for key, value in x.items():
    print(key, value)


# 25.2.1  딕셔너리의 키만 출력하기

# * items: 키-값 쌍을 모두 가져옴
# * keys: 키를 모두 가져옴
# * values: 값을 모두 가져옴
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys():
    print(key, end = ' ')

# 25.2.2  딕셔너리의 값만 출력하기
for value in x.values():
    print(value)


# 25.3 딕셔너리 표현식 사용하기 ------------------------------------------------

# * {키: 값 for 키, 값 in 딕셔너리}
# * dict({키: 값 for 키, 값 in 딕셔너리})

keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
y = {key: random.randint(1, 6) for key, value in dict.fromkeys(keys).items()}
z = {key: random.randint(1, 6) for key in ['a','b','c','d']}

# 딕셔너리 표현식을 사용할 때는 for in 다음에 딕셔너리를 지정하고 items를 사용합니다.
# 그리고 키, 값을 가져온 뒤에는 키: 값 형식으로 변수나 값을 배치하여 딕셔너리를 생성하면 됩니다.


# 25.3.1  딕셔너리 표현식에서 if 조건문 사용하기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    if value == 20:
        x.pop(key)
print(x)

# 딕셔너리는 for 반복문으로 반복하면서 키-값 쌍을 삭제하면 안 됩니다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)



# 25.4 딕셔너리 안에서 딕셔너리 사용하기
# * 딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}

terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

print(terrestrial_planet['Venus']['mean_radius'])  # 반지름

# 딕셔너리[키][키]
# 딕셔너리[키][키] = 값




# 25.5 딕셔너리의 할당과 복사 ---------------------------------------------------

# 리스트와 마찬가지로 딕셔너리도 할당과 복사는 큰 차이점이 있습니다.
# 먼저 딕셔너리를 만든 뒤 다른 변수에 할당합니다.
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
print(x is y)  # True

# x와 y는 같으므로 y['a'] = 99와 같이 키 'a'의 값을 변경하면
# 딕셔너리 x와 y에 모두 반영됩니다.

# 딕셔너리 x와 y를 완전히 두 개로 만들려면
# copy 메서드로 모든 키-값 쌍을 복사해야 합니다.

y = x.copy()
print(x is y)  # False


# 25.5.1  중첩 딕셔너리의 할당과 복사 알아보기
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()  # 중첩 딕셔너리는 copy 메서드로 복사가 불가능하다.

# 중첩 딕셔너리의 복사는 deepcopy를 사용해야 한다.
import copy
y = copy.deepcopy(x)

