class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if root.right:
            if root.val != root.right.val: 
                return root.val == root.right.val
            
        if root.left:
            if root.val != root.left.val: 
                return False
        
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
        