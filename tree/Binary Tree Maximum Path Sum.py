# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.global_max=float('-inf')
        def fun(node):
            if not node:
                return 0
            l=max(fun(node.left),0)
            r=max(fun(node.right),0)
            curr=l+r+node.val
            self.global_max=max(curr,self.global_max)
            return node.val + max(l,r)
        fun(root)
        return self.global_max


