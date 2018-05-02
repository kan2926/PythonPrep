def insertion_sort(a):

    for i in range(len(a)):
        key = a[i]
        j = i-1
        while j>= 0 and key<a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    
a= [3,1,5,8,10,2]
insertion_sort(a)
print(a)
