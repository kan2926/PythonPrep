
def three_sum(nums):
    nums.sort()
    #size of the array
    n = len(nums)

    # Hash table
    solutions = set()

    # O(n): hash tables are really fast :)
    unique_set = set(nums)
    # covers a lot of edge cases with 2 memory lookups and 1 hash so it's worth the time
    if len(unique_set) == 1 and 0 in unique_set and len(nums) > 2:
        return [[0, 0, 0]]
    i = 0
    while i < n - 2:
        num = nums[i]

        left = i + 1
        right = n - 1
        while left < right:
            left_num = nums[left]
            right_num = nums[right]
            s = num + left_num + right_num  # check if current sum is 0
            if s == 0:
                # add to the solution set only if this triplet is unique
                # Hash lookup
                solutions.add(tuple([right_num, num, left_num]))
                right -= 1
                left += 1
            elif s > 0:
                right -= 1
            else:
                left += 1
        i += 1

    return list(solutions)
nums = [-1, 0, 1,2,-1,-4]
print(three_sum(nums))
