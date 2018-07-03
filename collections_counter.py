from collections import Counter

cnt = Counter()
arr = [1,4,4,5,3]
for i in arr:
    cnt[i] += 1

print(cnt)
print(cnt.most_common(1))
d = {}
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
print(max(d, key = d.get))
counts = dict()
for i in arr:
  counts[i] = counts.get(i, 0) + 1
print(counts)
print(max(counts, key = counts.get))
