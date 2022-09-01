# 2022. 09. 01
# Algorithm Day 1
# BaekJoon 2805 (Silver 2)

from sys import stdin

_, take = map(int, stdin.readline().split(' '))
forest = list(map(int, stdin.readline().split(' ')))

start, end = 1, sum(forest)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    
    for tree in forest:
        if tree > mid:
            cnt = cnt + tree - mid
    if cnt >= take:
        start = mid + 1
    else:
        end = mid - 1
print(end)
        