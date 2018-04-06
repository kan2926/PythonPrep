from collections import OrderedDict

def checkOrder(inp, pattern):
    odict = OrderedDict.fromkeys(inp)
    pattern_len = 0
    for key, value in odict.items():
        if key == pattern[pattern_len]:
             pattern_len = pattern_len+1
        if pattern_len == len(pattern):
            return True
    return False

if __name__ == "__main__":
    inp = "I love kids"
    pattern = 'vkiy'
    #False
    print(checkOrder(inp,pattern))
    #True
    pattern = 'ois'
    print(checkOrder(inp,pattern))
