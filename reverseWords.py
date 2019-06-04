
def reverseWords(s):
    w = s.split(' ')
    res = []
    for i in w:        
        res.append(i[::-1])
    return ' '.join(res)
    


inp = "Let's take LeetCode contest"
reverseWords(inp)