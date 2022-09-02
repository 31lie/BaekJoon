# 2022. 09. 02
# Algorithm Day 2
# BaekJoon 1002 (Silver 3)

import math


tc_num = int(input())
tc_list = []

for i in range (tc_num):
    tc_list.append(list(map(int, input().split(' '))))


for tc in tc_list:
    dis = math.dist([tc[0],tc[1]],[tc[3], tc[4]])
    r1r2_sum = tc[2] + tc[5]
    r1r2_sub = abs(tc[2] - tc[5])
    cnt = 0
    
    if dis == 0 and r1r2_sub == 0:
        cnt = -1
    elif r1r2_sum == dis or r1r2_sub == dis:
        cnt = 1
    elif r1r2_sub < dis and dis < r1r2_sum:
        cnt = 2
    else:
        cnt = 0
    print (cnt)

        


