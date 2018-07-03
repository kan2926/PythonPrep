def partition(a, low, high):
    i = low - 1
    pivot = a[high]
    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1] , a[high] = a[high], a[i+1]
    return i+1

def qs(a, low, high):
    if low< high:
        pi = partition(a, low, high)
        qs(a, low, pi-1)
        qs(a, pi+1, high)
        

a = [2,1,4,6,3,8,10,5]
qs(a, 0, len(a)-1)
print(a)
