# 2022. 09. 02
# Algorithm Day 2
# BaekJoon 1110 (Bronze 1)


num = input()
new = ''
cnt = 0

if len(num) == 1:
    num = '0' + num

while new != num:
    if cnt == 0:
        new = num
    if len(new) == 1:
        new = new + new
    else:
        temp = str(int(new[0]) + int(new[1]))
        new = new[1] + temp[-1]
    cnt += 1
print(cnt)