# Unit 27. 파일 사용하기

# 27.1 파일에 문자열 쓰기, 읽기 ----------------------------------------

# 27.1.1  파일에 문자열 쓰기

# 파일에 문자열을 쓸 때는 open 함수로 파일을 열어서 파일 객체(file object)를 얻은 뒤에
# write 메서드를 사용합니다.

# 파일 처리

# 1. Open
# 2. Write/Read/Update
# 3. Close

# 파일객체 = open(파일이름, 파일모드)
# 파일객체.write('문자열')
# 파일객체.close()

# 파일모드 : w(쓰기), r(읽기)

import os
os.getcwd()  # 현재 디렉토리 위치를 출력
os.chdir('D:\\limworkspace\\Python-lecture\\Python_coding_dojang')   # change directory, 경로는 '\'
# os.mkdir('경로')  폴더 만들기
# 파일 이동

import shutil  # 모듈 사용
# 파일 복사
# 파일 이동
# shutil.move(a, b)

file = open('test.txt','w')  # open 함수로 파일을 열어서 파일 객체(file object)를 얻는다.
file.write("hello, world")   # 파일에 문자열 저장, Write한 글자 수 반환
file.close()                 # 파일 객체 닫기!


# 27.1.2  파일에서 문자열 읽기

os.getcwd()  # 현재 디렉토리 위치를 출력

file = open('test.txt', 'r')  # 파일을 읽기 모드로 열기, 파일 객체 반환
s = file.read()               # 파일에서 문자열 읽기
print(s)
file.close()                  # 파일 객체 닫기




# 27.1.3  자동으로 파일 객체 닫기

# 파일을 열 때마다 매번 close로 닫으려니 좀 귀찮습니다.
# 파이썬에서는 with as를 사용하면 파일을 사용한 뒤 자동으로 파일 객체를 닫아줍니다.

# with open(파일이름, 파일모드) as 파일객체:
#     코드

with open('test.txt', 'r') as file:  # test.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                  # 파일에서 문자열 읽기
    print(s)




# 27.2 문자열 여러 줄을 파일에 쓰기, 읽기 -----------------------------------


# 27.2.1  반복문으로 문자열 여러 줄을 파일에 쓰기
with open('test.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world {0}\n'.format(i))  # '\n'이 없으면 한줄로 출력

# 27.2.2  리스트에 들어있는 문자열을 파일에 쓰기
# * 파일객체.writelines(문자열리스트)
lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']  # '\n' 주의

with open('hello.txt', 'w') as file:
    file.writelines(lines)

# 27.2.3  파일의 내용을 한 줄씩 리스트로 가져오기
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# 27.2.4  파일의 내용을 한 줄씩 읽기
with open('hello.txt', 'r') as file:
    line = None        # None != ''
    while line != '':  # 빈 문자열이 아닐 떄 반복
        line = file.readline()
        print(line.strip('\n'))  # '\n' 삭제

with open('hello.txt', 'r') as file:
    while True:  # 빈 문자열이 아닐 떄 반복
        line = file.readline()
        if line == '':
            break
        print(line.strip('\n'))  # '\n' 삭제



# 특히 변수 line은 while로 반복하기 전에 None으로 초기화해줍니다.
# 만약 변수 line을 만들지 않고 while을 실행하면
# 없는 변수와 빈 문자열 ''을 비교하게 되므로 에러가 발생합니다.
# 또는, line을 None이 아닌 ''로 초기화하면
# 처음부터 line != ''는 거짓이 되므로 반복을 하지 않고 코드가 그냥 끝나버립니다.
# while을 사용할 때는 이 부분을 주의해주세요.


# 27.2.5  for 반복문으로 파일의 내용을 줄 단위로 읽기

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:                   # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))         # 파일에서 읽어온 문자열에서 \n 삭제하여 출력



# 참고 :  파일 객체는 이터레이터
# 파일 객체는 이터레이터입니다.
# 따라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능합니다
# (이터레이터는 'Unit 39 이터레이터 사용하기' 참조).

file = open('hello.txt', 'r')
a, b ,c = file
print(a, b, c)




# 27.3 파이썬 객체를 파일에 저장하기, 가져오기 -------------------------------

# 파일에서 문자열만 읽고 쓴다면 조금 불편하겠죠? 파이썬은 객체를 파일에 저장하는 pickle 모듈을 제공합니다.
#
# 다음과 같이 파이썬 객체를 파일에 저장하는 과정을 피클링(pickling)이라고 하고,
# 파일에서 객체를 읽어오는 과정을 언피클링(unpickling)이라고 합니다.



# 27.3.1  파이썬 객체를 파일에 저장하기

# 파이썬 객체를 파일에 저장하는 피클링을 해보겠습니다. 피클링은 pickle 모듈의 dump 메서드를 사용합니다.

import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb') as file:  # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

#  b는 바이너리(binary)를 뜻하는데, 바이너리 파일은 컴퓨터가 처리하는 파일 형식입니다.
#  따라서 메모장 같은 텍스트 편집기로 열어도 사람이 알아보기 어렵습니다.


# 27.3.2  파일에서 파이썬 객체 읽기

# 이제 파일에서 파이썬 객체를 읽어오는 언피클링을 해보겠습니다.
# 언피클링은 pickle 모듈의 load를 사용합니다.
# 그리고 언피클링을 할 때는 반드시 파일 모드를 바이너리 읽기 모드 'rb'로 지정해야 합니다

import pickle

with open('james.p', 'rb') as file:  # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)

# 사실 파일 모드는 조합에 따라 여러 종류가 있습니다.
# 읽기 'r', 쓰기 'w' 이외에 추가 'a', 배타적 생성 'x'도 있습니다.
# 추가 모드는 이미 있는 파일에서 끝에 새로운 내용을 추가할 때 사용하고,
# 배타적 생성 모드는 파일이 이미 있으면 에러(FileExistsError)를 발생시키고
# 없으면 파일을 만듭니다. 'x'는 베타적 생성(exclusive creation)의 x입니다
