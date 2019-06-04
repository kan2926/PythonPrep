class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        q = root and [root]
        while q:
            node = q.pop()
            res.append(node.val)
            q += [child for child in node.children[::-1] if child]
        return res