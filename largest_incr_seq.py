
def largest_incr_seq(arr):
    n = len(arr) 
    if n == 0:
        return
    if n == 1:
        return 1

    res = []
    
    for i in range(n):
        tmp = max(arr[:i+1])
        if res and tmp == res[-1]:
            pass
        else:
            res.append(tmp)
    print(res)
    return len(res)
    
arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
print(largest_incr_seq(arr))
