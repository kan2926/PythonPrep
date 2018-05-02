def binary_search(a, l, r, x):
    
    if r >= 1:
        mid = l + (r-1)//2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return binary_search(a, l, mid-1, x)
        else:
            return binary_search(a, mid+1, r, x)
    else:
        return -1
        



a = [ 2, 3, 4, 10, 40 ]
x=10

print(binary_search(a, 0, len(a)-1, x))
