def print_brackets(s, start, end, length, output):
    if len(s) == 2*length:
        return s
    
    s.append('(')
    print_brackets(s, start, end-1, length, output)
    
    s.append(')')
    print_brackets(s, start+1, end, length, output)    
    return s

def find_all_well_formed_brackets(n):
    if n== 0:
        return
    s = []
    output = [] 
    res = print_brackets(s, 0, n, n, output)
    return res          


if __name__ == "__main__":

    n = int(input())

    res = find_all_well_formed_brackets(n);
    for res_cur in res:
         print( str(res_cur) + "\n" )
