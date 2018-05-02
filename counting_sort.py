def counting_sort(a,n):
    cnt_arr = [0]*(n+1)
    for i in range(len(a)+1):
        cnt_arr[i] = a.count(i)
    for k in range(len(cnt_arr)):
        cnt_arr[k] = cnt_arr[k] + cnt_arr[k-1]

    res = [0] * len(a)
    for p in range(len(a)):
        pos = cnt_arr[a[p]]
        res[pos-1] = a[p]
        cnt_arr[a[p]]= cnt_arr[a[p]]-1
    return res

a = [1,4,1,2,7,5,2]
n=9
res =counting_sort(a,n)
print(res)
