# 17.6 심사문제

# 표준 입력으로 금액(정수)이 입력됩니다.
# 1회당 요금은 1,350원이고, 교통카드를 사용했을 때마다의 잔액을 각 줄에
# 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 최초 금액은 출력하지 않아야 합니다. 그리고 잔액은 음수가 될 수 없으며
# 잔액이 부족하면 출력을 끝냅니다.

money = int(input())

# while money > 0:
#     money -= 1350
#     if money <= 0:
#         break
#     print(money)

while money >= 1350:
    money -= 1350
    print(money)