# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:03:19 2019

@author: kanyad
"""

def peak_index(a):
    return a.index(max(a))


def peak_index_with_binary_search(a):
    l, r = 0, len(a)-1
    
    while l < r:
        mid = (l+r)//2
        if a[mid] < a[mid+1]:
            l = mid
        elif a[mid-1] > a[mid]:
            r = mid
        else:
            return mid




a = [0,2,1,0]
print(peak_index(a))

print(peak_index_with_binary_search(a))