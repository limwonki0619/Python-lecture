# Unit 28. 회문 판별과 N-gram 만들기


# 28.1 회문 판별하기 -----------------------------------------------------------------------------
# 28.1.1  반복문으로 문자 검사하기

word = input('단어를 입력하세요:').lower()

is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 -i]:
        is_palindrome = False
        break

print(is_palindrome)


# 28.1.2  시퀀스 뒤집기로 문자 검사하기

word = input('단어를 입력하세요:').lower()
print(word == word[::-1])  # 원래 문자열과 반대로 뒤집은 문자열을 비교


# 28.1.3  리스트와 reversed 사용하기

word = input('단어를 입력하세요:').lower()
print(list(word) == list(reversed(word)))


# 28.1.4  문자열의 join 메서드와 reversed 사용하기
word = input('단어를 입력하세요:').lower()
print(word == ''.join(reversed(word)))



# 28.2 N-gram 만들기 ----------------------------------------------------------------------------

# N-gram은 문자열에서 N개의 연속된 요소를 추출하는 방법입니다.
# 만약 'Hello'라는 문자열을 문자(글자) 단위 2-gram으로 추출하면 다음과 같이 됩니다.
# 즉, 문자열의 처음부터 문자열 끝까지 한 글자씩 이동하면서 2글자를 추출합니다.
# 3-gram은 3글자, 4-gram은 4글자를 추출하겠죠?

# 28.2.1  반복문으로 N-gram 출력하기

text = 'Hello'

for i in range(len(text)-1):  # 2-gram이므로 문자열의 끝에서 한 글자 앞까지만 반복함
    print(text[i], text[i+1], sep='')   # 현재 문자와 그다음 문자 출력

text = 'this is python script'  # 공백을 기준으로 문자열을 분리하여 리스트로 만듦
words = text.split()

for i in range(len(words)-1):
    print(words[i], words[i+1])


# 28.2.2  zip으로 2-gram 만들기

text = 'Hello'

two_gram = zip(text, text[1:])  # Hello, ello, zip 함수는 반복 가능한 객체의 각 요소를 튜플로 묶어줍니다.
for i in two_gram:
    print(i[0], i[1], sep='')

list(zip(text, text[1:]))

# 28.2.3  zip과 리스트 표현식으로 N-gram 만들기

text = 'Hello'
print(list(zip(*[text[i:] for i in range(2)])))


# 28.3 연습문제: 단어 단위 N-gram 만들기

# 표준 입력으로 정수와 문자열이 각 줄에 입력됩니다.
# 다음 소스 코드를 완성하여 입력된 숫자에 해당하는 단어 단위
# N-gram을 튜플로 출력하세요(리스트 표현식 사용).
# 만약 입력된 문자열의 단어 개수가 입력된 정수 미만이라면 'wrong'을 출력하세요.

n = int(input())
text = input()
'Python is a programming language that lets you work quickly'
words = text.split(' ')

if len(words) < n:
    print('wrong')
else:
    n_gram = list(zip(*[words[i:] for i in range(n)]))
    for i in n_gram:
        print(i)



# 28.4 심사문제: 파일에서 회문인 단어 출력하기 --------------------------------------------------

# 단어가 줄 단위로 저장된 words.txt 파일이 주어집니다.
# palindrome.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력해야 합니다.
# 그리고 파일에서 읽은 단어는 \n이 붙어있으므로 \n을 제외한 뒤
# 회문인지 판단해야 하며 단어를 출력할 때도 \n이 출력되면 안 됩니다(단어 사이에 줄바꿈이 두 번 일어나면 안 됨).

import os
os.getcwd()  # 현재 작업 디렉토리 확인

# 코드로 파일 생성 해보기
list = ['apache', 'decal', 'did', 'neep', 'noon', 'refer', 'river']

with open('Unit28_palindrome.txt','w') as file:
    for i in list:
        file.writelines(i+'\n')  # 각 단어끝에 \n 추가하기

# 심사문제 답안
with open('Unit28_palindrome.txt', 'r') as file:  # 심사볼떄는 words.txt, 파일 모드 잊지말기!
    for text in file:
        string = text.strip('\n')

        if string == string[::-1]:
            print(string)
        else:
            continue
