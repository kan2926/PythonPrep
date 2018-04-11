def printperms(s, i, res):
    if i == len(s):
        print(res)
        return
    for j in range(0, len(res)):
        if res[j] == ' ':
            res[j] = s[i]
            printperms(s, i+1, res)
            res[j] = ' '

s = 'abc'
res = [' ']*len(s)
print('res---', res,'---')
printperms(s, 0, res)
