# 2.3 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?
#  - 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됨.

# 오답
# total = 0
# for i in range(24):
#     for k in range(60):
#         if i % 10 == 3 or k % 10 == 3 or k // 10 == 3:
#             print(i, k)
#             total = (i*3600) + (k*60)
#         else:
#             print(end='')
# print(total)



# 모범답안 ------------------------------------------------------------

# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면
# 총 몇 초(second) 인가?
total = 0
# for hour in range(24):
#     if hour % 10 == 3:          # 3시, 13시, 23시
#         total += 60 * 60;
#     else:
#         for min in range(60):
#             if min // 10 == 3:  # 30분 ~ 39분
#                 total += 60
#             elif min % 10 == 3: # 3분, 13분, 23분, 43분, 53분
#                 total += 60

for hour in range(24):
    for min in range(60):
        time = str(hour) + str(min)
        if '3' in time:
            total += 60

print(total)