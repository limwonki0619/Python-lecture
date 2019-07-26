# 47.4.1  time 모듈로 현재 시간 구하기

# 먼저 시간을 표현하는 time 모듈입니다.
# 다음과 같이 time 모듈의 time 함수를 호출하면 1970년 1월 1일 0시 0분 0초 이후 경과한 시간을 초단위로 반환합니다. 시간대는 UTC(Universal Time Coordinated, 협정 세계시)를 사용합니다.

import time
time.time()



# 47.4.2  날짜와 시간 형태로 변환하기

# time 모듈의 localtime 함수를 사용하면 time에서 반환한 값을 날짜와 시간 형태로 변환해줍니다.
# 특히 localtime이라는 이름 그대로 현재 지역의 시간대를 사용합니다.
# 우리나라에서 실행했다면 UTC에 9시간을 더한 KST(Korea Standard Time, 한국 표준시)를 사용합니다(UTC+09:00).

# * time.localtime(초)

time.localtime(time.time())

# 여기서 tm_wday는 요일(월요일~일요일, 0~6),
# tm_yday는 1월 1일부터 경과한 일수, tm_isdst는 서머타임 여부입니다.




# 47.4.3  날짜/시간 포맷에 맞춰서 출력하기

# time.localtime으로 만든 객체는 time.strftime 함수를 사용하여
# 원하는 날짜/시간 포맷으로 출력할 수 있습니다.

# * time.strftime('포맷', 시간객체)

time.strftime('%Y-%m-%d', time.localtime(time.time()))

time.strftime('%c', time.localtime(time.time()))

# %Y는 연, %m은 월, %d는 일인데, '%Y-%m-%d'는 '연-월-일' 포맷이라는 뜻입니다.
# 그리고 %c는 날짜와 시간을 함께 출력합니다.





# 47.4.4 datetime 모듈로 현재 날짜와 시간 구하기

# 이번에는 datetime 모듈의 datetime 클래스를 사용해보겠습니다.
# datetime.datetime으로 현재 날짜와 시간을 구할 때는 today 메서드를 사용합니다(현재 시간대 기준, KST).

# * datetime.datetime.today()

import datetime

datetime.datetime.today()

# 만약 datetime 모듈로 현재 시간을 구할 때 UTC를 기준으로 구하고 싶다면
# now 메서드에 pytz 모듈로 시간대를 지정해주어야 합니다.




# 47.4.5  특정 날짜와 시간으로 객체 만들기

# 또는, datetime.datetime에 연, 월, 일, 시, 분, 초, 마이크로초를 넣어서
# 객체를 만들 수도 있습니다.

# * datetime.datetime(year, month, day, hour=0, minute=0, second=0, mirosecond=0)

d = datetime.datetime(2018, 5, 19)



# 47.4.6  문자열로 날짜/시간 객체 만들기

# strptime 메서드를 사용하면 문자열 형태의 날짜를 datetime.datetime 객체로 만들 수 있습니다.
# 이때는 날짜/시간 포맷을 지정해줘야 합니다.

# * datetime.datetime.strptime('날짜문자열', '포맷')

d = datetime.datetime.strptime('2018-05-19', '%Y-%m-%d')



# 47.4.7  날짜/시간 객체를 문자열로 만들기
d.strftime('%Y-%m-%d')
d.strftime('%c')




# 47.4.8  날짜와 시간 속성에 접근하기

# datetime.datetime 객체는 연( year), 월(month), 일(day), 시(hour), 분(minute),
# 초(second), 마이크로초(microsecond) 속성을 따로 가져올 수 있습니다.

today = datetime.datetime.today()


# 47.4.9  날짜와 시간 차이 계산하기

# datetime 모듈에서 유용한 기능이 바로 datetime.timedelta입니다.
# datetime.timedelta는 두 날짜와 시간 사이의 차이를 계산할 때 사용합니다.
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0,
#                    minutes=0, hours=0, weeks=0)

d = datetime.datetime(2018, 5, 13)

from datetime import timedelta

d - timedelta(days = 20)

# 즉, datetime.datetime 객체에서 datetime.timedelta를 빼면 이전 날짜와 시간을 구하고,
# 더하면 이후 날짜와 시간을 구합니다.
# 특히 datetime.datetime 객체에서
# datetime.datetime 객체를 빼면 datetime.timedelta 객체가 나옵니다.

datetime.datetime(2018, 5, 13) - datetime.datetime(2018, 4, 1)
