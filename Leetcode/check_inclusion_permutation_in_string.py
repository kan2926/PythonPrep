# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 22:23:15 2019

@author: kanyad
"""
import collections
def checkInclusion( s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    len1 = len(s1)
    len2 = len(s2)
    d1 = collections.Counter(s1)
    sw = collections.Counter(s2[0:len1])
    print(d1)
    for i in range(len1, len2):
        if d1 == sw:
            return True
        
        sw[s2[i]] = sw.get(s2[i], 0) + 1
        sw[s2[i - len1]] -= 1
        if sw[s2[i - len1]] <= 0:
            del sw[s2[i - len1]]                               
            
    return d1 == sw


s1 = "aab" 
s2 = "eidabaoaooo"
print(checkInclusion(s1,s2))