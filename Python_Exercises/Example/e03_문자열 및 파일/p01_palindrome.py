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


# 응용문제 2

# 시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데,
# 예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는 알파벳이 출력되는 것이다.
# 예를 들어 바꾸려는 단어가 'CAT'고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
# 어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성하시오.

# - 입력 : 화면에서 문자열과 n값을 입력받는다. (예: ROSE 5)
# - 출력 : 암호화된 문자열을 출력

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
len(a)

def ceaser(string, n):
    length = ord('Z') - ord('A') + 1  # 알파벳 갯수
    list_s = list(string)
    new_s = ''  # 빈 문자열 생성

    for s in list_s:
        if ord(s) + n < ord('Z'):
            new_s += chr(ord(s) + n)
        else:
            new_s += chr(ord(s) + n - length)  # 알파벳 'Z'의 인데스 숫자를 넘으면, 앞으로 26칸 당겨라

    print('암호화 전 문자 = {0}'.format(string))
    print('암호화 후 문자 = {0}'.format(new_s))

ceaser('CAT', 5)

# 응용문제 3


# 응용문제 4


# 응용문제 5

# 다음의 지시대로 폴더와 파일을 프로그램에서 만드시오.
# 랜덤으로 1, 2, 3 중 하나를 내용으로 갖는 txt 파일100개를
# 하나의 디렉토리(c:/Temp/Ex04) 안에 생성하는 코드를 작성하시오.

#   (파일 제목은 4자리 정수를 랜덤으로 할당.
#   ex - 1382.txt , 0201.txt , 9012.txt , ......... )
#   제목이 0000~3333 인 txt 파일은 low 폴더로,
#   3334~6666인 txt 파일은 mid 폴더로,
#   6667~9999 인 파일은 high 폴더로 이동시키는 코드를 작성하시오.

#   low, mid, high 폴더 안에 제목이 1, 2, 3 인 폴더를 각각 만들고, txt 파일 안의 내용에 따라
#   txt파일을 폴더안으로 이동시켜 분류하시오.
#   결론적으로 c:/Temp/Ex04 폴더 밑에는 low, mid, high 폴더 3개가 생기고,
#   이 각각의 폴더에는 1, 2, 3 폴더가 각각 생기고 이 폴더밑에 파일이 들어 있어야 함.

import os
os.getcwd()

import random

PATH = 'D:/limworkspace/Python-lecture/Python_Exercises/Example/e03_문자열 및 파일/p04_file'  # 생성할 폴더 경로 설정
os.mkdir(PATH)  # 해당 경로에 폴더 생성
os.chdir(PATH)  # 해당 경로로 작업 폴더 변경
os.getcwd()

for dirname in ('low', 'mid', 'high'):  # 생성 폴더 이름
    os.mkdir(PATH + '/' + dirname)      # 각각 이름으로 폴더 생성 준비
    for num in ('1', '2', '3'):         # 각각 숫자로 내부 폴더 생성 준비
        os.mkdir(PATH + '/' + dirname + '/' + num)  # 작업 디렉토리 내 폴더 생성

for i in range(100):
    file_number = random.randint(1111, 9999)
    rn = str(random.randint(1, 3))

    if file_number <= 3333:   # 이동할 파일 위치
        dirname = 'low'
    elif file_number <= 6666:
        dirname = 'mid'
    else:
        dirname = 'high'

    with open(dirname + '/' + rn + '/' + '{0:4>}.txt'.format(file_number), 'w') as file:  # 각각의 경로로 하는 파일 생성
        file.write(rn)

