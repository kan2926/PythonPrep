def permute(A):
    def directpermutation(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        for j in range(i, len(A)):
            A[i], A[j]=A[j],A[i]
            directpermutation(i+1)
            A[i], A[j] = A[j],A[i]
    result = []
    directpermutation(0)
    return result

A=[3,4,5]
res = permute(A)
print(res)
