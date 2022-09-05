# 2022. 09. 05
# Algorithm Day 5
# BaekJoon 1003 (Silver 3)

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(n):
    leng = len(zero)
    if n >= leng:
        for i in range(leng, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])


tc = int(input())

for _ in range(tc):
    fibonacci(int(input()))
