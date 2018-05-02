def fib(num):
    a, b = 0,1
    for x in range(num):
        yield a
        a, b = b, a+b

for i in fib(10):
    print(i)
