# 2022. 09. 02
# Algorithm Day 2
# BaekJoon 2750 (Bronze 2)

cnt = int(input())
num_list = []

for i in range (cnt):
    num_list.append(int(input()))

num_list.sort()
for num in num_list:
    print(num)