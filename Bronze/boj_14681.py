# 2022. 09. 14
# Algorithm Day 14
# BaekJoon 14681 (Bronze 

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0 :
    print(3)
else:
    print(4)
