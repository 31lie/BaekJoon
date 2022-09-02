# 2022. 09. 02
# Algorithm Day 2
# BaekJoon 10430 (Bronze 5)

a, b, c = map(int,input().split(' '))

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)