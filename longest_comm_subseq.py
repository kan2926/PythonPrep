def lcs(a,b):
    m = len(a)
    n = len(b)
    c = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    for i in range(m):
        for j in range(n):
            print(c[i][j], end =' ')
        print()
    return c[m][n]

a = "AGGTAB"
b = "GXTXAYB"
print(lcs(a,b))
