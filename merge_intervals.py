import operator
def merge_intervals(a, b):
    if a and b:
        if a[1] < b[0]:
            return True, [a[0], b[1]]
        else:
            return False, b
        
def getMergedIntervals(inputArray):
    inputArray.sort(key = operator.itemgetter(1))
    print(inputArray)
    res = []
    for i in range(len(inputArray)-1):
        if i == 0:
            change, tmp = merge_intervals(inputArray[i], inputArray[i+1])
        else:
            change, tmp = merge_intervals(tmp, inputArray[i+1])

        if change:
            res.append(tmp)
        else:
            res.append(inputArray[i])
            
    return res
    
if __name__ == "__main__":

    inputArray_rows = int(input())
    inputArray_columns = int(input())

    inputArray = []

    for _ in range(inputArray_rows):
        inputArray.append(list(map(int, input().rstrip().split())))

    res = getMergedIntervals(inputArray)

    print('\n'.join([' '.join(map(str, x)) for x in res]))
