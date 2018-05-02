
def quicksort(s, start, end):
    if start < end:
        pi = partition(s, start, end)
        quicksort(s, start, pi-1)
        quicksort(s, pi+1, end)

def partition(s, start, end):
    pivot = s[end]
    pi = start-1
    for i in range(start, end):
        if s[i] <= pivot:
            pi = pi+1
            s[pi], s[i] = s[i], s[pi]
    s[pi+1] , s[end] = s[end], s[pi+1]
    return pi+1


s=[6,12,4,1,9,10,0,5]
print(s)
quicksort(s, 0, len(s)-1)
print(s)
