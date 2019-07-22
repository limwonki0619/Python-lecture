# Unit 24 심사문제 1

# 표준 입력으로 문자열이 입력됩니다.
# 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야 합니다.

text = str(input())
words = text.split()

count = 0
for word in words:
    if word.strip(',.') == 'the':
        count += 1
print(count)

# Unit 24 심사문제 2

# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고,
# 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
# 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고
# 천단위로 ,(콤마)를 넣으세요.

price = list(map(int, input().split(';')))
price.sort(reverse=True)

for i in price:
    print('{0:>9,}'.format(i))  # 길이는 9, 오른쪽 정렬, 천 단위로 콤마, 텍스트는 i