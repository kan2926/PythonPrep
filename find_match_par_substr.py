def find_match_par_substr(s):
    dp , stack = [0]* (len(s) +1), []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                print(p)
                print(dp)
                print('i---',i)
                dp[i+1] = i-p+1
                print(dp)
    print(dp)
    return max(dp)
    
s ='(())))((()))'
l = list(s)
res = find_match_par_substr(s)
print(res)
