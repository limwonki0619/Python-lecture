# 12.1 딕셔너리 만들기
# 딕셔너리는 { }(중괄호) 안에 키: 값 형식으로 저장하며, 각 키와 값은 ,로 구분해준다.
# - 딕셔너리 = {키1: 값, 키2:값2}
lux = {'health': 450, 'mana': 314, 'melee': 550, 'armor': 18.72}
print(lux)

# 12.1.1 키 이름이 중복되면?
lux = {'health': 450, 'health': 800, 'mana': 314, 'melee': 550, 'armor': 18.72}
print(lux)  # 딕셔너리에 키가 중복되면 가장 뒤에 있는 값만 사용된다.

# 12.1.2 딕셔너리 키의 자료형
# 딕셔너리의 키는 문자열뿐만 아니라 정수, 실수, 불도 사용할 수 있으며 자료형을 섞어서 사용해도 됩니다. 그리고 값에는 리스트, 딕셔너리 등을 포함하여 모든 자료형을 사용할 수 있습니다.
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print(x)

# 12.1.3 빈 딕셔너리 만들기
# 빈 딕셔너리를 만들 때는 { }만 지정하거나 dict를 사용하면 됩니다. 보통은 { }를 주로 사용합니다.
x = {}
print(x)

x = dict()
print(x)

# 12.1.4 dict의 다양한 활용법으로 딕셔너리 만들기
# 딕셔너리 = dict(키1=값1, 키2=값2)
# 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
# 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
# 딕셔너리 = dict({키1: 값1, 키2: 값2})

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)  # 다양한 딕셔너리 문법 적용이 가능

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [400, 334, 550, 18.72]))
print(lux2)  # zip함수로 키와 값을 각각 묶어줄 수 있다.

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(lux4)

# 12.2 딕셔너리의 키에 접근하고 값 할당하기
print(lux['health'])
print(lux['armor'])

# 12.2.1 딕셔너리의 키에 값 할당하기
lux['health'] = 2034  # 키에 해당하는 값 변경하기
lux['armor'] = 20.15  # 키에 해당하는 값 변경하기
print(lux)

lux['mana_regen'] = 3.28  # 딕셔너리 추가
print(lux)

print(lux['attact'])  # 딕셔너리에 없는 키를 호출하면 에러 발생

# 12.2.2 딕셔너리에 키가 있는지 확인하기
print('health' in lux)


# 12.2.3 딕셔너리의 키 개수 구하기
print(len(lux))  # 딕셔너리에서 Key의 갯수 구하기
