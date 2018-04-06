def rec(x,n):
    if n == 0:
        return x
    elif n %2 ==0:
        y = rec(x, n/2)
        return y * y
    else:
        return rec(x, n-1)

if __name__ == "__main__":
    x = int(input("Enter value of x in x^n:"))
    n = int(input("Enter value of n in x^n:"))
    print(rec(x,n))
