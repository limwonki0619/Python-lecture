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