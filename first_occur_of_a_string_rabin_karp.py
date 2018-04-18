import math
pr = 3
di = {'a':1, 'b':2, 'c':3, 'd':4,'e':5,'f':6}
def create_hash(str, end):
    h = 0
    for i in range(0, end):
        h += di[str[i]]*(math.pow(pr, i))
    return h

def check_equal(str1, st1, en1, str2, st2, en2):
    if en1 - st1 != en2 - st2:
        return False
    while st1 < en1 and st2<en2 :
        if str1[st1] != str2[st2]:
            return False
        st1+=1
        st2+=1
    return True

def recalculateHash(txt, old_index, new_index, old_hash, pattern_len):
    new_hash = old_hash - di[txt[old_index]]
    new_hash = new_hash/pr
    new_hash += (di[txt[new_index]] * math.pow(pr, pattern_len-1))
    return new_hash

def patternsearch(pat, txt):
    m = len(pat)
    n = len(txt)
    res = []
##    pattern_hash = create_hash(pat, m)
##    print(pattern_hash)
##    text_hash = create_hash(txt, n)
##    print(text_hash)
    pattern_hash = create_hash(pat, m)
    text_hash = create_hash(txt, m)
    for i in range(0, n-m+1):
        print(text_hash)
        if pattern_hash == text_hash :
            if check_equal(txt, i, i+m, pat, 0, m) :
                res.append(i)
        if i< n-m:
            text_hash = recalculateHash(txt, i, i+m, text_hash, m)
    if not res:
        return -1
    else:
        return res
 
 
# Driver program to test the above function
txt = "abedabc"
pat = "abc"
print(patternsearch(list(pat),list(txt)))

