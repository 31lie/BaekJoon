# 2022. 09. 01
# Algorithm Day 1
# BaekJoon 3003 (Bronze 5)

chess = [1, 1, 2, 2, 2, 8]

data = list(map(int,input().split(' ')))

for i in range(len(data)):
    print(chess[i] - data[i], end=" ")