from collections import Counter
def commonChars(A):
    common = Counter(A[0])
    for i in A[1:]:
        common &= Counter(i)
    print(common)
    return list(common.elements())


inp = ["cool","lock","cook"]
print(commonChars(inp))