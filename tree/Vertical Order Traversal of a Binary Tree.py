# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.dir={}
        def vertical(root,row,col):
            if not root:
                return
            if col not in self.dir:
                self.dir[col] = []
            self.dir[col].append((row, root.val))
            vertical(root.left, row + 1, col - 1)
            vertical(root.right, row + 1, col + 1)

        vertical(root,0,0)
        sorted_items = sorted(self.dir.items())
        b=[]
        
        for col,values in sorted_items: 
            values.sort()
            b.append([val for row,val in values])
            
        return b


            

        
