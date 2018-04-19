
def mergeSort(l):
    res = []
    size = len(l)
    if size < 2:
        return l
    mid = size //2
    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])

    i= j =0
    while i< len(left) and j< len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]

    return res
        

l = [-1,9,0,-2]
m = [0,4,6]
n = [7,8]
p = []
p.append(l[:])
p.append(m)
p.append(n)

cons_list = []
for i in p:
    cons_list +=i
print(cons_list)
print(mergeSort(cons_list))


