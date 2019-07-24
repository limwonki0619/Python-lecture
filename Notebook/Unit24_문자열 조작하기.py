# Unit 24. 문자열 응용하기

# 24.1 문자열 조작하기 -----------

# 24.1.1 문자열 바꾸기
'Hello world!'.replace('world', 'python')
s = 'Hello world!'
s.replace('world', 'python')


# 24.1.2 문자 바꾸기
table = str.maketrans('aeiou', '12345')  # str_replace
'apple'.translate(table)

# 24.1.3 문자 분리하기
'apple pear grape pineapple orange'.split()          # 구분자로 문자열 분리하기
'apple, pear, grape, pineapple, orange'.split(', ')  # 구분자로 문자열 분리하기

# 24.1.4 문자 연결하기
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])  # 공백으로 리스트 연결하기
'-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])  # '-'로 리스트 연결하기

# 24.1.5 대소문자 바꾸기
'python'.upper()  # 대문자로 변경
'PYTHON'.lower()  # 소문자로 변경
'PytHon'.lower()

# 24.1.6 공백 삭제
'   Python   '.lstrip()  # 왼쪽 공백 삭제
'   Python   '.rstrip()  # 오른쪽 공백 삭제
'   Python   '.strip()   # 양쪽 공백 삭제

# 24.1.7 특정문자 삭제
', python.'.lstrip(',.')  # 왼쪽의 특정문자 삭제
', python.'.rstrip(',.')  # 오른쪽의 특정문자 삭제
', python.'.strip(',.')   # 양쪽의 특정 문자 삭제

import string # 구두점 삭제
', python.'.strip(string.punctuation)

# 24.1.8 문자열 정렬
'python'.ljust(10)  # 문자열을 길이로 만든 후 왼쪽 정렬
'python'.rjust(10)  # 문자열을 길이로 만든 후 오른쪽 정렬
'python'.center(10) # 문자열을 길이로 만든 후 가운데 정렬

# 24.1.9 메서드 체이닝
'python'.rjust(10).upper()  # 문자열을 길이로 만들고 오른쪽 정렬 후 대문자로 변경


# 24.1.10 문자열 왼쪽에 0채우기
'35'.zfill(4)        # 숫자 앞에 0을 채움, 숫자는 총 길이
'3.5'.zfill(6)       # 숫자 앞에 0을 채움, 숫자는 총 길이
'hello'.zfill(10)    # 문자열 앞에 0을 채울 수도 있음, 숫자는 총 길이

# 24.1.11 문자열 위치 찾기(디폴트는 왼쪽 )
'apple pineapple'.find('pl')   # 해당 문자가 있는 (첫)인덱스 출력
'apple pineapple'.find('xy')   # 해당 문자가 없는 경우 '-1' 출력
'apple pineapple'.index('pl')  # find와 같음

'apple pineapple'.rfind('pl')  # 해당 문자를 오른쪽에서 부터 찾음
'apple pineapple'.rfind('xy')
'apple pineapple'.rindex('pl') # rfind와 같음

# 24.1.12 문자열 개수 세기
'apple pineapple'.count('pin')  # 'pin'을 포함하는 개수 출력

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

print('%08.2f' % 3.6)  # 실수에서는 숫자 개수에 정수부분, 소수점, 소수점 이하 자릿수가
# 따라서 '00005' 5개, '.'1개, '60' 2개 총 8개가 된다.
print('{0:08.2f}'.format(150.37))

# 24.2.14 채우기와 정렬을 조합해서 사용하기
# 문자열 포매팅은 채우기와 정렬을 조합해서 사용할 수 있습니다.
# 다음과 같이 { }에 인덱스, 채우기, 정렬, 길이, 자릿수, 자료형 순으로 지정해줍니다.
# * '{인덱스:[[채우기]정렬][길이][. 자릿수][자료형]}'

'{0:0<10}'.format(15)  # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로
'{0:0>10}'.format(15)  # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로
'{0:0>10.2f}'.format(15)  # 길이 10, 오른쪽으로 정렬하고 소수점 자릿수는 2

# 특히 채우기 부분에 0이 아닌 다른 문자를 넣어도 됩니다. 공백을 넣어도 되고, 문자를 넣어도 됩니다.
# 만약 채우기 부분을 생략하면 공백이 들어갑니다.
'{0: >10}'.format(15)  # 길이 10, 오른쪽으로 정렬하고, 남는 공간은 공백
'{0:>10}'.format(15)  # 같은결과, 채우기 생략
'{0:x>10}'.format(15)  # 남은공간을 x로 채움

# 참고 : 금액에서 천단위로 콤마 넣기
format(1493500, ',')
type(format(1493500, ','))  # 출력값은 str

'%20s' % format(1493500, ',')  # 길이 20, 오른쪽 정렬
'{0:,}'.format(1493500)
'{0:>20,}'.format(1493500)  # 길이 20, 오른쪽 정렬 후 천단위 컴마


'125,000'.zfill(10)

