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


def mergeArrays(arr):
    res = []
    for i in arr:
        res += i
    res = mergeSort(res)
    return res

if __name__ == "__main__":

    arr_rows = int(input())
    arr_columns = int(input())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    res = mergeArrays(arr)

    print('\n'.join(map(str, res)))
