def fibo(n):
    fib = list()
    for k in range(0, n+1,1):
        if k < 2:
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib.append(f)
    return fib

if __name__ == "__main__":
    n = int(input('Enter the fibonacci nth no.:'))
    print(fibo(n))
