def jump(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return "NO"
    elif ((x2-x1)%(v1-v2) == 0):
        return "YES"



print(jump(0,3,4,2))
print(jump(0,2,5,3))
