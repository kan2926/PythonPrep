def findTriplets(arr, n):
    res = []
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):             
                if (arr[i] + arr[j] + arr[k] == 0):
                    res.append([arr[i], arr[j], arr[k]])

    return res
 
# Driver code
arr = [0, 5, -5, 3, -3]
n = len(arr)
res = findTriplets(arr, n)
print(res)
