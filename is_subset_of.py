
def is_subsetof(a,b):
    m = len(a)
    n = len(b)
    match = 0
    i = j = 0
    while  i<m and  j <n :
        if a[i] == b[j]:
            print(a[i],'---',b[j])
            match += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return match == min(m,n)
                


a = [1,2,3,5,7]
b = [1,2,3,4,5]
print(is_subsetof(a,b))
