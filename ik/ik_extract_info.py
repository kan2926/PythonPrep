
from collections import defaultdict
def solve(arr):
    d = defaultdict(list)

    for i in range(len(arr)):
        key = arr[i].split(' ')[0]
        value = arr[i].split(' ')[1]
        d[key].append(value)
    s = []
    for k,v in d.items():
        s.append(k+':'+str(len(v))+',' +max(v))
    return s


arr = ["key1 abcd", "key2 zzz",  "key1 hello", "key3 world", "key1 hello"]
res = solve(arr)
print('\n'.join(res))
