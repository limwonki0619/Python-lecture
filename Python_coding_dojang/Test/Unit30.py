# 30.7 심사문제 : 가장 낮은 점수, 높은 점수와 평균점수를 구하는 함수 만들기

# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가 출력되게 만드세요.
# 평균 점수는 실수로 출력되어야 합니다.

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):  # 가변 인수 함수는 매개변수 앞에 *를 붙여서 만든다.
    return min(args), max(args)

def get_average(**kwargs):  # 키워드 인수를 사용하는 가변 인수 함수는 매개변수 앞에 **를 붙여서 만든다.
    return sum(kwargs.values()) / len(kwargs)


min_score, max_score = get_min_max_score(korean, english, mathematics, science)

average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
