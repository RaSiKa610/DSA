# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return [True, 0]

            l = dfs(node.left)
            r = dfs(node.right)

            l_b, l_h = l[0], l[1]
            r_b, r_h = r[0], r[1]

            current_b = (l_b and r_b and abs(l_h - r_h) <= 1)

            current_h = max(l_h, r_h) + 1
            return [current_b, current_h]

        return dfs(root)[0]
