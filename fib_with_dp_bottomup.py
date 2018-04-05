def fibo(n):
    fib = list()
    for k in range(0, n+1,1):
        if k < 2:
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib.append(f)
    return fib

def mem_fib(n, _cache={}):
    '''efficiently memoized recursive function, returns a Fibonacci number'''
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, mem_fib(n-1) + mem_fib(n-2))
    return n

if __name__ == "__main__":
    n = int(input('Enter the fibonacci nth no.:'))
    #print(fibo(n))
    for i in range(1,n+1):
        print(i,'---', mem_fib(i))
