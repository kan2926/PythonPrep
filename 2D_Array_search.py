
def isPresent(arr, x):
    for i in range(len(arr)):
            if x in arr[i]:
                return "present"
            
    return "not present"




if __name__ == "__main__":

    arr_rows = int(input())
    arr_columns = int(input())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    q = int(input())
    for _ in range(q):
        x = int(input())
        res = isPresent(arr, x)
        print(res)
    
