def find_missing_number(s):
    s.sort()
    n = len(s)
    x1 = 0
    x2 = 0
    for i in range(n):
        x1 ^= s[i]
    for i in range(n+2):
        x2 ^= i
    return x1 ^ x2

s = [2,4,3]
print(find_missing_number(s))
