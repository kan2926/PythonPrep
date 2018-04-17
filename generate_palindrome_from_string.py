


def ispalindrome(s):
    return s == s[::-1]


def dfs(s, path, res):
    if not s:
        res.append('|'.join(path))
    for i in range(1, len(s)+1):
        if ispalindrome(s[:i]):
            dfs(s[i:], path+[s[:i]], res)


def generate_palindromic_decompositions(a):
    res = []
    dfs(a, [], res)
    return res


if __name__ == "__main__":

    try:
        s = str(input())
    except:
        s = None

    res = generate_palindromic_decompositions(s);
    for res_cur in res:
        print( str(res_cur) + "\n" )




