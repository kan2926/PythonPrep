l = [3,4,5,6]
def powerset(A):
    res = [[]]
    for x in A:
        newsubsets = [subset + [x] for subset in res]
        res.extend(newsubsets)
    return res

print(powerset(l))
