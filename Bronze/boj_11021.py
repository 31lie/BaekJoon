# 2022. 09. 27
# Algorithm Day 27
# BaekJoon 11021 (Bronze 5)


import sys


tc = int(input())

for i in range(tc):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print("Case #%d: %d" % (i+1, a+b))