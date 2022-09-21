# 2022. 09. 21
# Algorithm Day 21
# BaekJoon 1708 (Platinum 5)

import math

def ccw(i, j, k):
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0: return True
    else: return False



def grahamScan(points):
    
    # find the start point
    start = points[0]
    p_index = 0
    for i in range(len(points)):
        if points[i][1] < start[1]:
            start = points[i]
            p_index = i
        elif points[i][1] == start[1] and points[i][0] > start[0] :
            start = points[i]
            p_index = i
        
    # Make new Tuple with radians
    cal_points = []
    for i in range(len(points)):
        if i == p_index:
            cal_points.append((points[i][0], points[i][1], 0))
        else :
            angle = math.atan2(points[i][1] - start[1], points[i][0] - start[0])
            cal_points.append((points[i][0], points[i][1], angle))
        
    # Sort
    cal_points = sorted(cal_points, key = lambda cal_points: (cal_points[2], cal_points[1], cal_points[0]))

    ConvexHull = []
    ConvexHull.extend([cal_points[0], cal_points[1], cal_points[2]])
    for i in range(3, len(cal_points)+1):
        while len(ConvexHull) >= 3 and ccw(ConvexHull[-3], ConvexHull[-2], ConvexHull[-1]) == False:
            del ConvexHull[-2]
        if i != len(cal_points):
            ConvexHull.append(cal_points[i])
        elif not ccw(ConvexHull[-2], ConvexHull[-1], ConvexHull[0]):
            del ConvexHull[-1]
    return ConvexHull




p_num = int(input())
_points = []

for _ in range (p_num):
    a, b = map(int, input().split(' '))
    _points.append((a,b))
    
print(len(grahamScan(_points)))