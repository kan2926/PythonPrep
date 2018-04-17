def powset(a, i, res):
    if i == len(a):
        print( res)
        return
    res.append(a[i])
    powset(a, i+1, res)
    res.pop()
    powset(a, i+1, res)

a= [1,2,3]
powset(a, 0, [])
