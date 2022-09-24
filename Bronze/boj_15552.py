# 2022. 09. 24
# Algorithm Day 24
# BaekJoon 15552 (Bronze 4)


import sys


tc = int(input())

for _ in range(tc):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print(a+b)