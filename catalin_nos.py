

def catalan(n):
    if n == 1 or n == 0:
        return 1
    c = [0 for i in range(n+1)]
    c[0] = 1
    c[1] = 1
    for i in range(2, n+1):
        c[i] = 0
        for j in range(i):
            c[i] = c[i] + c[j] * c[i-j-1]
    return c[n]

n = int(input('enter no. of nodes: '))

print(catalan(n))
