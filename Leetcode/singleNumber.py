import operator
from collections import Counter
from functools import reduce

def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (Counter(list(set(nums)) * 3) - Counter(nums)).keys()[0]

arr = [2,2,3,2]
singleNumber(arr)
c = Counter(arr)
print(c.values())
