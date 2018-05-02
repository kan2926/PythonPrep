
def two_sum(n, k):
    for i in range(len(n)):
        f = n[i]
        for j in range(len(n)):
            s = n[j]
            total_sum = f + s
            if total_sum == k:
                res = [i,j]
                return res
            else:
                pass

def twosum(arr,targ):
    look_for = {}
    for n,x in enumerate(arr):
        try:
            print(look_for[x] )
            return look_for[x] , n 
        except KeyError:
            look_for.setdefault(targ - x,n)
            print(look_for)

a = (2,7,1,15)
t = 16
print(twosum(a,t))  # (1,2)

a = (-3,4,3,90)
t = 0
print(twosum(a,t))  # (1,3)

