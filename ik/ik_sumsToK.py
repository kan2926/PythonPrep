def sumsToK(arr, n, k):
    if n == 0 and k != 0:
        return False
    if k == 0 and n ==0:
        print(k)
        return True
    if arr[n-1] > k:
        return sumsToK(arr, n-1, k)
    
    return sumsToK(arr, n-1,k) or sumsToK(arr, n-1, k-arr[n-1])

def check_if_sum_possible(arr, k):
    
    if k == 0:
        cnt = 0
        for i in arr:
            if i == 0:
                cnt += 1
        if cnt == len(arr):
            return True
        else:
            print('else')
            return sumsToK(arr,len(arr),k)
    else:
        return sumsToK(arr, len(arr), k)
        


if __name__ == "__main__":

    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input());
        arr.append(arr_item)
        arr_i += 1
    k = int(input());
    print(check_if_sum_possible(arr, k))
    
