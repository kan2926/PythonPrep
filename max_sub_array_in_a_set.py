
def find_min_diff(a, n):
    diff = 10**20
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(a[i] - a[j]) < diff:
                diff = abs(a[i] - a[j])
    return diff

def find_max_sub_array(a,n):
    max_sum = a[0]
    for i in range(n-1):
        for j in range(i+1, n):
            if (a[i] + a[j]) > max_sum:
                max_sum = a[i] +a[j]
    return max_sum
    
a = [-3,2,-4,-1,-3,1,5]
b = [1,5,3,19,18,25]
print(find_min_diff(b, len(b)))

print(find_max_sub_array(a,len(a)))
