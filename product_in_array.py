import functools
def prod(a):
    res = 1
    if a:
        res = functools.reduce(lambda x, y: x*y, a)
    return res
    

p = [1,2,3,4,5]
res = []
for i in range(len(p)):
    left = p[:i]
    right = p[i+1:]
    tmp = prod(left) * prod(right)
    res.append(tmp)

nums = [1,2,3]
p,q = 1,1
results = [1] * len(nums)
print(results)
for i in range(len(nums)):
    print(nums[i])
    print(nums[~i])
    results[i] *= p
    results[~i] *= q
    print(results)
    p *= nums[i]
    print('p--',p)
    
    q *= nums[~i]
    print('a --- ', q)
print(results)
