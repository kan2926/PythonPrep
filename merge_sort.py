def merge_sort(a,b):
    m = len(a)
    n= len(b)
    i = 0
    j = 0
    k = 0
    res = []
    while i < m and j< n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    res += a[i:]
    res += b[j:]

    return sorted(res)


a = [3,1,2,5,7,4]
b = [4,1,2,8,9,10]
print(merge_sort(a,b))
