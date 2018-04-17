import itertools
def findLongestConseqSubseq(arr, n):
 
    s = set()
    ans=0
 
    # Hash all the array elements
    for ele in arr:
        s.add(ele)
    c =[]
    k=0
 
    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):

         # if current element is the starting
        # element of a sequence
        if (arr[i]-1) not in s:            
            # Then check for next elements in the
            # sequence
            j=arr[i]
            k += 1
            
            while(j in s):                
                c.append(j)
                j+=1
                
            print(arr[i],'---',j)
            # update  optimal length if this length
            # is more
            ans=max(ans, j-arr[i])
    print(c)
    return ans
 
# Driver function 
if __name__=='__main__':
    n = 5
    arr = [4,5,6,7,10]
    print("Length of the Longest contiguous subsequence is ",)
    print(findLongestConseqSubseq(arr, n))
