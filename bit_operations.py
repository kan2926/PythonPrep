print( int('1001',2))
print("0x%x" % int('0110',2))
print("0x%x" % int('111011',2))

print(chr(int('111011',2)))
print(ord('u'))
print(chr(int('01110101',2)))
print(int('01110101',2))


print(1<<2)
print(1<<7)

def bitLen(int_type):
    l = 0
    while(int_type):
        int_type >>= 1
        l+=1
    return l

def bitCount(int_type):
    count = 0
    while int_type:
        int_type &= int_type - 1
        count += 1
    return count

def lowestSet(i):
    low = (i & -i)
    lowBit = -1
    while low:
        low >>= 1
        lowBit += 1
    return lowBit
print('----',lowestSet(64))

def parityOf(n):
    res = 0
    while n:
        res ^=1
        n = n & n-1
    return res

print(parityOf(44))

for i in range(10):
    #print(bitLen(i))
    print(i ,'---',bitCount(i))    
