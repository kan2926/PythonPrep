

def marsExploration(s):
    n= len(s)
    original_message = 'SOS'
    no_of_messages = n//3
    total_cnt = 0
    for i in range(0,n,3):
        st = s[i:i+3]
        if st == original_message:
            continue
        else:
            diff_len = len(list([c for c in st if c not in original_message]))
            total_cnt += 1
    return total_cnt





s = 'SOSSPSSQSSOR'
print(marsExploration(s))
