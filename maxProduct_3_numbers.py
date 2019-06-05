def maxProduct( nums):
    max1,max2,max3,min1,min2 = float('-Inf'),float('-Inf'),float('-Inf'),float('Inf'),float('Inf')
    for num in nums:
        print("num---",num)
        if num >= max1:
            max3,max2,max1 = max2,max1,num
        elif num >= max2:
            max3,max2 = max2,num
            max3 = num
        if num <= min1:
            min2,min1 = min1,num
        elif num < min2:
            min2 = num
        print(max3, max2, max1, min1, min2)
    return max(max1*max2*max3,min1*min2*max1)
    


def maxProduct_with_sort(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


inp = [1,2,3,1, 2]
print(maxProduct(inp))
print(maxProduct_with_sort(inp))