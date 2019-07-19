# Unit 27. 파일 사용하기

# 27.1 파일에 문자열 쓰기, 읽기 ------------------------------------------------------

# 27.1.1  파일에 문자열 쓰기

# 파일에 문자열을 쓸 때는 open 함수로 파일을 열어서
# 파일 객체(file object)를 얻은 뒤에 write 메서드를 사용합니다.

# 파일객체 = open(파일이름, 파일모드)
# 파일객체.write('문자열')
# 파일객체.close()

import os
os.getcwd()  # 현재 작업 디렉토리 확인

file = open('hello.txt', 'w')  # 쓰기(write) 모드로 파일 객체 반환
file.write('hello, world!')
file.close()

# 27.1.2  파일에서 문자열 읽기

# 파일을 읽을 때도 open 함수로 파일을 열어서 파일 객체를 얻은 뒤
# read 메서드로 파일의 내용을 읽습니다. 단, 이때는 파일 모드를 읽기 모드 'r'로 지정합니다.

# * 변수 = 파일객체.read()

file = open('hello.txt', 'r')  # 읽기(read) 모드로 파일 객체 반환
s = file.readline()
print(s)
file.close()


# 27.1.3  자동으로 파일 객체 닫기

# 이썬에서는 with as를 사용하면 파일을 사용한 뒤 자동으로 파일 객체를 닫아줍니다.
# 다음과 같이 with 다음에 open으로 파일을 열고 as 뒤에 파일 객체를 지정합니다.

# with open(파일이름, 파일모드) as 파일객체:
#     코드


with open('hello.txt', 'r') as file:  # hello.txt를 읽은 후 file로 이름 붙이기
    s = file.readline()               # 변수 s에 파일을 읽은 후 저장
    print(s)                          # 출력




# 27.2 문자열 여러 줄을 파일에 쓰기, 읽기 -------------------------------------

# 27.2.1  반복문으로 문자열 여러 줄을 파일에 쓰기

with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))  # 만약 \n을 붙이지 않으면 문자열이 모두 한 줄로 붙어서 저장되므로 주의해야 합니다.


# 27.2.2  리스트에 들어있는 문자열을 파일에 쓰기
# 파일객체.writelines(문자열리스트)

lines =  ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
with open('hello.txt', 'w') as file:
    file.writelines(lines)

# writelines는 리스트에 들어있는 문자열을 파일에 씁니다.
# 특히 writelines를 사용할 때는 반드시 리스트의 각 문자열 끝에
# 개행 문자 \n을 붙여주어야 합니다.
# 그렇지 않으면 문자열이 모두 한 줄로 붙어서 저장되므로 주의해야 합니다.


# 27.2.3  파일의 내용을 한 줄씩 리스트로 가져오기
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)


# 27.2.5  for 반복문으로 파일의 내용을 줄 단위로 읽기
# 변수 = 파일객체.readline()

with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))


# 참고 : 파일 객체는 이터레이터
# 파일 객체는 이터레이터입니다.
# 따라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능합니다
# (이터레이터는 'Unit 39 이터레이터 사용하기' 참조).
file = open('hello.txt', 'r')
a, b, c= file
print(a, b, c)



# 27.3 파이썬 객체를 파일에 저장하기, 가져오기 --------------------------------

# 27.3.1  파이썬 객체를 파일에 저장하기

# 파이썬 객체를 파일에 저장하는 피클링을 해보겠습니다. 피클링은 pickle 모듈의 dump 메서드를 사용합니다.

import pickle

name = 'james'
age = 17
address = '대전 동구 용전동'
scores = dict(zip(['korean', 'english', 'mathematics', 'science'], [90, 95, 85, 82]))

with open('james.p', 'wb') as file:  # james.p 파일을 바이너리 쓰기 모드로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


# 27.3.2  파일에서 파이썬 객체 읽기
import pickle

with open('james.p', 'rb') as file:  # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name, age, address, scores)


# 27.5 연습문제 : 파일에서 10자 이하인 단어 개수 세기 -------------------------
words = ['anonymously\n', 'compatibility\n', 'dashboard\n', 'experience\n', 'photography\n', 'spotlight\n', 'warehouse\n']
with open('words.txt', 'w') as file:  # 파일 만들어 저장
    file.writelines(words)

with open('words.txt', 'r') as file:
    count = 0
    for line in file:
        if len(line.strip('\n')) <= 10 :
            count += 1
print(count)


# 27.6 심사문제 : 특정 문자가 들어있는 단어 찾기

# 문자열이 저장된 words.txt 파일이 주어집니다
# (문자열은 한 줄로 저장되어 있습니다).
# words.txt 파일에서 문자 c가 포함된 단어를
# 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력해야 하며
# ,(콤마)와 .(점)은 출력하지 않아야 합니다.

import string

with open('words.txt', 'r') as file:
    for contents in file:
        for text in contents.split(' '):  # 공백 기준으로 분리
            #if text.count('c') >= 1:     # 'c' 가 1개 이상 있는것만 출력
            if 'c' in text:  # 'c'가 text에 들어있냐? 반대로 해서 틀림 ..
                print(text.strip(string.punctuation))


