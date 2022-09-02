# 2022. 09. 02
# Algorithm Day 2
# BaekJoon 1065 (Silver 4)


def find_cold(num):
    str_num = str(num)
    if num < 10:
        return 0
    else:
        temp = int(str_num[0]) - int(str_num[1])
        for i in range (2, len(str_num)):
            cha = int(str_num[i-1]) - int(str_num[i])
            if temp != cha:
                return 1
        return 0
            
n = int(input())
re, cnt = 0, 0

for i in range (1, n+1):
    re = find_cold(i)
    if re == 0:
        cnt += 1
        
print(cnt)