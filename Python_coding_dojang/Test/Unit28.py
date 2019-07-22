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