# Unit 15. elif를 사용하여 여러 방향으로 분기하기

# if 콜라 버튼을 눌렀다면:
#     콜라를 내보냄
# elif 사이다 버튼을 눌렀다면:
#     사이다를 내보냄
# elif 환타 버튼을 눌렀다면:
#     환타를 내보냄:
# else:
#     제공하지 않는 메뉴

# 15.1 elif 사용하기 -----------------------------------------------------
# elif는 else인 상태에서 조건식을 지정할 때 사용하며 else if라는 뜻입니다.
# 물론 if, else와 마찬가지로 조건식 끝에 :(콜론)을 붙여야 하고,
# elif 단독으로 사용할 수 없습니다.

x = 20

if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')

# 15.1.1 if, elif, else를 모두 사용하기
# elif와 else는 단독으로 사용할 수 없으며 if, else 형태로 사용하거나,
# if, elif, else 형태로 사용합니다. 이번에는 if, elif, else를 모두 사용해보겠습니다.

# if 조건식:
#     코드1
# elif 조건식:
#     코드2
# else:
#     코드3

x = 30

if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')

# 15.1.2 음료수 자판기 만들기
button = int(input())

if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

# 15.3 연습문제 : if, elif, else 모두 사용하기 --------------------------------
x = int(input())

if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# 15.4 심사문제 : 교통카드 시스템 만들기 --------------------------------------
age = int(input())
balance = 9000    # 교통카드 잔액

if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
elif 19 <= age:
    balance -= 1250

print(balance)

