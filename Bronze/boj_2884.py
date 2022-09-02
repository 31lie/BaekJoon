# 2022. 09. 02
# Algorithm Day 2
# BaekJoon 2884 (Bronze 3)

hour, min = map(int, input().split(' '))

if min >= 45:
    min = min - 45
else:
    min = min + (60-45)
    hour = hour - 1
    if hour < 0:
        hour = hour + 24

print(hour, min)