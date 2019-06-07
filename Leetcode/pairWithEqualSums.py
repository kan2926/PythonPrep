def pairWithEqualSums(a):
    tmp = {}
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            k = a[i]+a[j]
            if k in tmp:
                tmp[k].append((a[i],a[j]))
            else:
                tmp[k] = [(a[i],a[j])]
    result = []
    for k, v in tmp.items():
        if len(v) > 1:
            result.append(v)
    return result

a = [9, 4, 3, 1, 7, 12]
print(pairWithEqualSums(a))