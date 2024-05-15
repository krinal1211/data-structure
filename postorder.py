# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # # ---------------->using 2 stack
        # result=[]
        # stack1=[root]
        # stack2=[]
        # while stack1:
        #     node=stack1.pop()
        #     if node:
        #         stack2.append(node)
        #         if node.left:
        #             stack1.append(node.left)
        #         if node.right:
        #             stack1.append(node.right)
        # postorder=[]
        # while stack2:
        #     postorder.append(stack2.pop().val)
        # return postorder


        # # ------------->using 1 stack
        # result=[]
        # stack=[root]
        # while stack:
        #     node=stack.pop()
        #     if node:
        #         result.append(node.val)
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        # return result[::-1]

        # ----------------------->using recursion
        a=[]
        def fun(root):
            if not root:
                return a 
            fun(root.left)
            fun(root.right)
            a.append(root.val)
            return a
        return fun(root)
        
