# Python program to remove characters from first string which
# are present in the second string

def toString(List):
    return ''.join(List)
 
def removeDirtyChars(s, mask_string):
    ip_ind = 0
    res_ind = 0
    temp = ''
    str_list = list(s)
    m_s = list(mask_string)
 
    while ip_ind != len(str_list):
        temp = str_list[ip_ind]
        if temp not in m_s:
            str_list[res_ind] = str_list[ip_ind]
            res_ind += 1
        ip_ind+=1
    return toString(str_list[0:res_ind])
 
# Driver function to test the above functions
mask_string = "mask"
s = "testing"
print( removeDirtyChars(s, mask_string))
 
