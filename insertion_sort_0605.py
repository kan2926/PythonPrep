def insertion_sort(a):
    for i in range(len(a)):
        key = a[i]
        j = i-1
        while j >=0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key



a = [5,3,2,1,6,7,0]
insertion_sort(a)
print(a)
