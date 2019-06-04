def flipAndInvertImage(A):
    for i in range(len(A)):
        A[i] = A[i][::-1]
        A[i] = [x^1 for x in A[i]]
    return A
    
A = [[1, 1, 0], [1,0,1],[0,0,0]]
print('Flip and Invert:',flipAndInvertImage(A))