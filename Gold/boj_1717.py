# 2022. 09. 17
# Algorithm Day 17
# BaekJoon 1717 (Gold 4)

# Using WQU


N, M = map(int, input().split(' '))

ids = []
size = []
for idx in range(N+1):
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
        
for i in range(M):
    n, a, b = map(int, input().split(' '))
    if n == 0:
        union(a, b)
    else:
        if connected(a, b):
            print("YES")
        else:
            print("NO")