def permute(so_far, rem):
    if rem == '':
        print(so_far)
        return
    else:
        for i in range(0, len(rem)):
            next = so_far + rem[i]
            rest = rem[0:i] + rem[i+1:]
            permute(next, rest)




s = input()
print(s)
permute('',s)
