
def topK(arr,k):    
    arr = sorted(set(arr))
    return list(arr)[-k:]


if __name__ == "__main__":

    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input())
        arr.append(arr_item)
        arr_i += 1


    k = int(input())

    res = topK(arr, k);
    for res_cur in res:
        print( str(res_cur) + "\n" )

