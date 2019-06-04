
def reverseStr(s, k):
    for i in range(0, len(s), 2*k):
        s = s[:i] + s[i:k+i][::-1] + s[k+i:]
        
    return s

    

s = "abcdefg"
k = 3
print(reverseStr(s,k))
