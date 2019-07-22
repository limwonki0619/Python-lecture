# 응용문제 1

# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부른다.
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 이다.
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마인가?

def palindrome():
    maxI = 0
    maxK = 0
    pal = []
    for i in range(999, 101, -1):
        for k in range(999, 101-i, -1):
            value = i * k
            if str(value) == str(value)[::-1]:
                pal.append(value)
                maxI = i
                maxK = k

    print('세 자리 수 Palindrome 중 가장 큰 수는 : {0} x {1} = {2}'.format(maxI, maxK, max(pal)))

palindrome()
