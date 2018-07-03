

def toh_helper(n, A, C, B, res = []):
    if n == 1:
        s = A, '->', C
        res.append(s)
        return
    toh_helper(n-1, A, B, C, res)
    s = A, '->',C
    res.append(s)
    toh_helper(n-1, B, C, A, res)
    return res

def toh(n):
    return toh_helper(n, 'A','C','B')


n = 3
res = toh(n)
print(res)
