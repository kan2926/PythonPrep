
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

def printInorder(root):
    if root == None:
        return
    printInorder(root.left)
    print (root.val,) 
    printInorder(root.right)

def inorder(root,res):
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)
        return res

def mergesort(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    m = len(l1) if l1 else 0
    n = len(l2) if l2 else 0         
    i = j = 0
    l3=[]
    while i < m and j < n :
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1
    l3 += l1[i:]
    l3 += l2[j:]
    return l3

def sortedArrayToBST(arr, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    node = Node(arr[mid])
    node.left = sortedArrayToBST(arr, start, mid-1)
    node.right = sortedArrayToBST(arr, mid+1, end)
    return node

def  mergeTrees(node1, node2):
    l1 = inorder(node1,[])
    l2 = inorder(node2, [])
    l3 = mergesort(l1, l2)
    if l3:
        root = sortedArrayToBST(l3, 0, len(l3)-1)
        return root
    else:
        return None


_size1 = int(input());


_str1 = input()
n1 = createTree(_str1);

_size2 = int(input());


_str2 = input()
n2 = createTree(_str2);

res = mergeTrees(n1,n2);
printInorder(res)




