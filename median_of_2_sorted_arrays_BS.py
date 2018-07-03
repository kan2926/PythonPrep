
def median_sorted_arrays(a,b):
    if len(a) > len(b):
        return median_sorted_arrays(b,a)
    x = len(a)
    y = len(b)

    low = 0
    high = x
    MIN_VALUE = float('-inf')
    MAX_VALUE = float('inf')

    while low <= high:

        px = (low + high)//2
        py = (x+y+1)//2 - px

        maxLeftX = MIN_VALUE if px ==0 else a[px - 1]
        minRightX = MAX_VALUE if px == x else a[px]

        maxLeftY = MIN_VALUE if py == 0 else b[py-1]
        minRightY = MAX_VALUE if py == y else b[py]

        if maxLeftX <= minRightY and maxLeftY <= minRightX :
            if (x+y)%2 == 0:
                return (max(maxLeftX, maxLeftY), max(minLeftY, minRightY))/2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = px -1
        else:
            low = px + 1

a = [1,3,8,9,15]
b = [7, 11,18,19,21,25]
print(median_sorted_arrays(a,b))
