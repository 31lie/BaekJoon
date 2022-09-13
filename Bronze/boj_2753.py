# 2022. 09. 13
# Algorithm Day 13
# BaekJoon 2753 (Bronze 5)

year = int(input())

if year % 4 == 0 and year % 100 != 0 :
    print(1)
elif year % 400 == 0:
    print(1)
else:
    print(0)