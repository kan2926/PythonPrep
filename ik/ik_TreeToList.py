#!/bin/python

import sys

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
    print (root.val, end=' ')
    printInorder(root.right)

def display(head):
    if head is None:
        return None
    curr = head
    while curr:
        print (curr.val, end = ' ')
        curr = curr.right
        if curr == head:
            break
    
def concatenate(left_list, right_list):
    if left_list is None and right_list is None:
        return None
    if left_list is None:
        return right_list
    if right_list is None:
        return left_list
    
    left_last = left_list.left
    right_last = right_list.left
    
    left_last.right = right_list
    right_list.left = left_last
    left_list.left = right_last
    right_list.right = left_list
    
    return display(left_list)
    
    
def  BSTtoLL(node):
    if node is None:
        return None
    left_list = BSTtoLL(node.left)
    right_list = BSTtoLL(node.right)
    node.left = node.right = node
    return concatenate(concatenate(left_list, node), right_list)


_size = int(input());


_str = input()

node = createTree(_str);
BSTtoLL(node);
