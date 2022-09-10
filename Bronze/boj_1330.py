# 2022. 09. 10
# Algorithm Day 10
# BaekJoon 1330 (Bronze 5)

a, b = map(int, input().split(' '))

if a>b:
    print(">")
elif a<b:
    print("<")
else:
    print("==")