# 2022. 09. 21
# Algorithm Day 21
# BaekJoon 4181 (Platinum 5)

import math

def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0: return True
    else: return False
    
p_num = int(input())
points = []

for _ in range(p_num):
    x, y, a = input().split(' ')
    x, y = int(x), int(y)
    if a == 'Y':
        points.append([x,y])

start = points[0]
p_index = 0
for i in range(len(points)):
    if points[i][0] < start[0]:
        start = points[i]
        p_index = i
    elif points[i][0] == start[0] and points[i][1] < start[1] :
        start = points[i]
        p_index = i

cal_points = []
for i in range(len(points)):
    if i == p_index:
        cal_points.append((points[i][0], points[i][1], -181))
    else :
        angle = math.atan2(points[i][1] - start[1], points[i][0] - start[0])
        cal_points.append((points[i][0], points[i][1], angle))

cal_points = sorted(cal_points, key = lambda cal_points: (cal_points[2], -cal_points[1], cal_points[0]))


print(len(cal_points))   
for p in cal_points:
    print("%d %d" % (p[0], p[1]))