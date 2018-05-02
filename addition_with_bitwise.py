def add(x, y):
    while (y != 0):
        carry = x& y
        print('carry ---',carry)
        x = x^ y
        print('x --- ',x)
        y = carry <<1
        print('y ---',y)
    return x



print(add(10,30))
