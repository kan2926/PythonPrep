
def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target-num in lookup:
            print(lookup)
            return [ lookup[target-num], i]
        lookup[num] = i
        


nums = [2,7,11,12]
target = 14
print(twoSum(nums, target))
