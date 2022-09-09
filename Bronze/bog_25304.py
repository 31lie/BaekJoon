# 2022. 09. 09
# Algorithm Day 9
# BaekJoon 25304 (Bronze 5)


total = int(input())
cnt = int(input())
price = []

for i in range (cnt):
    a, b = map(int, input().split(' '))
    price.append(a*b)

if sum(price) == total:
    print("Yes")
else:
    print("No")