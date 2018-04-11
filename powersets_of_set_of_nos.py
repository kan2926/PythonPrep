
def generate_all_subsets(lst):
    tmp = []
    final_res = printall(lst, 0, tmp)

def printall(s, i,res):
    if i == len(s):
        print(res)
        return
    res.append(s[i])
    printall(s, i+1, res);
    res.pop()
    printall(s, i+1, res)

s = [1,2,3]

res = generate_all_subsets(s)
