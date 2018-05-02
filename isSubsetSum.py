
def isSubsetSum(s, n, target_sum):

    if target_sum == 0:
        return True
    if n == 0 and target_sum != 0:
        return False
    if s[n-1] > target_sum:
        return isSubsetSum(s, n-1, target_sum)

    return isSubsetSum(s, n-1, target_sum) or isSubsetSum(s, n-1, target_sum-s[n-1])





s = [ 1,2,3,4,5]
target_sum = 21
print(isSubsetSum(s, len(s), target_sum))
