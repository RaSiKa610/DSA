# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def dfs(node):
            if not node:
                return 0, 0

            l_sum, l_count = dfs(node.left)
            r_sum, r_count = dfs(node.right)

            current_sum = l_sum + r_sum + node.val
            current_count = r_count + l_count + 1

            if current_sum // current_count ==  node.val:
                self.result += 1

            return current_sum, current_count

        dfs(root)
        return self.result
