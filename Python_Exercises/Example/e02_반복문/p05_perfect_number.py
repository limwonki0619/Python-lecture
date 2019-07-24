# 자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수

def getDivisor(number):  # 자기 자신을 제외한 약수를 구하는 함수
    result = list()
    for i in range(1, number):
        if number % i == 0:
            result.append(i)
    return result

def getPerfectNumber(n):
    for i in range(1, n+1):
        div = getDivisor(i)
        if i == sum(div):
            print(i)

getPerfectNumber(10000)




# 모범답안 ---------------------------------------------------------

# def getDivisor(number):
#     result = list()
#     for i in range(1, number):
#         if number % i == 0:
#             result.append(i)
#     return result
#
# n = int(input('정수 입력> '))
# for i in range(1, n+1):
#     div = getDivisor(i)
#     if i == sum(div):
#         print(i)