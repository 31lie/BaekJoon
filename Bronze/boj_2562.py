# 2022. 09. 16
# Algorithm Day 16
# BaekJoon 2562 (Bronze 3)





num_list = []

for i in range(9):
    num_list.append(int(input()))

lar = max(num_list)
print(lar)
print(num_list.index(lar)+1)