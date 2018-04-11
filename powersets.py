
def generate_all_subsets(lst):
    tmp = []
    final_res = []
    a = list(lst)
    
    final_res = printall(a, 0, tmp, final_res)
    
    return final_res

def printall(s, i,res,final_res):
    if i == len(s):
        return final_res.append(''.join(res))
    res.append(str(s[i]))
    printall(s, i+1, res, final_res);
    res.pop()
    printall(s, i+1, res, final_res)
    return final_res

s = str(input())

res = generate_all_subsets(s)
print(res)
for res_cur in res:
    print(str(res_cur))
