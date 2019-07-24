# 2.4 1~1000에서 각 숫자의 개수를 구하시오.
#  - 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자.

def num_counting(start, end):

    num = [str(i) for i in range(10)]
    count = [0] * 10

    temp = []
    for i in range(start, end+1):
        num_list = list(str(i))
        temp.append(num_list)

    for k in temp:
        for z in k:

            if '0' in z:
                count[0] += 1
            elif '1' in z:
                count[1] += 1
            elif '2' in z:
                count[2] += 1
            elif '3' in z:
                count[3] += 1
            elif '4' in z:
                count[4] += 1
            elif '5' in z:
                count[5] += 1
            elif '6' in z:
                count[6] += 1
            elif '7' in z:
                count[7] += 1
            elif '8' in z:
                count[8] += 1
            else:
                count[9] += 1
    print('0 : {0}개\n'
          '1 : {1}개\n'
          '2 : {2}개\n'
          '3 : {3}개\n'
          '4 : {4}개\n'
          '5 : {5}개\n'
          '6 : {6}개\n'
          '7 : {7}개\n'
          '8 : {8}개\n'
          '9 : {9}개'.format(
        count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7], count[8], count[9]))

num_counting(1, 1000)



# 모범답안 ----------------------------------------------------------

# 1~1000에서 각 숫자의 개수

# counts = [0] * 10
#
# for i in range(1, 10):
#     counts[i] += 1
# for i in range(10, 100):
#     counts[i // 10] += 1
#     counts[i % 10] += 1
# for i in range(100, 1000):
#     counts[i // 100] += 1
#     counts[(i % 100) // 10] += 1
#     counts[i % 10] += 1
# for i in range(1000, 1001):
#     counts[i // 1000] += 1
#     counts[(i % 1000) // 100] += 1
#     counts[(i % 100) // 10] += 1
#     counts[i % 10] += 1
#
# print(counts)