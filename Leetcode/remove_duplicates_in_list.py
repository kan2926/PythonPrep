# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:36:00 2019

@author: kanyad
"""


def removeDuplicates_count_by_2( nums) :
    i = 1
    cnt = 1
    while i < len(nums):
        print(nums)
        
        if nums[i] == nums[i-1]:
            cnt += 1
        else:
            cnt = 1
        
        if cnt >2:
            del(nums[i])
        else:
            i += 1

nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates_count_by_2(nums)
s = set(nums)
print(len(s))
n = 1

while n < len(nums):
    if nums[n] == nums[n-1]:
        del(nums[n])
        print(nums)
    else:
        n += 1
        