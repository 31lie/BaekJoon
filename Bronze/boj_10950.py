# 2022. 09. 03
# Algorithm Day 3
# BaekJoon 10950 (Bronze 5)

tc = int(input())
result = []

for i in range (tc):
    a, b = map(int,input().split(' '))
    result.append(a+b)

for n in result:
    print(n)