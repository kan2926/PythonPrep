



def solve(arr):
    even = list(filter(lambda x: x%2 == 0, arr))
    odd = list(filter(lambda x: x%2 != 0, arr))
    res = even + odd    
    return res


if __name__ == "__main__":
    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input())
        arr.append(arr_item)
        arr_i += 1

    res = solve(arr);
    for res_cur in res:
        print( str(res_cur) + "\n" )


