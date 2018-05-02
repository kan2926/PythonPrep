
from itertools import combinations
def findZeroSum(arr):
    # Write your code here.
    m = list(combinations(arr, 3))

    valid_combos = [i for i in m if sum(i) == 0]
    res = set()
    for i in valid_combos:
        res.add(','.join(map(str, sorted(i))))
    return res
    



if __name__ == "__main__":
    arr_size = int(input())

    arr = []
    for _ in range(arr_size):
        arr_item = int(input())
        arr.append(arr_item)

    res = findZeroSum(arr)

    print("\n".join(res))

    print('\n')
