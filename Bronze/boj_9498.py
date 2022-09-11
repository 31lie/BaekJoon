# 2022. 09. 11
# Algorithm Day 11
# BaekJoon 9498 (Bronze 5)


score = int(input())

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")