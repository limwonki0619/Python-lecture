# 1.3 세 정수 a, b, c를 입력으로 받아 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. -----------------------------

def order():
    a, b, c = map(int, input().split())
    txt = [a, b, c]
    for i in range(0, len(txt)-1):  # list의 0 1 2 요소 가져오기
        for k in range(i+1, len(txt)):
            if txt[i] > txt[k]:
                txt[i], txt[k] = txt[k], txt[i]
    print(txt[1])

order()


# 모범답안 -------------------------------------------------------------------------------

# 세 정수 a, b, c를 입력으로 받아 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오
a, b, c = map(int, input('정수 3개 입력> ').split())

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if a > b:
        print(a)
    else:
        print(b)