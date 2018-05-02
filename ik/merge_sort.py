
def MergeSort(intArr):
    res = []
    if len(intArr) < 2:
        return intArr
    
    mid = len(intArr)//2
    left = MergeSort(intArr[:mid])
    right = MergeSort(intArr[mid:])
    
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



if __name__ == "__main__":

    intArr_cnt = 0
    intArr_cnt = int(input())
    intArr_i = 0
    intArr = []
    while intArr_i < intArr_cnt:
        intArr_item = int(input())
        intArr.append(intArr_item)
        intArr_i += 1


    res = MergeSort(intArr);
    for res_cur in res:
        print( str(res_cur) + "\n" )

