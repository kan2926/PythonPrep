
def countpaths(m, n):
    if m == 1 or n== 1:
        return 1
    sum_down = countpaths(m-1, n)
    sum_right = countpaths(m, n-1)
    return sum_down + sum_right

m = 3
n = 3
print(countpaths(m,n))
