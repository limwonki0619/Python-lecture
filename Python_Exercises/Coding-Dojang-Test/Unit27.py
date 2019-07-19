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