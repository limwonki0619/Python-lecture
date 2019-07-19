# Unit 28. 회문 판별과 N-gram 만들기

# 문자열을 응용해서 회문을 판별하는 방법과 N-gram을 만드는 방법을 알아보겠습니다.

# 회문은 유전자 염기서열 분석에서 많이 쓰고,
# N-gram은 빅 데이터 분석, 검색 엔진에서 많이 쓰입니다.

# 28.1 회문 판별하기 -------------------------------------------

# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 말합니다. 예를 들면 "level", "SOS", "rotator", "nurses run"과 같은 단어와 문장이 있지요.
# 그럼 문자열이 회문인지 판별하려면 어떻게 해야 할까요?
# 먼저 회문을 잘 살펴보면 첫 번째 글자와 마지막 글자가 같습니다.
# 그리고 안쪽으로 한 글자씩 좁혔을 때 글자가 서로 같으면 회문입니다.


# 28.1.1  반복문으로 문자 검사하기
import string

word = input('단어를 입력하세요: ')
"Madam I'm Adam"

word = word.strip(string.punctuation + "'").lower()

is_palindrome = True                             # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):                  # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:  # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False                    # 회문이 아님
        break

print(is_palindrome)  # 회문 판별값 출력


# 28.1.2  시퀀스 뒤집기로 문자 검사하기
word = input('단어를 입력하세요: ')
print(word.lower() == word[::-1].lower())  # 원래 문자열과 반대로 뒤집은 문자열을 비교


# 28.1.3  리스트와 reversed 사용하기
word = input('단어를 입력하세요: ')
print(list(word) == list(reversed(word)))

# 28.1.4  문자열의 join 메서드와 reversed 사용하기
word = input('단어를 입력하세요: ')
print(word.lower() == ''.join(reversed(word.lower())))

