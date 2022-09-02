# 2022. 09. 02
# Algorithm Day 2
# BaekJoon 2525 (Bronze 3)


hour, min = map(int, input().split(' '))
take = int(input())

min_sum = take + min

if min_sum < 60:
    print(hour, min_sum)
else :
    hour = hour + min_sum // 60
    min = min_sum % 60
    if hour >= 24:
        hour = hour - 24 * (hour//24)
    print(hour, min)