

def catalan(n):
    if n <= 1:
        return 1
    res = 0
    
    for i in range(n):
        res +=  catalan(i) * catalan(n-i-1)        

    return res

def BinominalCoefficient(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

def CatalanNumbers(n):
   c = BinominalCoefficient(2*n, n)
   return (c//(n+1))

# A dynamic programming based function to find nth
# Catalan number
def catalanDP(n):
    if (n == 0 or n == 1):
        return 1
 
    # Table to store results of subproblems
    catalan = [0 for i in range(n + 1)]
 
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
 
    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]
            print('i---',i, catalan[i])
     return catalan[n]


n = int(input("enter no. of nodes: "))
#print(catalan(n))

#T = [1,1]
#print(CatalanNumbers(n))

print (catalanDP(n))
