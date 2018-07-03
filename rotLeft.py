def rotLeft(a, d):
    if a:
        if d > 0:
            for i in range(0,d):
                temp = a[1:]
                temp.append(a[0])
                a = temp
                print(i, ' ', a)
            return a
        elif d ==0:
            return a 
    else:
        return a

def rotateLeft(a,k):
    d = k % len(a)
    return a[d:] + a[:d]

print(rotateLeft([1,2,3,4,5],3))
