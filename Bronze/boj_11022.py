# 2022. 09. 29
# Algorithm Day 29
# BaekJoon 11022 (Bronze 5)


import sys


tc = int(input())

for i in range(tc):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    print("Case #%d: %d + %d = %d" % (i+1,a,b,a+b))