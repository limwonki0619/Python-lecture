# 파이썬 연습문제

# 1. 조건문 ---------------------------------------------------------------------------------------------------

# 1.1 연도를 입력으로 받아 윤년인지 아닌지를 출력하는 프로그램을 작성하시오. ----------------------------------

# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때
# 또는 400의 배수일 때이다. 예를들어, 2012년은 4의 배수라서 윤년이지만,
# 1900년은 4의 배수이지만, 100의 배수이기 때문에 윤년이 아니다.
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.)

# 4의 배수이면서 100의 배수가 아니고, 400의 배수일 때 윤년이다.

# 윤년 : 4의 배수이지만 100의 배수는 아니며, 400의 배수인 해
# 평년 : not 윤년

years = list(range(1900, 2013, 1))

for year in years:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, '윤년')
    else:
        print(year, '평년')

for year in years:
    if year % 400 == 0:
        print(year, '윤년')
    elif year % 4 == 0 and year % 100 != 0:
        print(year, '운년')
    else:
        print(year, '평년')        
        
# 1900년도 일때,
print(1900 % 4 == 0)    # T 4의 배수다.
print(1900 % 100 != 0)  # F 100의 배수다. -> 평년
print(1900 % 400 == 0)  # F 400의 배수가 아니다. -> 평년



# 모범답안 ------------------------------------------------------------------------------------------------------------

# 연도를 입력으로 받아 윤년인지 아닌지를 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

year = int(input('연도 입력> '))

if year % 4 == 0:
    if year % 400 == 0:
        print(year, '년은 윤년입니다.')
    elif year % 100 == 0:
        print(year, '년은 윤년이 아닙니다.')
    else:
        print(year, '년은 윤년입니다.')
else:
    print(year, '년은 윤년이 아닙니다.')
