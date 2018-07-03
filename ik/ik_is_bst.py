
import sys
import os

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(data):
    def deserialize():
        val = next(vals,None)
        if val == None:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize()
        node.right = deserialize()
        return node
    vals = iter(data.split())
    return deserialize()



INT_MIN = -4294967296
INT_MAX = 4294967296
def is_Bst(root):
    if root is None:
        return True
    
    return isBstUtil(root, INT_MIN, INT_MAX)

def isBstUtil(node, mini, maxi):
    if node is None:
        return True

    if node.val < mini or node.val > maxi :
        return False

    return (isBstUtil(node.left, mini, node.val) and
             isBstUtil(node.right, node.val, maxi))




def  isBST(root):
    if root is None:
        return True
    
    def isBSTUtil(node, min, max):
        if node is None:
            return True
            
        if node.val <= min:
            return False
        if node.val >= max:
            return False
            
        left_ok = True
        right_ok = True
        
        if not node.left:
            left_ok = isBSTUtil(node.left, min, node.val)
        
        if not node.right:
            right_ok = isBSTUtil(node.right, node.val, max)
        
        return left_ok and right_ok
    return isBSTUtil(root, float('-inf'), float('inf'))


_size = int(input());


_str = input()
root = createTree(_str);
res = is_Bst(root);
print(str(int(res)) + "\n")
