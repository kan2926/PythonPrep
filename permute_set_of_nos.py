def permute(s, i, res):
    if i == len(s):
        print(''.join(res))
        return
    else:
        for j in range(0, len(s)):
            if res[j] == ' ':
                res[j] = s[i]
                permute(s, i+1, res)
                res[j] = ' '
                
s = 'abc' #or list of nos.
res = [' ']* len(s)
permute(s, 0, res)
