# 2022. 09. 15
# Algorithm Day 15
# BaekJoon 2480 (Bronze 4)

a, b, c = map(int, input().split(' '))

price = 0

if a==b and b==c:
    price = 10000 + a * 1000

elif a==b:
    price = 1000 + a * 100

elif a==c:
    price = 1000 + a * 100
    
elif c==b:
    price = 1000 + c * 100

else:
    dice = [a, b, c]
    price = max(dice) * 100

print(price)