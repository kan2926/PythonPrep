# 
# Your previous JavaScript content is preserved below:
# 
# /*
# Write a function called answer(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list. For instance, if data was [5, 10, 15, 10, 7] and n was 1, answer(data, n ) would return the list [5, 15, 7] because 10 occurs twice, and was thus removed from the list entirely.
# */
# 
# 

from collections import Counter
def answer(data, n):
    if data:
        cnt = Counter()
        for i in arr:
            cnt[i] += 1
        
        d =dict(cnt)        
        l = [x for x in data if d[x] <= n]
##        print(l)
##        for i, j in enumerate(data): 
##            if d[j] > n:
##                continue
##            else:
##                result.append(j)
##    
        return l
    
    
if __name__ == '__main__':
    arr = [5, 15, 10, 7, 10, 15, 10]
    n = 2
    print(answer(arr, n))

