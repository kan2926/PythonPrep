def wild_char(s, i , res):
    if i == len(s):
        res.append(s)
        return res
    if s[i] == '?':
        s = s[:i] +'0' +s[i+1:]
        wild_char(s, i+1, res)
        s = s[:i] +'1' +s[i+1:]
        wild_char(s, i+1, res)
    else:
        wild_char(s, i+1, res)
    return res

def find_all_possibilities(s):
    res = []
    r = wild_char(s, 0, res)
    return r

s = input()
res = find_all_possibilities(s)
print(res)
