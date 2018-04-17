
def printall(s, i,res,final_res):
    if i == len(s):
        final_res.append(''.join(res))
        return final_res
    res.append(str(s[i]))
    printall(s, i+1, res, final_res);
    res.pop()
    printall(s, i+1, res, final_res)
    return final_res
    

def generate_all_subsets(lst):
    a = list(lst)
    res = printall(a, 0, [], [])
    n = len(res)
    result = list()
    result.append(n)
    for i in res:
        result.append(i)    
    return result


if __name__ == "__main__":

    try:
        s = str(input())
    except:
        s = None

    res = generate_all_subsets(s);
    for res_cur in res:
         print( str(res_cur) + "\n" )


