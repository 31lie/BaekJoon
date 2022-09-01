# 2022. 09. 01
# Algorithm Day 1
# BaekJoon 1920 (Silver 4)

def binary_search(target, list):
    start = 0 ; end = len(list) -1
    
    while start <= end:
        mid = (start+end) // 2
        
        if list[mid] == target:
            print(1)
            return 0
        elif list[mid] < target:
            start = mid + 1
        else :
            end = mid - 1
    print(0)
    return None

num = input()
num_list = list(map(int, input().split(' ')))
num_list.sort()

count = int(input())
search = list(map(int, input().split(' ')))


for s in search:
    binary_search(s, num_list)