# 2022. 09. 17
# Algorithm Day 17
# BaekJoon 1976 (Gold 4)

# Using WQU

city = int(input())
plan_n = int(input())
con_list = []

for i in range(city) :
    con_list.append(list(map(int, input().split(' '))))

ids = []
size = []

for idx in range(city+1):
    ids.append(idx)
    size.append(1)

def root(i):
    while i != ids[i]: i = ids[i]
    return i

def connected(p, q):
    return root(p) == root(q)

def union(p, q):
    id1, id2 = root(p), root(q)
    if id1 == id2: return
    if size[id1] <= size[id2] :
        ids[id1] = id2
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]

for i in range(city):
    for j in range(city):
        if i >= j and con_list[i][j] == 1:
            union(i+1, j+1)
            
plan = list(map(int, input().split(' ')))

p = "YES"
for i in range(plan_n-1):
    if not connected(plan[i], plan[i+1]):
        p = "NO"

print(p)
            
    