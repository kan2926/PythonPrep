
def sumsToK(a, count, target):
    if target == 0:
        return True

    if count == 0:
        return False

    return sumsToK(a, count - 1, target) or sumsToK(a, count-1, sum - a[count-1])



a=[2,4,8]
target = 6
print(sumsToK(a, len(a), target))
