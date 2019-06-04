def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

def fib(n):
    fib_dict = {0:0, 1:1}
    if n not in fib_dict: 
        fib_dict[n] = fib(n-1) + fib(n-2)
    return fib_dict[n]
    

def arrayPairSum(nums):
    print(sorted(nums)[::2])
    return sum(sorted(nums)[::2])
    
print(arrayPairSum([1,2,3,4,5,6]))

A = [[1,2,3],[4,5,6],[7,8,9]]

#print(transpose(A))

#print(fib(5))