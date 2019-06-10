# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:50:57 2019

@author: kanyad
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def pathSum(self, root, sum):
        if root is None:
            return False
               
        
        if not root.left and not root.right and root.val == sum:
            return True
        
        sum = sum - root.val
        
        return self.pathSum(root.left, sum) or self.pathSum(root.right, sum)