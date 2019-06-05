def findReplaceString( S: str, indexes, sources, targets):    
    for i,s,t in sorted(zip(indexes, sources, targets), reverse=True):        
        if S[i:i+len(s)] == s:
            S = S[:i]+t+S[i+len(s):]
    return S
    
    
S = "abcd" 
indexes = [0,2] 
sources = ["a","cd"]
targets = ["eee","ffff"]
print(findReplaceString(S,indexes,sources,targets))