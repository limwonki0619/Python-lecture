# Unit 24. 문자열 응용하기

# 24.1 문자열 조작하기 ----------------------------------------------------

# 문자열은 문자열을 조작하거나 정보를 얻는 다양한 메서드(method)를 제공합니다
# (메서드는 '?34.1 클래스와 메서드 만들기'에서 설명하겠습니다).
# 파이썬에서 제공하는 문자열 메서드는 여러 가지가 있지만
# 여기서는 자주 쓰는 메서드를 다루겠습니다.

# 24.1.1 문자열 바꾸기

# * replace('바꿀문자열', '새문자열')은 문자열 안의 문자열을 다른 문자열로 바꿉니다.
#   (문자열 자체는 변경하지 않으며 바뀐 결과를 반환합니다.)

print('hello, world!'.replace('world', 'Python'))

# 바뀐 결과를 유지하고자 한다면 문자열이 저장된 변수에 replace를 적용하면 됩니다.
s = 'hello?'
s = s.replace('o', 'world')
print(s)


# 24.1.2 문자 바꾸기

# replace는 문자열을 바꿨는데 문자를 바꾸는 방법도 있겠죠?
# translate는 문자열 안의 문자를 다른 문자로 바꾼다.
# 먼저 str.maketrans('바꿀문자', '새문자')로 변환 테이블을 만든다.
# 그 다음 translate(테이블)을 사용하면 문자를 바꾼 뒤 결과를 반환한다.

table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))


# 24.1.3 문자열 분리하기
# split()은 공백을 기준으로 문자열을 분리하여 리스트로 만듭니다.
# 지금까지 input으로 문자열을 입력받은 뒤 리스트로 만든 메서드가
# 바로 이 split입니다.

print('apple pear grape pineapple orange'.split())

# split('기준문자열')을 지정하면 기준 문자열로 문자열을 분리한다.

print('apple, pear, grape, pineapple, orange'.split(', '))


# 24.1.4 구분자 문자열과 문자열 리스트 연결하기 : '구분자'.join(리스트)

# join(리스트)는 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만듭니다.
# 다음은 공백 ' '에 join을 사용하여 각 문자열 사이에 공백이 들어가도록 만듭니다.

print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))

# 24.1.5 소문자를 대문자로 바꾸기 : '문자열'.upper()
print('python'.upper())


# 24.1.6 대문자를 소문자로 바꾸기 : '문자열'.lower()
print('PYTHON'.lower())

# 24.1.7 왼쪽 공백 삭제하기 : '문자열'.lstrip()
print('      python       '.lstrip())


# 24.1.7 오른쪽 공백 삭제하기 : '문자열'.rstrip()
print('      python       '.lstrip())

# 24.1.10 왼쪽의 특정 문자 삭제하기 : lstrio()
print(',        python.'.lstrip(',. '))  # 왼쪽의 특정 문자, 공백 다 제거

# 24.1.11 오른쪽의 특정 문자 삭제하기 : rstrip()
print(',  python.,,,     '.rstrip(',. '))  # 오른쪽의 특정 문자, 공백 다 제거

# 24.1.12 양쪽의 특정 문자 삭제하기 : strip()
print(',    python.... ,'.strip(",. "))  # 양쪽의 특정 문자, 공백 제거

# 참고 : 구두점을 간단하게 삭제하기 : string.punctuation
import string as st
print('\>^&%$%$, python..!!!$%^%@'.strip(st.punctuation + st.whitespace))  # 구두점과 공백 제거
print(', python..'.strip(st.punctuation).strip())  # 메서드 체이닝


# 24.1.13 문자열을 왼쪽으로 정렬하기 : ljust(길이)

'  python'.ljust(10)  # 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하며 남는 공간을 공백으로 채움

# 24.1.14 문자열을 오른쪽으로 정렬하기 : rjust(길이)
' python'.rjust(10)

# 24.1.15 문자열을 가운데 정렬하기 : center(길이)
'python'.center(10)



# 24.1.16 메서드 체이닝
'python'.rjust(10).upper()


# 24.1.17 문자열 왼쪽에 0 채우기 : zfill(길이) == zero fill
'35'.zfill(4)  # 지정된 길이에 맞춰 문자열의 왼쪽에 0을 채운다
'3.5'.zfill(6)


# 24.1.18 문자열 위치찾기 : find('찾을 문자열')

'apple pineapple'.find('pl')  # pl이 두개 있지만 처음 찾은 pl의 인덱스 2를 반환
'apple pineapple'.find('xy')  # -1이 출력되는경우 이는 해당 문자열이 없음을 의미


# 24.1.19 오른쪽에서부터 문자열 위치 찾기 : rfind('찾을 문자열')
'apple pineapple'.rfind('pl')  # 오른쪽에서부터 찾을 수 있다.
'apple pineapple'.rfind('xy')  # -1이 출력되는경우 이는 해당 문자열이 없음을 의미


# 24.1.20 문자열 위치 찾기 : index('찾을 문자열), rindex('찾을 문자열)
'apple pineapple'.index('pl')

# 24.1.21 오른쪽에서부터 문자열 위치 찾기 : rindex('pl')
'apple pineapple'.rindex('pl')

# 24.1.22 문자열 개수 세기  : count('문자열')
'apple pineapple'.count('pl')



# 24.2 문자열 서식 지정자와 포매팅 사용하기 -------------------------------
# format 함수에 들어가는 숫자는 기본적으로 str 타입


# 24.2.1 서식 지정자로 문자열 넣기 : '%s'
# * '%s' % '문자열'
# s == string

print('I am %s.' % 'james')

name = 'maria'
print('I am %s.' % name)


# 24.2.2 서식 지정자로 숫자 넣기 : '%d'
# * '%d' % 숫자
# d == decimal intege
print('I am %d years old.' % 20)


# 24.2.3 서식 지정자로 소수점 표현하기 : '%f'
# * '%f' % 숫자
# f == fixed point, 기본적으로 소수점 이하 6자리까지 표시함.
print('%f' % 2.3)

# 소수점 이하 자릿수를 지정하고 싶으면 f 앞에 .(점)과 자릿수를 지정해주면 된다.
# * '.자릿수f' % 숫자
print('%.2f' % 2.3)
print('%.5f' % 2.3)


# 24.2.4 서식 지정자로 문자열 정렬하기
# * %길이s
print('%10s' % 'python')  # %뒤에 숫자를 붙이면 문자열을 지정된 길이로 만든 뒤 오른쪽으로 정렬하고 남는 공간을 공백으로 채운다.


# 참고 : 자릿수가 다른 숫자 출력하기
# %길이d (기본적으로 오른쪽 정렬)
print('%10d' % 150)

# %길이.자릿수f
print('%10.2f' % 2.3)
print('%10.2f' % 2000.3)


# 왼쪽정렬을 위해서는 -를 붙여야함
print('%-10s' % 'python')  # 'python    '


# 24.2.5 서식 지정자로 문자열 안에 값 여러개 넣기
# * '%d %s' % (숫자, '문자열')
print('Today is %d %s.' % (3, 'April'))


# 24.2.6 format 메서드 사용하기 ***
# '{인덱스}.format(값)

print('Hello, {0}'.format('world'))
print('Hello, {0}'.format('100'))


# 24.2.7 format 메서드로 값을 여러 개 넣기
print('Hello, {0} {2} {1}'.format('python', 'Script', 3.6))


# 24.2.8 format 메서드로 같은 값을 여러 개 넣기
print('{0} {0} {1} {1}'.format('python', 'Script'))

# 24.2.9 format 메서드에서 인덱스 생략하기
print('Hello, {} {} {}'.format('Python', 'Script', 3.6))

# 24.2.10 format 메서드에서 인덱스 대신 이름 지정하기
print('Hello {language} {version}'.format(language='Python', version=3.6))

# 24.2.11 문자열 포매팅에 변수를 그대로 사용하기
language = 'Python'
version = 3.6

print(f'Hello, {language} {version}')  # 여기서 'f'sms formatting를 뜻함

# 24.2.12 format 메서드로 문자열 정렬하기
# * '{인덱스:<길이}'.format(값)
# 인덱스 뒤에 ':'을 붙이고 정렬할 방향과 길이를 정해준다

print('{0:<10}'.format('python'))  # 길이 10, 왼쪽 정렬
print('{0:<10}'.format('python'))  # 길이 10, 오른쪽 정렬

# 24.2.13 숫자 개수 맞추기
# * '%0개수d' % 숫자
# * '{인덱스:0개수d}'.format(숫자)

print('%03d' % 1)
print('%05d' % 1)
print('{0:03d}'.format(35))
print('{0:05d}'.format(35))

# * '%0개수.자리수f' % 숫자
# * '{인덱스:0개수.자리수f}'.format(숫자)

print('%08.2f' % 3.6)  # 실수에서는 숫자 개수에 정수부분, 소수점, 소수점 이하 자릿수가 모두 포함된다.
# 따라서 '00005' 5개, '.'1개, '60' 2개 총 8개가 된다.
print('{0:08.2f}'.format(150.37))


# 24.2.14 채우기와 정렬을 조합해서 사용하기
# 문자열 포매팅은 채우기와 정렬을 조합해서 사용할 수 있습니다.
# 다음과 같이 { }에 인덱스, 채우기, 정렬, 길이, 자릿수, 자료형 순으로 지정해줍니다.
# * '{인덱스:[[채우기]정렬][길이][. 자릿수][자료형]}'

'{0:0<10}'.format(15)         # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움
'{0:0>10}'.format(15)         # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움
'{0:0>10.2f}'.format(15)      # 길이 10, 오른쪽으로 정렬하고 소수점 자릿수는 2자리

# 특히 채우기 부분에 0이 아닌 다른 문자를 넣어도 됩니다. 공백을 넣어도 되고, 문자를 넣어도 됩니다.
# 만약 채우기 부분을 생략하면 공백이 들어갑니다.
'{0: >10}'.format(15)         # 길이 10, 오른쪽으로 정렬하고, 남는 공간은 공백으로 채우기
'{0:>10}'.format(15)          # 같은결과, 채우기 생략
'{0:x>10}'.format(15)         # 남은공간을 x로 채움

# 참고 : 금액에서 천단위로 콤마 넣기
format(1493500, ',')
type(format(1493500, ','))    # 출력값은 str

'%20s' % format(1493500, ',') # 길이 20, 오른쪽 정렬
'{0:,}'.format(1493500)
'{0:>20,}'.format(1493500)    # 길이 20, 오른쪽 정렬 후 천단위 컴마


# 연습문제 : 파일 경로에서 파일명만 가져오기
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
path.split('\\')[-1]


# 모범답안

# x = path.split('\\')
# filename = x[-1]
# 또는

# x = path.split('\\')
# x.reverse()
# filename = x[0]
# 또는

# filename = path[path.rfind('\\') + 1:]

# 24.5 심사문제 1 ------------------------------------------------

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

# 24.6 심사문제 2 -------------------------------------------------

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
