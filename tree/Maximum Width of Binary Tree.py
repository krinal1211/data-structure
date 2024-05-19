class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def widthOfBinaryTree(self, root):
        self.max_width=0
        dirr={}
        def dfs(root,level,index):
            if not root:
                return 0
            if level not in dirr:
                dirr[level]=index
            curr_width=index-dirr[level]+1
            self.max_width=max(self.max_width,curr_width)
            dfs(root.left,level+1,2*index)
            dfs(root.right,level+1,2*index+1)
        dfs(root,0,1)
        return self.max_width
        


