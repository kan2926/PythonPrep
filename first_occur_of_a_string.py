import math
pr = 3
di = {'a':1, 'b':2, 'c':3, 'd':4,'e':5,'f':6}
def create_hash(str, end):
    h = 0
    for i in range(0, end):
        h += di[str[i]]*(math.pow(pr, i))
    return h

def check_equal(str1, st1, en1, str2, st2, en2):
    print(str1)
    print(st1, '  ' , en1)
    print(str2)
    print(st2, '  ', en2)
    if en1 - st1 != en2 - st2:
        return False
    while st1 < en1 and st2<en2 :
        print('in while')
        if str1[st1] != str2[st2]:
            print('not match')
            return False
        st1+=1
        st2+=1
    return True

def recalculateHash(txt, old_index, new_index, old_hash, pattern_len):
    print('ni ---',new_index, ' text ---', txt[new_index])
    print('oi---',old_index, ' old -- ', txt[old_index])
    print('old hash ', old_hash)
    new_hash = old_hash - di[txt[old_index]]
    print('after minus  ', new_hash)
    new_hash = new_hash/pr
    print('after divide ' , new_hash)
    new_hash += (di[txt[new_index]] * math.pow(pr, pattern_len-1))
    print('after add ' , new_hash)
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
    print('ph---',pattern_hash)
    text_hash = create_hash(txt, m)
    for i in range(0, n-m+1):
        print('th --- ',text_hash)
        print(text_hash)
        if pattern_hash == text_hash :
            print('match found compare strings')
            if check_equal(txt, i, i+m, pat, 0, m) :
                print('match at ', i)
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

