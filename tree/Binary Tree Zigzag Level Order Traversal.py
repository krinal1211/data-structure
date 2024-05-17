class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def zigzag(root):
            if not root:
                return []
            h = height(root)
            result = []
            for i in range(1, h + 1):
                level_values = []
                cal(root, i, level_values, i % 2 == 0)
                result.append(level_values)
            return result
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        def cal(root, level, level_values, reverse):
            if not root:
                return
            if level == 1:
                level_values.append(root.val)
            elif level > 1:
                if reverse:
                    cal(root.right, level - 1, level_values, reverse)
                    cal(root.left, level - 1, level_values, reverse)
                else:
                    cal(root.left, level - 1, level_values, reverse)
                    cal(root.right, level - 1, level_values, reverse)
        
        return zigzag(root)
