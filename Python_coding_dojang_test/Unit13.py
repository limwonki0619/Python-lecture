# 13.7 심사문제 : 온라인 할인 쿠폰 시스템 만들기 

# 표준 입력으로 가격(정수)과 쿠폰 이름이 각 줄에 입력됩니다.
# Cash3000 쿠폰은 3,000원, Cash5000 쿠폰은 5,000원을 할인합니다.
# 쿠폰에 따라 할인된 가격을 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).


price = int(input())
coupon = str(input())

if coupon == 'Cash3000':
    print(price - int(coupon[-4:]))

if coupon == 'Cash5000':
    print(price - int(coupon[-4:]))
