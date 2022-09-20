# 2022. 09. 20
# Algorithm Day 20
# BaekJoon 4195 (Gold 2)

def find(x):
    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]

def union(x, y):
    r_x = find(x)
    r_y = find(y)
    
    if r_x != r_y:
        parent[r_y] = r_x
        number[r_x] += number[r_y]
    


tc = int(input())

for _ in range(tc):
    parent = dict()
    number = dict()
    
    n = int(input())
    
    for _ in range (n):
        x, y = input().split(' ')
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)
        print(number[find(x)])