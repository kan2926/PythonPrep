from itertools import combinations


l = [10, 3, -4, 1, -6, 9]
m = list(combinations(l, 3))

valid_combos = [i for i in m if sum(i) == 0]
res = set()
for i in valid_combos:
    res.add(','.join(map(str, sorted(i))))

print(res)



