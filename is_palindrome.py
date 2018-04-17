    
def is_palRec(st, s, e):
    if s == e:
        return True
    if st[s] != st[e]:
        print(st[s],'---',st[e])
        return False
    if s< e-1:
        return is_palRec(st, s+1, e-1)
    return True
def is_palindrome(s):
    #
    # Write your code here.
    n = len(s)
    
    punc = ('.',',','!',';',':','\'','"')
    import re
    ns = re.sub(r'[^\w\s]','',s).replace(' ','')
##    for i,j in enumerate(s):
##        if (j  in punc):
##            pass
##        else:
##            ns += j
    print(ns)
    n = len(ns)
    if n == 0 :
        return True
    return is_palRec(ns.lower(), 0, n-1)

# Main Function
s = "Never a foot too Far, even."
if (is_palindrome(s)) :
    print ("Yes")
else :
    print ("No")
