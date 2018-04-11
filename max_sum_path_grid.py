
def maxPaths(a, row, col):
    if row >= len(a) or col >= len(a[0]):
        return 0
    if row == len(a) - 1 and col == len(a[0]) - 1:
        return a[row][col]
    maxRight = maxPaths(a, row, col+1)
    maxDown = maxPaths(a, row+1, col)
    return a[row][col] + max(maxRight, maxDown)

a = [[1,3,4,5],[1,4,10,11],[5,9,12,14],[5,6,2,1]]
row = len(a)
col = len(a[0])
for i in range(row):
    for j in range(col):
        print(a[i][j], end = ' ')
    print()

print(maxPaths(a, 0,0))
