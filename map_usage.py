
def sq(x):
    return x* x

def my_map(func, inp):
    res = []
    for i in inp:
        res.append(func(i))
    return res


inp = [-2,-3,4,6]
output = my_map(sq, inp)
print(output)
