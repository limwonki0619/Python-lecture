# 1.4 세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부른다.
# (여기서 a < b < c 이고 a + b > c)
# 예를 들면, 32 + 42 = 9 + 16 = 25 = 52 이므로 3, 4, 5는 피타고라스 수다.
# a + b + c = 1000 인 피타고라스 수를 구하시오. (답은 한가지 뿐이다.)

# a^2 + b^2 = c^2
# c = (1000 - a - b)

# 코드출처 : https://www.opentutorials.org/module/2980/17440
for a in range(1, 1000):    # a에 들어갈 수 있는 수를 모두 뽑는다.
    for b in range(1, a):   # 뽑은 a의 범위에서 조합가능한 모든 b를 뽑는다.
        if a**2 + b**2 == (1000 - a - b)**2:  # a^2 + b^2 == c^2이 되는 값을 구한다.
            print('a =',a , 'b =', b, 'c =', 1000 - a - b)  # 조건이 만족하는 a와 b와 c를 출력한다.
            print(a**2, '+', b**2, '=', (1000 - a - b)**2)
            break                                           # 조건이 만족되면 루프를 빠져나온다.


# 모범답안 --------------------------------------------------------------------------------------

# a + b + c = 1000 인 피타고라스 수
# (단, a < b < c 이고 a + b > c)
outerBreak = False
for a in range(1, 333):
    if outerBreak:
        break
    for b in range(a+1, 500):
        c = 1000 - a - b
        if c < b:
            continue
        if a**2 + b**2 == c**2:
            print(a, b, c, a+b+c)
            print(a**2, b**2, c**2)
            outerBreak = True
            break;