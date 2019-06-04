def generate(numRows):
    
    a = [[1] * (i+1) for i in range(numRows)]
    print(a)
    for i in range(numRows):
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    return a

print(generate(5))