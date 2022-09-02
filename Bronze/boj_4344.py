# 2022. 09. 02
# Algorithm Day 2
# BaekJoon 4344 (Bronze 1)

def compare(data):
    tc_sum = sum(data[1:])
    avg = tc_sum/data[0]
    
    i = 1
    while i < len(data) and data[i] <= avg:
        i += 1
    
    good = len(data) - i
    return good/(len(data)-1)*100
 
testcase = int(input())
scorelist = []

for i in range(testcase):
    scorelist.append(list(map(int, input().split(' '))))
    
for tc in scorelist:
    temp = tc.pop(0)
    tc.sort()
    tc.insert(0, temp)
    print('%.3f%%'%compare(tc))
    