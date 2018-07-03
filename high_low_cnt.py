#arr = [10,5,20,20,4,5,2,25,1]
arr = [3,4,21,36,10,28,35,5,24,42]
low_cnt = 0
high_cnt = 0

high = low = arr[0]
for i in arr:
    if i > high:
        high = i
        high_cnt += 1
    elif i < low:
        low = i
        low_cnt += 1

print(high_cnt, '  ', low_cnt)
