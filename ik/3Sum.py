from itertools import combinations
def findZeroSum(arr):
    # Write your code here.
    m = list(combinations(arr, 3))

    valid_combos = [i for i in m if sum(i) == 0]
    res = set()
    for i in valid_combos:
        res.add(','.join(map(str, sorted(i))))
    return res

print(findZeroSum([2,-2,0,2,-2,3]))
print(findZeroSum([0,0,0]))
