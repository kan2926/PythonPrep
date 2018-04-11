

def binary_search(a, start, stop, key):
    if start > stop:
        return False
    mid = int((start + stop)/2)
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a, start, mid-1, key)
    else:
        return binary_search(a, mid+1, stop, key)

a = [4,5,6,7,8,9,10,11,12,13,14]
print(binary_search(a,0,len(a)-1,16))
