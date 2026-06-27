# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.count = 0

        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            left_path = l + 1 if node.left else 0
            right_path = r + 1 if node.right else 0

            self.count = max(self.count, right_path + left_path)

            return max(left_path, right_path)

        dfs(root)
        return self.count     
