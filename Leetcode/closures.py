def Foo(n):
    def multiplier(x):
        print(x)
        return x * n
    return multiplier

a = Foo(5)
b = Foo(5)
print(a(4))
print(a(b(2)))
