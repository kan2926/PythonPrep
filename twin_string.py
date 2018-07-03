def check_equals(a,b):
    if set(a) == set(b):
        return True
    else:
        return False
    
def twins(a, b):
    
    result = []  # to store the result array of Yes or No
    for i in range(len(a)):
        a_odd = []
        a_even = []
        b_odd = []
        b_even = []
        if len(a[i]) == len(b[i]):
            for index in range(len(a[i])):
                if index %2 == 0:
                    a_even.append(a[i][index])
                    b_even.append(b[i][index])
                else:
                    a_odd.append(a[i][index])
                    b_odd.append(b[i][index])
        else:
            result.insert(i,'No')
            break

        if check_equals(a_odd, b_odd) and check_equals(a_even, b_even):
            result.append('Yes')
        else:
            result.append('No')
    return result

def chunkstring(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))

def reverse(strings):
    return [x[::-1] for x in strings]

def t(a, b):
    result = []
    for i in range(len(a)):
        m = len(a[i])
        n = len(b[i])
        if m == n:
            a_chunks = chunkstring(a[i], 2)
            b_chunks = chunkstring(b[i],2)    
            a_set = (reverse(a_chunks))
            b_set = (reverse(b_chunks))
        else:
            result.append('No')
            break
        if set(a_set) == set(b_set):
            result.append('Yes')
        else:
            result.append('No')
    print(result)


    
##a = ['cdab']s
##b = ['abcd']
##    
a = ['cdab','dcba', 'abcd']
b = ['abcd','abcd', 'abcdcd']
t(a,b)
#print(twins(a,b))
